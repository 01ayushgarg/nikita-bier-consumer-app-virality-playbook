#!/usr/bin/env python3
"""Check local documentation links and required thin agent adapters (stdlib only)."""
import re
from pathlib import Path
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
adapters = ['cursor-rules.md', 'github-copilot-instructions.md', 'windsurf-rules.md',
            'cline-roo-rules.md', 'gemini.md', 'opencode-instructions.md', 'aider-conventions.md']
errors = []
for name in adapters:
    path = root / 'agents' / name
    if not path.is_file():
        errors.append(f'Missing adapter: {path.relative_to(root)}')
        continue
    text = path.read_text()
    for required in ['SKILL.md', 'references/benchmarks.md',
                     'references/12-positive-design-and-guardrails.md', 'source IDs',
                     'our reading', 'our suggestion']:
        if required not in text:
            errors.append(f'{name}: missing delegation requirement {required}')
count = 0
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', path.read_text()):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        target = unquote(target.split('#')[0])
        if not target:
            continue
        count += 1
        if not (path.parent / target).exists():
            errors.append(f'{path.relative_to(root)}: broken local link {target}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(adapters)} thin adapters and {count} local Markdown link targets')
