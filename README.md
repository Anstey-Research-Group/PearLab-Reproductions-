# PEAR Lab Replication

This repository is a learning-oriented, documentation-first project for capturing and organizing a PEAR Lab-style plant anomaly experiment. It is meant to be clear, reproducible, and easy to extend as the project evolves.

## Purpose

The goal of this repository is to turn a speculative experiment into a structured, reviewable artifact. It includes:

- a narrative experimental ledger,
- a concrete firmware sketch for the Arduino implementation,
- and a lightweight development tracker for improving the repository itself.

## Repository layout

- `pear_lab_replication_ledger.md` — the main experimental framework, BOM, circuit notes, and test protocol.
- `firmware/plant_anomaly.ino` — the Arduino sketch derived from the ledger.
- `repo_development_targets.jsonl` — a JSONL ledger of repository development tasks and status, with each target traced back to a source section in the coach ledger.
- `mirrored_coach_ledger.jsonl` — a structured mirror of the coach ledger's major sections, including parent targets and child subtasks for each mirrored area.
- `CONTRIBUTING.md` — guidance for making changes.
- `CHANGELOG.md` — a short history of notable repository updates.

## Current status

This repository is intentionally simple and educational. It is not presented as a validated scientific result; it is a structured baseline for discussion, replication, and refinement.

## Usage

1. Read the experimental ledger to understand the setup and rationale.
2. Review the firmware sketch in `firmware/plant_anomaly.ino`.
3. Build the described circuit and run the protocol carefully.
4. Record observations and results in a separate data folder or log file as the experiment progresses.

## Safety and scope notes

- Treat this as a hands-on educational project rather than a proven scientific method.
- Exercise normal caution with mains-powered hardware and electronic assemblies.
- Keep the experiment focused on reproducibility and documentation rather than claiming a result too early.

## Contributing

See `CONTRIBUTING.md` for guidance on improving the repository.
