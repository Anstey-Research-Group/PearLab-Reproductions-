#!/usr/bin/env python3
"""
skill_validate.py
Wrapper for the ledger validator to expose a uniform skill CLI.
"""
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Wrapper: validate mirrored ledger')
parser.add_argument('ledger', nargs='?', default='mirrored_coach_ledger_v3.jsonl', help='Path to ledger JSONL')
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()

cmd = ['python3', 'scripts/validate_mirrored_ledger.py', args.ledger]
if args.verbose:
    print('Running:', ' '.join(cmd))

rc = subprocess.call(cmd)
if rc != 0:
    print('Validator failed with exit code', rc, file=sys.stderr)
sys.exit(rc)
