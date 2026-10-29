#!/usr/bin/env python3
"""Regroup site nav by app family and rename Stage Recorder → Stage Multitrack."""
from __future__ import annotations

import html as htmlmod
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]

# Localized chrome for nav (not product names)
NAV_UI = {
    "es": {
        "aria": "Principal",
        "home": "Inicio",
        "audio": "Audio",
        "midi": "MIDI / OSC",
        "rf": "RF",
        "access": "Accesibilidad",
        "proj": "Proyectores y pantalla",
        "patch": "Patch y routing",
        "rehearsal": "Ensayo actoral",
        "compare": "Comparativa",
        "resources": "Recursos",
        "faq": "FAQ",
        "support": "Soporte",
    },
    "en": {
        "aria": "Main",
        "home": "Home",
        "audio": "Audio",
        "midi": "MIDI / OSC",
        "rf": "RF",
        "access": "Accessibility",
        "proj": "Projectors & screen",
        "patch": "Patch & routing",
        "rehearsal": "Acting rehearsal",
        "compare": "Compare",
        "resources": "Resources",
        "faq": "FAQ",
        "support": "Support",
    },
    "fr": {
        "aria": "Principal",
        "home": "Accueil",
        "audio": "Audio",
        "midi": "MIDI / OSC",
        "rf": "RF",
        "access": "Accessibilité",
        "proj": "Projecteurs et écran",
        "patch": "Patch et routing",
        "rehearsal": "Répétition théâtre",
        "compare": "Comparatif",
        "resources": "Ressources",
        "faq": "FAQ",
        "support": "Support",
    },
    "de": {
        "aria": "Hauptnavigation",
        "home": "Start",
        "audio": "Audio",
        "midi": "MIDI / OSC",
        "rf": "RF",
        "access": "Barrierefreiheit",
        "proj": "Projektoren & Bildschirm",
        "patch": "Patch & Routing",
        "rehearsal": "Schauspiel-Probe",
        "compare": "Vergleich",
        "resources": "Ressourcen",
        "faq": "FAQ",
        "support": "Support",
    },
    "gl": {
        "aria": "Principal",
        "home": "Inicio",
        "audio": "Audio",
        "midi": "MIDI / OSC",
        "rf": "RF",
        "access": "Accesibilidade",
        "proj": "Proxectores e pantalla",
        "patch": "Patch e routing",
        "rehearsal": "Ensaio actoral",
        "compare": "Comparativa",
        "resources": "Recursos",
        "faq": "FAQ",
        "support": "Soporte",
    },
    "ca": {
        "aria": "Principal",
        "home": "Inici",
        "audio": "Àudio",
        "midi": "MIDI / OSC",
        "rf": "RF",
        "access": "Accessibilitat",
        "proj": "Projectors i pantalla",
        "patch": "Patch i routing",
        "rehearsal": "Assaig actoral",
        "compare": "Comparativa",
        "resources": "Recursos",
        "faq": "FAQ",
        "support": "Suport",
    },
    "eu": {
        "aria": "Nagusia",
        "home": "Hasiera",
        "audio": "Audioa",
        "midi": "MIDI / OSC",
        "rf": "RF",
        "access": "Irisgarritasuna",
        "proj": "Proiektoreak eta pantaila",
        "patch": "Patch eta routing",
        "rehearsal": "Antzezlan entsegua",
        "compare": "Konparaketa",
        "resources": "Baliabideak",
        "faq": "FAQ",
        "support": "Laguntza",
    },
}

# Family order for orbit / compare
FAMILY_ORDER = [
    "Stage Multitrack",
    "Stage Edit",
    "MIDItoOSC",
    "Stage RF",
    "Accesible",
    "Shutter PJ-OSC",
    "Shutter PJLINK",
    "Transparent Screen",
    "Easy Routing",
    "M32 Patch",
    "Stage With Me",
]

NAV_RE = re.compile(
    r'<nav class="nav" aria-label="[^"]*">\s*.*?</nav>',
    re.S,
)


