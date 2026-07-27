#!/usr/bin/env python3
"""Generate m32-patch.html for all locales and update catalog/compare/nav."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent
LANGS = ["es", "en", "fr", "de", "ca", "gl", "eu"]
FILE = "m32-patch.html"
APP_STORE = "https://apple.co/44TAL9z"
BADGE_WHITE = "../assets/images/download-on-the-app-store-en-us-white.svg"
BANNER = "../assets/images/m32-patch-banner-1200x720.png?v=1"
SQUARE = "../assets/images/m32-patch-square-1080.png?v=1"
CSS = "../css/styles.css?v=17"

LABELS = {
    "es": "Español",
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
    "eu": "Euskara",
    "gl": "Galego",
    "ca": "Català",
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
    "es": (
        "Soporte",
        "Privacidad",
        "QLab es una marca de Figure 53. Este sitio y estas apps son productos independientes y no están afiliados, respaldados ni patrocinados por Figure 53.",
        "Software independiente · Santiago de Compostela",
    ),
    "en": (
        "Support",
        "Privacy",
        "QLab is a trademark of Figure 53. This site and these apps are independent and are not affiliated with, endorsed by, or sponsored by Figure 53.",
        "Independent software · Santiago de Compostela, Spain",
    ),
    "fr": (
        "Support",
        "Confidentialité",
        "QLab est une marque de Figure 53. Ce site et ces apps sont des produits indépendants et ne sont pas affiliés, approuvés ou sponsorisés par Figure 53.",
        "Logiciel indépendant · Santiago de Compostela",
    ),
    "de": (
        "Support",
        "Datenschutz",
        "QLab ist eine Marke von Figure 53. Diese Website und diese Apps sind unabhängig und nicht mit Figure 53 verbunden, von ihr unterstützt oder gesponsert.",
        "Unabhängige Software · Santiago de Compostela",
    ),
    "ca": (
        "Suport",
        "Privacitat",
        "QLab és una marca comercial de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, avalats ni patrocinats per Figure 53.",
        "Programari independent · Santiago de Compostela",
    ),
    "gl": (
        "Soporte",
        "Privacidade",
        "QLab é unha marca de Figure 53. Este sitio e estas apps son independentes e non están afiliados, respaldados nin patrocinados por Figure 53.",
        "Software independente · Santiago de Compostela",
    ),
    "eu": (
        "Laguntza",
        "Pribatutasuna",
        "QLab Figure 53-ren marka da. Gune hau eta app hauek independenteak dira eta ez daude Figure 53-rekin afiliatuta, onartuta edo babestuta.",
        "Software independente · Santiago de Compostela",
    ),
}

COMPARE_ROW = {
    "en": ("M32 Patch", "Visual M32/X32 routing on iPhone/iPad", "OSC", "iOS / iPadOS"),
    "es": ("M32 Patch", "Routing visual M32/X32 en iPhone/iPad", "OSC", "iOS / iPadOS"),
    "fr": ("M32 Patch", "Routage visuel M32/X32 sur iPhone/iPad", "OSC", "iOS / iPadOS"),
    "de": ("M32 Patch", "Visuelles M32/X32-Routing auf iPhone/iPad", "OSC", "iOS / iPadOS"),
    "ca": ("M32 Patch", "Routing visual M32/X32 a iPhone/iPad", "OSC", "iOS / iPadOS"),
    "gl": ("M32 Patch", "Routing visual M32/X32 en iPhone/iPad", "OSC", "iOS / iPadOS"),
    "eu": ("M32 Patch", "M32/X32 routing bisuala iPhone/iPad-en", "OSC", "iOS / iPadOS"),
}

T = {
    "en": {
        "desc": "M32 Patch is an independent iPhone and iPad app for visual matrix routing on Midas M32 and Behringer X32 — the same kind of workflow as Easy Routing on Mac.",
        "hero": "Independent iOS app for visual M32/X32 matrix routing on iPhone and iPad.",
        "banner_aria": "M32 Patch on the App Store",
        "banner_alt": "M32 Patch — available on the App Store for iPhone and iPad",
        "lead": "Available now on the App Store for iPhone and iPad.",
        "h_what": "What it does",
        "intro": "M32 Patch is a standalone app: it does not require <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> on the Mac. Both apps offer the same style of fast, grid-based routing for M32/X32 over OSC. Map inputs and outputs in seconds: tap a cell to assign a source, tap again for OFF, and manage Local, AES50, AUX, and USB Card paths on the same network as your console.",
        "h_promo": "App Store promo (short)",
        "promo": "Independent iOS app for visual M32/X32 matrix routing on iPhone and iPad — tap to assign or set OFF, Local / AES50 / AUX / USB.",
        "h_features": "Key features",
        "features": [
            "Visual matrix routing for Inputs and Outputs on iPhone and iPad.",
            "Quick tap-to-assign / tap-again-to-OFF workflow.",
            "Routing across Local, AES50, AUX, and USB/Card paths.",
            "Network discovery and direct OSC connection to the desk.",
            "Built for live shows, stage boxes, and fast patch changes on the floor.",
            "Independent from Easy Routing on Mac — same idea, separate apps for each platform.",
        ],
        "closing": "Choose <strong>M32 Patch</strong> for iPhone/iPad, or <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> for Mac — each works on its own.",
        "store_h3": "App Store",
        "store_p": "Available now on the App Store for iPhone and iPad.",
        "badge_aria": "Download M32 Patch on the App Store",
        "links": '<a href="easy-routing-m32-x32.html">Easy Routing (Mac)</a> · <a href="compare.html">See comparison</a> · <a href="support.html">Support</a>',
        "card": "Independent iOS app for visual matrix routing on Midas M32 and Behringer X32 — same idea as Easy Routing on Mac, separate apps.",
        "card_hint": "<strong>Available on the App Store</strong> for iPhone and iPad.",
        "card_aria": "Open M32 Patch on the App Store",
        "card_more": "Learn more",
        "title_h3": "M32 Patch (iOS)",
    },
    "es": {
        "desc": "M32 Patch es una app independiente para iPhone e iPad con routing visual en parrilla para Midas M32 y Behringer X32 — el mismo tipo de flujo que Easy Routing en Mac.",
        "hero": "App independiente para iOS: routing visual M32/X32 en iPhone e iPad.",
        "banner_aria": "M32 Patch en la App Store",
        "banner_alt": "M32 Patch — disponible en la App Store para iPhone e iPad",
        "lead": "Ya disponible en la App Store para iPhone e iPad.",
        "h_what": "Qué hace",
        "intro": "M32 Patch es una app <strong>independiente</strong>: no necesita <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> en el Mac. Ambas ofrecen el mismo estilo de routing rápido en parrilla para M32/X32 por OSC. Mapea entradas y salidas en segundos: toca una celda para asignar, otra vez para OFF, y gestiona rutas Local, AES50, AUX y USB Card en la misma red que tu consola.",
        "h_promo": "Texto promocional corto",
        "promo": "App independiente para iOS: routing visual M32/X32 en iPhone e iPad — toca para asignar u OFF, Local / AES50 / AUX / USB.",
        "h_features": "Características clave",
        "features": [
            "Routing visual en parrilla para entradas y salidas en iPhone e iPad.",
            "Flujo rápido: tocar para asignar / tocar otra vez para OFF.",
            "Routing en rutas Local, AES50, AUX y USB/Card.",
            "Descubrimiento por red y conexión OSC directa a la mesa.",
            "Pensada para shows en vivo, stageboxes y cambios de patch en el suelo.",
            "Independiente de Easy Routing en Mac: misma idea, apps separadas por plataforma.",
        ],
        "closing": "Elige <strong>M32 Patch</strong> para iPhone/iPad, o <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> para Mac — cada una funciona por su cuenta.",
        "store_h3": "App Store",
        "store_p": "Ya disponible en la App Store para iPhone e iPad.",
        "badge_aria": "Descargar M32 Patch en la App Store",
        "links": '<a href="easy-routing-m32-x32.html">Easy Routing (Mac)</a> · <a href="compare.html">Ver comparativa</a> · <a href="support.html">Soporte</a>',
        "card": "App independiente para iOS: routing visual en parrilla para Midas M32 y Behringer X32 — misma idea que Easy Routing en Mac, apps separadas.",
        "card_hint": "<strong>Ya en la App Store</strong> para iPhone e iPad.",
        "card_aria": "Abrir M32 Patch en la App Store",
        "card_more": "Ver más",
        "title_h3": "M32 Patch (iOS)",
    },
    "fr": {
        "desc": "M32 Patch est une app indépendante pour iPhone et iPad : routage matriciel visuel pour Midas M32 et Behringer X32 — le même type de flux qu'Easy Routing sur Mac.",
        "hero": "App iOS indépendante : routage visuel M32/X32 sur iPhone et iPad.",
        "banner_aria": "M32 Patch sur l'App Store",
        "banner_alt": "M32 Patch — disponible sur l'App Store pour iPhone et iPad",
        "lead": "Disponible dès maintenant sur l'App Store pour iPhone et iPad.",
        "h_what": "Ce qu'elle fait",
        "intro": "M32 Patch est une app <strong>indépendante</strong> : elle n'a pas besoin d'<a href=\"easy-routing-m32-x32.html\">Easy Routing</a> sur Mac. Les deux proposent le même style de routage rapide en grille pour M32/X32 via OSC. Affectez entrées et sorties en quelques secondes : touchez une cellule pour assigner, retouchez pour OFF, et gérez Local, AES50, AUX et USB Card sur le même réseau que la console.",
        "h_promo": "Promo App Store (court)",
        "promo": "App iOS indépendante : routage matriciel M32/X32 sur iPhone et iPad — touchez pour assigner ou OFF, Local / AES50 / AUX / USB.",
        "h_features": "Fonctions clés",
        "features": [
            "Routage matriciel visuel des entrées et sorties sur iPhone et iPad.",
            "Flux rapide : toucher pour assigner / retoucher pour OFF.",
            "Chemins Local, AES50, AUX et USB/Card.",
            "Découverte réseau et connexion OSC directe à la console.",
            "Pensée pour le live, les stageboxes et les changements de patch sur le plateau.",
            "Indépendante d'Easy Routing sur Mac : même idée, apps séparées par plateforme.",
        ],
        "closing": "Choisissez <strong>M32 Patch</strong> pour iPhone/iPad, ou <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> pour Mac — chacune fonctionne seule.",
        "store_h3": "App Store",
        "store_p": "Disponible dès maintenant sur l'App Store pour iPhone et iPad.",
        "badge_aria": "Télécharger M32 Patch sur l'App Store",
        "links": '<a href="easy-routing-m32-x32.html">Easy Routing (Mac)</a> · <a href="compare.html">Comparatif</a> · <a href="support.html">Support</a>',
        "card": "App iOS indépendante : routage matriciel pour Midas M32 et Behringer X32 — même idée qu'Easy Routing sur Mac, apps séparées.",
        "card_hint": "<strong>Disponible sur l'App Store</strong> pour iPhone et iPad.",
        "card_aria": "Ouvrir M32 Patch sur l'App Store",
        "card_more": "En savoir plus",
        "title_h3": "M32 Patch (iOS)",
    },
    "de": {
        "desc": "M32 Patch ist eine eigenständige iPhone-/iPad-App für visuelles Matrix-Routing auf Midas M32 und Behringer X32 — derselbe Workflow-Typ wie Easy Routing auf dem Mac.",
        "hero": "Eigenständige iOS-App: visuelles M32/X32-Routing auf iPhone und iPad.",
        "banner_aria": "M32 Patch im App Store",
        "banner_alt": "M32 Patch — im App Store für iPhone und iPad verfügbar",
        "lead": "Jetzt im App Store für iPhone und iPad verfügbar.",
        "h_what": "Was sie macht",
        "intro": "M32 Patch ist eine <strong>eigenständige</strong> App: sie braucht <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> auf dem Mac nicht. Beide bieten denselben schnellen Raster-Workflow für M32/X32 per OSC. Ein-/Ausgänge in Sekunden zuweisen: Zelle tippen zum Assign, nochmal für OFF; Local, AES50, AUX und USB Card im gleichen Netz wie die Konsole.",
        "h_promo": "App-Store-Promo (kurz)",
        "promo": "Eigenständige iOS-App: visuelles M32/X32-Routing auf iPhone und iPad — tippen zum Zuweisen oder OFF, Local / AES50 / AUX / USB.",
        "h_features": "Wichtige Funktionen",
        "features": [
            "Visuelles Matrix-Routing für Ein- und Ausgänge auf iPhone und iPad.",
            "Schneller Workflow: tippen zum Zuweisen / nochmal tippen für OFF.",
            "Routing über Local, AES50, AUX und USB/Card.",
            "Netzwerk-Discovery und direkte OSC-Verbindung zur Konsole.",
            "Für Live-Shows, Stageboxes und schnelle Patch-Änderungen auf der Bühne.",
            "Unabhängig von Easy Routing auf dem Mac — gleiche Idee, getrennte Apps je Plattform.",
        ],
        "closing": "Wählen Sie <strong>M32 Patch</strong> für iPhone/iPad oder <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> für Mac — jede App funktioniert allein.",
        "store_h3": "App Store",
        "store_p": "Jetzt im App Store für iPhone und iPad verfügbar.",
        "badge_aria": "M32 Patch im App Store laden",
        "links": '<a href="easy-routing-m32-x32.html">Easy Routing (Mac)</a> · <a href="compare.html">Vergleich</a> · <a href="support.html">Support</a>',
        "card": "Eigenständige iOS-App: visuelles Matrix-Routing für Midas M32 und Behringer X32 — gleiche Idee wie Easy Routing auf dem Mac, getrennte Apps.",
        "card_hint": "<strong>Im App Store</strong> für iPhone und iPad.",
        "card_aria": "M32 Patch im App Store öffnen",
        "card_more": "Mehr erfahren",
        "title_h3": "M32 Patch (iOS)",
    },
    "ca": {
        "desc": "M32 Patch és una app independent per a iPhone i iPad amb routing visual en graella per a Midas M32 i Behringer X32 — el mateix tipus de flux qu'Easy Routing al Mac.",
        "hero": "App independent per a iOS: routing visual M32/X32 a iPhone i iPad.",
        "banner_aria": "M32 Patch a l'App Store",
        "banner_alt": "M32 Patch — disponible a l'App Store per a iPhone i iPad",
        "lead": "Ja disponible a l'App Store per a iPhone i iPad.",
        "h_what": "Què fa",
        "intro": "M32 Patch és una app <strong>independent</strong>: no necessita <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> al Mac. Totes dues ofereixen el mateix estil de routing ràpid en graella per a M32/X32 via OSC. Mapeja entrades i sortides en segons: toca una cel·la per assignar, una altra vegada per OFF, i gestiona Local, AES50, AUX i USB Card a la mateixa xarxa que la consola.",
        "h_promo": "Text promocional curt",
        "promo": "App independent per a iOS: routing visual M32/X32 a iPhone i iPad — toca per assignar o OFF, Local / AES50 / AUX / USB.",
        "h_features": "Característiques clau",
        "features": [
            "Routing visual en graella per a entrades i sortides a iPhone i iPad.",
            "Flux ràpid: tocar per assignar / tornar a tocar per OFF.",
            "Routing en rutes Local, AES50, AUX i USB/Card.",
            "Descobriment per xarxa i connexió OSC directa a la taula.",
            "Pensada per a shows en viu, stageboxes i canvis de patch a terra.",
            "Independent d'Easy Routing al Mac: mateixa idea, apps separades per plataforma.",
        ],
        "closing": "Tria <strong>M32 Patch</strong> per a iPhone/iPad, o <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> per al Mac — cadascuna funciona sola.",
        "store_h3": "App Store",
        "store_p": "Ja disponible a l'App Store per a iPhone i iPad.",
        "badge_aria": "Descarregar M32 Patch a l'App Store",
        "links": '<a href="easy-routing-m32-x32.html">Easy Routing (Mac)</a> · <a href="compare.html">Comparativa</a> · <a href="support.html">Suport</a>',
        "card": "App independent per a iOS: routing visual en graella per a Midas M32 i Behringer X32 — mateixa idea qu'Easy Routing al Mac, apps separades.",
        "card_hint": "<strong>Ja a l'App Store</strong> per a iPhone i iPad.",
        "card_aria": "Obrir M32 Patch a l'App Store",
        "card_more": "Veure més",
        "title_h3": "M32 Patch (iOS)",
    },
    "gl": {
        "desc": "M32 Patch é unha app independente para iPhone e iPad con routing visual en grella para Midas M32 e Behringer X32 — o mesmo tipo de fluxo que Easy Routing no Mac.",
        "hero": "App independente para iOS: routing visual M32/X32 en iPhone e iPad.",
        "banner_aria": "M32 Patch na App Store",
        "banner_alt": "M32 Patch — dispoñible na App Store para iPhone e iPad",
        "lead": "Xa dispoñible na App Store para iPhone e iPad.",
        "h_what": "Que fai",
        "intro": "M32 Patch é unha app <strong>independente</strong>: non precisa <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> no Mac. Ambas ofrecen o mesmo estilo de routing rápido en grella para M32/X32 por OSC. Mapea entradas e saídas en segundos: toca unha cela para asignar, outra vez para OFF, e xestiona Local, AES50, AUX e USB Card na mesma rede que a consola.",
        "h_promo": "Texto promocional curto",
        "promo": "App independente para iOS: routing visual M32/X32 en iPhone e iPad — toca para asignar ou OFF, Local / AES50 / AUX / USB.",
        "h_features": "Características clave",
        "features": [
            "Routing visual en grella para entradas e saídas en iPhone e iPad.",
            "Fluxo rápido: tocar para asignar / tocar outra vez para OFF.",
            "Routing en rutas Local, AES50, AUX e USB/Card.",
            "Descubrimento por rede e conexión OSC directa á mesa.",
            "Pensada para shows en vivo, stageboxes e cambios de patch no chan.",
            "Independiente de Easy Routing no Mac: mesma idea, apps separadas por plataforma.",
        ],
        "closing": "Escolle <strong>M32 Patch</strong> para iPhone/iPad, ou <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> para Mac — cada unha funciona por si soa.",
        "store_h3": "App Store",
        "store_p": "Xa dispoñible na App Store para iPhone e iPad.",
        "badge_aria": "Descargar M32 Patch na App Store",
        "links": '<a href="easy-routing-m32-x32.html">Easy Routing (Mac)</a> · <a href="compare.html">Comparativa</a> · <a href="support.html">Soporte</a>',
        "card": "App independente para iOS: routing visual en grella para Midas M32 e Behringer X32 — mesma idea que Easy Routing no Mac, apps separadas.",
        "card_hint": "<strong>Xa na App Store</strong> para iPhone e iPad.",
        "card_aria": "Abrir M32 Patch na App Store",
        "card_more": "Ver máis",
        "title_h3": "M32 Patch (iOS)",
    },
    "eu": {
        "desc": "M32 Patch iPhone eta iPad-erako app independentea da: matrize routing bisuala Midas M32 eta Behringer X32rako — Easy Routing Mac-ekoaren fluxu mota bera.",
        "hero": "iOS app independentea: M32/X32 routing bisuala iPhone eta iPad-en.",
        "banner_aria": "M32 Patch App Store-n",
        "banner_alt": "M32 Patch — App Store-n eskuragarri iPhone eta iPad-erako",
        "lead": "App Store-n eskuragarri iPhone eta iPad-erako.",
        "h_what": "Zer egiten du",
        "intro": "M32 Patch <strong>independentea</strong> da: ez du <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> Mac-ean behar. Biek M32/X32rako matrize fluxu azkar bera eskaintzen dute OSC bidez. Sarrerak eta irteerak segundo gutxitan mapatu: ukitu gelaxka bat esleitzeko, berriro OFF jartzeko, eta kudeatu Local, AES50, AUX eta USB Card kontsolaren sare berean.",
        "h_promo": "App Store promo laburra",
        "promo": "iOS app independentea: M32/X32 routing bisuala iPhone eta iPad-en — ukitu esleitzeko edo OFF, Local / AES50 / AUX / USB.",
        "h_features": "Ezaugarri nagusiak",
        "features": [
            "Sarrera eta irteeretarako matrize routing bisuala iPhone eta iPad-en.",
            "Fluxu azkarra: ukitu esleitzeko / berriro OFF.",
            "Local, AES50, AUX eta USB/Card bideak.",
            "Sare aurkikuntza eta OSC konexio zuzena mesara.",
            "Zuzeneko showetarako, stageboxetarako eta oholtzako patch aldaketetarako.",
            "Easy Routing Mac-etik independentea — ideia bera, plataforma bakoitzerako app bereiziak.",
        ],
        "closing": "Aukeratu <strong>M32 Patch</strong> iPhone/iPad-erako, edo <a href=\"easy-routing-m32-x32.html\">Easy Routing</a> Mac-erako — bakoitza bere kasa funtzionatzen du.",
        "store_h3": "App Store",
        "store_p": "App Store-n eskuragarri iPhone eta iPad-erako.",
        "badge_aria": "Deskargatu M32 Patch App Store-n",
        "links": '<a href="easy-routing-m32-x32.html">Easy Routing (Mac)</a> · <a href="compare.html">Konparaketa</a> · <a href="support.html">Laguntza</a>',
        "card": "iOS app independentea: matrize routing bisuala Midas M32 eta Behringer X32rako — Easy Routing Mac-ekoaren ideia bera, app bereiziak.",
        "card_hint": "<strong>App Store-n eskuragarri</strong> iPhone eta iPad-erako.",
        "card_aria": "Ireki M32 Patch App Store-n",
        "card_more": "Gehiago ikusi",
        "title_h3": "M32 Patch (iOS)",
    },
}

# Short note injected into Easy Routing pages (after lead / first strong paragraph).
IOS_NOTE = {
    "en": '<p><strong>Also on iOS:</strong> <a href="m32-patch.html">M32 Patch</a> is an independent iPhone and iPad app with the same style of visual routing — <a href="https://apple.co/44TAL9z" target="_blank" rel="noopener noreferrer">App Store</a>.</p>',
    "es": '<p><strong>También en iOS:</strong> <a href="m32-patch.html">M32 Patch</a> es una app independiente para iPhone e iPad con el mismo estilo de routing visual — <a href="https://apple.co/44TAL9z" target="_blank" rel="noopener noreferrer">App Store</a>.</p>',
    "fr": '<p><strong>Aussi sur iOS :</strong> <a href="m32-patch.html">M32 Patch</a> est une app indépendante pour iPhone et iPad avec le même style de routage visuel — <a href="https://apple.co/44TAL9z" target="_blank" rel="noopener noreferrer">App Store</a>.</p>',
    "de": '<p><strong>Auch auf iOS:</strong> <a href="m32-patch.html">M32 Patch</a> ist eine eigenständige iPhone-/iPad-App mit demselben visuellen Routing-Stil — <a href="https://apple.co/44TAL9z" target="_blank" rel="noopener noreferrer">App Store</a>.</p>',
    "ca": '<p><strong>També a iOS:</strong> <a href="m32-patch.html">M32 Patch</a> és una app independent per a iPhone i iPad amb el mateix estil de routing visual — <a href="https://apple.co/44TAL9z" target="_blank" rel="noopener noreferrer">App Store</a>.</p>',
    "gl": '<p><strong>Tamén en iOS:</strong> <a href="m32-patch.html">M32 Patch</a> é unha app independente para iPhone e iPad co mesmo estilo de routing visual — <a href="https://apple.co/44TAL9z" target="_blank" rel="noopener noreferrer">App Store</a>.</p>',
    "eu": '<p><strong>iOS-en ere:</strong> <a href="m32-patch.html">M32 Patch</a> iPhone eta iPad-erako app independentea da, routing bisual estilo berarekin — <a href="https://apple.co/44TAL9z" target="_blank" rel="noopener noreferrer">App Store</a>.</p>',
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
  <title>M32 Patch — Stage Apps</title>
{hreflangs}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
  <link rel="icon" href="/favicon.ico?v=3" sizes="any">
  <link rel="icon" href="/assets/images/stageapps-favicon-32.png?v=3" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/images/stageapps-favicon-180.png?v=3">
  <link rel="stylesheet" href="{CSS}">
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
        <h1>M32 Patch</h1>
        <p class="meta">{t['hero']}</p>
      </section>
      <section>
        <div class="wrap">
          <div class="app-hero-banner" aria-label="{t['banner_aria']}">
            <a href="{APP_STORE}" target="_blank" rel="noopener noreferrer">
              <img src="{BANNER}" alt="{t['banner_alt']}" width="1200" height="720" loading="eager" decoding="async">
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
</html>
"""


