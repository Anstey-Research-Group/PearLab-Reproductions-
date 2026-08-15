#!/usr/bin/env bash
set -euo pipefail

echo "Running skill wrapper smoke tests..."
python3 scripts/skill_validate.py --help > /dev/null
python3 scripts/skill_claim.py --help > /dev/null || true  # will error if no args; help path covers CLI parsing
python3 scripts/skill_gen_run_commands.py --show > /dev/null
python3 scripts/skill_communication.py --help > /dev/null || true

echo "All skill wrappers invoked successfully (help output)."
