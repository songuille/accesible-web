#!/usr/bin/env python3
"""Add Stage Align (coming soon) to the Stage Apps site — under Audio family."""
from __future__ import annotations

import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
IMAGE = "../assets/images/stage-align-square-1080.png"
HREF = "stage-align.html"
NAME = "Stage Align"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]
CSS_V = "38"
JS_V = "27"

COPY = {
    "es": {
        "meta": "Alineado TOP↔SUB y retardos de sistema en Mac: asistente, fase en el cruce y aplicación OSC a M32/X32.",
        "title": "Stage Align (macOS) — Stage Apps",
        "h1": "Stage Align (macOS)",
        "lead": "Stage Align guía el alineado TOP↔SUB y los retardos del sistema: mide, afina la fase en el cruce, aplica delays a la mesa por OSC y comprueba el resultado. Interfaz genérica o modo M32/USB, con mando remoto en el teléfono.",
        "features_h": "Características",
        "features": [
            "Asistente guiado: Configurar → Cruce → Modo → Medir → Resultados → Comprobar.",
            "Alineado TOP↔SUB por respuesta al impulso y Auto Align (barrido fino + polaridad).",
            "Fase en el cruce: busca el retardo que maximiza la suma alrededor de la frecuencia de crossover.",
            "Retardo natural de escenario y pares de delay (fills) con totales Natural + Alineado + Zona.",
            "Modo interfaz genérica o mesa M32/USB (DN32): patch Card→CH por OSC y delays en Out físicas.",
            "Aplicar a la mesa: envía delays e inversión por OSC a M32/X32 (puerto 10023).",
            "Varias posiciones en patio para un promedio espacial más estable.",
            "Mando remoto por Wi‑Fi: QR con URL y PIN para medir y avanzar desde el teléfono.",
        ],
        "soon_h": "Próximamente",
        "soon_p": "<strong>En breve en la Mac App Store.</strong> Requiere macOS 15 o posterior.",
        "icon_alt": "Icono de Stage Align",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "nav_home": "Inicio",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_backup": "Backup",
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
        "aria_nav": "Principal",
        "privacy": "Privacidad",
        "support": "Soporte",
        "disclaimer": "QLab es una marca de Figure 53. Este sitio y estas apps son productos independientes y no están afiliados, respaldados ni patrocinados por Figure 53.",
        "made": "Software independiente · Santiago de Compostela",
        "blurb": "Alineado TOP↔SUB y retardos de sistema en Mac.",
        "detail": "Asistente de medición, fase en el cruce y aplicación OSC a M32/X32. Interfaz genérica o modo USB. Mando remoto por QR. Próximamente en la Mac App Store.",
        "compare_best": "Alinear TOP↔SUB y aplicar retardos (fase en el cruce)",
        "compare_proto": "Audio / OSC M32·X32",
        "compare_plat": "macOS 15+ · próximamente",
    },
    "en": {
        "meta": "TOP↔SUB alignment and system delays on Mac: guided wizard, crossover phase, and OSC apply to M32/X32.",
        "title": "Stage Align (macOS) — Stage Apps",
        "h1": "Stage Align (macOS)",
        "lead": "Stage Align walks you through TOP↔SUB alignment and system delays: measure, refine phase at the crossover, apply delays to the console via OSC, and verify. Generic interface or M32/USB mode, with a phone remote.",
        "features_h": "Features",
        "features": [
            "Guided wizard: Set up → Crossover → Mode → Measure → Results → Verify.",
            "TOP↔SUB alignment from impulse response plus Auto Align (fine sweep + polarity).",
            "Crossover phase: finds the delay that maximizes summing around the crossover frequency.",
            "Natural stage delay and delay pairs (fills) with Natural + Align + Zone totals.",
            "Generic interface or M32/USB (DN32) mode: Card→CH patch via OSC and delays on physical Outs.",
            "Apply to console: send delays and invert over OSC to M32/X32 (port 10023).",
            "Multiple house positions for a more stable spatial average.",
            "Wi‑Fi remote: QR with URL and PIN to measure and advance from your phone.",
        ],
        "soon_h": "Coming soon",
        "soon_p": "<strong>Coming soon to the Mac App Store.</strong> Requires macOS 15 or later.",
        "icon_alt": "Stage Align icon",
        "footer_links": '<p><a href="compare.html">Compare apps</a> · <a href="use-cases.html">Use cases</a> · <a href="support.html">Support</a></p>',
        "nav_home": "Home",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_backup": "Backup",
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
        "aria_nav": "Main",
        "privacy": "Privacy",
        "support": "Support",
        "disclaimer": "QLab is a trademark of Figure 53. This site and these apps are independent products and are not affiliated with, endorsed by, or sponsored by Figure 53.",
        "made": "Independent software · Santiago de Compostela",
        "blurb": "TOP↔SUB alignment and system delays on Mac.",
        "detail": "Measurement wizard, crossover phase, and OSC apply to M32/X32. Generic or USB mode. Phone remote via QR. Coming soon to the Mac App Store.",
        "compare_best": "Align TOP↔SUB and apply delays (crossover phase)",
        "compare_proto": "Audio / OSC M32·X32",
        "compare_plat": "macOS 15+ · coming soon",
    },
    "fr": {
        "meta": "Alignement TOP↔SUB et délais système sur Mac : assistant, phase au crossover et envoi OSC vers M32/X32.",
        "title": "Stage Align (macOS) — Stage Apps",
        "h1": "Stage Align (macOS)",
        "lead": "Stage Align guide l’alignement TOP↔SUB et les délais système : mesure, affine la phase au crossover, applique les délais à la console via OSC et vérifie. Interface générique ou mode M32/USB, avec télécommande téléphone.",
        "features_h": "Fonctionnalités",
        "features": [
            "Assistant guidé : Configurer → Crossover → Mode → Mesurer → Résultats → Vérifier.",
            "Alignement TOP↔SUB par réponse impulsionnelle et Auto Align (balayage fin + polarité).",
            "Phase au crossover : délai qui maximise la somme autour de la fréquence de coupure.",
            "Délai naturel de scène et paires de delay (fills) avec totaux Naturel + Align + Zone.",
            "Interface générique ou mode M32/USB (DN32) : patch Card→CH via OSC et délais sur Out physiques.",
            "Appliquer à la console : délais et inversion OSC vers M32/X32 (port 10023).",
            "Plusieurs positions en salle pour une moyenne spatiale plus stable.",
            "Télécommande Wi‑Fi : QR avec URL et PIN pour mesurer et avancer depuis le téléphone.",
        ],
        "soon_h": "Bientôt",
        "soon_p": "<strong>Bientôt sur le Mac App Store.</strong> macOS 15 ou plus récent.",
        "icon_alt": "Icône Stage Align",
        "footer_links": '<p><a href="compare.html">Comparatif</a> · <a href="use-cases.html">Cas d’usage</a> · <a href="support.html">Support</a></p>',
        "nav_home": "Accueil",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_backup": "Backup",
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
        "aria_nav": "Principal",
        "privacy": "Confidentialité",
        "support": "Support",
        "disclaimer": "QLab est une marque de Figure 53. Ce site et ces apps sont des produits indépendants et ne sont pas affiliés, cautionnés ni sponsorisés par Figure 53.",
        "made": "Logiciel indépendant · Santiago de Compostela",
        "blurb": "Alignement TOP↔SUB et délais système sur Mac.",
        "detail": "Assistant de mesure, phase au crossover et envoi OSC vers M32/X32. Mode générique ou USB. Télécommande QR. Bientôt sur le Mac App Store.",
        "compare_best": "Aligner TOP↔SUB et appliquer les délais (phase crossover)",
        "compare_proto": "Audio / OSC M32·X32",
        "compare_plat": "macOS 15+ · bientôt",
    },
    "de": {
        "meta": "TOP↔SUB-Alignment und System-Delays auf dem Mac: Assistent, Phase am Crossover und OSC an M32/X32.",
        "title": "Stage Align (macOS) — Stage Apps",
        "h1": "Stage Align (macOS)",
        "lead": "Stage Align führt durch TOP↔SUB-Alignment und System-Delays: messen, Phase am Crossover feinjustieren, Delays per OSC an die Konsole senden und prüfen. Generisches Interface oder M32/USB-Modus, mit Handy-Fernbedienung.",
        "features_h": "Funktionen",
        "features": [
            "Geführter Assistent: Einrichten → Trennfrequenz → Modus → Messen → Ergebnisse → Prüfen.",
            "TOP↔SUB-Alignment per Impulsantwort plus Auto Align (Feinsweep + Polarität).",
            "Phase am Crossover: Delay, das die Summe um die Trennfrequenz maximiert.",
            "Natürliche Bühnenverzögerung und Delay-Paare (Fills) mit Natural + Align + Zone.",
            "Generisches Interface oder M32/USB (DN32): Card→CH-Patch per OSC und Delays auf physischen Outs.",
            "An Konsole anwenden: Delays und Invert per OSC an M32/X32 (Port 10023).",
            "Mehrere Saalpositionen für einen stabileren räumlichen Mittelwert.",
            "Wi‑Fi-Fernbedienung: QR mit URL und PIN zum Messen und Weiterschalten vom Telefon.",
        ],
        "soon_h": "Demnächst",
        "soon_p": "<strong>Demnächst im Mac App Store.</strong> Erfordert macOS 15 oder neuer.",
        "icon_alt": "Stage-Align-Symbol",
        "footer_links": '<p><a href="compare.html">Vergleich</a> · <a href="use-cases.html">Anwendungsfälle</a> · <a href="support.html">Support</a></p>',
        "nav_home": "Start",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_backup": "Backup",
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
        "aria_nav": "Hauptnavigation",
        "privacy": "Datenschutz",
        "support": "Support",
        "disclaimer": "QLab ist eine Marke von Figure 53. Diese Website und Apps sind unabhängige Produkte und nicht mit Figure 53 verbunden, von Figure 53 unterstützt oder gesponsert.",
        "made": "Unabhängige Software · Santiago de Compostela",
        "blurb": "TOP↔SUB-Alignment und System-Delays auf dem Mac.",
        "detail": "Mess-Assistent, Phase am Crossover und OSC an M32/X32. Generisch oder USB. Fernbedienung per QR. Demnächst im Mac App Store.",
        "compare_best": "TOP↔SUB alignen und Delays anwenden (Crossover-Phase)",
        "compare_proto": "Audio / OSC M32·X32",
        "compare_plat": "macOS 15+ · demnächst",
    },
    "gl": {
        "meta": "Aliñado TOP↔SUB e retardos de sistema en Mac: asistente, fase no cruce e OSC a M32/X32.",
        "title": "Stage Align (macOS) — Stage Apps",
        "h1": "Stage Align (macOS)",
        "lead": "Stage Align guía o aliñado TOP↔SUB e os retardos do sistema: mide, afina a fase no cruce, aplica delays á mesa por OSC e comproba. Interface xenérica ou modo M32/USB, con mando remoto no teléfono.",
        "features_h": "Características",
        "features": [
            "Asistente guiado: Configurar → Cruce → Modo → Medir → Resultados → Comprobar.",
            "Aliñado TOP↔SUB por resposta ao impulso e Auto Align (varrido fino + polaridade).",
            "Fase no cruce: retardo que maximiza a suma arredor da frecuencia de crossover.",
            "Retardo natural de escenario e pares de delay (fills) con totais Natural + Aliñado + Zona.",
            "Modo interface xenérica ou mesa M32/USB (DN32): patch Card→CH por OSC e delays en Out físicas.",
            "Aplicar á mesa: envía delays e inversión por OSC a M32/X32 (porto 10023).",
            "Varias posicións no patio para unha media espacial máis estable.",
            "Mando remoto por Wi‑Fi: QR con URL e PIN para medir e avanzar desde o teléfono.",
        ],
        "soon_h": "Proximamente",
        "soon_p": "<strong>En breve na Mac App Store.</strong> Require macOS 15 ou posterior.",
        "icon_alt": "Icona de Stage Align",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "nav_home": "Inicio",
        "nav_audio": "Audio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_backup": "Backup",
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
        "aria_lang": "Selector de lingua",
        "aria_nav": "Navegación principal",
        "privacy": "Privacidade",
        "support": "Soporte",
        "disclaimer": "QLab é unha marca de Figure 53. Este sitio e estas apps son produtos independentes e non están afiliados, respaldados nin patrocinados por Figure 53.",
        "made": "Software independente · Santiago de Compostela",
        "blurb": "Aliñado TOP↔SUB e retardos de sistema en Mac.",
        "detail": "Asistente de medición, fase no cruce e OSC a M32/X32. Interface xenérica ou USB. Mando remoto por QR. Proximamente na Mac App Store.",
        "compare_best": "Aliñar TOP↔SUB e aplicar retardos (fase no cruce)",
        "compare_proto": "Audio / OSC M32·X32",
        "compare_plat": "macOS 15+ · proximamente",
    },
    "ca": {
        "meta": "Alineament TOP↔SUB i retards de sistema a Mac: assistent, fase al croament i OSC a M32/X32.",
        "title": "Stage Align (macOS) — Stage Apps",
        "h1": "Stage Align (macOS)",
        "lead": "Stage Align guia l’alineament TOP↔SUB i els retards del sistema: mesura, afina la fase al croament, aplica delays a la taula per OSC i comprova. Interfície genèrica o mode M32/USB, amb comandament remot al telèfon.",
        "features_h": "Característiques",
        "features": [
            "Assistent guiat: Configurar → Croament → Mode → Mesurar → Resultats → Comprovar.",
            "Alineament TOP↔SUB per resposta a l’impuls i Auto Align (escombrat fi + polaritat).",
            "Fase al croament: retard que maximitza la suma al voltant de la freqüència de crossover.",
            "Retard natural d’escenari i parells de delay (fills) amb totals Natural + Alineat + Zona.",
            "Mode interfície genèrica o taula M32/USB (DN32): patch Card→CH per OSC i delays a Out físiques.",
            "Aplicar a la taula: envia delays i inversió per OSC a M32/X32 (port 10023).",
            "Diverses posicions al pati per a una mitjana espacial més estable.",
            "Comandament remot per Wi‑Fi: QR amb URL i PIN per mesurar i avançar des del telèfon.",
        ],
        "soon_h": "Properament",
        "soon_p": "<strong>Aviat a la Mac App Store.</strong> Requereix macOS 15 o posterior.",
        "icon_alt": "Icona de Stage Align",
        "footer_links": '<p><a href="compare.html">Veure comparativa</a> · <a href="use-cases.html">Veure casos d’ús</a> · <a href="support.html">Suport</a></p>',
        "nav_home": "Inici",
        "nav_audio": "Àudio",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_backup": "Backup",
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
        "aria_nav": "Navegació principal",
        "privacy": "Privacitat",
        "support": "Suport",
        "disclaimer": "QLab és una marca de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, avalats ni patrocinats per Figure 53.",
        "made": "Programari independent · Santiago de Compostela",
        "blurb": "Alineament TOP↔SUB i retards de sistema a Mac.",
        "detail": "Assistent de mesura, fase al croament i OSC a M32/X32. Interfície genèrica o USB. Comandament remot per QR. Properament a la Mac App Store.",
        "compare_best": "Alinear TOP↔SUB i aplicar retards (fase al croament)",
        "compare_proto": "Àudio / OSC M32·X32",
        "compare_plat": "macOS 15+ · properament",
    },
    "eu": {
        "meta": "TOP↔SUB lerrokatzea eta sistemaren atzerapenak Mac-en: laguntzailea, fasea gurutzatzean eta OSC M32/X32-ra.",
        "title": "Stage Align (macOS) — Stage Apps",
        "h1": "Stage Align (macOS)",
        "lead": "Stage Align-ek TOP↔SUB lerrokatzea eta sistemaren atzerapenak gidatzen ditu: neurtu, fasea doitu gurutzatzean, delay-ak OSC bidez mahaira aplikatu eta egiaztatu. Interfaze generikoa edo M32/USB modua, telefono urrutikoarekin.",
        "features_h": "Ezaugarriak",
        "features": [
            "Laguntzaile gidatua: Konfiguratu → Gurutzatzea → Modua → Neurtu → Emaitzak → Egiaztatu.",
            "TOP↔SUB lerrokatzea impulsu-erantzunetik eta Auto Align (sarrera fina + polaritatea).",
            "Fasea gurutzatzean: crossover inguruan batura maximizatzen duen atzerapena.",
            "Eszenatokiko atzerapen naturala eta delay bikoteak (fills) Natural + Lerrokatu + Zona totalekin.",
            "Interfaze generikoa edo M32/USB (DN32): Card→CH patch OSC bidez eta delay-ak Out fisikoetan.",
            "Mahaira aplikatu: delay-ak eta inbertsioa OSC bidez M32/X32-ra (10023 ataka).",
            "Patioan hainbat posizio batezbesteko espazial egonkorrago baterako.",
            "Wi‑Fi urrutikoa: QR URL eta PIN-ekin telefonoan neurtu eta aurrera egiteko.",
        ],
        "soon_h": "Laster",
        "soon_p": "<strong>Laster Mac App Store-n.</strong> macOS 15 edo berriagoa behar du.",
        "icon_alt": "Stage Align ikonoa",
        "footer_links": '<p><a href="compare.html">Konparaketa ikusi</a> · <a href="use-cases.html">Erabilera-kasuak</a> · <a href="support.html">Laguntza</a></p>',
        "nav_home": "Hasiera",
        "nav_audio": "Audioa",
        "nav_midi": "MIDI / OSC",
        "nav_rf": "RF",
        "nav_backup": "Backup",
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
        "aria_lang": "Hizkuntza-hautatzailea",
        "aria_nav": "Menu nagusia",
        "privacy": "Pribatutasuna",
        "support": "Laguntza",
        "disclaimer": "QLab Figure 53-ren marka da. Gune hau eta app hauek produktu independenteak dira eta ez daude Figure 53-rekin afiliatuta, babestuta edo babestuta.",
        "made": "Software independentea · Santiago de Compostela",
        "blurb": "TOP↔SUB lerrokatzea eta sistemaren atzerapenak Mac-en.",
        "detail": "Neurketa-laguntzailea, fasea gurutzatzean eta OSC M32/X32-ra. Generikoa edo USB. QR urrutikoa. Laster Mac App Store-n.",
        "compare_best": "TOP↔SUB lerrokatu eta atzerapenak aplikatu (fasea gurutzatzean)",
        "compare_proto": "Audio / OSC M32·X32",
        "compare_plat": "macOS 15+ · laster",
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
                ("stage-edit.html", "Stage Audio Edit"),
                (HREF, "Stage Align"),
            ],
        ),
        link("miditoosc.html", c["nav_midi"]),
        link("stage-rf.html", c["nav_rf"]),
        link("stage-backup.html", c["nav_backup"]),
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
  <link rel="stylesheet" href="../css/styles.css?v={CSS_V}">
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
          <div class="app-icon-hero" aria-label="{c["icon_alt"]}">
            <img src="{IMAGE}" alt="{c["icon_alt"]}" width="320" height="320" loading="eager" decoding="async">
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
            <h3>{c["soon_h"]}</h3>
            <p>{c["soon_p"]}</p>
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


