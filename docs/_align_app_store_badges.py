#!/usr/bin/env python3
"""Split App Store badges into a dedicated subgrid row on catalog cards."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent
LANGS = ["es", "en", "fr", "de", "ca", "gl", "eu"]

CTA_BLOCK = re.compile(
    r'(<div class="app-card-actions">\s*'
    r'<p class="app-card-store-hint">[\s\S]*?</p>\s*)'
    r'<div class="app-card-cta">\s*'
    r'(<a class="store-badge-link" href="https://apple\.co/[\s\S]*?</a>\s*)'
    r'([\s\S]*?)'
    r'</div>\s*'
    r'</div>',
    re.MULTILINE,
)


def transform(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        actions_open = match.group(1)
        badge = match.group(2).strip()
        secondary = match.group(3).strip()
        secondary_block = (
            f'\n            <div class="app-card-cta-secondary">\n              {secondary}\n            </div>'
            if secondary
            else ""
        )
        return (
            f"{actions_open}</div>\n"
            f'            <div class="app-card-badge-row">\n              {badge}\n            </div>{secondary_block}'
        )

    return CTA_BLOCK.sub(repl, text)


def main() -> None:
    for lang in LANGS:
        path = ROOT / lang / "index.html"
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print("updated", path.relative_to(ROOT))
        else:
            print("unchanged", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