def current_mark(href: str, current_file: str) -> str:
    return ' aria-current="page"' if Path(current_file).name == href else ""


def build_nav(lang: str, current_file: str) -> str:
    ui = NAV_UI[lang]
    cur = Path(current_file).name

    def link(href: str, label: str) -> str:
        return f'<a href="{href}"{current_mark(href, cur)}>{label}</a>'

    def group(summary: str, items: list[tuple[str, str]]) -> str:
        links = "\n              ".join(link(h, lab) for h, lab in items)
        return (
            f'<details class="nav-group">\n'
            f"            <summary>{summary}</summary>\n"
            f'            <div class="nav-group-menu">\n'
            f"              {links}\n"
            f"            </div>\n"
            f"          </details>"
        )

    parts = [
        link("index.html", ui["home"]),
        group(
            ui["audio"],
            [
                ("stage-multitrack.html", "Stage Multitrack"),
                ("stage-edit.html", "Stage Edit"),
            ],
        ),
        link("miditoosc.html", ui["midi"]),
        link("stage-rf.html", ui["rf"]),
        link("accesible.html", ui["access"]),
        group(
            ui["proj"],
            [
                ("shutter-pj-osc.html", "Shutter PJ-OSC"),
                ("shutter-pjlink-ios.html", "Shutter PJLINK"),
                ("transparent-screen.html", "Transparent Screen"),
            ],
        ),
        group(
            ui["patch"],
            [
                ("easy-routing-m32-x32.html", "Easy Routing"),
                ("m32-patch.html", "M32 Patch"),
            ],
        ),
        link("stage-with-me.html", ui["rehearsal"]),
        link("compare.html", ui["compare"]),
        link("resources.html", ui["resources"]),
        link("faq.html", ui["faq"]),
        link("support.html", ui["support"]),
    ]
    inner = "\n            ".join(parts)
    return f'<nav class="nav" aria-label="{ui["aria"]}">\n            {inner}\n          </nav>'


def replace_nav(html: str, lang: str, path: Path) -> str:
    if not NAV_RE.search(html):
        return html  # preview stubs / pages without site chrome
    nav = build_nav(lang, path.name)
    new, n = NAV_RE.subn(nav, html, count=1)
    if n != 1:
        raise SystemExit(f"nav replace failed ({n}): {path}")
    return new


def bump_styles(html: str) -> str:
    return re.sub(r"styles\.css\?v=\d+", "styles.css?v=36", html)


def rename_copy_in_text(text: str) -> str:
    # Order matters: longer / specific first
    reps = [
        ("Stage Recorder (macOS)", "Stage Multitrack (macOS)"),
        ("Stage Recorder", "Stage Multitrack"),
        ("stage-recorder.html", "stage-multitrack.html"),
        # Keep image filenames
    ]
    # Don't rewrite image paths that contain stage-recorder-square
    out = text
    for old, new in reps:
        if old == "stage-recorder.html":
            # replace href/links but not if already in redirect stub content carefully
            out = out.replace(old, new)
        else:
            out = out.replace(old, new)
    # Restore image paths if accidentally changed (Stage Multitrack-square shouldn't exist)
    out = out.replace(
        "stage-multitrack-square-1080.png",
        "stage-recorder-square-1080.png",
    )
    return out


