#!/usr/bin/env python3
"""
skill_communication.py
Small helper to post/read messages to the agent_comm_ledger.jsonl with the recommended minimal decision schema.
"""
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Post or read messages to the agent_comm_ledger.jsonl')
subparsers = parser.add_subparsers(dest='cmd')

post = subparsers.add_parser('post')
post.add_argument('--from', dest='frm', required=True)
post.add_argument('--to', dest='to', default='all')
post.add_argument('--subject', required=True)
post.add_argument('--body', required=True)
post.add_argument('--refs', nargs='*', default=[])
post.add_argument('--decision_id', help='Optional decision id')
post.add_argument('--owner', help='Owner for follow-up')

read = subparsers.add_parser('read')
read.add_argument('--since', help='ISO timestamp to filter from')

args = parser.parse_args()

if args.cmd == 'post':
    # Build agent_post_message.py invocation
    cmd = ['python3', 'scripts/agent_post_message.py', '--from', args.frm, '--to', args.to, '--subject', args.subject, '--body', args.body, '--refs', ','.join(args.refs)]
    # optional fields appended to body for decision schema
    if args.decision_id or args.owner:
        extra = '\n\nDecision metadata:\n'
        if args.decision_id:
            extra += f"decision_id: {args.decision_id}\n"
        if args.owner:
            extra += f"owner: {args.owner}\n"
        cmd += ['--body', args.body + extra]

    rc = subprocess.call(cmd)
    sys.exit(rc)

elif args.cmd == 'read':
    cmd = ['python3', 'scripts/agent_read_messages.py']
    if args.since:
        cmd += ['--since', args.since]
    rc = subprocess.call(cmd)
    sys.exit(rc)

else:
    parser.print_help()
    sys.exit(1)
