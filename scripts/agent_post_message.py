#!/usr/bin/env python3
"""Append a JSONL message to agent_comm_ledger.jsonl.
Usage:
  scripts/agent_post_message.py --from engineer-bot --to coach-bot --subject "..." --body "..." --refs mirrored_coach_ledger_v3
"""
import argparse
import json
import os
import uuid
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, 'agent_comm_ledger.jsonl')

parser = argparse.ArgumentParser()
parser.add_argument('--from', dest='frm', required=True)
parser.add_argument('--to', required=True)
parser.add_argument('--subject', required=True)
parser.add_argument('--body', required=True)
parser.add_argument('--refs', nargs='*', default=[])
args = parser.parse_args()

msg = {
    'id': f'msg-{uuid.uuid4().hex[:8]}',
    'timestamp': datetime.now().astimezone().isoformat(),
    'from': args.frm,
    'to': args.to,
    'subject': args.subject,
    'status': 'open',
    'refs': args.refs,
    'body': args.body
}

with open(LEDGER, 'a') as f:
    f.write(json.dumps(msg) + '\n')

print(json.dumps(msg, indent=2))
