#!/usr/bin/env python3
"""Add Stage SPL (coming soon, free) to the Stage Apps site — under Audio family."""
from __future__ import annotations

import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
IMAGE = "../assets/images/stage-spl-square-1080.png"
HREF = "stage-spl.html"
NAME = "Stage SPL"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]
CSS_V = "38"
JS_V = "28"

COPY = {'es': {'meta': 'Medidor SPL para iPhone e iPad: dB(A)/dB(C)/dB(Z), Fast/Slow/Impulse, Max/Min/Leq y calibración.', 'title': 'Stage SPL (iOS) — Stage Apps', 'h1': 'Stage SPL (iOS)', 'lead': 'Stage SPL mide el nivel de presión sonora en la sala con el mic del iPhone o un mic externo. Ponderación A/C/Z, constantes de tiempo, lectura grande, módulos VU/pico/barra y calibración frente a un sonómetro. Orientativo para directo; no sustituye un medidor certificado IEC 61672.', 'features_h': 'Características', 'features': ['Lectura SPL en vivo con Max, Min y Leq de la sesión.', 'Ponderación dB(A), dB(C) y dB(Z); tiempos Fast, Slow e Impulse.', 'Módulos ciclables: vúmetro analógico, picómetro LED y barra de nivel.', 'Calibración con offset frente a un sonómetro o calibrador (94 dB @ 1 kHz).', 'Micrófono del iPhone o entrada externa (USB / Lightning / interfaz).', 'Límite de alerta configurable: por debajo en azul, al llegar o superar en rojo.', 'Orientación vertical u horizontal; en landscape, número grande + un módulo.', 'iPhone e iPad · iOS 16 o posterior.'], 'soon_h': 'Próximamente', 'soon_p': '<strong>En breve en la App Store.</strong> Será gratis. Requiere iOS 16 o posterior.', 'icon_alt': 'Icono de Stage SPL', 'footer_links': '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>', 'nav_home': 'Inicio', 'nav_audio': 'Audio', 'nav_midi': 'MIDI / OSC', 'nav_rf': 'RF', 'nav_backup': 'Backup', 'nav_access': 'Accesibilidad', 'nav_proj': 'Proyectores y pantalla', 'nav_patch': 'Patch y routing', 'nav_rehearsal': 'Ensayo actoral', 'nav_compare': 'Comparativa', 'nav_resources': 'Recursos', 'nav_faq': 'FAQ', 'nav_support': 'Soporte', 'lang_label': 'Español', 'lang_emoji': '🇪🇸', 'aria_lang': 'Selector de idioma', 'aria_nav': 'Principal', 'privacy': 'Privacidad', 'support': 'Soporte', 'disclaimer': 'QLab es una marca de Figure 53. Este sitio y estas apps son productos independientes y no están afiliados, respaldados ni patrocinados por Figure 53.', 'made': 'Software independiente · Santiago de Compostela', 'blurb': 'Medidor SPL para iPhone e iPad.', 'detail': 'dB(A)/C/Z, Fast/Slow/Impulse, Max/Min/Leq, calibración y módulos VU/pico/barra. Próximamente en la App Store (gratis).', 'compare_best': 'Medir SPL en sala (orientativo, no IEC certificado)', 'compare_proto': 'Mic iPhone / externo', 'compare_plat': 'iOS 16+ · gratis · próximamente'}, 'en': {'meta': 'SPL meter for iPhone and iPad: dB(A)/dB(C)/dB(Z), Fast/Slow/Impulse, Max/Min/Leq and calibration.', 'title': 'Stage SPL (iOS) — Stage Apps', 'h1': 'Stage SPL (iOS)', 'lead': 'Stage SPL measures sound pressure level in the room with the iPhone mic or an external mic. A/C/Z weighting, time constants, big readout, VU/peak/bar modules and calibration against a meter. For live guidance; not a certified IEC 61672 replacement.', 'features_h': 'Features', 'features': ['Live SPL readout with session Max, Min and Leq.', 'dB(A), dB(C) and dB(Z) weighting; Fast, Slow and Impulse times.', 'Cycling modules: analog VU, LED peak meter and level bar.', 'Offset calibration against a sound level meter or calibrator (94 dB @ 1 kHz).', 'iPhone microphone or external input (USB / Lightning / interface).', 'Configurable alert limit: blue below, red at or above.', 'Portrait or landscape; in landscape, big number + one module.', 'iPhone and iPad · iOS 16 or later.'], 'soon_h': 'Coming soon', 'soon_p': '<strong>Coming soon to the App Store.</strong> It will be free. Requires iOS 16 or later.', 'icon_alt': 'Stage SPL icon', 'footer_links': '<p><a href="compare.html">Compare apps</a> · <a href="use-cases.html">Use cases</a> · <a href="support.html">Support</a></p>', 'nav_home': 'Home', 'nav_audio': 'Audio', 'nav_midi': 'MIDI / OSC', 'nav_rf': 'RF', 'nav_backup': 'Backup', 'nav_access': 'Accessibility', 'nav_proj': 'Projectors & screen', 'nav_patch': 'Patch & routing', 'nav_rehearsal': 'Acting rehearsal', 'nav_compare': 'Compare', 'nav_resources': 'Resources', 'nav_faq': 'FAQ', 'nav_support': 'Support', 'lang_label': 'English', 'lang_emoji': '🇬🇧', 'aria_lang': 'Language selector', 'aria_nav': 'Main', 'privacy': 'Privacy', 'support': 'Support', 'disclaimer': 'QLab is a trademark of Figure 53. This site and these apps are independent products and are not affiliated with, endorsed by, or sponsored by Figure 53.', 'made': 'Independent software · Santiago de Compostela', 'blurb': 'SPL meter for iPhone and iPad.', 'detail': 'dB(A)/C/Z, Fast/Slow/Impulse, Max/Min/Leq, calibration and VU/peak/bar modules. Coming soon to the App Store (free).', 'compare_best': 'Measure room SPL (guidance only, not certified IEC)', 'compare_proto': 'iPhone / external mic', 'compare_plat': 'iOS 16+ · free · coming soon'}, 'fr': {'meta': 'Sonomètre SPL pour iPhone et iPad : dB(A)/dB(C)/dB(Z), Fast/Slow/Impulse, Max/Min/Leq et étalonnage.', 'title': 'Stage SPL (iOS) — Stage Apps', 'h1': 'Stage SPL (iOS)', 'lead': 'Stage SPL mesure le niveau de pression acoustique dans la salle avec le micro de l’iPhone ou un micro externe. Pondération A/C/Z, constantes de temps, grand affichage, modules VU/crête/barre et étalonnage. Pour le live ; ne remplace pas un sonomètre certifié IEC 61672.', 'features_h': 'Fonctionnalités', 'features': ['Lecture SPL en direct avec Max, Min et Leq de session.', 'Pondération dB(A), dB(C) et dB(Z) ; temps Fast, Slow et Impulse.', 'Modules cyclables : VU analogique, crête LED et barre de niveau.', 'Étalonnage d’offset avec un sonomètre ou calibrateur (94 dB @ 1 kHz).', 'Micro iPhone ou entrée externe (USB / Lightning / interface).', 'Limite d’alerte réglable : bleu en dessous, rouge à/au-dessus.', 'Portrait ou paysage ; en paysage, grand chiffre + un module.', 'iPhone et iPad · iOS 16 ou plus récent.'], 'soon_h': 'Bientôt', 'soon_p': '<strong>Bientôt sur l’App Store.</strong> Ce sera gratuit. iOS 16 ou plus récent.', 'icon_alt': 'Icône Stage SPL', 'footer_links': '<p><a href="compare.html">Comparatif</a> · <a href="use-cases.html">Cas d’usage</a> · <a href="support.html">Support</a></p>', 'nav_home': 'Accueil', 'nav_audio': 'Audio', 'nav_midi': 'MIDI / OSC', 'nav_rf': 'RF', 'nav_backup': 'Backup', 'nav_access': 'Accessibilité', 'nav_proj': 'Projecteurs et écran', 'nav_patch': 'Patch et routing', 'nav_rehearsal': 'Répétition théâtre', 'nav_compare': 'Comparatif', 'nav_resources': 'Ressources', 'nav_faq': 'FAQ', 'nav_support': 'Support', 'lang_label': 'Français', 'lang_emoji': '🇫🇷', 'aria_lang': 'Sélecteur de langue', 'aria_nav': 'Principal', 'privacy': 'Confidentialité', 'support': 'Support', 'disclaimer': 'QLab est une marque de Figure 53. Ce site et ces apps sont des produits indépendants et ne sont pas affiliés, cautionnés ni sponsorisés par Figure 53.', 'made': 'Logiciel indépendant · Santiago de Compostela', 'blurb': 'Sonomètre SPL pour iPhone et iPad.', 'detail': 'dB(A)/C/Z, Fast/Slow/Impulse, Max/Min/Leq, étalonnage et modules VU/crête/barre. Bientôt sur l’App Store (gratuit).', 'compare_best': 'Mesurer le SPL en salle (indicatif, pas IEC certifié)', 'compare_proto': 'Micro iPhone / externe', 'compare_plat': 'iOS 16+ · gratuit · bientôt'}, 'de': {'meta': 'SPL-Messgerät für iPhone und iPad: dB(A)/dB(C)/dB(Z), Fast/Slow/Impulse, Max/Min/Leq und Kalibrierung.', 'title': 'Stage SPL (iOS) — Stage Apps', 'h1': 'Stage SPL (iOS)', 'lead': 'Stage SPL misst den Schalldruckpegel im Raum mit dem iPhone-Mikrofon oder einem Externmikrofon. A/C/Z-Bewertung, Zeitkonstanten, große Anzeige, VU/Peak/Balken-Module und Kalibrierung. Für Live-Orientierung; kein zertifizierter IEC-61672-Ersatz.', 'features_h': 'Funktionen', 'features': ['Live-SPL mit Max, Min und Leq der Sitzung.', 'dB(A)-, dB(C)- und dB(Z)-Bewertung; Fast, Slow und Impulse.', 'Wechselmodule: analoges VU, LED-Peakmeter und Pegelbalken.', 'Offset-Kalibrierung mit Schallpegelmesser oder Kalibrator (94 dB @ 1 kHz).', 'iPhone-Mikrofon oder externer Eingang (USB / Lightning / Interface).', 'Konfigurierbare Alarmgrenze: blau darunter, rot ab Grenze.', 'Hoch- oder Querformat; Querformat: große Zahl + ein Modul.', 'iPhone und iPad · iOS 16 oder neuer.'], 'soon_h': 'Demnächst', 'soon_p': '<strong>Demnächst im App Store.</strong> Kostenlos. Erfordert iOS 16 oder neuer.', 'icon_alt': 'Stage-SPL-Symbol', 'footer_links': '<p><a href="compare.html">Vergleich</a> · <a href="use-cases.html">Anwendungsfälle</a> · <a href="support.html">Support</a></p>', 'nav_home': 'Start', 'nav_audio': 'Audio', 'nav_midi': 'MIDI / OSC', 'nav_rf': 'RF', 'nav_backup': 'Backup', 'nav_access': 'Barrierefreiheit', 'nav_proj': 'Projektoren & Bildschirm', 'nav_patch': 'Patch & Routing', 'nav_rehearsal': 'Schauspiel-Probe', 'nav_compare': 'Vergleich', 'nav_resources': 'Ressourcen', 'nav_faq': 'FAQ', 'nav_support': 'Support', 'lang_label': 'Deutsch', 'lang_emoji': '🇩🇪', 'aria_lang': 'Sprachauswahl', 'aria_nav': 'Hauptnavigation', 'privacy': 'Datenschutz', 'support': 'Support', 'disclaimer': 'QLab ist eine Marke von Figure 53. Diese Website und Apps sind unabhängige Produkte und nicht mit Figure 53 verbunden, von Figure 53 unterstützt oder gesponsert.', 'made': 'Unabhängige Software · Santiago de Compostela', 'blurb': 'SPL-Messgerät für iPhone und iPad.', 'detail': 'dB(A)/C/Z, Fast/Slow/Impulse, Max/Min/Leq, Kalibrierung und VU/Peak/Balken. Demnächst im App Store (kostenlos).', 'compare_best': 'Raum-SPL messen (Orientierung, nicht IEC-zertifiziert)', 'compare_proto': 'iPhone- / Externmikrofon', 'compare_plat': 'iOS 16+ · kostenlos · demnächst'}, 'gl': {'meta': 'Medidor SPL para iPhone e iPad: dB(A)/dB(C)/dB(Z), Fast/Slow/Impulse, Max/Min/Leq e calibración.', 'title': 'Stage SPL (iOS) — Stage Apps', 'h1': 'Stage SPL (iOS)', 'lead': 'Stage SPL mide o nivel de presión sonora na sala co mic do iPhone ou un mic externo. Ponderación A/C/Z, constantes de tempo, lectura grande, módulos VU/pico/barra e calibración. Orientativo para directo; non substitúe un medidor certificado IEC 61672.', 'features_h': 'Características', 'features': ['Lectura SPL en vivo con Max, Min e Leq da sesión.', 'Ponderación dB(A), dB(C) e dB(Z); tempos Fast, Slow e Impulse.', 'Módulos ciclables: vúmetro analóxico, picómetro LED e barra de nivel.', 'Calibración con offset fronte a un sonómetro ou calibrador (94 dB @ 1 kHz).', 'Micrófono do iPhone ou entrada externa (USB / Lightning / interface).', 'Límite de alerta configurable: por debaixo en azul, ao chegar ou superar en vermello.', 'Orientación vertical ou horizontal; en landscape, número grande + un módulo.', 'iPhone e iPad · iOS 16 ou posterior.'], 'soon_h': 'Proximamente', 'soon_p': '<strong>En breve na App Store.</strong> Será gratis. Require iOS 16 ou posterior.', 'icon_alt': 'Icona de Stage SPL', 'footer_links': '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>', 'nav_home': 'Inicio', 'nav_audio': 'Audio', 'nav_midi': 'MIDI / OSC', 'nav_rf': 'RF', 'nav_backup': 'Backup', 'nav_access': 'Accesibilidade', 'nav_proj': 'Proxectores e pantalla', 'nav_patch': 'Patch e routing', 'nav_rehearsal': 'Ensaio actoral', 'nav_compare': 'Comparativa', 'nav_resources': 'Recursos', 'nav_faq': 'FAQ', 'nav_support': 'Soporte', 'lang_label': 'Galego', 'lang_emoji': '', 'aria_lang': 'Selector de lingua', 'aria_nav': 'Navegación principal', 'privacy': 'Privacidade', 'support': 'Soporte', 'disclaimer': 'QLab é unha marca de Figure 53. Este sitio e estas apps son produtos independentes e non están afiliados, respaldados nin patrocinados por Figure 53.', 'made': 'Software independente · Santiago de Compostela', 'blurb': 'Medidor SPL para iPhone e iPad.', 'detail': 'dB(A)/C/Z, Fast/Slow/Impulse, Max/Min/Leq, calibración e módulos VU/pico/barra. Proximamente na App Store (gratis).', 'compare_best': 'Medir SPL na sala (orientativo, non IEC certificado)', 'compare_proto': 'Mic iPhone / externo', 'compare_plat': 'iOS 16+ · gratis · proximamente'}, 'ca': {'meta': 'Mesurador SPL per a iPhone i iPad: dB(A)/dB(C)/dB(Z), Fast/Slow/Impulse, Max/Min/Leq i calibratge.', 'title': 'Stage SPL (iOS) — Stage Apps', 'h1': 'Stage SPL (iOS)', 'lead': 'Stage SPL mesura el nivell de pressió sonora a la sala amb el mic de l’iPhone o un mic extern. Ponderació A/C/Z, constants de temps, lectura gran, mòduls VU/pic/barra i calibratge. Orientatiu per a directe; no substitueix un mesurador certificat IEC 61672.', 'features_h': 'Característiques', 'features': ['Lectura SPL en directe amb Max, Min i Leq de la sessió.', 'Ponderació dB(A), dB(C) i dB(Z); temps Fast, Slow i Impulse.', 'Mòduls ciclables: vúmetre analògic, picòmetre LED i barra de nivell.', 'Calibratge amb offset davant d’un sonòmetre o calibrador (94 dB @ 1 kHz).', 'Micròfon de l’iPhone o entrada externa (USB / Lightning / interface).', 'Límit d’alerta configurable: per sota en blau, en arribar o superar en vermell.', 'Orientació vertical o horitzontal; en landscape, número gran + un mòdul.', 'iPhone i iPad · iOS 16 o posterior.'], 'soon_h': 'Properament', 'soon_p': '<strong>Aviat a l’App Store.</strong> Serà gratuït. Requereix iOS 16 o posterior.', 'icon_alt': 'Icona de Stage SPL', 'footer_links': '<p><a href="compare.html">Veure comparativa</a> · <a href="use-cases.html">Veure casos d’ús</a> · <a href="support.html">Suport</a></p>', 'nav_home': 'Inici', 'nav_audio': 'Àudio', 'nav_midi': 'MIDI / OSC', 'nav_rf': 'RF', 'nav_backup': 'Backup', 'nav_access': 'Accessibilitat', 'nav_proj': 'Projectors i pantalla', 'nav_patch': 'Patch i routing', 'nav_rehearsal': 'Assaig actoral', 'nav_compare': 'Comparativa', 'nav_resources': 'Recursos', 'nav_faq': 'FAQ', 'nav_support': 'Suport', 'lang_label': 'Català', 'lang_emoji': '', 'aria_lang': 'Selector d’idioma', 'aria_nav': 'Navegació principal', 'privacy': 'Privacitat', 'support': 'Suport', 'disclaimer': 'QLab és una marca de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, avalats ni patrocinats per Figure 53.', 'made': 'Programari independent · Santiago de Compostela', 'blurb': 'Mesurador SPL per a iPhone i iPad.', 'detail': 'dB(A)/C/Z, Fast/Slow/Impulse, Max/Min/Leq, calibratge i mòduls VU/pic/barra. Properament a l’App Store (gratuït).', 'compare_best': 'Mesurar SPL a la sala (orientatiu, no IEC certificat)', 'compare_proto': 'Mic iPhone / extern', 'compare_plat': 'iOS 16+ · gratuït · properament'}, 'eu': {'meta': 'SPL neurgailua iPhone eta iPad-erako: dB(A)/dB(C)/dB(Z), Fast/Slow/Impulse, Max/Min/Leq eta kalibrazioa.', 'title': 'Stage SPL (iOS) — Stage Apps', 'h1': 'Stage SPL (iOS)', 'lead': 'Stage SPL-k gelako soinu-presioaren maila neurtzen du iPhonearen mikroarekin edo kanpoko mikro batekin. A/C/Z ponderazioa, denbora-konstanteak, irakurketa handia, VU/goi/barra moduluak eta kalibrazioa. Zuzenekorako orientagarria; ez du IEC 61672 neurgailu ziurtatua ordezkatzen.', 'features_h': 'Ezaugarriak', 'features': ['SPL irakurketa zuzenean Max, Min eta Leq-ekin.', 'dB(A), dB(C) eta dB(Z) ponderazioa; Fast, Slow eta Impulse.', 'Modulu ziklikoak: VU analogikoa, LED goilurra eta maila-barra.', 'Offset kalibrazioa sonometro edo kalibratzailearekin (94 dB @ 1 kHz).', 'iPhone mikrofonoa edo kanpoko sarrera (USB / Lightning / interface).', 'Alerta-muga konfiguragarria: azpitik urdinez, iristean edo gainditzean gorriz.', 'Orientazio bertikala edo horizontala; landscape-n zenbaki handia + modulu bat.', 'iPhone eta iPad · iOS 16 edo berriagoa.'], 'soon_h': 'Laster', 'soon_p': '<strong>Laster App Store-n.</strong> Doan izango da. iOS 16 edo berriagoa behar du.', 'icon_alt': 'Stage SPL ikonoa', 'footer_links': '<p><a href="compare.html">Konparaketa ikusi</a> · <a href="use-cases.html">Erabilera-kasuak</a> · <a href="support.html">Laguntza</a></p>', 'nav_home': 'Hasiera', 'nav_audio': 'Audioa', 'nav_midi': 'MIDI / OSC', 'nav_rf': 'RF', 'nav_backup': 'Backup', 'nav_access': 'Irisgarritasuna', 'nav_proj': 'Proiektoreak eta pantaila', 'nav_patch': 'Patch eta routing', 'nav_rehearsal': 'Antzezlan entsegua', 'nav_compare': 'Konparaketa', 'nav_resources': 'Baliabideak', 'nav_faq': 'FAQ', 'nav_support': 'Laguntza', 'lang_label': 'Euskara', 'lang_emoji': '', 'aria_lang': 'Hizkuntza-hautatzailea', 'aria_nav': 'Menu nagusia', 'privacy': 'Pribatutasuna', 'support': 'Laguntza', 'disclaimer': 'QLab Figure 53-ren marka da. Gune hau eta app hauek produktu independenteak dira eta ez daude Figure 53-rekin afiliatuta, babestuta edo babestuta.', 'made': 'Software independentea · Santiago de Compostela', 'blurb': 'SPL neurgailua iPhone eta iPad-erako.', 'detail': 'dB(A)/C/Z, Fast/Slow/Impulse, Max/Min/Leq, kalibrazioa eta VU/goi/barra. Laster App Store-n (doan).', 'compare_best': 'Gelako SPL neurtu (orientagarria, ez IEC ziurtatua)', 'compare_proto': 'iPhone / kanpoko mikrofonoa', 'compare_plat': 'iOS 16+ · doan · laster'}}

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
                (HREF, "Stage SPL"),
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
    insert = '''      } else if (app.name === "Stage SPL") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("SPL"));
      } else if (app.name === "Stage Backup") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Backup"));
      }'''
    if 'app.name === "Stage SPL"' not in js:
        if needle not in js:
            raise SystemExit("js needle missing")
        js = js.replace(needle, insert)
        path.write_text(js, encoding="utf-8")
        print("js ok")
    else:
        print("js already")


def update_sitemap() -> None:
    skip = {"stage-recorder.html", "home-carousel-preview.html"}
    urls = ["https://stageapps.org/"]
    for lang in LANGS:
        for p in sorted((DOCS / lang).glob("*.html")):
            if p.name in skip:
                continue
            urls.append(f"https://stageapps.org/{lang}/{p.name}")
    for name in ("support.html", "privacy.html"):
        if (DOCS / name).exists():
            urls.append(f"https://stageapps.org/{name}")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        lines.append(f"  <url><loc>{u}</loc></url>")
    lines.append("</urlset>")
    (DOCS / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("sitemap", len(urls))


def main() -> None:
    update_js()
    for lang in LANGS:
        write_product_page(lang)
        update_index(lang)
        update_compare(lang)
        update_other_pages(lang)
    update_sitemap()
    print("DONE")


if __name__ == "__main__":
    main()
