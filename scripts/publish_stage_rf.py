#!/usr/bin/env python3
"""Add Stage RF (coming soon) to the Stage Apps site."""
import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "../assets/images/stage-rf-square-1080.png"
HREF = "stage-rf.html"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]

COPY = {
    "es": {
        "meta": "Espectro UHF en vivo (tinySA) y rack de micros inalámbricos en la misma vista. macOS 15+.",
        "title": "Stage RF (macOS) — Stage Apps",
        "h1": "Stage RF (macOS)",
        "lead": "Stage RF es la herramienta de escenario para ver el espectro UHF y todo el rack de micros inalámbricos en la misma app, en la misma vista. Conecta un tinySA por USB y trabaja el barrido en vivo sin dejar de gestionar los receptores de red.",
        "features_h": "Características",
        "features": [
            "Barrido en vivo con tinySA: líneas de frecuencia, picos detectados e iconos para anclar lo que oyes en el aire a cada receptor.",
            "Espectro y rack a la vez: el escaneo no bloquea la gestión de receptores en red.",
            "Construye el rack: busca receptores en la red o añade una IP, bloquea el inventario y carga la sesión.",
            "Modo show: solo receptores cargados, telemetría en vivo, espectro en vivo y anclaje de picos arrastrando a un receptor.",
            "Escala MHz, zoom y pan alineados: barrido y marcadores del rack comparten el mismo eje de frecuencia.",
            "De un vistazo: estado TX (verde / rojo), picos aún no anclados (naranja) y todos los canales del inventario.",
            "Vista remota en el navegador (móvil, tablet u otro ordenador): estado casi en tiempo real y chat con la app del Mac.",
            "Guarda la sesión para restaurar rack y ajustes en el siguiente bolo. Modo simulador para practicar sin equipo.",
        ],
        "soon_h": "Próximamente",
        "soon_p": "<strong>En breve en la Mac App Store.</strong> Requiere macOS 15 Sequoia o posterior; para espectro hardware, un tinySA Ultra con cable USB de datos.",
        "disclaimer_note": "Compatible con sistemas inalámbricos de escenario habituales (Shure, Sennheiser y similares). No es un producto oficial de esos fabricantes.",
        "icon_alt": "Icono de Stage RF",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "nav_home": "Inicio",
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
        "blurb": "Espectro UHF y rack inalámbrico en la misma vista.",
        "detail": "Barrido tinySA en vivo y gestión de receptores de red sin saltar de app. Vista remota en el navegador. Próximamente en la Mac App Store.",
        "compare_best": "Espectro UHF en vivo y control unificado del rack inalámbrico",
        "compare_proto": "USB tinySA · red OSC/IP",
        "compare_plat": "macOS 15+ · próximamente",
    },
    "en": {
        "meta": "Live UHF spectrum (tinySA) and your wireless mic rack in the same view. macOS 15+.",
        "title": "Stage RF (macOS) — Stage Apps",
        "h1": "Stage RF (macOS)",
        "lead": "Stage RF is the stage tool for watching the UHF spectrum and your whole wireless mic rack in the same app, in the same view. Connect a tinySA over USB and keep rack management open while the sweep runs.",
        "features_h": "Features",
        "features": [
            "Live tinySA sweep: frequency lines, detected peaks, and icons to anchor what you hear on air to each receiver.",
            "Spectrum scanning does not block rack management—work with network receivers while the tinySA sweeps.",
            "Build rack: search the network for receivers or add an IP, lock the inventory, and load the session.",
            "Show mode: only loaded receivers, live chip telemetry, live spectrum, and peak anchoring by dragging onto a receiver.",
            "MHz scale, zoom, and pan stay aligned: sweep and rack markers share the same frequency axis.",
            "At a glance: TX status (green / red), peaks not yet anchored (orange), and every inventory channel together.",
            "Remote browser view on phone, tablet, or another computer: near-real-time receiver status and chat linked to the Mac app.",
            "Save the session for the next gig. Simulator mode to practice without gear.",
        ],
        "soon_h": "Coming soon",
        "soon_p": "<strong>Coming soon to the Mac App Store.</strong> Requires macOS 15 Sequoia or later; for hardware spectrum, a tinySA Ultra on a data USB cable.",
        "disclaimer_note": "Works with common stage network wireless systems (Shure, Sennheiser, and similar). Not an official product of those manufacturers.",
        "icon_alt": "Stage RF icon",
        "footer_links": '<p><a href="compare.html">Compare apps</a> · <a href="use-cases.html">Use cases</a> · <a href="support.html">Support</a></p>',
        "nav_home": "Home",
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
        "blurb": "UHF spectrum and wireless rack in one view.",
        "detail": "Live tinySA sweep plus network receiver management without switching apps. Browser remote view. Coming soon to the Mac App Store.",
        "compare_best": "Live UHF spectrum and unified wireless rack control",
        "compare_proto": "USB tinySA · network OSC/IP",
        "compare_plat": "macOS 15+ · coming soon",
    },
    "fr": {
        "meta": "Spectre UHF en direct (tinySA) et rack de micros HF dans la même vue. macOS 15+.",
        "title": "Stage RF (macOS) — Stage Apps",
        "h1": "Stage RF (macOS)",
        "lead": "Stage RF regroupe le spectre UHF et tout le rack de micros sans fil dans la même app, la même vue. Branchez un tinySA en USB et gérez les récepteurs réseau pendant le balayage.",
        "features_h": "Fonctionnalités",
        "features": [
            "Balayage tinySA en direct : lignes de fréquence, pics détectés et icônes pour ancrer ce que vous entendez à chaque récepteur.",
            "Le spectre n’interrompt pas la gestion du rack réseau.",
            "Construisez le rack : recherche réseau ou IP, verrouillez l’inventaire et chargez la session.",
            "Mode show : récepteurs chargés, télémétrie en direct, spectre en direct et ancrage des pics par glisser-déposer.",
            "Échelle MHz, zoom et panoramique alignés sur le même axe de fréquence.",
            "D’un coup d’œil : état TX (vert / rouge), pics non ancrés (orange) et tous les canaux.",
            "Vue distante dans le navigateur (téléphone, tablette ou autre Mac) avec chat vers l’app principale.",
            "Enregistrez la session pour le prochain concert. Mode simulateur sans matériel.",
        ],
        "soon_h": "Bientôt",
        "soon_p": "<strong>Bientôt sur le Mac App Store.</strong> macOS 15 Sequoia ou plus récent ; pour le spectre matériel, un tinySA Ultra en câble USB données.",
        "disclaimer_note": "Compatible avec les systèmes HF de scène courants (Shure, Sennheiser et similaires). Produit non officiel de ces fabricants.",
        "icon_alt": "Icône Stage RF",
        "footer_links": '<p><a href="compare.html">Comparatif</a> · <a href="use-cases.html">Cas d’usage</a> · <a href="support.html">Support</a></p>',
        "nav_home": "Accueil",
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
        "disclaimer": "QLab est une marque de Figure 53. Ce site et ces apps sont des produits indépendants et ne sont pas affiliés, approuvés ni sponsorisés par Figure 53.",
        "made": "Logiciel indépendant · Santiago de Compostela",
        "blurb": "Spectre UHF et rack HF dans la même vue.",
        "detail": "Balayage tinySA en direct et gestion des récepteurs réseau sans changer d’app. Vue distante navigateur. Bientôt sur le Mac App Store.",
        "compare_best": "Spectre UHF en direct et contrôle unifié du rack HF",
        "compare_proto": "USB tinySA · réseau OSC/IP",
        "compare_plat": "macOS 15+ · bientôt",
    },
    "de": {
        "meta": "Live-UHF-Spektrum (tinySA) und drahtloses Mic-Rack in derselben Ansicht. macOS 15+.",
        "title": "Stage RF (macOS) — Stage Apps",
        "h1": "Stage RF (macOS)",
        "lead": "Stage RF zeigt UHF-Spektrum und das gesamte Wireless-Mic-Rack in derselben App und Ansicht. tinySA per USB anschließen und Empfänger im Netz verwalten, während der Sweep läuft.",
        "features_h": "Funktionen",
        "features": [
            "Live-tinySA-Sweep: Frequenzlinien, erkannte Peaks und Icons zum Ankern auf Empfänger.",
            "Spektrum blockiert nicht die Rack-Verwaltung im Netzwerk.",
            "Rack aufbauen: Netzwerksuche oder IP, Inventar sperren und Session laden.",
            "Show-Modus: geladene Empfänger, Live-Telemetrie, Live-Spektrum und Peak-Ankern per Drag & Drop.",
            "MHz-Skala, Zoom und Pan auf derselben Frequenzachse.",
            "Auf einen Blick: TX-Status (grün / rot), noch nicht verankerte Peaks (orange), alle Kanäle.",
            "Remote-Ansicht im Browser (Telefon, Tablet oder anderer Rechner) mit Chat zur Mac-App.",
            "Session speichern für den nächsten Gig. Simulator ohne Hardware.",
        ],
        "soon_h": "Demnächst",
        "soon_p": "<strong>Demnächst im Mac App Store.</strong> macOS 15 Sequoia oder neuer; für Hardware-Spektrum ein tinySA Ultra am Daten-USB-Kabel.",
        "disclaimer_note": "Funktioniert mit gängigen Bühnen-Wireless-Systemen (Shure, Sennheiser u. a.). Kein offizielles Produkt dieser Hersteller.",
        "icon_alt": "Stage-RF-Symbol",
        "footer_links": '<p><a href="compare.html">Vergleich</a> · <a href="use-cases.html">Anwendungsfälle</a> · <a href="support.html">Support</a></p>',
        "nav_home": "Start",
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
        "disclaimer": "QLab ist eine Marke von Figure 53. Diese Website und Apps sind unabhängige Produkte und stehen in keiner Verbindung zu Figure 53.",
        "made": "Unabhängige Software · Santiago de Compostela",
        "blurb": "UHF-Spektrum und Wireless-Rack in einer Ansicht.",
        "detail": "Live-tinySA-Sweep plus Netzwerk-Empfänger ohne App-Wechsel. Browser-Remote. Demnächst im Mac App Store.",
        "compare_best": "Live-UHF-Spektrum und einheitliche Wireless-Rack-Steuerung",
        "compare_proto": "USB tinySA · Netzwerk OSC/IP",
        "compare_plat": "macOS 15+ · demnächst",
    },
    "gl": {
        "meta": "Espectro UHF en vivo (tinySA) e rack de micros inalámbricos na mesma vista. macOS 15+.",
        "title": "Stage RF (macOS) — Stage Apps",
        "h1": "Stage RF (macOS)",
        "lead": "Stage RF amosa o espectro UHF e todo o rack de micros inalámbricos na mesma app e vista. Conecta un tinySA por USB e xestiona os receptores de rede mentres o varrido continúa.",
        "features_h": "Características",
        "features": [
            "Varrido tinySA en vivo: liñas de frecuencia, picos detectados e iconas para ancorar o que oyes a cada receptor.",
            "O espectro non bloquea a xestión do rack en rede.",
            "Constrúe o rack: busca na rede ou engade IP, bloquea o inventario e carga a sesión.",
            "Modo show: receptores cargados, telemetría en vivo, espectro en vivo e ancoraxe de picos arrastrando.",
            "Escala MHz, zoom e pan aliñados no mesmo eixe de frecuencia.",
            "Dun vistazo: estado TX (verde / vermello), picos sen ancorar (laranxa) e todos os canais.",
            "Vista remota no navegador (móbil, tablet ou outro PC) con chat cara á app do Mac.",
            "Garda a sesión para o seguinte bolo. Modo simulador sen equipo.",
        ],
        "soon_h": "Proximamente",
        "soon_p": "<strong>En breve na Mac App Store.</strong> macOS 15 Sequoia ou posterior; para espectro hardware, un tinySA Ultra con cable USB de datos.",
        "disclaimer_note": "Compatible con sistemas inalámbricos de escenario habituais (Shure, Sennheiser e similares). Non é un produto oficial deses fabricantes.",
        "icon_alt": "Icona de Stage RF",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "nav_home": "Inicio",
        "nav_compare": "Comparativa",
        "nav_resources": "Recursos",
        "nav_faq": "FAQ",
        "nav_support": "Soporte",
        "lang_label": "Galego",
        "lang_emoji": None,
        "lang_flag": "../assets/flags/gl.svg",
        "aria_lang": "Selector de idioma",
        "aria_nav": "Principal",
        "privacy": "Privacidade",
        "support": "Soporte",
        "disclaimer": "QLab é unha marca de Figure 53. Este sitio e estas apps son produtos independentes e non están afiliados, respaldados nin patrocinados por Figure 53.",
        "made": "Software independente · Santiago de Compostela",
        "blurb": "Espectro UHF e rack inalámbrico na mesma vista.",
        "detail": "Varrido tinySA en vivo e xestión de receptores de rede sen cambiar de app. Vista remota no navegador. Proximamente na Mac App Store.",
        "compare_best": "Espectro UHF en vivo e control unificado do rack inalámbrico",
        "compare_proto": "USB tinySA · rede OSC/IP",
        "compare_plat": "macOS 15+ · proximamente",
    },
    "ca": {
        "meta": "Espectre UHF en viu (tinySA) i rack de micros sense fil a la mateixa vista. macOS 15+.",
        "title": "Stage RF (macOS) — Stage Apps",
        "h1": "Stage RF (macOS)",
        "lead": "Stage RF mostra l’espectre UHF i tot el rack de micros sense fil a la mateixa app i vista. Connecta un tinySA per USB i gestiona els receptors de xarxa mentre el barrido continua.",
        "features_h": "Característiques",
        "features": [
            "Barrido tinySA en viu: línies de freqüència, pics detectats i icones per ancorar el que sents a cada receptor.",
            "L’espectre no bloqueja la gestió del rack a la xarxa.",
            "Construeix el rack: cerca a la xarxa o afegeix IP, bloqueja l’inventari i carrega la sessió.",
            "Mode show: receptors carregats, telemetria en viu, espectre en viu i ancoratge de pics arrossegant.",
            "Escala MHz, zoom i pan alineats al mateix eix de freqüència.",
            "D’un cop d’ull: estat TX (verd / vermell), pics sense ancorar (taronja) i tots els canals.",
            "Vista remota al navegador (mòbil, tablet o un altre ordinador) amb xat cap a l’app del Mac.",
            "Desa la sessió per al proper bolo. Mode simulador sense equip.",
        ],
        "soon_h": "Properament",
        "soon_p": "<strong>Aviat al Mac App Store.</strong> macOS 15 Sequoia o posterior; per a espectre hardware, un tinySA Ultra amb cable USB de dades.",
        "disclaimer_note": "Compatible amb sistemes sense fil d’escenari habituals (Shure, Sennheiser i similars). No és un producte oficial d’aquests fabricants.",
        "icon_alt": "Icona de Stage RF",
        "footer_links": '<p><a href="compare.html">Veure comparativa</a> · <a href="use-cases.html">Veure casos d’ús</a> · <a href="support.html">Suport</a></p>',
        "nav_home": "Inici",
        "nav_compare": "Comparativa",
        "nav_resources": "Recursos",
        "nav_faq": "FAQ",
        "nav_support": "Suport",
        "lang_label": "Català",
        "lang_emoji": None,
        "lang_flag": "../assets/flags/ca.svg",
        "aria_lang": "Selector d’idioma",
        "aria_nav": "Principal",
        "privacy": "Privacitat",
        "support": "Suport",
        "disclaimer": "QLab és una marca de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, recolzats ni patrocinats per Figure 53.",
        "made": "Programari independent · Santiago de Compostela",
        "blurb": "Espectre UHF i rack sense fil a la mateixa vista.",
        "detail": "Barrido tinySA en viu i gestió de receptors de xarxa sense canviar d’app. Vista remota al navegador. Properament al Mac App Store.",
        "compare_best": "Espectre UHF en viu i control unificat del rack sense fil",
        "compare_proto": "USB tinySA · xarxa OSC/IP",
        "compare_plat": "macOS 15+ · properament",
    },
    "eu": {
        "meta": "UHF espektroa zuzenean (tinySA) eta hari gabeko mic rack-a ikuspegi berean. macOS 15+.",
        "title": "Stage RF (macOS) — Stage Apps",
        "h1": "Stage RF (macOS)",
        "lead": "Stage RF-k UHF espektroa eta hari gabeko mic rack osoa app eta ikuspegi berean erakusten ditu. Konektatu tinySA USB bidez eta kudeatu sareko hargailuak scan-a martxan dagoen bitartean.",
        "features_h": "Ezaugarriak",
        "features": [
            "tinySA scan zuzenean: maiztasun-lerroak, detektatutako peak-ak eta ikonoak hargailu bakoitzean ainguratzeko.",
            "Espektroak ez du blokeatzen sareko rack kudeaketa.",
            "Eraiki rack-a: bilatu sarean edo gehitu IP, blokeatu inbentarioa eta kargatu saioa.",
            "Show modua: kargatutako hargailuak, telemetria zuzenean, espektroa zuzenean eta peak ainguratzea arrastatuz.",
            "MHz eskala, zoom eta pan maiztasun-ardatz berean.",
            "Begirada batean: TX egoera (berdea / gorria), ainguratu gabeko peak-ak (laranja) eta kanal guztiak.",
            "Urruneko ikuspegia nabigatzailean (mugikor, tablet edo beste PC) Mac app-arekin txatarekin.",
            "Gorde saioa hurrengo bolorako. Simuladore modua ekiporik gabe.",
        ],
        "soon_h": "Laster",
        "soon_p": "<strong>Laster Mac App Store-n.</strong> macOS 15 Sequoia edo berriagoa; hardware espektroarako, tinySA Ultra USB datu-kablearekin.",
        "disclaimer_note": "Ohiko eszena hari gabeko sistemekin bateragarria (Shure, Sennheiser eta antzekoak). Ez da fabrikatzaile horien produktu ofiziala.",
        "icon_alt": "Stage RF ikonoa",
        "footer_links": '<p><a href="compare.html">Konparaketa</a> · <a href="use-cases.html">Erabilera kasuak</a> · <a href="support.html">Laguntza</a></p>',
        "nav_home": "Hasiera",
        "nav_compare": "Konparaketa",
        "nav_resources": "Baliabideak",
        "nav_faq": "FAQ",
        "nav_support": "Laguntza",
        "lang_label": "Euskara",
        "lang_emoji": None,
        "lang_flag": "../assets/flags/eu.svg",
        "aria_lang": "Hizkuntza hautatzailea",
        "aria_nav": "Nagusia",
        "privacy": "Pribatutasuna",
        "support": "Laguntza",
        "disclaimer": "QLab Figure 53-ren marka da. Gune hau eta app hauek produktu independenteak dira eta ez daude Figure 53rekin afiliatuta.",
        "made": "Software independentea · Santiago de Compostela",
        "blurb": "UHF espektroa eta hari gabeko rack-a ikuspegi berean.",
        "detail": "tinySA scan zuzenean eta sareko hargailuen kudeaketa app aldatu gabe. Nabigatzaileko urruneko ikuspegia. Laster Mac App Store-n.",
        "compare_best": "UHF espektroa zuzenean eta hari gabeko rack kontrol bateratua",
        "compare_proto": "USB tinySA · sare OSC/IP",
        "compare_plat": "macOS 15+ · laster",
    },
}

