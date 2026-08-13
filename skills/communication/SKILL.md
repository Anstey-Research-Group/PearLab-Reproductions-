# communication

Purpose

Document the agent-to-agent ledger communication conventions and provide a discoverable skill for posting/reading structured messages from the discussion ledger.

What it does

- Documents the agent_comm_ledger.jsonl message format and decision schema
- Points to scripts/agent_post_message.py and scripts/agent_read_messages.py
- Recommends common workflows for claims, acknowledgements, and semantic reviews

Usage examples

- Post a message (direct): python3 scripts/agent_post_message.py --from engineer-bot --to coach-bot --subject "..." --body "..." --refs "task-id"
- Post a message (wrapper): python3 scripts/skill_communication.py post --from engineer-bot --to coach-bot --subject "..." --body "..." --refs task-id --decision_id dec-001 --owner "Engineer"
- Read messages: python3 scripts/agent_read_messages.py --since "2026-01-01T00:00:00Z"
- Read messages (wrapper): python3 scripts/skill_communication.py read --since "2026-01-01T00:00:00Z"

Notes

This SKILL.md is a documentation entry; the ledger scripts are the operational pieces.