def insert_index_card(code: str) -> None:
    p = ROOT / code / "index.html"
    t = T[code]
    text = p.read_text(encoding="utf-8")
    block = f"""<div class="app-grid-item">
            <article class="card app-card">
            <div class="app-card-text">
              <h3>{t['title_h3']}</h3>
              <p>{t['card']}</p>
            </div>
            </article>
            <a class="app-card-thumb" href="m32-patch.html" aria-label="{t['card_aria']}">
              <img src="{SQUARE}" alt="{t['banner_alt']}" loading="lazy" decoding="async">
            </a>
            <div class="app-card-actions">
              <p class="app-card-store-hint">{t['card_hint']}</p>
            </div>
            <div class="app-card-badge-row">
              {store_badge_html(t['badge_aria'], inline=True)}
            </div>
            <div class="app-card-cta-secondary">
              <a class="btn btn-secondary" href="m32-patch.html">{t['card_more']}</a>
            </div>
          </div>
"""
    # Replace existing card if present; otherwise insert before Stage With Me.
    card_re = re.compile(
        r'<div class="app-grid-item">\s*<article class="card app-card">\s*'
        r'<div class="app-card-text">\s*<h3>M32 Patch \(iOS\)</h3>.*?'
        r'(?=<div class="app-grid-item">\s*<article class="card app-card">\s*'
        r'<div class="app-card-text">\s*<h3>Stage With Me)',
        re.DOTALL,
    )
    if card_re.search(text):
        updated, n = card_re.subn(block, text, count=1)
        if n != 1:
            raise SystemExit(f"Could not replace M32 Patch card in {p}")
    else:
        pattern = (
            r'(</div>\s*)'
            r'(<div class="app-grid-item">\s*<article class="card app-card">\s*'
            r'<div class="app-card-text">\s*<h3>Stage With Me)'
        )
        updated, n = re.subn(pattern, r"\1" + block + r"\2", text, count=1, flags=re.DOTALL)
        if n != 1:
            raise SystemExit(f"Could not insert M32 Patch card in {p}")
    updated = updated.replace("styles.css?v=16", "styles.css?v=17").replace(
        "styles.css?v=15", "styles.css?v=17"
    )
    p.write_text(updated, encoding="utf-8")


