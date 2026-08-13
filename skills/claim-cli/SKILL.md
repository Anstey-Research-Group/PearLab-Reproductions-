# claim-cli

Purpose

Skill describing the claim/unclaim CLI used to claim ledger child tasks. Makes claiming discoverable and documents the intended claim PR flow.

What it does

- Uses scripts/claim_unclaim.py to mark a child task owner, set last_updated, and change status
- Intended to be used in short-lived branches: task/<child-id>-owner
- Optionally opens a small claim PR that updates only owner+status (example flow)

Usage examples

- Claim: python3 scripts/claim_unclaim.py claim <child-id> --owner "Engineer"
- Unclaim: python3 scripts/claim_unclaim.py unclaim <child-id> --owner "Engineer"

Notes

The claim CLI should be idempotent and minimal — only change owner and last_updated and validate the child id exists in mirrored_coach_ledger_v3.jsonl.