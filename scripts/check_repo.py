"""Offline structural/integrity checks for the editorial archive."""
from __future__ import annotations
import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check_hashes() -> None:
    path = ROOT / 'reproducibility/source_file_hashes.csv'
    with path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 5, 'Expected five preserved source records'
    for row in rows:
        target = ROOT / row['path']
        assert target.exists(), f'Missing original source record: {target}'
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        assert actual == row['sha256'], f'Frozen source changed: {row["path"]}'


def check_manifests() -> None:
    with (ROOT / 'reproducibility/checkpoint_manifest.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert rows, 'Missing checkpoint manifest'
    for row in rows:
        assert row['present_in_repo'] in ('true', 'false')
        assert row['status'] in ('included', 'missing')
        if row['present_in_repo'] == 'false':
            assert row['status'] == 'missing'


def check_links() -> None:
    # Markdown inline local links; images in the retained original note are known
    # absent and their absence must stay explicit until original figures arrive.
    excluded = {ROOT/'paper/nca_fold_case_study/RESEARCH_NOTE.md'}
    # The archived NCA note links to a missing original empirical PNG.
    # Image links are intentionally not tested as normal Markdown links.
    missing = []
    for path in ROOT.rglob('*.md'):
        if path in excluded:
            continue
        content = path.read_text(encoding='utf-8')
        for raw in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if raw.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            target = raw.split('#', 1)[0].strip()
            if target and not (path.parent / target).exists():
                missing.append(f'{path.relative_to(ROOT)} -> {target}')
    assert not missing, 'Broken internal Markdown links: ' + '; '.join(missing)


def check_all() -> None:
    check_hashes()
    check_manifests()
    check_links()


if __name__ == '__main__':
    check_all()
    print('PASS: 5 frozen source hashes, checkpoint manifest, and local Markdown links')