def update_compare(code: str) -> None:
    p = ROOT / code / "compare.html"
    text = p.read_text(encoding="utf-8")
    if ">M32 Patch<" in text:
        return
    name, best, proto, platform = COMPARE_ROW[code]
    row = f"                <tr><td>{name}</td><td>{best}</td><td>{proto}</td><td>{platform}</td></tr>\n"
    # Place after Easy Routing row if present, else after MIDItoOSC.
    if "M32 / X32 Easy Routing" in text:
        text = re.sub(
            r'(<tr><td>M32 / X32 Easy Routing</td>.*?</tr>\n)',
            r"\1" + row,
            text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        text = text.replace(
            "                <tr><td>MIDItoOSC</td>",
            row + "                <tr><td>MIDItoOSC</td>",
            1,
        )
    p.write_text(text, encoding="utf-8")


def update_nav_all() -> None:
    """Insert M32 Patch nav link after Easy Routing on every HTML page."""
    needle = '<a href="easy-routing-m32-x32.html">Easy Routing</a>'
    insert = needle + '\n            <a href="m32-patch.html">M32 Patch</a>'
    for path in ROOT.rglob("*.html"):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        if "m32-patch.html\">M32 Patch</a>" in text:
            continue
        if needle not in text:
            continue
        path.write_text(text.replace(needle, insert), encoding="utf-8")
        print("nav", path.relative_to(ROOT))


def update_easy_routing_crosslink(code: str) -> None:
    p = ROOT / code / "easy-routing-m32-x32.html"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    note = IOS_NOTE[code]
    # Replace any existing iOS note that points at M32 Patch.
    note_re = re.compile(
        r'<p><strong>(?:Also on iOS|También en iOS|Aussi sur iOS\s*:|Auch auf iOS|També a iOS|Tamén en iOS|iOS-en ere)[:：]?</strong>[\s\S]*?</p>\s*',
    )
    if note_re.search(text):
        text = note_re.sub(note + "\n          ", text, count=1)
    else:
        updated, n = re.subn(
            r'(<p><strong>[^<]*</strong></p>\s*)(<h2>[^<]+</h2>)',
            r"\1" + note + "\n          \\2",
            text,
            count=1,
        )
        if n != 1:
            raise SystemExit(f"Could not insert iOS note in {p}")
        text = updated
    needle = '<a href="easy-routing-m32-x32.html">Easy Routing</a>'
    if 'href="m32-patch.html">M32 Patch</a>' not in text.split("<main>", 1)[0]:
        text = text.replace(
            needle,
            needle + '\n            <a href="m32-patch.html">M32 Patch</a>',
            1,
        )
    p.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    for code in LANGS:
        (ROOT / code / FILE).write_text(render_page(code), encoding="utf-8")
        insert_index_card(code)
        update_compare(code)
        update_easy_routing_crosslink(code)
        print("wrote", code)
    update_nav_all()
    print("done")
