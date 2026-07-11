#!/usr/bin/env python3
"""Replace custom App Store buttons with the official en-US badge."""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
LANGS = ["es", "en", "fr", "de", "ca", "gl", "eu"]
BADGE = "../assets/images/download-on-the-app-store-en-us-white.svg"
IMG = (
    f'<img src="{BADGE}" alt="Download on the App Store" width="120" height="40" '
    f'loading="lazy" decoding="async">'
)


def badge(url: str, aria: str, wrapped: bool = False) -> str:
    aria = html.escape(aria.strip(), quote=True)
    link = (
        f'<a class="store-badge-link" href="{url}" target="_blank" rel="noopener noreferrer" '
        f'aria-label="{aria}">{IMG}</a>'
    )
    return f"<p>{link}</p>" if wrapped else link


def transform(text: str) -> str:
    if "download-on-the-app-store-en-us-white.svg" in text and "btn-app-store" not in text:
        # Still replace plain btn-primary apple.co links if any remain.
        pass

    # Multiline btn-app-store (accesible hero).
    text = re.sub(
        r'<a class="btn btn-primary btn-app-store" href="([^"]+)" target="_blank" rel="noopener noreferrer">\s*'
        r'<span class="btn-app-store-title">[^<]*</span>\s*'
        r'<span class="btn-app-store-sub">([^<]*)</span>\s*</a>',
        lambda m: badge(m.group(1), m.group(2) or "Download on the App Store"),
        text,
        flags=re.DOTALL,
    )

    # Single-line btn-app-store (catalog cards).
    text = re.sub(
        r'<a class="btn btn-primary btn-app-store" href="([^"]+)" target="_blank" rel="noopener noreferrer">'
        r'<span class="btn-app-store-title">[^<]*</span>'
        r'<span class="btn-app-store-sub">([^<]*)</span></a>',
        lambda m: badge(m.group(1), m.group(2) or "Download on the App Store"),
        text,
    )

    # Paragraph-wrapped primary button to App Store.
    text = re.sub(
        r'<p><a class="btn btn-primary" href="(https://apple\.co/[^"]+)" target="_blank" rel="noopener noreferrer">'
        r'([^<]+)</a></p>',
        lambda m: badge(m.group(1), m.group(2), wrapped=True),
        text,
    )

    # Inline primary button to App Store (CTA rows).
    text = re.sub(
        r'<a class="btn btn-primary" href="(https://apple\.co/[^"]+)" target="_blank" rel="noopener noreferrer">'
        r'([^<]+)</a>',
        lambda m: badge(m.group(1), m.group(2)),
        text,
    )

    return text


def main() -> None:
    changed = 0
    for lang in LANGS:
        for path in sorted((ROOT / lang).glob("*.html")):
            original = path.read_text(encoding="utf-8")
            updated = transform(original)
            if updated != original:
                path.write_text(updated, encoding="utf-8")
                changed += 1
                print("updated", path.relative_to(ROOT))
    print("files changed:", changed)


if __name__ == "__main__":
    main()