LANG_META = {
    "es": ("🇪🇸", "Español"),
    "en": ("🇬🇧", "English"),
    "fr": ("🇫🇷", "Français"),
    "de": ("🇩🇪", "Deutsch"),
    "eu": (None, "Euskara"),
    "gl": (None, "Galego"),
    "ca": (None, "Català"),
}


def lang_item(cur, target):
    emoji, label = LANG_META[target]
    href = HREF if target == cur else f"../{target}/{HREF}"
    current = ' aria-current="page"' if target == cur else ""
    if emoji:
        inner = (
            f'<span class="lang-emoji" aria-hidden="true">{emoji}</span>'
            f'<span class="lang-dropdown-item-label">{label}</span>'
        )
    else:
        flag = f"../assets/flags/{target}.svg"
        inner = (
            f'<img class="lang-dropdown-flag" src="{flag}" alt="" decoding="async">'
            f'<span class="lang-dropdown-item-label">{label}</span>'
        )
    return (
        f'<a class="lang-dropdown-item" href="{href}" hreflang="{target}"'
        f'{current} role="menuitem">{inner}</a>'
    )


def build_page(lang):
    c = COPY[lang]
    features = "".join(f"<li>{f}</li>" for f in c["features"])
    if c.get("lang_emoji"):
        summary = (
            f'<span class="lang-emoji" aria-hidden="true">{c["lang_emoji"]}</span> '
            f'<span class="lang-dropdown-label">{c["lang_label"]}</span>'
        )
    else:
        summary = (
            f'<img class="lang-dropdown-flag" src="{c["lang_flag"]}" alt="" decoding="async"> '
            f'<span class="lang-dropdown-label">{c["lang_label"]}</span>'
        )
    hreflangs = "\n".join(
        f'  <link rel="alternate" hreflang="{L}" href="../{L}/{HREF}">' for L in LANGS
    )
    items = " ".join(lang_item(lang, L) for L in LANGS)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{htmlmod.escape(c['meta'])}">
  <title>{htmlmod.escape(c['title'])}</title>
{hreflangs}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
  <link rel="icon" href="/favicon.ico?v=3" sizes="any">
  <link rel="icon" href="/assets/images/stageapps-favicon-32.png?v=3" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/images/stageapps-favicon-180.png?v=3">
  <link rel="stylesheet" href="../css/styles.css?v=35">
