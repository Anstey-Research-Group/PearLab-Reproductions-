Title: [Draft] Claim: Author circuit docs (circuit-mirror)

Branch: task/claim-example

Summary

This draft PR demonstrates the claim workflow. Changes in this branch:

- Claim: mirrored_coach_ledger_v3.jsonl updated for id `circuit-mirror` to set owner="Engineer" and status="in_progress".
- Added/updated documentation draft: docs/circuit-docs.md (initial draft for circuit stages and testing notes).
- plan.md updated with recent progress and next steps.

Why

The engineer claims the circuit-mirror task to author the circuit documentation and produce an SVG diagram for review. This PR is intended as a small, focused example of the claim+workflow and should be used as a template for future claim PRs.

How to review

- Verify mirrored_coach_ledger_v3.jsonl change only touches the owner/status/last_updated for the claimed id.
- Review docs/circuit-docs.md for completeness and safety notes.
- Coach should ACK in agent_comm_ledger.jsonl (reference msg-eb3ac2cf) or propose reassignment.

Notes

- This branch is prepared locally. No remote push was performed from this worktree. If you want this pushed and a draft PR opened on a remote, provide the remote URL or confirm adding 'origin'.

