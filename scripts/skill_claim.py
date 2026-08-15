#!/usr/bin/env python3
"""
skill_claim.py
Wrapper for the claim/unclaim CLI to expose the claim skill.
"""
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Wrapper: claim or unclaim a mirrored ledger child task')
parser.add_argument('action', choices=['claim','unclaim'])
parser.add_argument('child_id')
parser.add_argument('--owner', required=True, help='Owner name')
parser.add_argument('--message', help='Optional claim note')
args = parser.parse_args()

cmd = ['python3', 'scripts/claim_unclaim.py', args.action, args.child_id, '--owner', args.owner]
if args.message:
    cmd += ['--message', args.message]

rc = subprocess.call(cmd)
if rc != 0:
    print('Claim CLI failed with exit code', rc, file=sys.stderr)
sys.exit(rc)