</head>
<body>
  <div class="page">
    <header class="site-header">
      <div class="wrap inner">
        <a class="logo" href="index.html"><img class="logo-mark" src="/assets/images/stageapps-mark.png?v=3" alt="" width="36" height="36" decoding="async"><span class="logo-text">StageApps</span></a>
        <div class="header-right">
          <nav class="nav" aria-label="{c['aria_nav']}">
            <a href="index.html">{c['nav_home']}</a>
            <a href="accesible.html">Accesible</a>
            <a href="shutter-pj-osc.html">Shutter PJ-OSC</a>
            <a href="shutter-pjlink-ios.html">Shutter PJLINK</a>
            <a href="miditoosc.html">MIDItoOSC</a>
            <a href="easy-routing-m32-x32.html">Easy Routing</a>
            <a href="m32-patch.html">M32 Patch</a>
            <a href="stage-with-me.html">Stage With Me</a>
            <a href="transparent-screen.html">Transparent Screen</a>
            <a href="stage-recorder.html">Stage Recorder</a>
            <a href="stage-edit.html">Stage Edit</a>
            <a href="stage-rf.html">Stage RF</a>
            <a href="compare.html">{c['nav_compare']}</a>
            <a href="resources.html">{c['nav_resources']}</a>
            <a href="faq.html">{c['nav_faq']}</a>
            <a href="support.html">{c['nav_support']}</a>
          </nav>
          <div class="lang-dropdown" role="navigation" aria-label="{c['aria_lang']}">
  <details>
    <summary>
      {summary}
    </summary>
    <div class="lang-dropdown-menu" role="menu">
      {items}
    </div>
  </details>
