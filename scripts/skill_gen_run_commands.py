#!/usr/bin/env python3
"""
skill_gen_run_commands.py
Wrapper to show or update recommended .vscode run commands for agents. By default prints the recommended tasks and their commands.
"""
import json
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Show recommended run commands for Agents')
parser.add_argument('--show', action='store_true', help='Print recommended tasks')
parser.add_argument('--write', action='store_true', help='Write recommended tasks to .vscode/tasks.json (merge mode)')
args = parser.parse_args()

recommended = {
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Validate mirrored ledger",
            "type": "shell",
            "command": "python3 scripts/skill_validate.py mirrored_coach_ledger_v3.jsonl",
            "presentation": {"reveal": "always"},
            "inAgents": True
        },
        {
            "label": "Read agent messages",
            "type": "shell",
            "command": "python3 scripts/agent_read_messages.py",
            "presentation": {"reveal": "always"},
            "inAgents": True
        },
        {
            "label": "Show ledger summary",
            "type": "shell",
            "command": "python3 -c \"import pathlib; p=pathlib.Path('mirrored_coach_ledger_summary.json'); print(p.read_text() if p.exists() else 'No summary available')\"",
            "presentation": {"reveal": "always"},
            "inAgents": True
        }
    ]
}

if args.show:
    print(json.dumps(recommended, indent=2))

if args.write:
    dst = Path('.vscode')
    dst.mkdir(exist_ok=True)
    out = dst / 'tasks.json'
    # Simple merge: overwrite or create
    out.write_text(json.dumps(recommended, indent=2))
    print('Wrote', out)
