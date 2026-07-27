#!/usr/bin/env python3
"""Generate easy-routing-m32-x32.html for all locales."""
from pathlib import Path
import re

LANGS = ["es", "en", "fr", "de", "ca", "gl", "eu"]
FILE = "easy-routing-m32-x32.html"
APP_STORE = "https://apple.co/4eXQev2"
BADGE_WHITE = "../assets/images/download-on-the-app-store-en-us-white.svg"

LABELS = {
    "es": "Español", "en": "English", "fr": "Français", "de": "Deutsch",
    "eu": "Euskara", "gl": "Galego", "ca": "Català",
}
EMOJIS = {"es": "🇪🇸", "en": "🇬🇧", "fr": "🇫🇷", "de": "🇩🇪"}
FLAGS = {"eu": "eu", "gl": "gl", "ca": "ca"}

NAV = {
    "es": ("Principal", "Inicio", "Comparativa", "Recursos", "Soporte", "Selector de idioma"),
    "en": ("Main", "Home", "Compare", "Resources", "Support", "Language selector"),
    "fr": ("Principal", "Accueil", "Comparatif", "Ressources", "Support", "Sélecteur de langue"),
    "de": ("Haupt", "Start", "Vergleich", "Ressourcen", "Support", "Sprachauswahl"),
    "ca": ("Principal", "Inici", "Comparativa", "Recursos", "Suport", "Selector d'idioma"),
    "gl": ("Principal", "Inicio", "Comparativa", "Recursos", "Soporte", "Selector de idioma"),
    "eu": ("Nagusia", "Hasiera", "Konparaketa", "Baliabideak", "Laguntza", "Hizkuntza-hautatzailea"),
}

FOOTER = {
    "es": ("Soporte", "Privacidad", "QLab es una marca de Figure 53. Este sitio y estas apps son productos independientes y no están afiliados, respaldados ni patrocinados por Figure 53.", "Software independiente · Santiago de Compostela"),
    "en": ("Support", "Privacy", "QLab is a trademark of Figure 53. This site and these apps are independent and are not affiliated with, endorsed by, or sponsored by Figure 53.", "Independent software · Santiago de Compostela, Spain"),
    "fr": ("Support", "Confidentialité", "QLab est une marque de Figure 53. Ce site et ces apps sont des produits indépendants et ne sont pas affiliés, approuvés ou sponsorisés par Figure 53.", "Logiciel indépendant · Santiago de Compostela"),
    "de": ("Support", "Datenschutz", "QLab ist eine Marke von Figure 53. Diese Website und diese Apps sind unabhängig und nicht mit Figure 53 verbunden, von ihr unterstützt oder gesponsert.", "Unabhängige Software · Santiago de Compostela"),
    "ca": ("Suport", "Privacitat", "QLab és una marca comercial de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, avalats ni patrocinats per Figure 53.", "Programari independent · Santiago de Compostela"),
    "gl": ("Soporte", "Privacidade", "QLab é unha marca de Figure 53. Este sitio e estas apps son independentes e non están afiliados, respaldados nin patrocinados por Figure 53.", "Software independente · Santiago de Compostela"),
    "eu": ("Laguntza", "Pribatutasuna", "QLab Figure 53-ren marka da. Gune hau eta app hauek independenteak dira eta ez daude Figure 53-rekin afiliatuta, onartuta edo babestuta.", "Software independente · Santiago de Compostela"),
}

COMPARE_ROW = {
    "en": ("M32 / X32 Easy Routing", "Visual M32/X32 input and output routing", "OSC", "macOS"),
    "es": ("M32 / X32 Easy Routing", "Routing visual de entradas y salidas M32/X32", "OSC", "macOS"),
    "fr": ("M32 / X32 Easy Routing", "Routage visuel entrées/sorties M32/X32", "OSC", "macOS"),
    "de": ("M32 / X32 Easy Routing", "Visuelles M32/X32 Ein-/Ausgangs-Routing", "OSC", "macOS"),
    "ca": ("M32 / X32 Easy Routing", "Routing visual d'entrades i sortides M32/X32", "OSC", "macOS"),
    "gl": ("M32 / X32 Easy Routing", "Routing visual de entradas e saídas M32/X32", "OSC", "macOS"),
    "eu": ("M32 / X32 Easy Routing", "M32/X32 sarrera eta irteera routing bisuala", "OSC", "macOS"),
}

