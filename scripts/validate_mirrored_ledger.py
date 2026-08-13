#!/usr/bin/env python3
"""
Validator for a mirrored ledger JSONL file.
Usage: validate_mirrored_ledger.py [path/to/ledger.jsonl]
If no path is given, defaults to mirrored_coach_ledger_v2.jsonl in repo root.
"""
import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
LEDGER = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'mirrored_coach_ledger_v2.jsonl'
SUMMARY_OUT = ROOT / 'mirrored_coach_ledger_summary.json'

ALLOWED_STATUS = {'planned','in_progress','blocked','done'}


def load_items(path):
    items = []
    with path.open() as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def validate_uniqueness(items):
    ids = [it['id'] for it in items]
    dupes = set([x for x in ids if ids.count(x) > 1])
    if dupes:
        raise SystemExit(f'Duplicate ids found: {dupes}')


def validate_children_have_parent(items, id_map):
    for it in items:
        for child_id in it.get('children', []):
            if child_id not in id_map:
                raise SystemExit(f'Parent {it["id"]} references missing child {child_id}')
            child = id_map[child_id]
            if child.get('parent_id') != it['id']:
                raise SystemExit(f'Child {child_id} parent_id mismatch (expected {it["id"]}, got {child.get("parent_id")})')


def validate_child_single_parent(items):
    parent_of = {}
    for it in items:
        for child in it.get('children', []):
            parent_of.setdefault(child, []).append(it['id'])
    for child, parents in parent_of.items():
        if len(parents) != 1:
            raise SystemExit(f'Child {child} listed under multiple parents: {parents}')


def detect_cycles(items):
    id_map = {it['id']: it for it in items}
    visited = set()
    recstack = set()

    def dfs(node):
        if node in recstack:
            return [node]
        if node in visited:
            return None
        visited.add(node)
        recstack.add(node)
        node_children = id_map[node].get('children', [])
        for c in node_children:
            path = dfs(c)
            if path:
                path.append(node)
                return path
        recstack.remove(node)
        return None

    for it in items:
        path = dfs(it['id'])
        if path:
            path.reverse()
            raise SystemExit(f'Cycle detected in parent-child graph: {path}')


def validate_root_trace(items):
    for it in items:
        if not it.get('source_file') or not it.get('root_section'):
            raise SystemExit(f'Item {it["id"]} missing root trace (source_file/root_section)')


def validate_status_values(items):
    for it in items:
        if it.get('status') not in ALLOWED_STATUS:
            raise SystemExit(f'Item {it["id"]} has invalid status: {it.get("status")}')


def validate_dependencies_no_cycles(items):
    # build dependency graph and detect cycles
    id_map = {it['id']: it for it in items}
    graph = {it['id']: set(it.get('dependencies', [])) for it in items}
    # simple DFS
    visited = set()
    recstack = set()

    def dfs(node):
        if node in recstack:
            return [node]
        if node in visited:
            return None
        visited.add(node)
        recstack.add(node)
        for c in graph.get(node, []):
            if c not in id_map:
                raise SystemExit(f'Dependency {c} referenced by {node} does not exist')
            path = dfs(c)
            if path:
                path.append(node)
                return path
        recstack.remove(node)
        return None

    for n in graph:
        path = dfs(n)
        if path:
            path.reverse()
            raise SystemExit(f'Dependency cycle detected: {path}')


def compute_rollups(items):
    id_map = {it['id']: it for it in items}
    parents = [it for it in items if it.get('parent_id') is None]
    summary = {}
    for p in parents:
        children = [id_map[cid] for cid in p.get('children', [])]
        total = len(children)
        completed = sum(1 for c in children if c.get('status') == 'done')
        blocked = sum(1 for c in children if c.get('status') == 'blocked')
        times = []
        for x in ([p] + children):
            t = x.get('last_updated')
            if t:
                try:
                    times.append(datetime.fromisoformat(t))
                except Exception:
                    pass
        last_changed = max(times).isoformat() if times else None
        summary[p['id']] = {'total_children': total, 'completed_children': completed, 'blocked_children': blocked, 'last_changed': last_changed}
    return summary


def main():
    items = load_items(LEDGER)
    validate_uniqueness(items)
    id_map = {it['id']: it for it in items}
    validate_children_have_parent(items, id_map)
    validate_child_single_parent(items)
    detect_cycles(items)
    validate_root_trace(items)
    validate_status_values(items)
    validate_dependencies_no_cycles(items)
    summary = compute_rollups(items)
    with SUMMARY_OUT.open('w') as f:
        json.dump(summary, f, indent=2)
    print('Validation passed; summary written to', SUMMARY_OUT)

if __name__ == '__main__':
    main()
