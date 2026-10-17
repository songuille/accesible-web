#!/usr/bin/env python3
"""Publish Transparent Screen on the Stage Apps site (all locales)."""
import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = "https://apple.co/4eCORRI"
IMAGE = "../assets/images/transparent-screen-square-1080.png"
BANNER = "../assets/images/transparent-screen-banner-1200x720.png"
HREF = "transparent-screen.html"

COPY = {
    "es": {
        "blurb": "Ve el escenario a través del Mac con cámara o NDI.",
        "detail": "Transparent Screen pone la cámara detrás de las ventanas: QLab y la cue list siguen encima. Webcam USB, Continuity Camera o NDI. En la Mac App Store.",
        "meta": "Ve el escenario a través del Mac con cámara USB, Continuity Camera o NDI.",
        "title": "Transparent Screen (macOS) — Stage Apps",
        "h1": "Transparent Screen (macOS)",
        "banner_aria": "Transparent Screen en la App Store",
        "banner_alt": "Transparent Screen — ya en la App Store",
        "features_h": "Características",
        "features": [
            "Coloca la imagen de la cámara detrás de todas las ventanas (click-through).",
            "Webcam USB, Continuity Camera (iPhone/iPad) o fuente NDI.",
            "Ajusta recorte, zoom, panorámica y opacidad.",
            "Doble clic para enviarla detrás de todo; zona de vídeo opcional adicional.",
            "Pensada para la cabina de control: el monitor deja de tapar el escenario.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Ya disponible</strong> en la App Store para Mac (0,99 €).",
        "store_aria": "Descargar en la App Store",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "compare_best": "Ver el escenario a través del monitor de cabina",
        "compare_proto": "Cámara, Continuity Camera, NDI",
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
    },
    "en": {
        "blurb": "See the stage through your Mac with camera or NDI.",
        "detail": "Transparent Screen puts the camera behind every window so QLab and your cue list stay on top. USB webcam, Continuity Camera or NDI. On the Mac App Store.",
        "meta": "See the stage through your Mac with a USB webcam, Continuity Camera or NDI.",
        "title": "Transparent Screen (macOS) — Stage Apps",
        "h1": "Transparent Screen (macOS)",
        "banner_aria": "Transparent Screen on the App Store",
        "banner_alt": "Transparent Screen — now on the App Store",
        "features_h": "Features",
        "features": [
            "Places the camera image behind every window (click-through).",
            "USB webcam, Continuity Camera (iPhone/iPad) or NDI source.",
            "Crop, zoom, pan and opacity controls.",
            "Double-click to send it behind everything; optional second video zone.",
            "Built for the control booth: the monitor no longer blocks the stage.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Available now</strong> on the Mac App Store ($0.99).",
        "store_aria": "Download on the App Store",
        "footer_links": '<p><a href="compare.html">Compare apps</a> · <a href="use-cases.html">Use cases</a> · <a href="support.html">Support</a></p>',
        "compare_best": "See the stage through the booth monitor",
        "compare_proto": "Camera, Continuity Camera, NDI",
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
    },
    "fr": {
        "blurb": "Voyez la scène à travers le Mac (caméra ou NDI).",
        "detail": "Transparent Screen place la caméra derrière les fenêtres : QLab et la cue list restent au-dessus. Webcam USB, Continuity Camera ou NDI. Sur le Mac App Store.",
        "meta": "Voyez la scène à travers le Mac avec webcam USB, Continuity Camera ou NDI.",
        "title": "Transparent Screen (macOS) — Stage Apps",
        "h1": "Transparent Screen (macOS)",
        "banner_aria": "Transparent Screen sur l’App Store",
        "banner_alt": "Transparent Screen — déjà sur l’App Store",
        "features_h": "Fonctionnalités",
        "features": [
            "Place l’image de la caméra derrière toutes les fenêtres (clics traversants).",
            "Webcam USB, Continuity Camera (iPhone/iPad) ou source NDI.",
            "Recadrage, zoom, panoramique et opacité.",
            "Double-clic pour l’envoyer derrière tout ; zone vidéo optionnelle.",
            "Pensée pour la régie : l’écran ne masque plus la scène.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Disponible</strong> sur le Mac App Store (0,99 €).",
        "store_aria": "Télécharger sur l’App Store",
        "footer_links": '<p><a href="compare.html">Comparatif</a> · <a href="use-cases.html">Cas d’usage</a> · <a href="support.html">Support</a></p>',
        "compare_best": "Voir la scène à travers l’écran de régie",
        "compare_proto": "Caméra, Continuity Camera, NDI",
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
    },
    "de": {
        "blurb": "Bühne durch den Mac sehen – Kamera oder NDI.",
        "detail": "Transparent Screen legt die Kamera hinter alle Fenster: QLab und Cue-Liste bleiben oben. USB-Webcam, Continuity Camera oder NDI. Im Mac App Store.",
        "meta": "Sehen Sie die Bühne durch den Mac mit USB-Webcam, Continuity Camera oder NDI.",
        "title": "Transparent Screen (macOS) — Stage Apps",
        "h1": "Transparent Screen (macOS)",
        "banner_aria": "Transparent Screen im App Store",
        "banner_alt": "Transparent Screen — jetzt im App Store",
        "features_h": "Funktionen",
        "features": [
            "Kamerabild hinter allen Fenstern (Klicks gehen durch).",
            "USB-Webcam, Continuity Camera (iPhone/iPad) oder NDI-Quelle.",
            "Zuschnitt, Zoom, Schwenken und Deckkraft.",
            "Doppelklick schickt es hinter alles; optionale zweite Videozone.",
            "Für die Regie: der Monitor verdeckt die Bühne nicht mehr.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Jetzt verfügbar</strong> im Mac App Store (0,99 €).",
        "store_aria": "Im App Store laden",
        "footer_links": '<p><a href="compare.html">Vergleich</a> · <a href="use-cases.html">Anwendungsfälle</a> · <a href="support.html">Support</a></p>',
        "compare_best": "Bühne durch den Regiemonitor sehen",
        "compare_proto": "Kamera, Continuity Camera, NDI",
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
    },
    "gl": {
        "blurb": "Ve o escenario a través do Mac con cámara ou NDI.",
        "detail": "Transparent Screen pon a cámara detrás das ventás: QLab e a cue list seguen enriba. Webcam USB, Continuity Camera ou NDI. Na Mac App Store.",
        "meta": "Ve o escenario a través do Mac con webcam USB, Continuity Camera ou NDI.",
        "title": "Transparent Screen (macOS) — Stage Apps",
        "h1": "Transparent Screen (macOS)",
        "banner_aria": "Transparent Screen na App Store",
        "banner_alt": "Transparent Screen — xa na App Store",
        "features_h": "Características",
        "features": [
            "Coloca a imaxe da cámara detrás de todas as ventás (click-through).",
            "Webcam USB, Continuity Camera (iPhone/iPad) ou fonte NDI.",
            "Recorte, zoom, panorámica e opacidade.",
            "Dobre clic para enviala detrás de todo; zona de vídeo opcional.",
            "Pensada para a cabina de control: o monitor deixa de tapar o escenario.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Xa dispoñible</strong> na App Store para Mac (0,99 €).",
        "store_aria": "Descargar na App Store",
        "footer_links": '<p><a href="compare.html">Ver comparativa</a> · <a href="use-cases.html">Ver casos de uso</a> · <a href="support.html">Soporte</a></p>',
        "compare_best": "Ver o escenario a través do monitor de cabina",
        "compare_proto": "Cámara, Continuity Camera, NDI",
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
    },
    "ca": {
        "blurb": "Veure l’escenari a través del Mac amb càmera o NDI.",
        "detail": "Transparent Screen posa la càmera darrere les finestres: QLab i la cue list queden a sobre. Webcam USB, Continuity Camera o NDI. Al Mac App Store.",
        "meta": "Veure l’escenari a través del Mac amb webcam USB, Continuity Camera o NDI.",
        "title": "Transparent Screen (macOS) — Stage Apps",
        "h1": "Transparent Screen (macOS)",
        "banner_aria": "Transparent Screen a l’App Store",
        "banner_alt": "Transparent Screen — ja a l’App Store",
        "features_h": "Característiques",
        "features": [
            "Posa la imatge de la càmera darrere de totes les finestres (click-through).",
            "Webcam USB, Continuity Camera (iPhone/iPad) o font NDI.",
            "Retall, zoom, panoràmica i opacitat.",
            "Doble clic per enviar-la darrere de tot; zona de vídeo opcional.",
            "Pensada per a la cabina de control: el monitor deixa de tapar l’escenari.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Ja disponible</strong> a l’App Store per a Mac (0,99 €).",
        "store_aria": "Descarregar a l’App Store",
        "footer_links": '<p><a href="compare.html">Veure comparativa</a> · <a href="use-cases.html">Veure casos d’ús</a> · <a href="support.html">Suport</a></p>',
        "compare_best": "Veure l’escenari a través del monitor de cabina",
        "compare_proto": "Càmera, Continuity Camera, NDI",
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
    },
    "eu": {
        "blurb": "Ikusi eszena Mac-etik kamera edo NDI bidez.",
        "detail": "Transparent Screen-ek kamera leihoen atzean jartzen du: QLab eta cue list goian geratzen dira. USB webcam, Continuity Camera edo NDI. Mac App Store-n.",
        "meta": "Ikusi eszena Mac-etik USB webcam, Continuity Camera edo NDI bidez.",
        "title": "Transparent Screen (macOS) — Stage Apps",
        "h1": "Transparent Screen (macOS)",
        "banner_aria": "Transparent Screen App Store-n",
        "banner_alt": "Transparent Screen — jada App Store-n",
        "features_h": "Ezaugarriak",
        "features": [
            "Kameraren irudia leiho guztien atzean jartzen du (klikak zeharkatzen dira).",
            "USB webcam, Continuity Camera (iPhone/iPad) edo NDI iturria.",
            "Moztu, zoom, panoramika eta opakutasuna.",
            "Klik bikoitza denaren atzean bidaltzeko; bigarren bideo-gune aukerakoa.",
            "Kontrol-kabinarako pentsatua: monitoreak ez du eszena estaltzen.",
        ],
        "store_h": "App Store",
        "store_p": "<strong>Jada eskuragarri</strong> Mac App Store-n (0,99 €).",
        "store_aria": "Deskargatu App Store-tik",
        "footer_links": '<p><a href="compare.html">Konparaketa</a> · <a href="use-cases.html">Erabilera kasuak</a> · <a href="support.html">Laguntza</a></p>',
        "compare_best": "Ikusi eszena kabina-monitoretik",
        "compare_proto": "Kamera, Continuity Camera, NDI",
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
    },
}

LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]
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
    href = "transparent-screen.html" if target == cur else f"../{target}/transparent-screen.html"
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
        f'  <link rel="alternate" hreflang="{L}" href="../{L}/transparent-screen.html">'
        for L in LANGS
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
  <link rel="stylesheet" href="../css/styles.css?v=32">
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
          <div class="app-hero-banner" aria-label="{htmlmod.escape(c['banner_aria'])}">
            <a href="{STORE}" target="_blank" rel="noopener noreferrer">
              <img src="{BANNER}" alt="{htmlmod.escape(c['banner_alt'])}" width="1200" height="720" loading="eager" decoding="async">
            </a>
          </div>
        </div>
      </section>
      <section>
        <div class="wrap prose">
          <h2>{c['features_h']}</h2>
          <ul>
            {features}
          </ul>

          <div class="beta-callout">
            <h3>{c['store_h']}</h3>
            <p>{c['store_p']}</p>
            <p><a class="store-badge-link" href="{STORE}" target="_blank" rel="noopener noreferrer" aria-label="{htmlmod.escape(c['store_aria'])}"><img src="../assets/images/download-on-the-app-store-en-us-white.svg" alt="Download on the App Store" width="120" height="40" loading="lazy" decoding="async"></a></p>
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
        path = ROOT / f"docs/{lang}/transparent-screen.html"
        path.write_text(build_page(lang), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))

    for lang in LANGS:
        path = ROOT / f"docs/{lang}/index.html"
        text = path.read_text(encoding="utf-8")
        m = re.search(r'data-apps="([^"]+)"', text)
        if not m:
            raise SystemExit(f"no data-apps {lang}")
        apps = json.loads(htmlmod.unescape(m.group(1)))
        found = False
        for app in apps:
            if app.get("name") == "Transparent Screen":
                app.pop("soon", None)
                app["blurb"] = COPY[lang]["blurb"]
                app["detail"] = COPY[lang]["detail"]
                app["href"] = HREF
                app["image"] = IMAGE
                app["store"] = STORE
                found = True
        if not found:
            raise SystemExit(f"no TS app {lang}")
        encoded = htmlmod.escape(json.dumps(apps, ensure_ascii=False), quote=True)
        text = text[: m.start(1)] + encoded + text[m.end(1) :]
        old_btn = (
            '<button type="button" class="app-orbit-planet" data-orbit-planet '
            'aria-label="Transparent Screen"><span class="soon-mark">Soon</span></button>'
        )
        new_btn = (
            '<button type="button" class="app-orbit-planet" data-orbit-planet '
            f'aria-label="Transparent Screen"><img src="{IMAGE}" alt=""></button>'
        )
        if old_btn not in text:
            raise SystemExit(f"no soon button {lang}")
        text = text.replace(old_btn, new_btn, 1)
        text = text.replace("home-carousel.css?v=39", "home-carousel.css?v=40")
        text = text.replace("styles.css?v=31", "styles.css?v=32")
        path.write_text(text, encoding="utf-8")
        print("index", lang)

    nav_pat = re.compile(
        r'(<a href="stage-with-me\.html">Stage With Me</a>)(?!\s*\n?\s*<a href="transparent-screen\.html">)'
    )
    nav_count = 0
    for path in (ROOT / "docs").rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if 'href="stage-with-me.html">Stage With Me</a>' not in text:
            continue
        if 'href="transparent-screen.html">Transparent Screen</a>' in text:
            continue
        new, n = nav_pat.subn(
            r'\1\n            <a href="transparent-screen.html">Transparent Screen</a>',
            text,
        )
        if n:
            path.write_text(new, encoding="utf-8")
            nav_count += n
    print("nav inserts", nav_count)

    for lang in LANGS:
        path = ROOT / f"docs/{lang}/compare.html"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "Transparent Screen" in text and "<td>Transparent Screen</td>" in text:
            print("compare already", lang)
            continue
        row = (
            f'<tr><td>Transparent Screen</td><td>{COPY[lang]["compare_best"]}</td>'
            f'<td>{COPY[lang]["compare_proto"]}</td><td>macOS</td></tr>'
        )
        if "</tbody>" not in text:
            continue
        text = text.replace("</tbody>", f"                {row}\n              </tbody>", 1)
        path.write_text(text, encoding="utf-8")
        print("compare", lang)

    print("DONE")


if __name__ == "__main__":
    main()
