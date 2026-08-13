#!/usr/bin/env python3
"""Read and print messages from agent_comm_ledger.jsonl.
Usage:
  scripts/agent_read_messages.py [--all]
By default prints messages with status != 'archived'
"""
import json
import os
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, 'agent_comm_ledger.jsonl')

parser = argparse.ArgumentParser()
parser.add_argument('--all', action='store_true')
args = parser.parse_args()

if not os.path.exists(LEDGER):
    print('No ledger found at', LEDGER)
    raise SystemExit(1)

with open(LEDGER) as f:
    for line in f:
        line=line.strip()
        if not line:
            continue
        msg = json.loads(line)
        if args.all or msg.get('status') != 'archived':
            print(json.dumps(msg, indent=2))