def migrate_multitrack_pages() -> None:
    for lang in LANGS:
        src = DOCS / lang / "stage-recorder.html"
        dst = DOCS / lang / "stage-multitrack.html"
        if dst.exists() and src.exists() and 'http-equiv="refresh"' in src.read_text(encoding="utf-8"):
            print("multitrack already", lang)
            continue
        if dst.exists() and not src.exists():
            print("already", lang)
            continue
        if not src.exists():
            raise SystemExit(f"missing {src}")
        content = src.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in content:
            # Stub already; need original from dst if present
            if dst.exists():
                print("multitrack already", lang)
                continue
            raise SystemExit(f"recorder is stub but no multitrack: {src}")
        content = rename_copy_in_text(content)
        # Fix hreflang links
        content = content.replace(
            f'href="../{lang}/stage-multitrack.html"',
            f'href="../{lang}/stage-multitrack.html"',
        )
        for L in LANGS:
            content = content.replace(
                f'href="../{L}/stage-recorder.html"',
                f'href="../{L}/stage-multitrack.html"',
            )
            content = content.replace(
                f'href="{L}/stage-recorder.html"',
                f'href="{L}/stage-multitrack.html"',
            )
        # Self-relative alternate for current lang
        content = re.sub(
            r'hreflang="' + lang + r'" href="[^"]*stage-(?:recorder|multitrack)\.html"',
            f'hreflang="{lang}" href="../{lang}/stage-multitrack.html"',
            content,
        )
        content = bump_styles(content)
        dst.write_text(content, encoding="utf-8")

        # Redirect stub
        stub = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=stage-multitrack.html">
  <link rel="canonical" href="stage-multitrack.html">
  <title>Stage Multitrack — Stage Apps</title>
  <script>location.replace("stage-multitrack.html");</script>
</head>
<body>
  <p><a href="stage-multitrack.html">Stage Multitrack</a></p>
