#!/usr/bin/env python3
"""Mark Stage Audio Edit as live on the Mac App Store across the site."""
from __future__ import annotations

import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]
STORE = "https://apps.apple.com/app/stage-audio-edit/id6824283111?mt=12"
BANNER = "../assets/images/stage-edit-banner-1200x720.png"
ICON = "../assets/images/stage-edit-square-1080.png"
HREF = "stage-edit.html"
NAME = "Stage Audio Edit"

COPY = {
    "es": {
        "meta": "Editor de dos pistas estéreo (L/R) para Mac: grabar, editar ondas y exportar sin un DAW completo.",
        "title": "Stage Audio Edit (macOS) — Stage Apps",
        "h1": "Stage Audio Edit (macOS)",
        "lead": "Stage Audio Edit es un editor de dos pistas estéreo (L/R) para Mac: grabar, editar ondas y exportar sin la complejidad de un DAW completo.",
        "features_h": "Características",
        "features": [
            "Dos pistas L/R con bus de efectos estéreo: ideal para escena, ensayo y podcast.",
            "Captura HAL (AUHAL) estable para tomas largas.",
            "Edición de onda: zoom, selección, cortar/copiar/pegar, fades, ganancia y normalizar.",
            "EQ y reverb offline, reducción de ruido; hasta 6 Audio Units en el bus estéreo.",
            "Importa audio o vídeo y exporta WAV o AIFF; proyectos .stageedit con autosave.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Ya disponible</strong> en la Mac App Store.",
        "store_aria": "Descargar Stage Audio Edit en la App Store",
        "banner_aria": "Stage Audio Edit en la Mac App Store",
        "banner_alt": "Stage Audio Edit — ya en la Mac App Store",
        "icon_alt": "Icono de Stage Audio Edit",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "blurb": "Editor de 2 pistas estéreo para Mac.",
        "detail": "Graba, edita ondas y exporta WAV/AIFF sin un DAW completo. Dos pistas L/R con efectos en bus estéreo. Disponible en la Mac App Store.",
        "compare_best": "Editar dos pistas estéreo (L/R) y exportar WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS",
        "aria_nav": "Principal",
        "nav_home": "Inicio",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_access": "Accesibilidad",
        "nav_proj": "Proyectores y pantalla",
        "nav_patch": "Patch y routing",
        "nav_rehearsal": "Ensayo actoral",
        "nav_compare": "Comparativa",
        "nav_resources": "Recursos",
        "nav_faq": "FAQ",
        "nav_support": "Soporte",
        "lang_label": "Español",
        "lang_emoji": "🇪🇸",
        "aria_lang": "Selector de idioma",
        "privacy": "Privacidad",
        "support": "Soporte",
        "disclaimer": "QLab es una marca de Figure 53. Este sitio y estas apps son productos independientes y no están afiliados, respaldados ni patrocinados por Figure 53.",
        "made": "Software independiente · Santiago de Compostela",
    },
    "en": {
        "meta": "Two-track stereo editor for Mac: record, edit waveforms and export without a full DAW.",
        "title": "Stage Audio Edit (macOS) — Stage Apps",
        "h1": "Stage Audio Edit (macOS)",
        "lead": "Stage Audio Edit is a two-track stereo editor for Mac: record, edit waveforms and export without full DAW complexity.",
        "features_h": "Features",
        "features": [
            "Two L/R tracks with a stereo effects bus: great for stage, rehearsal and podcasts.",
            "Stable HAL (AUHAL) capture for long takes.",
            "Waveform editing: zoom, selection, cut/copy/paste, fades, gain and normalize.",
            "Offline EQ and reverb, noise reduction; up to 6 Audio Units on the stereo bus.",
            "Import audio or video and export WAV or AIFF; .stageedit projects with autosave.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Available now</strong> on the Mac App Store.",
        "store_aria": "Download Stage Audio Edit on the App Store",
        "banner_aria": "Stage Audio Edit on the Mac App Store",
        "banner_alt": "Stage Audio Edit — now on the Mac App Store",
        "icon_alt": "Stage Audio Edit icon",
        "footer_links": '<p><a href="compare.html">Compare apps</a> · <a href="use-cases.html">Use cases</a> · <a href="support.html">Support</a></p>',
        "blurb": "2-track stereo editor for Mac.",
        "detail": "Record, edit waveforms and export WAV/AIFF without a full DAW. Two L/R tracks with stereo-bus effects. Available on the Mac App Store.",
        "compare_best": "Edit two stereo tracks (L/R) and export WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS",
        "aria_nav": "Main",
        "nav_home": "Home",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_access": "Accessibility",
        "nav_proj": "Projectors & screen",
        "nav_patch": "Patch & routing",
        "nav_rehearsal": "Acting rehearsal",
        "nav_compare": "Compare",
        "nav_resources": "Resources",
        "nav_faq": "FAQ",
        "nav_support": "Support",
        "lang_label": "English",
        "lang_emoji": "🇬🇧",
        "aria_lang": "Language selector",
        "privacy": "Privacy",
        "support": "Support",
        "disclaimer": "QLab is a trademark of Figure 53. This site and these apps are independent products and are not affiliated with, endorsed by, or sponsored by Figure 53.",
        "made": "Independent software · Santiago de Compostela",
    },
    "fr": {
        "meta": "Éditeur deux pistes stéréo (L/R) pour Mac : enregistrer, éditer les formes d’onde et exporter sans un DAW complet.",
        "title": "Stage Audio Edit (macOS) — Stage Apps",
        "h1": "Stage Audio Edit (macOS)",
        "lead": "Stage Audio Edit est un éditeur deux pistes stéréo (L/R) pour Mac : enregistrer, éditer les formes d’onde et exporter sans la complexité d’un DAW.",
        "features_h": "Fonctionnalités",
        "features": [
            "Deux pistes L/R avec bus d’effets stéréo : idéal pour la scène, les répétitions et le podcast.",
            "Capture HAL (AUHAL) stable pour les prises longues.",
            "Édition d’onde : zoom, sélection, couper/copier/coller, fades, gain et normalisation.",
            "EQ et réverb hors ligne, réduction de bruit ; jusqu’à 6 Audio Units sur le bus stéréo.",
            "Importez audio ou vidéo et exportez WAV ou AIFF ; projets .stageedit avec autosave.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Déjà disponible</strong> sur le Mac App Store.",
        "store_aria": "Télécharger Stage Audio Edit sur l’App Store",
        "banner_aria": "Stage Audio Edit sur le Mac App Store",
        "banner_alt": "Stage Audio Edit — déjà sur le Mac App Store",
        "icon_alt": "Icône Stage Audio Edit",
        "footer_links": '<p><a href="compare.html">Voir le comparatif</a> · <a href="use-cases.html">Cas d’usage</a> · <a href="support.html">Support</a></p>',
        "blurb": "Éditeur 2 pistes stéréo pour Mac.",
        "detail": "Enregistrez, éditez les formes d’onde et exportez WAV/AIFF sans un DAW complet. Deux pistes L/R avec effets sur bus stéréo. Disponible sur le Mac App Store.",
        "compare_best": "Éditer deux pistes stéréo (L/R) et exporter WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS",
        "aria_nav": "Principal",
        "nav_home": "Accueil",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_access": "Accessibilité",
        "nav_proj": "Projecteurs et écran",
        "nav_patch": "Patch et routing",
        "nav_rehearsal": "Répétition théâtre",
        "nav_compare": "Comparatif",
        "nav_resources": "Ressources",
        "nav_faq": "FAQ",
        "nav_support": "Support",
        "lang_label": "Français",
        "lang_emoji": "🇫🇷",
        "aria_lang": "Sélecteur de langue",
        "privacy": "Confidentialité",
        "support": "Support",
        "disclaimer": "QLab est une marque de Figure 53. Ce site et ces apps sont des produits indépendants et ne sont pas affiliés, cautionnés ni sponsorisés par Figure 53.",
        "made": "Logiciel indépendant · Santiago de Compostela",
    },
    "de": {
        "meta": "Zwei-Spur Stereo-Editor für den Mac: Aufnehmen, Wellenformen bearbeiten und ohne vollen DAW exportieren.",
        "title": "Stage Audio Edit (macOS) — Stage Apps",
        "h1": "Stage Audio Edit (macOS)",
        "lead": "Stage Audio Edit ist ein Zwei-Spur Stereo-Editor für den Mac: Aufnehmen, Wellenformen bearbeiten und ohne DAW-Komplexität exportieren.",
        "features_h": "Funktionen",
        "features": [
            "Zwei L/R-Spuren mit Stereo-Effektbus: ideal für Bühne, Probe und Podcast.",
            "Stabile HAL-(AUHAL)-Aufnahme für lange Takes.",
            "Wellenform-Bearbeitung: Zoom, Auswahl, Ausschneiden/Kopieren/Einfügen, Fades, Gain und Normalisieren.",
            "Offline-EQ und Hall, Rauschunterdrückung; bis zu 6 Audio Units auf dem Stereobus.",
            "Audio oder Video importieren und WAV oder AIFF exportieren; .stageedit-Projekte mit Autosave.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Jetzt verfügbar</strong> im Mac App Store.",
        "store_aria": "Stage Audio Edit im App Store laden",
        "banner_aria": "Stage Audio Edit im Mac App Store",
        "banner_alt": "Stage Audio Edit — jetzt im Mac App Store",
        "icon_alt": "Stage-Audio-Edit-Symbol",
        "footer_links": '<p><a href="compare.html">Vergleich ansehen</a> · <a href="use-cases.html">Anwendungsfälle</a> · <a href="support.html">Support</a></p>',
        "blurb": "2-Spur-Stereo-Editor für Mac.",
        "detail": "Aufnehmen, Wellenformen bearbeiten und WAV/AIFF ohne vollen DAW exportieren. Zwei L/R-Spuren mit Stereo-Bus-Effekten. Im Mac App Store verfügbar.",
        "compare_best": "Zwei Stereo-Spuren (L/R) bearbeiten und WAV/AIFF exportieren",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS",
        "aria_nav": "Hauptnavigation",
        "nav_home": "Start",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_access": "Barrierefreiheit",
        "nav_proj": "Projektoren & Bildschirm",
        "nav_patch": "Patch & Routing",
        "nav_rehearsal": "Schauspiel-Probe",
        "nav_compare": "Vergleich",
        "nav_resources": "Ressourcen",
        "nav_faq": "FAQ",
        "nav_support": "Support",
        "lang_label": "Deutsch",
        "lang_emoji": "🇩🇪",
        "aria_lang": "Sprachauswahl",
        "privacy": "Datenschutz",
        "support": "Support",
        "disclaimer": "QLab ist eine Marke von Figure 53. Diese Website und Apps sind unabhängige Produkte und nicht mit Figure 53 verbunden, von Figure 53 unterstützt oder gesponsert.",
        "made": "Unabhängige Software · Santiago de Compostela",
    },
    "gl": {
        "meta": "Editor de dúas pistas estéreo (L/R) para Mac: gravar, editar ondas e exportar sen un DAW completo.",
        "title": "Stage Audio Edit (macOS) — Stage Apps",
        "h1": "Stage Audio Edit (macOS)",
        "lead": "Stage Audio Edit é un editor de dúas pistas estéreo (L/R) para Mac: gravar, editar ondas e exportar sen a complexidade dun DAW completo.",
        "features_h": "Características",
        "features": [
            "Dúas pistas L/R con bus de efectos estéreo: ideal para escena, ensaio e podcast.",
            "Captura HAL (AUHAL) estable para tomas longas.",
            "Edición de onda: zoom, selección, cortar/copiar/pegar, fades, gañancia e normalizar.",
            "EQ e reverb offline, redución de ruído; ata 6 Audio Units no bus estéreo.",
            "Importa audio ou vídeo e exporta WAV ou AIFF; proxectos .stageedit con autosave.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Xa dispoñible</strong> na Mac App Store.",
        "store_aria": "Descargar Stage Audio Edit na App Store",
        "banner_aria": "Stage Audio Edit na Mac App Store",
        "banner_alt": "Stage Audio Edit — xa na Mac App Store",
        "icon_alt": "Icona de Stage Audio Edit",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "blurb": "Editor de 2 pistas estéreo para Mac.",
        "detail": "Grava, edita ondas e exporta WAV/AIFF sen un DAW completo. Dúas pistas L/R con efectos no bus estéreo. Dispoñible na Mac App Store.",
        "compare_best": "Editar dúas pistas estéreo (L/R) e exportar WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS",
        "aria_nav": "Principal",
        "nav_home": "Inicio",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_access": "Accesibilidade",
        "nav_proj": "Proxectores e pantalla",
        "nav_patch": "Patch e routing",
        "nav_rehearsal": "Ensaio actoral",
        "nav_compare": "Comparativa",
        "nav_resources": "Recursos",
        "nav_faq": "FAQ",
        "nav_support": "Soporte",
        "lang_label": "Galego",
        "lang_emoji": "",
        "aria_lang": "Selector de idioma",
        "privacy": "Privacidade",
        "support": "Soporte",
        "disclaimer": "QLab é unha marca de Figure 53. Este sitio e estas apps son produtos independentes e non están afiliados, respaldados nin patrocinados por Figure 53.",
        "made": "Software independente · Santiago de Compostela",
    },
    "ca": {
        "meta": "Editor de dues pistes estèreo (L/R) per a Mac: gravar, editar ones i exportar sense un DAW complet.",
        "title": "Stage Audio Edit (macOS) — Stage Apps",
        "h1": "Stage Audio Edit (macOS)",
        "lead": "Stage Audio Edit és un editor de dues pistes estèreo (L/R) per a Mac: gravar, editar ones i exportar sense la complexitat d’un DAW complet.",
        "features_h": "Característiques",
        "features": [
            "Dues pistes L/R amb bus d’efectes estèreo: ideal per a escena, assaig i podcast.",
            "Captura HAL (AUHAL) estable per a preses llargues.",
            "Edició d’ona: zoom, selecció, tallar/copiar/enganxar, fades, guany i normalitzar.",
            "EQ i reverb offline, reducció de soroll; fins a 6 Audio Units al bus estèreo.",
            "Importa àudio o vídeo i exporta WAV o AIFF; projectes .stageedit amb autosave.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Ja disponible</strong> al Mac App Store.",
        "store_aria": "Descarregar Stage Audio Edit a l’App Store",
        "banner_aria": "Stage Audio Edit al Mac App Store",
        "banner_alt": "Stage Audio Edit — ja al Mac App Store",
        "icon_alt": "Icona de Stage Audio Edit",
        "footer_links": '<p><a href="compare.html">Veure comparativa</a> · <a href="use-cases.html">Veure casos d’ús</a> · <a href="support.html">Suport</a></p>',
        "blurb": "Editor de 2 pistes estèreo per a Mac.",
        "detail": "Grava, edita ones i exporta WAV/AIFF sense un DAW complet. Dues pistes L/R amb efectes al bus estèreo. Disponible al Mac App Store.",
        "compare_best": "Editar dues pistes estèreo (L/R) i exportar WAV/AIFF",
        "compare_proto": "Àudio / WAV · AIFF",
        "compare_plat": "macOS",
        "aria_nav": "Principal",
        "nav_home": "Inici",
        "nav_audio": "Àudio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_access": "Accessibilitat",
        "nav_proj": "Projectors i pantalla",
        "nav_patch": "Patch i routing",
        "nav_rehearsal": "Assaig actoral",
        "nav_compare": "Comparativa",
        "nav_resources": "Recursos",
        "nav_faq": "FAQ",
        "nav_support": "Suport",
        "lang_label": "Català",
        "lang_emoji": "",
        "aria_lang": "Selector d’idioma",
        "privacy": "Privacitat",
        "support": "Suport",
        "disclaimer": "QLab és una marca de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, recolzats ni patrocinats per Figure 53.",
        "made": "Programari independent · Santiago de Compostela",
    },
    "eu": {
        "meta": "Mac-erako bi pista estereo (L/R) editorea: grabatu, uhina editatu eta esportatu DAW osorik gabe.",
        "title": "Stage Audio Edit (macOS) — Stage Apps",
        "h1": "Stage Audio Edit (macOS)",
        "lead": "Stage Audio Edit Mac-erako bi pista estereo (L/R) editorea da: grabatu, uhina editatu eta esportatu DAW baten konplexutasunik gabe.",
        "features_h": "Ezaugarriak",
        "features": [
            "Bi L/R pista efektu-bus estereoarekin: eszenarako, entseguetarako eta podcastetarako aproposa.",
            "HAL (AUHAL) captura egonkorra hartualdi luzeetarako.",
            "Uhin edizioa: zoom, hautaketa, moztu/kopiatu/itsatsi, fadeak, irabazia eta normalizatu.",
            "EQ eta reverb offline, zarata murrizketa; gehienez 6 Audio Unit bus estereoan.",
            "Inportatu audioa edo bideoa eta esportatu WAV edo AIFF; .stageedit proiektuak autosave-rekin.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Dagoeneko eskuragarri</strong> Mac App Store-n.",
        "store_aria": "Deskargatu Stage Audio Edit App Store-n",
        "banner_aria": "Stage Audio Edit Mac App Store-n",
        "banner_alt": "Stage Audio Edit — dagoeneko Mac App Store-n",
        "icon_alt": "Stage Audio Edit ikonoa",
        "footer_links": '<p><a href="compare.html">Ikusi konparaketa</a> · <a href="use-cases.html">Erabilera kasuak</a> · <a href="support.html">Laguntza</a></p>',
        "blurb": "Mac-erako 2 pistako estereo editorea.",
        "detail": "Grabatu, editatu uhinak eta esportatu WAV/AIFF DAW osorik gabe. Bi L/R pista efektu-bus estereoarekin. Mac App Store-n eskuragarri.",
        "compare_best": "Bi pista estereo (L/R) editatu eta WAV/AIFF esportatu",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS",
        "aria_nav": "Nagusia",
        "nav_home": "Hasiera",
        "nav_audio": "Audioa",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_access": "Irisgarritasuna",
        "nav_proj": "Proiektoreak eta pantaila",
        "nav_patch": "Patch eta routing",
        "nav_rehearsal": "Antzezlan entsegua",
        "nav_compare": "Konparaketa",
        "nav_resources": "Baliabideak",
        "nav_faq": "FAQ",
        "nav_support": "Laguntza",
        "lang_label": "Euskara",
        "lang_emoji": "",
        "aria_lang": "Hizkuntza hautatzailea",
        "privacy": "Pribatutasuna",
        "support": "Laguntza",
        "disclaimer": "QLab Figure 53-ren marka da. Gune hau eta app hauek produktu independenteak dira eta ez daude Figure 53-rekin afiliatuta, babestuta edo babestuta.",
        "made": "Software independentea · Santiago de Compostela",
    },
}

LANG_ITEMS = [
    ("es", "Español", "🇪🇸", None),
    ("en", "English", "🇬🇧", None),
    ("fr", "Français", "🇫🇷", None),
    ("de", "Deutsch", "🇩🇪", None),
    ("gl", "Galego", None, "../assets/flags/gl.svg"),
    ("ca", "Català", None, "../assets/flags/ca.svg"),
    ("eu", "Euskara", None, "../assets/flags/eu.svg"),
]

NAV_RE = re.compile(r'<nav class="nav" aria-label="[^"]*">\s*.*?</nav>', re.S)


def lang_dropdown(lang: str, page: str) -> str:
    items = []
    for code, label, emoji, flag in LANG_ITEMS:
        href = page if code == lang else f"../{code}/{page}"
        cur = ' aria-current="page"' if code == lang else ""
        if emoji:
            mark = f'<span class="lang-emoji" aria-hidden="true">{emoji}</span>'
        else:
            mark = f'<img class="lang-dropdown-flag" src="{flag}" alt="" decoding="async">'
        items.append(
            f'<a class="lang-dropdown-item" href="{href}" hreflang="{code}"{cur} role="menuitem">{mark}<span class="lang-dropdown-item-label">{label}</span></a>'
        )
    c = COPY[lang]
    summary_mark = (
        f'<span class="lang-emoji" aria-hidden="true">{c["lang_emoji"]}</span> '
        if c["lang_emoji"]
        else f'<img class="lang-dropdown-flag" src="../assets/flags/{lang}.svg" alt="" decoding="async"> '
    )
    return f'''<div class="lang-dropdown" role="navigation" aria-label="{c["aria_lang"]}">
  <details>
    <summary>
      {summary_mark}<span class="lang-dropdown-label">{c["lang_label"]}</span>
    </summary>
    <div class="lang-dropdown-menu" role="menu">
      {" ".join(items)}
    </div>
  </details>
</div>'''


def build_nav(lang: str, current: str) -> str:
    c = COPY[lang]

    def link(href: str, label: str) -> str:
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'

    def group(summary: str, items: list[tuple[str, str]]) -> str:
        links = "\n              ".join(link(h, lab) for h, lab in items)
        return (
            f'<details class="nav-group">\n'
            f"              <summary>{summary}</summary>\n"
            f'              <div class="nav-group-menu">\n'
            f"              {links}\n"
            f"              </div>\n"
            f"            </details>"
        )

    parts = [
        link("index.html", c["nav_home"]),
        group(
            c["nav_audio"],
            [
                ("stage-multitrack.html", "Stage Multitrack"),
                (HREF, NAME),
            ],
        ),
        link("miditoosc.html", c["nav_midi"]),
        link("stage-rf.html", c["nav_rf"]),
        link("accesible.html", c["nav_access"]),
        group(
            c["nav_proj"],
            [
                ("shutter-pj-osc.html", "Shutter PJ-OSC"),
                ("shutter-pjlink-ios.html", "Shutter PJLINK"),
                ("transparent-screen.html", "Transparent Screen"),
            ],
        ),
        group(
            c["nav_patch"],
            [
                ("easy-routing-m32-x32.html", "Easy Routing"),
                ("m32-patch.html", "M32 Patch"),
            ],
        ),
        link("stage-with-me.html", c["nav_rehearsal"]),
        link("compare.html", c["nav_compare"]),
        link("resources.html", c["nav_resources"]),
        link("faq.html", c["nav_faq"]),
        link("support.html", c["nav_support"]),
    ]
    inner = "\n            ".join(parts)
    return f'<nav class="nav" aria-label="{c["aria_nav"]}">\n            {inner}\n          </nav>'


def write_product_page(lang: str) -> None:
    c = COPY[lang]
    feats = "".join(f"<li>{f}</li>" for f in c["features"])
    alts = "\n".join(
        f'  <link rel="alternate" hreflang="{L}" href="../{L}/{HREF}">' for L in LANGS
    )
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{htmlmod.escape(c["meta"])}">
  <title>{c["title"]}</title>
{alts}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
  <link rel="icon" href="/favicon.ico?v=3" sizes="any">
  <link rel="icon" href="/assets/images/stageapps-favicon-32.png?v=3" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/images/stageapps-favicon-180.png?v=3">
  <link rel="stylesheet" href="../css/styles.css?v=37">
</head>
<body>
  <div class="page">
    <header class="site-header">
      <div class="wrap inner">
        <a class="logo" href="index.html"><img class="logo-mark" src="/assets/images/stageapps-mark.png?v=3" alt="" width="36" height="36" decoding="async"><span class="logo-text">StageApps</span></a>
        <div class="header-right">
          {build_nav(lang, HREF)}
          {lang_dropdown(lang, HREF)}
        </div>
      </div>
    </header>

    <main>
      <section class="page-hero wrap">
        <h1>{c["h1"]}</h1>
        <p class="meta">{c["meta"]}</p>
            </section>
      <section>
        <div class="wrap">
          <div class="app-hero-banner" aria-label="{c["banner_aria"]}">
            <a href="{STORE}" target="_blank" rel="noopener noreferrer">
              <img src="{BANNER}" alt="{c["banner_alt"]}" width="1200" height="720" loading="eager" decoding="async">
            </a>
          </div>
        </div>
      </section>
      <section>
        <div class="wrap prose">
          <p>{c["lead"]}</p>
          <h2>{c["features_h"]}</h2>
          <ul>
            {feats}
          </ul>

          <div class="beta-callout">
            <h3>{c["store_h"]}</h3>
            <p>{c["store_p"]}</p>
            <p><a class="store-badge-link" href="{STORE}" target="_blank" rel="noopener noreferrer" aria-label="{c["store_aria"]}"><img src="../assets/images/download-on-the-app-store-en-us-white.svg" alt="Download on the App Store" width="120" height="40" loading="lazy" decoding="async"></a></p>
          </div>
{c["footer_links"]}
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="wrap inner">
        <span>© <span id="y"></span> Stage Apps</span>
        <div class="links">
          <a href="support.html">{c["support"]}</a>
          <a href="privacy.html">{c["privacy"]}</a>
                    <a class="footer-social" href="https://instagram.com/stage.apps" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><img class="footer-social-icon" src="/assets/icons/instagram.svg" alt="" width="18" height="18" decoding="async"><span>Instagram</span></a>
          <a class="footer-social" href="https://www.tiktok.com/@stageapps" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><img class="footer-social-icon" src="/assets/icons/tiktok.svg" alt="" width="18" height="18" decoding="async"><span>TikTok</span></a>
          <a class="footer-social" href="https://www.youtube.com/@StageApps" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><img class="footer-social-icon" src="/assets/icons/youtube.svg" alt="" width="18" height="18" decoding="async"><span>YouTube</span></a>
        </div>
      </div>
      <p class="wrap footer-disclaimer">{c["disclaimer"]}</p>
      <p class="wrap footer-made-in">{c["made"]}</p>
    </footer>
  </div>
  <script>
    try {{ localStorage.setItem("accesible_lang", "{lang}"); }} catch (e) {{}}
  </script>
  <script>
    document.getElementById("y").textContent = new Date().getFullYear();
  </script>
</body>
</html>
'''
    (DOCS / lang / HREF).write_text(html, encoding="utf-8")
    print("page", lang)


def update_index(lang: str) -> None:
    path = DOCS / lang / "index.html"
    text = path.read_text(encoding="utf-8")
    c = COPY[lang]

    m = re.search(r'data-apps="([^"]+)"', text)
    if not m:
        raise SystemExit(f"no data-apps: {path}")
    apps = json.loads(htmlmod.unescape(m.group(1)))
    for app in apps:
        if app.get("name") in ("Stage Edit", "Stage Audio Edit"):
            app["name"] = NAME
            app["blurb"] = c["blurb"]
            app["detail"] = c["detail"]
            app["href"] = HREF
            app["image"] = ICON
            app["store"] = STORE
            app.pop("soon", None)
            app.pop("video", None)
    encoded = htmlmod.escape(json.dumps(apps, ensure_ascii=False), quote=True)
    text = text[: m.start(1)] + encoded + text[m.end(1) :]

    text = text.replace('aria-label="Stage Edit"', f'aria-label="{NAME}"')
    text = text.replace(">Stage Edit</a>", f">{NAME}</a>")
    text = re.sub(r"styles\.css\?v=\d+", "styles.css?v=37", text)
    text = re.sub(r"app-carousel\.js\?v=\d+", "app-carousel.js?v=25", text)

    # Keep family nav label for product
    text = text.replace(
        f'<a href="{HREF}">Stage Edit</a>',
        f'<a href="{HREF}">{NAME}</a>',
    )
    text = text.replace(
        f'<a href="{HREF}">{NAME}</a>',
        f'<a href="{HREF}">{NAME}</a>',
    )

    path.write_text(text, encoding="utf-8")
    print("index", lang)


def update_compare(lang: str) -> None:
    path = DOCS / lang / "compare.html"
    text = path.read_text(encoding="utf-8")
    c = COPY[lang]
    text = text.replace(">Stage Edit</a>", f">{NAME}</a>")
    text = re.sub(
        r"<tr><td>Stage (?:Edit|Audio Edit)</td><td>[^<]*</td><td>[^<]*</td><td>[^<]*</td></tr>",
        f"<tr><td>{NAME}</td><td>{c['compare_best']}</td><td>{c['compare_proto']}</td><td>{c['compare_plat']}</td></tr>",
        text,
        count=1,
    )
    text = re.sub(r"styles\.css\?v=\d+", "styles.css?v=37", text)
    path.write_text(text, encoding="utf-8")
    print("compare", lang)


def rename_nav_everywhere(lang: str) -> None:
    for path in sorted((DOCS / lang).glob("*.html")):
        if path.name in (HREF, "index.html", "compare.html", "stage-recorder.html"):
            continue
        text = path.read_text(encoding="utf-8")
        if "Stage Edit" not in text and "Stage Audio Edit" not in text:
            continue
        text2 = text.replace(
            f'<a href="{HREF}">Stage Edit</a>',
            f'<a href="{HREF}">{NAME}</a>',
        )
        text2 = text2.replace(
            f'<a href="{HREF}" aria-current="page">Stage Edit</a>',
            f'<a href="{HREF}" aria-current="page">{NAME}</a>',
        )
        # already renamed cases stay
        text2 = re.sub(r"styles\.css\?v=\d+", "styles.css?v=37", text2)
        if text2 != text:
            path.write_text(text2, encoding="utf-8")


def update_js() -> None:
    path = DOCS / "js" / "app-carousel.js"
    js = path.read_text(encoding="utf-8")
    js = js.replace(
        '''      } else if (app.name === "Stage Edit") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Edit"));
      }''',
        '''      } else if (app.name === "Stage Audio Edit" || app.name === "Stage Edit") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage Audio"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Edit"));
      }''',
    )
    path.write_text(js, encoding="utf-8")
    print("js ok")


def main() -> None:
    update_js()
    for lang in LANGS:
        write_product_page(lang)
        update_index(lang)
        update_compare(lang)
        rename_nav_everywhere(lang)
    print("DONE")


if __name__ == "__main__":
    main()
