Mirrored Coach Ledger Schema

Purpose: define the JSONL schema and validation rules for mirrored_coach_ledger_v2.jsonl

Record fields (per-line JSON object):

- id (string, required): unique identifier for the target
- kind (string, required): "mirror_target" or "child_target"
- source_file (string, required): origin file, e.g., pear_lab_replication_ledger.md
- root_section (string, required): the root section id from the coach ledger
- root_title (string, optional): human-friendly title of the root section
- title (string, required): human-friendly title for this target
- status (string, required): one of ["planned","in_progress","blocked","done"]
- priority (string, optional): one of ["low","medium","high"]
- parent_id (string|null): id of parent mirror target; null for top-level parents
- children (array of strings): list of child ids (empty array if none)
- owner (string|null): owner username or "unassigned"
- last_updated (string, required): ISO-8601 timestamp of last change
- dependencies (array of ids, optional): cross-task sequencing edges (may reference siblings or other child ids)
- summary (object, optional, for parent targets): { total_children:int, completed_children:int, blocked_children:int, last_changed:ISO timestamp }
- notes (string, optional): free-text notes

Validation rules (enforced by validator):
1. Each id must be unique.
2. Each child must have exactly one parent_id and be listed in that parent's children array.
3. No cycles in parent->child relations (acyclic tree structure).
4. Each record must include a non-empty root_source/root_section.
5. Status values must be one of the allowed set.
6. Dependencies may not create cycles across tasks. (Validator reports potential cycles.)

Roll-up rules:
- For each parent target, compute summary: total_children, completed_children (status=="done"), blocked_children (status=="blocked"), last_changed = max(last_updated of parent and children).

Notes on usage:
- Keep this file adjacent to mirrored_coach_ledger_v2.jsonl and re-run the validator after edits.
- The validator writes a roll-up summary file mirrored_coach_ledger_summary.json.