T = {
    "en": {
        "desc": "Easy visual matrix routing for Midas M32 and Behringer X32: map inputs and outputs in seconds with a fast grid workflow.",
        "hero": "Fast visual matrix routing for Midas M32 and Behringer X32 consoles.",
        "banner_aria": "M32 / X32 Easy Routing on the Mac App Store",
        "banner_alt": "M32 / X32 Easy Routing — available on the Mac App Store",
        "lead": "Available now on the Mac App Store (macOS).",
        "h_what": "What it does",
        "intro": "M32 / X32 Easy Routing gives you a fast, visual way to manage console routing with a grid-based workflow. Route inputs and outputs in seconds using a clear matrix: tap a cell to assign a source, tap again to set it to OFF, and see your signal layout at a glance. Manage Local, AES50, AUX, and USB Card paths from one streamlined workspace.",
        "h_promo": "App Store promo (short)",
        "promo": "Visual matrix routing for M32/X32: map inputs and outputs in seconds, tap to assign or set OFF, and manage Local, AES50, AUX, and USB paths.",
        "h_features": "Key features",
        "features": [
            "Visual matrix routing for Inputs and Outputs.",
            "Quick tap-to-assign / tap-again-to-OFF workflow.",
            "Routing across Local, AES50, AUX, and USB/Card paths.",
            "Dedicated Card tab for USB/DAW routing.",
            "Built-in desk sync to read current routing and refresh anytime.",
            "Network discovery and direct OSC connection support.",
            "Multilingual interface.",
        ],
        "closing": "Whether you are preparing a show, adjusting stage boxes, or updating DAW sends, M32 / X32 Easy Routing keeps routing clear, fast, and reliable.",
        "store_h3": "App Store",
        "store_p": "Available now on the Mac App Store (macOS).",
        "store_btn": "Download on the App Store",
        "badge_aria": "Download Easy Routing on the App Store",
        "h_demo": "Demo video",
        "demo_p": "See how routing edits in the app are reflected in M32-Edit on the same network.",
        "links": '<a href="compare.html">See comparison</a> · <a href="use-cases.html">View use cases</a> · <a href="support.html">Support</a>',
        "card": "Visual matrix routing for Midas M32 and Behringer X32. Map inputs and outputs in seconds with a tap-to-assign workflow.",
        "card_hint": "<strong>Available on the App Store</strong> for Mac.",
        "card_aria": "Open M32 / X32 Easy Routing on the Mac App Store",
        "card_store_title": "Mac App Store",
        "card_store_sub": "Download Easy Routing",
        "card_more": "Learn more",
    },
    "es": {
        "desc": "Routing visual en parrilla para Midas M32 y Behringer X32: mapea entradas y salidas en segundos.",
        "hero": "Routing visual en modo parrilla para mesas Midas M32 y Behringer X32.",
        "banner_aria": "M32 / X32 Easy Routing en la Mac App Store",
        "banner_alt": "M32 / X32 Easy Routing — disponible en la Mac App Store",
        "lead": "Ya disponible en la Mac App Store (macOS).",
        "h_what": "Qué hace",
        "intro": "M32 / X32 Easy Routing te ofrece una forma rápida y visual de gestionar el routing de la consola con un flujo en modo parrilla. Enruta entradas y salidas en segundos con una matriz clara: toca una celda para asignar una fuente, vuelve a tocar para poner OFF y visualiza el flujo de señal de un vistazo. Gestiona rutas Local, AES50, AUX y USB Card desde un único espacio de trabajo.",
        "h_promo": "Texto promocional corto",
        "promo": "Routing visual en matriz para M32/X32: mapea entradas y salidas en segundos, toca para asignar o poner OFF, y gestiona rutas Local, AES50, AUX y USB.",
        "h_features": "Características clave",
        "features": [
            "Routing visual en parrilla para entradas y salidas.",
            "Flujo rápido: tocar para asignar / tocar otra vez para OFF.",
            "Routing en rutas Local, AES50, AUX y USB/Card.",
            "Pestaña Card dedicada para routing USB/DAW.",
            "Sincronización con la mesa para leer el estado actual y refrescar cuando quieras.",
            "Descubrimiento por red y conexión OSC directa.",
            "Interfaz multilingüe.",
        ],
        "closing": "Tanto para preparar un show como para ajustar stageboxes o actualizar envíos hacia DAW, M32 / X32 Easy Routing mantiene el routing claro, rápido y fiable.",
        "store_h3": "App Store",
        "store_p": "Ya disponible en la Mac App Store (macOS).",
        "store_btn": "Descargar en la App Store",
        "badge_aria": "Descargar Easy Routing en la App Store",
        "h_demo": "Vídeo demo",
        "demo_p": "Mira cómo los cambios de routing en la app se reflejan en M32-Edit en la misma red.",
        "links": '<a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a>',
        "card": "Routing visual en modo parrilla para Midas M32 y Behringer X32. Mapea entradas y salidas en segundos con toques rápidos.",
        "card_hint": "<strong>Ya en la App Store</strong> para Mac.",
        "card_aria": "Abrir M32 / X32 Easy Routing en la Mac App Store",
        "card_store_title": "Mac App Store",
        "card_store_sub": "Descargar Easy Routing",
        "card_more": "Ver más",
    },
    "fr": {
        "desc": "Routage visuel en matrice pour Midas M32 et Behringer X32 : affectez entrées et sorties en quelques secondes.",
        "hero": "Routage visuel en grille pour consoles Midas M32 et Behringer X32.",
        "banner_aria": "M32 / X32 Easy Routing sur le Mac App Store",
        "banner_alt": "M32 / X32 Easy Routing — disponible sur le Mac App Store",
        "lead": "Déjà disponible sur le Mac App Store (macOS).",
        "h_what": "Ce qu'elle fait",
        "intro": "M32 / X32 Easy Routing offre une gestion rapide et visuelle du routage console grâce à une grille intuitive. Affectez entrées et sorties en quelques secondes : touchez une cellule pour assigner une source, retouchez pour passer en OFF, et visualisez votre signal d'un coup d'œil. Gérez les chemins Local, AES50, AUX et USB Card depuis un espace de travail unifié.",
        "h_promo": "Texte promotionnel court",
        "promo": "Routage matriciel visuel pour M32/X32 : affectez entrées et sorties en secondes, touchez pour assigner ou mettre OFF, et gérez Local, AES50, AUX et USB.",
        "h_features": "Fonctionnalités clés",
        "features": [
            "Routage matriciel visuel pour entrées et sorties.",
            "Flux rapide : toucher pour assigner / retoucher pour OFF.",
            "Routage sur Local, AES50, AUX et USB/Card.",
            "Onglet Card dédié au routage USB/DAW.",
            "Synchronisation avec la console pour lire l'état actuel et actualiser à tout moment.",
            "Découverte réseau et connexion OSC directe.",
            "Interface multilingue.",
        ],
        "closing": "Pour préparer un spectacle, ajuster des stageboxes ou mettre à jour des envois DAW, M32 / X32 Easy Routing garde le routage clair, rapide et fiable.",
        "store_h3": "App Store",
        "store_p": "Déjà disponible sur le Mac App Store (macOS).",
        "store_btn": "Télécharger sur l'App Store",
        "badge_aria": "Télécharger Easy Routing sur l'App Store",
        "h_demo": "Vidéo de démonstration",
        "demo_p": "Voyez comment les modifications de routage dans l'app se reflètent dans M32-Edit sur le même réseau.",
        "links": '<a href="compare.html">Voir le comparatif</a> · <a href="use-cases.html">Voir les cas d\'usage</a> · <a href="support.html">Assistance</a>',
        "card": "Routage visuel en matrice pour Midas M32 et Behringer X32. Affectez entrées et sorties en quelques secondes.",
        "card_hint": "<strong>Déjà sur l'App Store</strong> pour Mac.",
        "card_aria": "Ouvrir M32 / X32 Easy Routing sur le Mac App Store",
        "card_store_title": "Mac App Store",
        "card_store_sub": "Télécharger Easy Routing",
        "card_more": "En savoir plus",
    },
    "de": {
        "desc": "Visuelles Matrix-Routing für Midas M32 und Behringer X32: Eingänge und Ausgänge in Sekunden zuweisen.",
        "hero": "Schnelles visuelles Matrix-Routing für Midas M32 und Behringer X32.",
        "banner_aria": "M32 / X32 Easy Routing im Mac App Store",
        "banner_alt": "M32 / X32 Easy Routing — jetzt im Mac App Store",
        "lead": "Jetzt im Mac App Store (macOS) verfügbar.",
        "h_what": "Was die App macht",
        "intro": "M32 / X32 Easy Routing bietet eine schnelle, visuelle Steuerung des Konsolen-Routings mit einem Raster-Workflow. Weisen Sie Eingänge und Ausgänge in Sekunden zu: Zelle antippen zum Zuweisen, erneut antippen für OFF, und das Signalbild auf einen Blick sehen. Verwalten Sie Local-, AES50-, AUX- und USB-Card-Pfade in einer übersichtlichen Oberfläche.",
        "h_promo": "Kurzer App-Store-Text",
        "promo": "Visuelles Matrix-Routing für M32/X32: Eingänge und Ausgänge in Sekunden zuweisen, antippen zum Zuweisen oder OFF, und Local, AES50, AUX sowie USB verwalten.",
        "h_features": "Hauptfunktionen",
        "features": [
            "Visuelles Matrix-Routing für Eingänge und Ausgänge.",
            "Schneller Workflow: antippen zum Zuweisen / erneut antippen für OFF.",
            "Routing über Local, AES50, AUX und USB/Card.",
            "Eigener Card-Tab für USB/DAW-Routing.",
            "Eingebaute Pult-Synchronisation zum Lesen und Aktualisieren des aktuellen Routings.",
            "Netzwerkerkennung und direkte OSC-Verbindung.",
            "Mehrsprachige Oberfläche.",
        ],
        "closing": "Ob Show-Vorbereitung, Stagebox-Anpassung oder DAW-Sends: M32 / X32 Easy Routing hält Routing klar, schnell und zuverlässig.",
        "store_h3": "App Store",
        "store_p": "Jetzt im Mac App Store (macOS) verfügbar.",
        "store_btn": "Im App Store laden",
        "badge_aria": "Easy Routing im App Store laden",
        "h_demo": "Demo-Video",
        "demo_p": "Sehen Sie, wie Routing-Änderungen in der App in M32-Edit im selben Netzwerk übernommen werden.",
        "links": '<a href="compare.html">Vergleich ansehen</a> · <a href="use-cases.html">Anwendungsfälle</a> · <a href="support.html">Support</a>',
        "card": "Visuelles Matrix-Routing für Midas M32 und Behringer X32. Eingänge und Ausgänge in Sekunden per Antippen zuweisen.",
        "card_hint": "<strong>Jetzt im App Store</strong> für Mac.",
        "card_aria": "M32 / X32 Easy Routing im Mac App Store öffnen",
        "card_store_title": "Mac App Store",
        "card_store_sub": "Easy Routing laden",
        "card_more": "Mehr erfahren",
    },
    "ca": {
        "desc": "Routing visual en graella per Midas M32 i Behringer X32: assigna entrades i sortides en segons.",
        "hero": "Routing visual en mode graella per a consoles Midas M32 i Behringer X32.",
        "banner_aria": "M32 / X32 Easy Routing a la Mac App Store",
        "banner_alt": "M32 / X32 Easy Routing — disponible a la Mac App Store",
        "lead": "Ja disponible a la Mac App Store (macOS).",
        "h_what": "Què fa",
        "intro": "M32 / X32 Easy Routing ofereix una manera ràpida i visual de gestionar el routing de consola amb un flux en graella. Encamina entrades i sortides en segons amb una matriu clara: toca una cel·la per assignar una font, torna a tocar per posar OFF i visualitza el flux de senyal d'un cop d'ull. Gestiona rutes Local, AES50, AUX i USB Card des d'un únic espai de treball.",
        "h_promo": "Text promocional curt",
        "promo": "Routing visual en matriu per a M32/X32: assigna entrades i sortides en segons, toca per assignar o posar OFF, i gestiona Local, AES50, AUX i USB.",
        "h_features": "Característiques clau",
        "features": [
            "Routing visual en graella per a entrades i sortides.",
            "Flux ràpid: tocar per assignar / tornar a tocar per OFF.",
            "Routing en rutes Local, AES50, AUX i USB/Card.",
            "Pestanya Card dedicada per a routing USB/DAW.",
            "Sincronització amb la consola per llegir l'estat actual i actualitzar quan vulguis.",
            "Descobriment per xarxa i connexió OSC directa.",
            "Interfície multilingüe.",
        ],
        "closing": "Tant per preparar un espectacle com per ajustar stageboxes o actualitzar enviaments cap a DAW, M32 / X32 Easy Routing manté el routing clar, ràpid i fiable.",
        "store_h3": "App Store",
        "store_p": "Ja disponible a la Mac App Store (macOS).",
        "store_btn": "Descarregar a l'App Store",
        "badge_aria": "Descarregar Easy Routing a l'App Store",
        "h_demo": "Vídeo demo",
        "demo_p": "Mira com els canvis de routing a l'app es reflecteixen a M32-Edit a la mateixa xarxa.",
        "links": '<a href="compare.html">Veure comparativa</a> · <a href="use-cases.html">Veure casos d\'ús</a> · <a href="support.html">Suport</a>',
        "card": "Routing visual en mode graella per a Midas M32 i Behringer X32. Assigna entrades i sortides en segons amb tocs ràpids.",
        "card_hint": "<strong>Ja a l'App Store</strong> per a Mac.",
        "card_aria": "Obrir M32 / X32 Easy Routing a la Mac App Store",
        "card_store_title": "Mac App Store",
        "card_store_sub": "Descarregar Easy Routing",
        "card_more": "Veure més",
    },
    "gl": {
        "desc": "Routing visual en grella para Midas M32 e Behringer X32: asigna entradas e saídas en segundos.",
        "hero": "Routing visual en modo grella para mesas Midas M32 e Behringer X32.",
        "banner_aria": "M32 / X32 Easy Routing na Mac App Store",
        "banner_alt": "M32 / X32 Easy Routing — dispoñible na Mac App Store",
        "lead": "Xa dispoñible na Mac App Store (macOS).",
        "h_what": "Que fai",
        "intro": "M32 / X32 Easy Routing ofrece unha forma rápida e visual de xestionar o routing da consola cun fluxo en grella. Encamiña entradas e saídas en segundos cunha matriz clara: toca unha cela para asignar unha fonte, volve tocar para poñer OFF e visualiza o fluxo de sinal dunha ollada. Xestiona rutas Local, AES50, AUX e USB Card desde un único espazo de traballo.",
        "h_promo": "Texto promocional curto",
        "promo": "Routing visual en matriz para M32/X32: asigna entradas e saídas en segundos, toca para asignar ou poñer OFF, e xestiona Local, AES50, AUX e USB.",
        "h_features": "Características clave",
        "features": [
            "Routing visual en grella para entradas e saídas.",
            "Fluxo rápido: tocar para asignar / tocar outra vez para OFF.",
            "Routing en rutas Local, AES50, AUX e USB/Card.",
            "Pestana Card dedicada para routing USB/DAW.",
            "Sincronización coa mesa para ler o estado actual e refrescar cando queiras.",
            "Descubrimento por rede e conexión OSC directa.",
            "Interface multilingüe.",
        ],
        "closing": "Tanto para preparar un show como para axustar stageboxes ou actualizar envíos cara DAW, M32 / X32 Easy Routing mantén o routing claro, rápido e fiable.",
        "store_h3": "App Store",
        "store_p": "Xa dispoñible na Mac App Store (macOS).",
        "store_btn": "Descargar na App Store",
        "badge_aria": "Descargar Easy Routing na App Store",
        "h_demo": "Vídeo demo",
        "demo_p": "Mira como os cambios de routing na app se reflicten en M32-Edit na mesma rede.",
        "links": '<a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Axuda</a>',
        "card": "Routing visual en modo grella para Midas M32 e Behringer X32. Asigna entradas e saídas en segundos con toques rápidos.",
        "card_hint": "<strong>Xa na App Store</strong> para Mac.",
        "card_aria": "Abrir M32 / X32 Easy Routing na Mac App Store",
        "card_store_title": "Mac App Store",
        "card_store_sub": "Descargar Easy Routing",
        "card_more": "Ver máis",
    },
    "eu": {
        "desc": "Midas M32 eta Behringer X32-rako matrize bidezko routing bisuala: sarrerak eta irteerak segundo gutxitan esleitu.",
        "hero": "M32/X32-rako matrize bidezko routing bisual azkarra.",
        "banner_aria": "M32 / X32 Easy Routing Mac App Store-n",
        "banner_alt": "M32 / X32 Easy Routing — Mac App Store-n eskuragarri",
        "lead": "Mac App Store-n eskuragarri (macOS).",
        "h_what": "Zer egiten duen",
        "intro": "M32 / X32 Easy Routing-ek kontsolaren routinga modu azkar eta bisualean kudeatzeko aukera ematen du, sareta bidezko lan-fluxuarekin. Sarrerak eta irteerak segundo gutxitan esleitu: gelaxka sakatu iturria esleitzeko, berriro sakatu OFF jartzeko, eta seinalearen antolaketa begiratu batean ikusi. Kudeatu Local, AES50, AUX eta USB Card ibilbideak lan-eremu bakar batetik.",
        "h_promo": "Testu promozional laburra",
        "promo": "M32/X32-rako routing bisual matrizean: sarrerak eta irteerak segundo gutxitan esleitu, sakatu esleitzeko edo OFF jartzeko, eta kudeatu Local, AES50, AUX eta USB ibilbideak.",
        "h_features": "Ezaugarri nagusiak",
        "features": [
            "Routing bisual matrizean sarrerak eta irteerak kudeatzeko.",
            "Fluxu azkarra: sakatu esleitzeko / berriro sakatu OFF jartzeko.",
            "Routing Local, AES50, AUX eta USB/Card ibilbideetan.",
            "Card fitxa dedikatua USB/DAW routing-erako.",
            "Mesa-rekin sinkronizazioa uneko routinga irakurtzeko eta edozein unetan freskatzeko.",
            "Sareko aurkikuntza eta OSC konexio zuzena.",
            "Interfaze eleanitza.",
        ],
        "closing": "Ikuskizuna prestatzeko, stagebox-ak doitzeko edo DAW bidalketak eguneratzeko, M32 / X32 Easy Routing-ek routinga argi, azkar eta fidagarri mantentzen du.",
        "store_h3": "App Store",
        "store_p": "Mac App Store-n eskuragarri (macOS).",
        "store_btn": "Deskargatu App Store-n",
        "badge_aria": "Deskargatu Easy Routing App Store-n",
        "h_demo": "Demo bideoa",
        "demo_p": "Ikusi nola islatzen diren app-eko routing aldaketak M32-Edit-en sare berean.",
        "links": '<a href="compare.html">Konparaketa ikusi</a> · <a href="use-cases.html">Erabilera kasuak</a> · <a href="support.html">Laguntza</a>',
        "card": "Midas M32 eta Behringer X32-rako matrize bidezko routing bisuala. Sarrerak eta irteerak segundo gutxitan esleitu.",
        "card_hint": "<strong>App Store-n eskuragarri</strong> Mac-erako.",
        "card_aria": "Ireki M32 / X32 Easy Routing Mac App Store-n",
        "card_store_title": "Mac App Store",
        "card_store_sub": "Deskargatu Easy Routing",
        "card_more": "Gehiago ikusi",
    },
}