def upsert_nav(html: str, lang: str, path: Path) -> str:
    if not NAV_RE.search(html):
        return html
    nav = build_nav(lang, path.name)
    new, n = NAV_RE.subn(nav, html, count=1)
    if n != 1:
        raise SystemExit(f"nav replace failed ({n}): {path}")
    return new


def update_index(lang: str) -> None:
    path = DOCS / lang / "index.html"
    text = path.read_text(encoding="utf-8")
    c = COPY[lang]
    text = upsert_nav(text, lang, path)

    m = re.search(r'data-apps="([^"]+)"', text)
    if not m:
        raise SystemExit(f"no data-apps: {path}")
    apps = json.loads(htmlmod.unescape(m.group(1)))
    entry = {
        "name": NAME,
        "blurb": c["blurb"],
        "detail": c["detail"],
        "soon": True,
        "image": IMAGE,
        "href": HREF,
    }
    names = [a.get("name") for a in apps]
    if NAME in names:
        apps = [entry if a.get("name") == NAME else a for a in apps]
    else:
        insert_at = None
        for i, n in enumerate(names):
            if n in ("Stage Audio Edit", "Stage Edit"):
                insert_at = i + 1
                break
            if n in ("Stage Multitrack", "Stage Recorder") and insert_at is None:
                insert_at = i + 1
        if insert_at is None:
            apps.append(entry)
        else:
            apps.insert(insert_at, entry)

    encoded = htmlmod.escape(json.dumps(apps, ensure_ascii=False), quote=True)
    text = text[: m.start(1)] + encoded + text[m.end(1) :]

    buttons = []
    for i, app in enumerate(apps):
        active = ' class="app-orbit-planet is-active"' if i == 0 else ' class="app-orbit-planet"'
        aria_cur = ' aria-current="true"' if i == 0 else ""
        img = app.get("image", IMAGE)
        buttons.append(
            f'<button type="button"{active} data-orbit-planet aria-label="{htmlmod.escape(app["name"])}"{aria_cur}>'
            f'<img src="{img}" alt=""></button>'
        )
    block = "\n              ".join(buttons)
    pattern = re.compile(
        r'(<div class="app-orbit-ring"[^>]*>)\s*(?:<button type="button" class="app-orbit-planet[\s\S]*?</button>\s*)+',
        re.S,
    )

    def repl(mm: re.Match) -> str:
        return mm.group(1) + "\n              " + block + "\n\n              "

    text, n = pattern.subn(repl, text, count=1)
    if n != 1:
        raise SystemExit(f"planet rebuild failed ({n}): {path}")

    text = re.sub(r">\d+ / \d+<", f">1 / {len(apps)}<", text, count=1)
    text = re.sub(r"styles\.css\?v=\d+", f"styles.css?v={CSS_V}", text)
    text = re.sub(r"app-carousel\.js\?v=\d+", f"app-carousel.js?v={JS_V}", text)
    path.write_text(text, encoding="utf-8")
    print("index", lang, "apps", len(apps))