</body>
</html>
"""
        src.write_text(stub, encoding="utf-8")
        print("multitrack page", lang)


def reorder_apps(apps: list[dict]) -> list[dict]:
    # Rename Stage Recorder → Stage Multitrack in data
    for a in apps:
        if a.get("name") == "Stage Recorder":
            a["name"] = "Stage Multitrack"
        if a.get("href") == "stage-recorder.html":
            a["href"] = "stage-multitrack.html"
        # blurbs that say Recorder as product name — handled by string replace later
    by_name = {a["name"]: a for a in apps}
    ordered = []
    for name in FAMILY_ORDER:
        if name in by_name:
            ordered.append(by_name.pop(name))
    ordered.extend(by_name.values())
    return ordered


PLANET_ORDER = [
    ("Stage Multitrack", "stage-recorder-square-1080.png"),
    ("Stage Edit", "stage-edit-square-1080.png"),
    ("MIDItoOSC", "miditoosc-square-1080.png?v=2"),
    ("Stage RF", "stage-rf-square-1080.png"),
    ("Accesible", "accesible-square-1080.png"),
    ("Shutter PJ-OSC", "shutter-pj-osc-square-1080.png"),
    ("Shutter PJLINK", "shutter-pjlink-square-1080.png"),
    ("Transparent Screen", "transparent-screen-square-1080.png"),
    ("Easy Routing", "m32-x32-easy-routing-square-1080.png?v=1"),
    ("M32 Patch", "m32-patch-square-1080.png?v=1"),
    ("Stage With Me", "stage-with-me-square-1080.png"),
]


def rebuild_planets(html: str) -> str:
    buttons = []
    for i, (name, img) in enumerate(PLANET_ORDER):
        active = ' class="app-orbit-planet is-active"' if i == 0 else ' class="app-orbit-planet"'
        aria_cur = ' aria-current="true"' if i == 0 else ""
        src = f"../assets/images/{img}"
        buttons.append(
            f'<button type="button"{active} data-orbit-planet aria-label="{name}"{aria_cur}>'
            f'<img src="{src}" alt=""></button>'
        )
    block = "\n              ".join(buttons)
    # Replace all planet buttons inside the ring
    pattern = re.compile(
        r'(<div class="app-orbit-ring"[^>]*>)\s*(?:<button type="button" class="app-orbit-planet[\s\S]*?</button>\s*)+',
        re.S,
    )

    def repl(m: re.Match) -> str:
        return m.group(1) + "\n              " + block + "\n\n              "

    new, n = pattern.subn(repl, html, count=1)
    if n != 1:
        raise SystemExit(f"planet rebuild failed ({n})")
    return new


def reorder_compare(html: str, lang: str) -> str:
    # Extract tbody rows and reorder by known app names
    m = re.search(r"(<tbody>\s*)(.*?)(\s*</tbody>)", html, re.S)
    if not m:
        return html
    rows = re.findall(r"<tr>.*?</tr>", m.group(2), re.S)
    by_name = {}
    for row in rows:
        mm = re.search(r"<td>([^<]+)</td>", row)
        if mm:
            by_name[mm.group(1).strip()] = row
    # Map old name
    if "Stage Recorder" in by_name and "Stage Multitrack" not in by_name:
        by_name["Stage Multitrack"] = by_name.pop("Stage Recorder").replace(
            "Stage Recorder", "Stage Multitrack"
        )
    elif "Stage Multitrack" in by_name:
        pass
    ordered_rows = []
    for name in FAMILY_ORDER:
        # Compare table uses slightly different names for some apps
        aliases = {
            "Easy Routing": ["M32 / X32 Easy Routing", "Easy Routing"],
            "Accesible": ["Accesible"],
            "Stage Multitrack": ["Stage Multitrack", "Stage Recorder"],
        }
        keys = aliases.get(name, [name])
        for k in keys:
            if k in by_name:
                ordered_rows.append(by_name.pop(k))
                break
    ordered_rows.extend(by_name.values())
    body = "\n                ".join(ordered_rows)
    return html[: m.start()] + m.group(1) + body + m.group(3) + html[m.end() :]


def update_js() -> None:
    path = DOCS / "js" / "app-carousel.js"
    js = path.read_text(encoding="utf-8")
    if 'app.name === "Stage Multitrack"' in js and "Multitrack" in js:
        print("js already")
        return
    js = js.replace(
        '''      } else if (app.name === "Stage Recorder") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Recorder"));
      }''',
        '''      } else if (app.name === "Stage Multitrack" || app.name === "Stage Recorder") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Multitrack"));
      }''',
    )
    path.write_text(js, encoding="utf-8")
    print("js ok")


def process_html_file(path: Path, lang: str) -> None:
    text = path.read_text(encoding="utf-8")
    # Skip pure redirect stubs we just wrote (tiny)
    if path.name == "stage-recorder.html" and "http-equiv=\"refresh\"" in text:
        return

    text = rename_copy_in_text(text)
    text = bump_styles(text)
    text = replace_nav(text, lang, path)

    if path.name == "index.html":
        m = re.search(r'data-apps="([^"]+)"', text)
        if m:
            apps = json.loads(htmlmod.unescape(m.group(1)))
            apps = reorder_apps(apps)
            # Soften blurb/detail product name already via rename_copy
            encoded = htmlmod.escape(json.dumps(apps, ensure_ascii=False), quote=True)
            text = text[: m.start(1)] + encoded + text[m.end(1) :]
        text = rebuild_planets(text)
        text = text.replace("app-carousel.js?v=23", "app-carousel.js?v=24")
        text = text.replace("app-carousel.js?v=22", "app-carousel.js?v=24")
        text = text.replace("home-carousel.css?v=48", "home-carousel.css?v=49")
        text = text.replace("home-carousel.css?v=47", "home-carousel.css?v=49")

    if path.name == "compare.html":
        text = reorder_compare(text, lang)

    path.write_text(text, encoding="utf-8")


def main() -> None:
    migrate_multitrack_pages()
    update_js()

    for lang in LANGS:
        lang_dir = DOCS / lang
        for path in sorted(lang_dir.glob("*.html")):
            process_html_file(path, lang)
        print("lang done", lang)

    # Root docs html if any have flat nav
    for path in DOCS.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        if 'class="nav"' in text and "stage-recorder" in text:
            text = rename_copy_in_text(text)
            path.write_text(text, encoding="utf-8")

    # Publish scripts mention Stage Recorder
    skip_scripts = {Path(__file__).name, "reorg_nav_multitrack.py"}
    for script in (ROOT / "scripts").glob("*.py"):
        if script.name in skip_scripts:
            continue
        s = script.read_text(encoding="utf-8")
        if "Stage Recorder" in s or "stage-recorder.html" in s:
            s2 = rename_copy_in_text(s)
            script.write_text(s2, encoding="utf-8")
            print("script", script.name)

    print("DONE")


if __name__ == "__main__":
    main()
