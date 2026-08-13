Agent communication ledger (rapid back-and-forth)

Purpose

This file and tooling enable quick, structured messages between the engineer agent and the coach agent using a JSONL ledger as the canonical channel. Use this for short, auditable exchanges tied to ledger ids or tasks.

Files

- agent_comm_ledger.jsonl  — the canonical JSONL message file. Each line is one JSON object.
- scripts/agent_post_message.py — append a message from an agent to the ledger.
- scripts/agent_read_messages.py — read and print messages from the ledger.

Message format (per-line JSON object)

- id (string): unique message id (msg-...)
- timestamp (ISO-8601 string)
- from (string): agent identifier (e.g., engineer-bot, coach-bot)
- to (string): recipient identifier (or 'all')
- subject (string)
- status (string): open / ack / closed / archived
- refs (array of strings): related ledger ids or file refs (e.g., mirrored_coach_ledger_v3)
- body (string): free-text content

Working conventions

- Short messages only: use the ledger for quick confirmations, claims, or short questions. Use issues/PRs for longer discussions.
- When claiming a task, post a message with refs containing the child id and set owner in mirrored_coach_ledger_v3.jsonl.
- Agents should read the ledger frequently and reply with an ack message when they take action.
- Keep messages concise and link to specific ledger ids.

Example

Engineer posts:
  scripts/agent_post_message.py --from engineer-bot --to coach-bot --subject "Claiming hardware-bom-docs" --body "Claiming hardware-bom-docs; will produce BOM doc by EOD" --refs hardware-bom-docs

Coach replies:
  scripts/agent_post_message.py --from coach-bot --to engineer-bot --subject "ACK Claim" --body "Acknowledged; please ensure procurement notes are included" --refs hardware-bom-docs

Notes

- The ledger is append-only for message history. If a message must be updated, append a follow-up message that references the original id and changes status. Do not edit past lines except for cleanup or archival by agreement.