def lang_menu(current: str) -> str:
    parts = []
    for code in LANGS:
        cur = ' aria-current="page"' if code == current else ""
        if code in FLAGS:
            parts.append(
                f'<a class="lang-dropdown-item" href="../{code}/{FILE}" hreflang="{code}"{cur} role="menuitem">'
                f'<img class="lang-dropdown-flag" src="../assets/flags/{FLAGS[code]}.svg" alt="" decoding="async">'
                f'<span class="lang-dropdown-item-label">{LABELS[code]}</span></a>'
            )
        else:
            parts.append(
                f'<a class="lang-dropdown-item" href="../{code}/{FILE}" hreflang="{code}"{cur} role="menuitem">'
                f'<span class="lang-emoji" aria-hidden="true">{EMOJIS[code]}</span>'
                f'<span class="lang-dropdown-item-label">{LABELS[code]}</span></a>'
            )
    return " ".join(parts)


def summary_inner(code: str) -> str:
    if code in FLAGS:
        return (
            f'<img class="lang-dropdown-flag" src="../assets/flags/{FLAGS[code]}.svg" alt="" decoding="async"> '
            f'<span class="lang-dropdown-label">{LABELS[code]}</span>'
        )
    return (
        f'<span class="lang-emoji" aria-hidden="true">{EMOJIS[code]}</span> '
        f'<span class="lang-dropdown-label">{LABELS[code]}</span>'
    )


