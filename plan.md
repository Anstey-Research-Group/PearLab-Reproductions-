# Project Plan (summary)

Recent updates (2026-08-13):

- Added agent-facing skills and wrappers: validate-ledger, claim-cli, generate-run-commands, communication. See skills/ and scripts/skill_*.py for wrappers.
- Skills CI workflow (.github/workflows/skills-ci.yml) runs wrapper smoke tests on PRs and pushes to task/* and automation/* branches.
- Example claim branch created: task/claim-example. Circuit mirror (id: circuit-mirror) claimed by Engineer and status set to in_progress in mirrored_coach_ledger_v3.jsonl.

Next steps:

1. Coach: review circuit-mirror claim in agent_comm_ledger.jsonl (msg-eb3ac2cf) and ACK or propose reassignment.
2. Engineer: continue authoring circuit-docs on branch task/claim-example; push to remote and open PR when ready.
3. Both: finalize message schema and use agent_comm_ledger.jsonl for rapid deliberations. (COMMUNICATION.md updated.)
4. Update protective CI rules (branch protection) to require validate-ledger and skills-ci checks before merge.

Where things live:
- Ledger (architecture): pear_lab_replication_ledger.md
- Mirrored execution ledger: mirrored_coach_ledger_v3.jsonl
- Discussion ledger: agent_comm_ledger.jsonl
- Skills descriptors: skills/*/SKILL.md
- Wrapper scripts: scripts/skill_*.py
- Claim helper: scripts/claim_unclaim.py
- Run commands: .vscode/tasks.json

If you want, I can push the example branch to a remote and open a draft PR (requires remote configured).