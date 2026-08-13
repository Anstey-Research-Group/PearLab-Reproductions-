# validate-ledger

Purpose

Lightweight skill that wraps the repository's mirrored-ledger validator so agents can run it as a discoverable capability. Useful for CI, PR gating, and local checks.

What it does

- Invokes scripts/validate_mirrored_ledger.py against a given JSONL ledger (default: mirrored_coach_ledger_v3.jsonl)
- Produces a human-friendly summary and exits non-zero on validation errors

Usage examples

- Local: python3 scripts/validate_mirrored_ledger.py mirrored_coach_ledger_v3.jsonl
- CI: .github/workflows/validate-ledger.yml already invokes the validator; this skill documents the command and behavior.

Notes

This SKILL.md is a descriptor only. The actual validator implementation lives at scripts/validate_mirrored_ledger.py and should be kept authoritative.