def store_badge_html(aria: str, inline: bool = False) -> str:
    img = (
        f'<img src="{BADGE_WHITE}" alt="Download on the App Store" width="120" height="40" '
        f'loading="lazy" decoding="async">'
    )
    link = (
        f'<a class="store-badge-link" href="{APP_STORE}" target="_blank" rel="noopener noreferrer" '
        f'aria-label="{aria}">{img}</a>'
    )
    return link if inline else f"<p>{link}</p>"


def render_page(code: str) -> str:
    t = T[code]
    nav_aria, nav_home, nav_compare, nav_resources, nav_support, lang_aria = NAV[code]
    foot_support, foot_privacy, foot_disclaimer, foot_made = FOOTER[code]
    hreflangs = "\n".join(f'  <link rel="alternate" hreflang="{c}" href="../{c}/{FILE}">' for c in LANGS)
    features = "\n".join(f"            <li>{f}</li>" for f in t["features"])

    return f"""<!DOCTYPE html>
<html lang="{code}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{t['desc']}">
  <title>M32 / X32 Easy Routing — Stage Apps</title>
{hreflangs}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
  <link rel="icon" href="/favicon.ico?v=3" sizes="any">
  <link rel="icon" href="/assets/images/stageapps-favicon-32.png?v=3" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/images/stageapps-favicon-180.png?v=3">
  <link rel="stylesheet" href="../css/styles.css?v=15">
</head>
<body>
  <div class="page">
    <header class="site-header">
      <div class="wrap inner">
        <a class="logo" href="index.html"><img class="logo-mark" src="/assets/images/stageapps-mark.png?v=3" alt="" width="36" height="36" decoding="async"><span class="logo-text">StageApps</span></a>
        <div class="header-right">
          <nav class="nav" aria-label="{nav_aria}">
            <a href="index.html">{nav_home}</a>
            <a href="accesible.html">Accesible</a>
            <a href="shutter-pj-osc.html">Shutter PJ-OSC</a>
            <a href="shutter-pjlink-ios.html">Shutter PJLINK</a>
            <a href="miditoosc.html">MIDItoOSC</a>
            <a href="easy-routing-m32-x32.html">Easy Routing</a>
            <a href="m32-patch.html">M32 Patch</a>
            <a href="stage-with-me.html">Stage With Me</a>
            <a href="compare.html">{nav_compare}</a>
            <a href="resources.html">{nav_resources}</a>
            <a href="faq.html">FAQ</a>
            <a href="support.html">{nav_support}</a>
          </nav>
          <div class="lang-dropdown" role="navigation" aria-label="{lang_aria}">
  <details>
    <summary>
      {summary_inner(code)}
    </summary>
    <div class="lang-dropdown-menu" role="menu">
      {lang_menu(code)}
    </div>
  </details>
</div>
        </div>
      </div>
    </header>

    <main>
      <section class="page-hero wrap">
        <h1>M32 / X32 Easy Routing</h1>
        <p class="meta">{t['hero']}</p>
      </section>
      <section>
        <div class="wrap">
          <div class="app-hero-banner" aria-label="{t['banner_aria']}">
            <a href="{APP_STORE}" target="_blank" rel="noopener noreferrer">
              <img src="../assets/images/m32-x32-easy-routing-banner-1200x720.png?v=1" alt="{t['banner_alt']}" width="1200" height="720" loading="eager" decoding="async">
            </a>
          </div>
        </div>
      </section>
      <section>
        <div class="wrap prose">
          <p><strong>{t['lead']}</strong></p>
          <h2>{t['h_what']}</h2>
          <p>{t['intro']}</p>
          <h2>{t['h_promo']}</h2>
          <p>{t['promo']}</p>
          <h2>{t['h_features']}</h2>
          <ul>
{features}
          </ul>
          <p>{t['closing']}</p>
          <div class="beta-callout">
            <h3>{t['store_h3']}</h3>
            <p><strong>{t['store_p']}</strong></p>
            {store_badge_html(t['badge_aria'])}
          </div>
          <h2>{t['h_demo']}</h2>
          <p>{t['demo_p']}</p>
          <video controls preload="metadata" playsinline poster="../assets/videos/easy-routing-demo-poster.jpg" style="width:100%;max-width:960px;height:auto;border-radius:12px;">
            <source src="../assets/videos/easy-routing-demo.mp4" type="video/mp4">
          </video>
          <p>{t['links']}</p>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="wrap inner">
        <span>© <span id="y"></span> Stage Apps</span>
        <div class="links">
          <a href="support.html">{foot_support}</a>
          <a href="privacy.html">{foot_privacy}</a>
          <a class="footer-social" href="https://instagram.com/stage.apps" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><img class="footer-social-icon" src="/assets/icons/instagram.svg" alt="" width="18" height="18" decoding="async"><span>Instagram</span></a>
          <a class="footer-social" href="https://www.tiktok.com/@stageapps" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><img class="footer-social-icon" src="/assets/icons/tiktok.svg" alt="" width="18" height="18" decoding="async"><span>TikTok</span></a>
        </div>
      </div>
      <p class="wrap footer-disclaimer">{foot_disclaimer}</p>
      <p class="wrap footer-made-in">{foot_made}</p>
    </footer>
  </div>
  <script>
    try {{ localStorage.setItem("accesible_lang", "{code}"); }} catch (e) {{}}
  </script>
  <script>
    document.getElementById("y").textContent = new Date().getFullYear();
  </script>
</body>
</html>"""


