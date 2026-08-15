#!/usr/bin/env python3
"""
Simple claim/unclaim script that edits mirrored_coach_ledger_v3.jsonl in-place.
Usage:
  python3 scripts/claim_unclaim.py claim <id> --owner "Name" [--message "note"]
  python3 scripts/claim_unclaim.py unclaim <id> --owner "Name"

This is intentionally minimal: it updates owner, status, and last_updated timestamp.
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['claim','unclaim'])
parser.add_argument('id')
parser.add_argument('--owner', required=True)
parser.add_argument('--message')
args = parser.parse_args()

ledger_path = Path('mirrored_coach_ledger_v3.jsonl')
if not ledger_path.exists():
    print('Ledger not found:', ledger_path, file=sys.stderr)
    sys.exit(2)

lines = ledger_path.read_text().splitlines()
new_lines = []
found = False
for line in lines:
    try:
        obj = json.loads(line)
    except Exception:
        new_lines.append(line)
        continue
    if obj.get('id') == args.id:
        found = True
        now = datetime.now(timezone.utc).astimezone().isoformat()
        if args.action == 'claim':
            obj['owner'] = args.owner
            # If status is planned, set to in_progress; otherwise leave as-is
            if obj.get('status') in (None, 'planned'):
                obj['status'] = 'in_progress'
            obj['last_updated'] = now
            if args.message:
                obj['notes'] = (obj.get('notes','') + '\n' + args.message).strip()
        else:  # unclaim
            # Only remove owner if it matches
            if obj.get('owner') == args.owner:
                obj['owner'] = 'unassigned'
                obj['status'] = 'planned'
                obj['last_updated'] = now
                if args.message:
                    obj['notes'] = (obj.get('notes','') + '\n' + args.message).strip()
            else:
                print('Unclaim aborted: owner does not match current owner', file=sys.stderr)
                sys.exit(3)
        new_lines.append(json.dumps(obj, ensure_ascii=False))
    else:
        new_lines.append(line)

if not found:
    print('ID not found in ledger:', args.id, file=sys.stderr)
    sys.exit(4)

ledger_path.write_text('\n'.join(new_lines) + '\n')
print('Updated ledger for id', args.id)
sys.exit(0)
