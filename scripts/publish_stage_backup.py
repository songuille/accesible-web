#!/usr/bin/env python3
"""Add Stage Backup (coming soon) to the Stage Apps site."""
from __future__ import annotations

import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
IMAGE = "../assets/images/stage-backup-square-1080.png"
HREF = "stage-backup.html"
NAME = "Stage Backup"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]

COPY = {
    "es": {
        "meta": "Copias incrementales tranquilas de carpetas concretas en Mac: orígenes, destinos e instantáneas. No sustituye Time Machine.",
        "title": "Stage Backup (macOS) — Stage Apps",
        "h1": "Stage Backup (macOS)",
        "lead": "Stage Backup protege carpetas concretas con copias incrementales calmadas: une orígenes y destinos, guarda instantáneas por fecha y trabaja en segundo plano sin sorpresas. No sustituye Time Machine.",
        "features_h": "Características",
        "features": [
            "Orígenes y destinos visuales: une carpetas con flechas y ves de un vistazo qué está al día.",
            "Copia incremental con hard links / clonefile: ahorra espacio entre fechas.",
            "Instantáneas por fecha: vuelve atrás o restaura sin borrar nada solo.",
            "Nunca borra en el destino sin pedirte confirmación (incluida la poda).",
            "Segundo plano y barra de menús: cierra la ventana y sigue protegiendo.",
            "Copia al conectar un destino, al despertar o con «Copiar ahora»; ritmo calmado por intervalos.",
            "Informe de estado de Time Machine (solo lectura): no controla ni sustituye Time Machine.",
            "Prueba de velocidad del disco destino (~48 MB) para detectar pendrives lentos o falsos.",
        ],
        "soon_h": "Próximamente",
        "soon_p": "<strong>En breve en la Mac App Store.</strong> Requiere macOS 14 o posterior.",
        "icon_alt": "Icono de Stage Backup",
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
        "blurb": "Copias incrementales tranquilas de carpetas en Mac.",
        "detail": "Protege carpetas concretas con orígenes, destinos e instantáneas. Segundo plano y barra de menús. No sustituye Time Machine. Próximamente en la Mac App Store.",
        "compare_best": "Copias incrementales de carpetas concretas con instantáneas",
        "compare_proto": "Archivos locales / USB",
        "compare_plat": "macOS 14+ · próximamente",
    },
    "en": {
        "meta": "Calm incremental folder backups on Mac: sources, destinations and snapshots. Does not replace Time Machine.",
        "title": "Stage Backup (macOS) — Stage Apps",
        "h1": "Stage Backup (macOS)",
        "lead": "Stage Backup protects specific folders with calm incremental backups: link sources to destinations, keep dated snapshots, and run in the background without surprises. It does not replace Time Machine.",
        "features_h": "Features",
        "features": [
            "Visual sources and destinations: connect folders with arrows and see what’s up to date at a glance.",
            "Incremental copy with hard links / clonefile—saves space across dates.",
            "Dated snapshots: go back or restore; nothing is pruned automatically.",
            "Never deletes on the destination without asking first (including prune).",
            "Background and menu bar: close the window and keep protecting.",
            "Backs up when a destination connects, on wake, or via Back Up Now; calm interval pacing.",
            "Read-only Time Machine status: does not control or replace Time Machine.",
            "Destination disk speed test (~48 MB) to spot slow or fake USB sticks.",
        ],
        "soon_h": "Coming soon",
        "soon_p": "<strong>Coming soon to the Mac App Store.</strong> Requires macOS 14 or later.",
        "icon_alt": "Stage Backup icon",
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
        "blurb": "Calm incremental folder backups on Mac.",
        "detail": "Protect specific folders with sources, destinations and snapshots. Background and menu bar. Does not replace Time Machine. Coming soon to the Mac App Store.",
        "compare_best": "Incremental backups of specific folders with snapshots",
        "compare_proto": "Local files / USB",
        "compare_plat": "macOS 14+ · coming soon",
    },
    "fr": {
        "meta": "Sauvegardes incrémentielles discrètes de dossiers sur Mac : sources, destinations et instantanés. Ne remplace pas Time Machine.",
        "title": "Stage Backup (macOS) — Stage Apps",
        "h1": "Stage Backup (macOS)",
        "lead": "Stage Backup protège des dossiers précis avec des sauvegardes incrémentielles calmes : reliez sources et destinations, gardez des instantanés datés et travaillez en arrière-plan sans surprises. Ne remplace pas Time Machine.",
        "features_h": "Fonctionnalités",
        "features": [
            "Sources et destinations visuelles : flèches et statut d’un coup d’œil.",
            "Copie incrémentielle avec hard links / clonefile : économise l’espace entre dates.",
            "Instantanés datés : revenir en arrière ou restaurer ; rien n’est purgé tout seul.",
            "Ne supprime jamais sur la destination sans confirmation (purge incluse).",
            "Arrière-plan et barre de menus : fermez la fenêtre, la protection continue.",
            "Copie à la connexion d’une destination, au réveil ou via Sauvegarder maintenant.",
            "État Time Machine en lecture seule : ne pilote ni ne remplace Time Machine.",
            "Test de vitesse du disque destination (~48 Mo) pour détecter les clés lentes ou fausses.",
        ],
        "soon_h": "Bientôt",
        "soon_p": "<strong>Bientôt sur le Mac App Store.</strong> macOS 14 ou plus récent.",
        "icon_alt": "Icône Stage Backup",
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
        "blurb": "Sauvegardes incrémentielles calmes de dossiers sur Mac.",
        "detail": "Protégez des dossiers précis avec sources, destinations et instantanés. Arrière-plan et barre de menus. Ne remplace pas Time Machine. Bientôt sur le Mac App Store.",
        "compare_best": "Sauvegardes incrémentielles de dossiers précis avec instantanés",
        "compare_proto": "Fichiers locaux / USB",
        "compare_plat": "macOS 14+ · bientôt",
    },
    "de": {
        "meta": "Ruhige inkrementelle Ordner-Sicherungen auf dem Mac: Quellen, Ziele und Momentaufnahmen. Ersetzt Time Machine nicht.",
        "title": "Stage Backup (macOS) — Stage Apps",
        "h1": "Stage Backup (macOS)",
        "lead": "Stage Backup schützt ausgewählte Ordner mit ruhigen inkrementellen Sicherungen: Quellen und Ziele verbinden, datierte Snapshots behalten und im Hintergrund laufen lassen. Ersetzt Time Machine nicht.",
        "features_h": "Funktionen",
        "features": [
            "Visuelle Quellen und Ziele: Ordner per Pfeil verbinden und Status auf einen Blick sehen.",
            "Inkrementelle Kopie mit Hardlinks / clonefile — spart Platz über Datumsstände.",
            "Datierte Snapshots: zurückkehren oder wiederherstellen; nichts wird automatisch bereinigt.",
            "Löscht am Ziel nie ohne Bestätigung (auch Bereinigung).",
            "Hintergrund und Menüleiste: Fenster schließen und weiter schützen.",
            "Sichert beim Anschließen eines Ziels, beim Aufwachen oder mit Jetzt sichern.",
            "Time-Machine-Status nur lesend: steuert oder ersetzt Time Machine nicht.",
            "Geschwindigkeitstest des Ziel-Laufwerks (~48 MB) gegen langsame oder gefälschte Sticks.",
        ],
        "soon_h": "Demnächst",
        "soon_p": "<strong>Demnächst im Mac App Store.</strong> Erfordert macOS 14 oder neuer.",
        "icon_alt": "Stage-Backup-Symbol",
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
        "blurb": "Ruhige inkrementelle Ordner-Backups für Mac.",
        "detail": "Schützt ausgewählte Ordner mit Quellen, Zielen und Snapshots. Hintergrund und Menüleiste. Ersetzt Time Machine nicht. Demnächst im Mac App Store.",
        "compare_best": "Inkrementelle Sicherung ausgewählter Ordner mit Snapshots",
        "compare_proto": "Lokale Dateien / USB",
        "compare_plat": "macOS 14+ · demnächst",
    },
    "gl": {
        "meta": "Copias incrementais tranquilas de carpetas concretas no Mac: orixes, destinos e instantáneas. Non substitúe Time Machine.",
        "title": "Stage Backup (macOS) — Stage Apps",
        "h1": "Stage Backup (macOS)",
        "lead": "Stage Backup protexe carpetas concretas con copias incrementais calmadas: une orixes e destinos, garda instantáneas por data e traballa en segundo plano sen sorpresas. Non substitúe Time Machine.",
        "features_h": "Características",
        "features": [
            "Orixes e destinos visuais: une carpetas con frechas e ves de golpe o que está ao día.",
            "Copia incremental con hard links / clonefile: aforra espazo entre datas.",
            "Instantáneas por data: volve atrás ou restaura; nada se poda só.",
            "Nunca borra no destino sen confirmación (incluída a poda).",
            "Segundo plano e barra de menús: pecha a ventá e segue protexendo.",
            "Copia ao conectar un destino, ao espertar ou con «Copiar agora».",
            "Informe de estado de Time Machine (só lectura): non controla nin substitúe Time Machine.",
            "Proba de velocidade do disco destino (~48 MB) para detectar pendrives lentos ou falsos.",
        ],
        "soon_h": "Proximamente",
        "soon_p": "<strong>En breve na Mac App Store.</strong> Require macOS 14 ou posterior.",
        "icon_alt": "Icona de Stage Backup",
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
        "aria_lang": "Selector de idioma",
        "aria_nav": "Principal",
        "privacy": "Privacidade",
        "support": "Soporte",
        "disclaimer": "QLab é unha marca de Figure 53. Este sitio e estas apps son produtos independentes e non están afiliados, respaldados nin patrocinados por Figure 53.",
        "made": "Software independente · Santiago de Compostela",
        "blurb": "Copias incrementais tranquilas de carpetas no Mac.",
        "detail": "Protexe carpetas concretas con orixes, destinos e instantáneas. Segundo plano e barra de menús. Non substitúe Time Machine. Proximamente na Mac App Store.",
        "compare_best": "Copias incrementais de carpetas concretas con instantáneas",
        "compare_proto": "Arquivos locais / USB",
        "compare_plat": "macOS 14+ · proximamente",
    },
    "ca": {
        "meta": "Còpies incrementals tranquil·les de carpetes concretes al Mac: orígens, destinacions i instantànies. No substitueix Time Machine.",
        "title": "Stage Backup (macOS) — Stage Apps",
        "h1": "Stage Backup (macOS)",
        "lead": "Stage Backup protegeix carpetes concretes amb còpies incrementals calmades: uneix orígens i destinacions, desa instantànies per data i treballa en segon pla sense sorpreses. No substitueix Time Machine.",
        "features_h": "Característiques",
        "features": [
            "Orígens i destinacions visuals: uneix carpetes amb fletxes i veus d’un cop d’ull què està al dia.",
            "Còpia incremental amb hard links / clonefile: estalvia espai entre dates.",
            "Instantànies per data: torna enrere o restaura; res no es poda sol.",
            "Mai esborra a la destinació sense confirmació (inclosa la poda).",
            "Segon pla i barra de menús: tanca la finestra i continua protegint.",
            "Copia en connectar una destinació, en despertar o amb «Copia ara».",
            "Informe d’estat de Time Machine (només lectura): no controla ni substitueix Time Machine.",
            "Prova de velocitat del disc de destinació (~48 MB) per detectar llapis lents o falsos.",
        ],
        "soon_h": "Properament",
        "soon_p": "<strong>Aviat al Mac App Store.</strong> Requereix macOS 14 o posterior.",
        "icon_alt": "Icona de Stage Backup",
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
        "aria_nav": "Principal",
        "privacy": "Privacitat",
        "support": "Suport",
        "disclaimer": "QLab és una marca de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, recolzats ni patrocinats per Figure 53.",
        "made": "Programari independent · Santiago de Compostela",
        "blurb": "Còpies incrementals tranquil·les de carpetes al Mac.",
        "detail": "Protegeix carpetes concretes amb orígens, destinacions i instantànies. Segon pla i barra de menús. No substitueix Time Machine. Properament al Mac App Store.",
        "compare_best": "Còpies incrementals de carpetes concretes amb instantànies",
        "compare_proto": "Fitxers locals / USB",
        "compare_plat": "macOS 14+ · properament",
    },
    "eu": {
        "meta": "Mac-eko karpeta zehatzen kopia inkremental lasaiak: iturburuak, helmugak eta argazkiak. Ez du Time Machine ordezkatzen.",
        "title": "Stage Backup (macOS) — Stage Apps",
        "h1": "Stage Backup (macOS)",
        "lead": "Stage Backup-ek karpeta zehatzak babesten ditu kopia inkremental lasaiekin: lotu iturburuak eta helmugak, gorde datazko argazkiak eta lan egin atzeko planoan. Ez du Time Machine ordezkatzen.",
        "features_h": "Ezaugarriak",
        "features": [
            "Iturburu eta helmuga bisualak: lotu karpetak gezuekin eta ikusi berehala zer dagoen eguneratuta.",
            "Kopia inkrementala hard link / clonefile-ekin: lekua aurrezten du dataz data.",
            "Datazko argazkiak: atzera joan edo berreskuratu; ezer ez da automatikoki mozten.",
            "Ez du inoiz ezabatzen helmugan berretsi gabe (garbiketa barne).",
            "Atzeko planoa eta menu-barra: itxi leihoa eta jarraitu babesten.",
            "Kopiatu helmuga konektatzean, esnatzean edo «Kopiatu orain»-ekin.",
            "Time Machine egoeraren txostena (irakurtzeko soilik): ez du kontrolatzen ez ordezkatzen.",
            "Helmuga-diskoaren abiadura proba (~48 MB) pendrive motel edo faltsuak detektatzeko.",
        ],
        "soon_h": "Laster",
        "soon_p": "<strong>Laster Mac App Store-n.</strong> macOS 14 edo berriagoa behar du.",
        "icon_alt": "Stage Backup ikonoa",
        "footer_links": '<p><a href="compare.html">Ikusi konparaketa</a> · <a href="use-cases.html">Erabilera kasuak</a> · <a href="support.html">Laguntza</a></p>',
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
        "aria_lang": "Hizkuntza hautatzailea",
        "aria_nav": "Nagusia",
        "privacy": "Pribatutasuna",
        "support": "Laguntza",
        "disclaimer": "QLab Figure 53-ren marka da. Gune hau eta app hauek produktu independenteak dira eta ez daude Figure 53-rekin afiliatuta, babestuta edo babestuta.",
        "made": "Software independentea · Santiago de Compostela",
        "blurb": "Mac-eko karpeten kopia inkremental lasaiak.",
        "detail": "Babestu karpeta zehatzak iturburu, helmuga eta argazkiekin. Atzeko planoa eta menu-barra. Ez du Time Machine ordezkatzen. Laster Mac App Store-n.",
        "compare_best": "Karpeta zehatzen kopia inkrementalak argazkiekin",
        "compare_proto": "Fitxategi lokalak / USB",
        "compare_plat": "macOS 14+ · laster",
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
            ],
        ),
        link("miditoosc.html", c["nav_midi"]),
        link("stage-rf.html", c["nav_rf"]),
        link(HREF, c["nav_backup"]),
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
  <link rel="stylesheet" href="../css/styles.css?v=38">
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
    # Insert after Stage Audio Edit if present, else after Multitrack, else append
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

    # Rebuild planet buttons in family/orbit order from apps
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
    text = re.sub(r"styles\.css\?v=\d+", "styles.css?v=38", text)
    text = re.sub(r"app-carousel\.js\?v=\d+", "app-carousel.js?v=26", text)
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
        # Insert after Stage Audio Edit row if present
        m = re.search(
            r"(<tr><td>Stage Audio Edit</td>.*?</tr>)",
            text,
            re.S,
        )
        if m:
            text = text[: m.end(1)] + "\n                " + row + text[m.end(1) :]
        else:
            text = text.replace("</tbody>", f"                {row}\n              </tbody>", 1)
    text = re.sub(r"styles\.css\?v=\d+", "styles.css?v=38", text)
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
        text2 = re.sub(r"styles\.css\?v=\d+", "styles.css?v=38", text2)
        if text2 != text:
            path.write_text(text2, encoding="utf-8")


def update_js() -> None:
    path = DOCS / "js" / "app-carousel.js"
    js = path.read_text(encoding="utf-8")
    needle = '''      } else if (app.name === "Stage RF") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("RF"));
      }'''
    insert = '''      } else if (app.name === "Stage Backup") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Backup"));
      } else if (app.name === "Stage RF") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("RF"));
      }'''
    if 'app.name === "Stage Backup"' not in js:
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