def update_index_card(code: str) -> None:
    p = Path(__file__).parent / code / "index.html"
    t = T[code]
    text = p.read_text(encoding="utf-8")
    block = f"""<div class="app-grid-item">
            <article class="card app-card">
            <div class="app-card-text">
              <h3>M32 / X32 Easy Routing</h3>
              <p>{t['card']}</p>
            </div>
            </article>
            <a class="app-card-thumb" href="easy-routing-m32-x32.html" aria-label="{t['card_aria']}">
              <img src="../assets/images/m32-x32-easy-routing-square-1080.png?v=1" alt="{t['banner_alt']}" loading="lazy" decoding="async">
            </a>
            <div class="app-card-actions">
              <p class="app-card-store-hint">{t['card_hint']}</p>
            </div>
            <div class="app-card-badge-row">
              {store_badge_html(t['badge_aria'], inline=True)}
            </div>
            <div class="app-card-cta-secondary">
              <a class="btn btn-secondary" href="easy-routing-m32-x32.html">{t['card_more']}</a>
            </div>
          </div>
"""
    text = re.sub(
        r'<div class="app-grid-item">\s*<article class="card app-card">\s*<div class="app-card-text">\s*<h3>M32 / X32 Easy Routing</h3>.*?(?=<div class="app-grid-item">\s*<article class="card app-card">\s*<div class="app-card-text">\s*<h3>Stage With Me)',
        block,
        text,
        count=1,
        flags=re.DOTALL,
    )
    p.write_text(text, encoding="utf-8")


def update_compare(code: str) -> None:
    p = Path(__file__).parent / code / "compare.html"
    text = p.read_text(encoding="utf-8")
    if "M32 / X32 Easy Routing" in text:
        return
    name, best, proto, platform = COMPARE_ROW[code]
    row = f'                <tr><td>{name}</td><td>{best}</td><td>{proto}</td><td>{platform}</td></tr>\n'
    text = text.replace(
        '                <tr><td>MIDItoOSC</td>',
        row + '                <tr><td>MIDItoOSC</td>',
        1,
    )
    p.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    root = Path(__file__).parent
    for code in LANGS:
        (root / code / FILE).write_text(render_page(code), encoding="utf-8")
        update_index_card(code)
        update_compare(code)
        print("wrote", code)