</div>
        </div>
      </div>
    </header>

    <main>
      <section class="page-hero wrap">
        <h1>{htmlmod.escape(c['h1'])}</h1>
        <p class="meta">{htmlmod.escape(c['meta'])}</p>
            </section>
      <section>
        <div class="wrap">
          <div class="app-icon-hero" aria-label="{htmlmod.escape(c['icon_alt'])}">
            <img src="{IMAGE}" alt="{htmlmod.escape(c['icon_alt'])}" width="320" height="320" loading="eager" decoding="async">
          </div>
        </div>
      </section>
      <section>
        <div class="wrap prose">
          <p>{htmlmod.escape(c['lead'])}</p>
          <h2>{c['features_h']}</h2>
          <ul>
            {features}
          </ul>
          <p>{htmlmod.escape(c['disclaimer_note'])}</p>

          <div class="beta-callout">
            <h3>{c['soon_h']}</h3>
            <p>{c['soon_p']}</p>
          </div>
{c['footer_links']}
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="wrap inner">
        <span>© <span id="y"></span> Stage Apps</span>
        <div class="links">
          <a href="support.html">{c['support']}</a>
          <a href="privacy.html">{c['privacy']}</a>
                    <a class="footer-social" href="https://instagram.com/stage.apps" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><img class="footer-social-icon" src="/assets/icons/instagram.svg" alt="" width="18" height="18" decoding="async"><span>Instagram</span></a>
          <a class="footer-social" href="https://www.tiktok.com/@stageapps" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><img class="footer-social-icon" src="/assets/icons/tiktok.svg" alt="" width="18" height="18" decoding="async"><span>TikTok</span></a>
          <a class="footer-social" href="https://www.youtube.com/@StageApps" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><img class="footer-social-icon" src="/assets/icons/youtube.svg" alt="" width="18" height="18" decoding="async"><span>YouTube</span></a>
        </div>
      </div>
      <p class="wrap footer-disclaimer">{c['disclaimer']}</p>
      <p class="wrap footer-made-in">{c['made']}</p>
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
"""


def main():
    for lang in LANGS:
        path = ROOT / f"docs/{lang}/{HREF}"
        path.write_text(build_page(lang), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))

    planet_btn = (
        f'<button type="button" class="app-orbit-planet" data-orbit-planet '
        f'aria-label="Stage RF"><img src="{IMAGE}" alt=""></button>'
    )

    for lang in LANGS:
        path = ROOT / f"docs/{lang}/index.html"
        text = path.read_text(encoding="utf-8")
        m = re.search(r'data-apps="([^"]+)"', text)
        apps = json.loads(htmlmod.unescape(m.group(1)))
        if not any(a.get("name") == "Stage RF" for a in apps):
            apps.append(
                {
                    "name": "Stage RF",
                    "blurb": COPY[lang]["blurb"],
                    "detail": COPY[lang]["detail"],
                    "soon": True,
                    "image": IMAGE,
                    "href": HREF,
                }
            )
        else:
            for app in apps:
                if app.get("name") == "Stage RF":
                    app.update(
                        {
                            "blurb": COPY[lang]["blurb"],
                            "detail": COPY[lang]["detail"],
                            "soon": True,
                            "image": IMAGE,
                            "href": HREF,
                        }
                    )
        encoded = htmlmod.escape(json.dumps(apps, ensure_ascii=False), quote=True)
        text = text[: m.start(1)] + encoded + text[m.end(1) :]

        if 'aria-label="Stage RF"' not in text:
            marker = 'aria-label="Stage Edit"'
            i = text.find(marker)
            if i < 0:
                raise SystemExit(f"no Stage Edit planet {lang}")
            btn_end = text.find("</button>", i) + len("</button>")
            text = text[:btn_end] + "\n              " + planet_btn + text[btn_end:]

        text = text.replace(">1 / 10</p>", ">1 / 11</p>")
        text = text.replace("home-carousel.css?v=47", "home-carousel.css?v=48")
        text = text.replace("app-carousel.js?v=22", "app-carousel.js?v=23")
        text = text.replace("styles.css?v=34", "styles.css?v=35")
        path.write_text(text, encoding="utf-8")
        print("index", lang, "apps", len(apps))

        cpath = ROOT / f"docs/{lang}/compare.html"
        if cpath.exists():
            ctext = cpath.read_text(encoding="utf-8")
            if "<td>Stage RF</td>" not in ctext:
                row = (
                    f'<tr><td>Stage RF</td><td>{COPY[lang]["compare_best"]}</td>'
                    f'<td>{COPY[lang]["compare_proto"]}</td>'
                    f'<td>{COPY[lang]["compare_plat"]}</td></tr>'
                )
                ctext = ctext.replace("</tbody>", f"                {row}\n              </tbody>", 1)
                cpath.write_text(ctext, encoding="utf-8")
                print("compare", lang)

    nav_pat = re.compile(
        r'(<a href="stage-edit\.html">Stage Edit</a>)'
        r'(?!\s*\n?\s*<a href="stage-rf\.html">)'
    )
    nav_count = 0
    for path in (ROOT / "docs").rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if 'href="stage-edit.html">Stage Edit</a>' not in text:
            continue
        if 'href="stage-rf.html">Stage RF</a>' in text:
            continue
        new, n = nav_pat.subn(
            r'\1\n            <a href="stage-rf.html">Stage RF</a>',
            text,
        )
        if n:
            path.write_text(new, encoding="utf-8")
            nav_count += n
    print("nav inserts", nav_count)

    js_path = ROOT / "docs/js/app-carousel.js"
    js = js_path.read_text(encoding="utf-8")
    if 'app.name === "Stage RF"' not in js:
        old = '''      } else if (app.name === "Stage Edit") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Edit"));
      } else {
        label.textContent = app.name;
      }'''
        new = '''      } else if (app.name === "Stage Edit") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Edit"));
      } else if (app.name === "Stage RF") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("RF"));
      } else {
        label.textContent = app.name;
      }'''
        if old not in js:
            raise SystemExit("js stacked pattern missing")
        js_path.write_text(js.replace(old, new), encoding="utf-8")
        print("js stacked ok")

    print("DONE")


if __name__ == "__main__":
    main()