def update_compare(lang: str) -> None:
    path = DOCS / lang / "compare.html"
    text = path.read_text(encoding="utf-8")
    c = COPY[lang]
    text = upsert_nav(text, lang, path)
    row = (
        f"<tr><td>{NAME}</td><td>{c['compare_best']}</td>"
        f"<td>{c['compare_proto']}</td><td>{c['compare_plat']}</td></tr>"
    )
    if f"<td>{NAME}</td>" in text:
        text = re.sub(
            rf"<tr><td>{re.escape(NAME)}</td><td>[^<]*</td><td>[^<]*</td><td>[^<]*</td></tr>",
            row,
            text,
            count=1,
        )
    else:
        m = re.search(
            r"(<tr><td>Stage Audio Edit</td>.*?</tr>)",
            text,
            re.S,
        )
        if m:
            text = text[: m.end(1)] + "\n                " + row + text[m.end(1) :]
        else:
            text = text.replace("</tbody>", f"                {row}\n              </tbody>", 1)
    text = re.sub(r"styles\.css\?v=\d+", f"styles.css?v={CSS_V}", text)
    path.write_text(text, encoding="utf-8")
    print("compare", lang)


def update_other_pages(lang: str) -> None:
    for path in sorted((DOCS / lang).glob("*.html")):
        if path.name in (HREF, "index.html", "compare.html", "stage-recorder.html"):
            continue
        text = path.read_text(encoding="utf-8")
        if 'class="nav"' not in text:
            continue
        text2 = upsert_nav(text, lang, path)
        text2 = re.sub(r"styles\.css\?v=\d+", f"styles.css?v={CSS_V}", text2)
        if text2 != text:
            path.write_text(text2, encoding="utf-8")


def update_js() -> None:
    path = DOCS / "js" / "app-carousel.js"
    js = path.read_text(encoding="utf-8")
    needle = '''      } else if (app.name === "Stage Backup") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Backup"));
      }'''
    insert = '''      } else if (app.name === "Stage Align") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Align"));
      } else if (app.name === "Stage Backup") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Backup"));
      }'''
    if 'app.name === "Stage Align"' not in js:
        if needle not in js:
            raise SystemExit("js needle missing")
        js = js.replace(needle, insert)
        path.write_text(js, encoding="utf-8")
        print("js ok")
    else:
        print("js already")


def main() -> None:
    update_js()
    for lang in LANGS:
        write_product_page(lang)
        update_index(lang)
        update_compare(lang)
        update_other_pages(lang)
    print("DONE")


if __name__ == "__main__":
    main()
