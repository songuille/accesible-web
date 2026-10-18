#!/usr/bin/env python3
"""Create Stage Recorder product pages (coming soon) and wire them into the site."""
import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "../assets/images/stage-recorder-square-1080.png"
HREF = "stage-recorder.html"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]

COPY = {
    "es": {
        "meta": "Grabadora multipista sencilla para Mac: captura sesiones (p. ej. M32/DN32) y exporta pistas o un WAV estéreo de referencia.",
        "title": "Stage Recorder (macOS) — Stage Apps",
        "h1": "Stage Recorder (macOS)",
        "lead": "Stage Recorder no pretende ser un DAW: es una grabadora multipista sencilla para Mac. Sirve para obtener las pistas que luego editarás en tu DAW, o un WAV estéreo L/R de referencia.",
        "features_h": "Características",
        "features": [
            "Grabación multipista sencilla: crea una sesión, asigna entradas y graba.",
            "Pensada para cabina: captura salidas de mesas como M32 / DN32 hacia el Mac.",
            "Exporta las pistas individuales para abrirlas en tu DAW.",
            "Exporta también una mezcla estéreo WAV de referencia (L/R).",
            "No es un DAW: sin mezcla compleja ni edición avanzada; solo capturar y sacar.",
        ],
        "soon_h": "Próximamente",
        "soon_p": "<strong>En breve en la Mac App Store.</strong> Mientras tanto puedes seguir las novedades de Stage Apps.",
        "icon_alt": "Icono de Stage Recorder",
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
        "blurb": "Grabadora multipista sencilla (no es un DAW).",
        "detail": "Graba sesiones multipista (p. ej. desde una M32), exporta las pistas a tu DAW y una mezcla estéreo WAV de referencia. Próximamente en la Mac App Store.",
    },
    "en": {
        "meta": "Simple multitrack recorder for Mac: capture sessions (e.g. M32/DN32) and export stems or a stereo WAV reference mix.",
        "title": "Stage Recorder (macOS) — Stage Apps",
        "h1": "Stage Recorder (macOS)",
        "lead": "Stage Recorder is not trying to be a DAW: it is a simple multitrack recorder for Mac. Capture the tracks you will edit later in your DAW, or a stereo L/R WAV for reference.",
        "features_h": "Features",
        "features": [
            "Simple multitrack recording: create a session, assign inputs and record.",
            "Built for the booth: capture desk outputs such as M32 / DN32 into the Mac.",
            "Export individual tracks to open in your DAW.",
            "Also export a stereo WAV reference mix (L/R).",
            "Not a DAW: no complex mixing or deep editing—just capture and get out.",
        ],
        "soon_h": "Coming soon",
        "soon_p": "<strong>Coming soon to the Mac App Store.</strong> Follow Stage Apps for updates.",
        "icon_alt": "Stage Recorder icon",
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
        "blurb": "Simple multitrack recorder (not a DAW).",
        "detail": "Record multitrack sessions (e.g. from an M32), export stems to your DAW and a stereo WAV reference mix. Coming soon to the Mac App Store.",
    },
    "fr": {
        "meta": "Enregistreur multipiste simple pour Mac : capturez des sessions (p. ex. M32/DN32) et exportez les pistes ou un mix stéréo WAV de référence.",
        "title": "Stage Recorder (macOS) — Stage Apps",
        "h1": "Stage Recorder (macOS)",
        "lead": "Stage Recorder n’est pas un DAW : c’est un enregistreur multipiste simple pour Mac. Obtenez les pistes à éditer ensuite dans votre DAW, ou un WAV stéréo L/R de référence.",
        "features_h": "Fonctionnalités",
        "features": [
            "Enregistrement multipiste simple : créez une session, assignez les entrées et enregistrez.",
            "Pensé pour la régie : capturez les sorties de consoles comme M32 / DN32 vers le Mac.",
            "Exportez les pistes individuelles pour votre DAW.",
            "Exportez aussi un mix stéréo WAV de référence (L/R).",
            "Pas un DAW : pas de mixage complexe ni d’édition avancée — capturer et sortir.",
        ],
        "soon_h": "Bientôt",
        "soon_p": "<strong>Bientôt sur le Mac App Store.</strong> Suivez Stage Apps pour les nouveautés.",
        "icon_alt": "Icône Stage Recorder",
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
        "blurb": "Enregistreur multipiste simple (pas un DAW).",
        "detail": "Enregistrez des sessions multipistes (p. ex. depuis une M32), exportez les pistes vers votre DAW et un mix stéréo WAV de référence. Bientôt sur le Mac App Store.",
    },
    "de": {
        "meta": "Einfacher Mehrspur-Recorder für den Mac: Sessions aufnehmen (z. B. M32/DN32) und Spuren oder eine Stereo-WAV-Referenz exportieren.",
        "title": "Stage Recorder (macOS) — Stage Apps",
        "h1": "Stage Recorder (macOS)",
        "lead": "Stage Recorder will kein DAW sein: ein einfacher Mehrspur-Recorder für den Mac. Holen Sie die Spuren für Ihr DAW — oder eine Stereo-WAV-Referenz (L/R).",
        "features_h": "Funktionen",
        "features": [
            "Einfache Mehrspuraufnahme: Session anlegen, Eingänge zuweisen und aufnehmen.",
            "Für die Regie: Ausgänge von Mischpulten wie M32 / DN32 auf den Mac aufnehmen.",
            "Einzelne Spuren für Ihr DAW exportieren.",
            "Zusätzlich eine Stereo-WAV-Referenzmischung (L/R) exportieren.",
            "Kein DAW: keine komplexe Mischung oder Tiefeneditierung — aufnehmen und raus.",
        ],
        "soon_h": "Demnächst",
        "soon_p": "<strong>Demnächst im Mac App Store.</strong> Folgen Sie Stage Apps für Neuigkeiten.",
        "icon_alt": "Stage-Recorder-Symbol",
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
        "blurb": "Einfacher Mehrspur-Recorder (kein DAW).",
        "detail": "Mehrspur-Sessions aufnehmen (z. B. von einer M32), Spuren in Ihr DAW und eine Stereo-WAV-Referenzmischung exportieren. Demnächst im Mac App Store.",
    },
    "gl": {
        "meta": "Gravadora multipista sinxela para Mac: captura sesións (p. ex. M32/DN32) e exporta pistas ou un WAV estéreo de referencia.",
        "title": "Stage Recorder (macOS) — Stage Apps",
        "h1": "Stage Recorder (macOS)",
        "lead": "Stage Recorder non pretende ser un DAW: é unha gravadora multipista sinxela para Mac. Serve para obter as pistas que logo editarás no teu DAW, ou un WAV estéreo L/R de referencia.",
        "features_h": "Características",
        "features": [
            "Gravación multipista sinxela: crea unha sesión, asigna entradas e grava.",
            "Pensada para cabina: captura saídas de mesas como M32 / DN32 cara ao Mac.",
            "Exporta as pistas individuais para o teu DAW.",
            "Exporta tamén unha mestura estéreo WAV de referencia (L/R).",
            "Non é un DAW: sen mestura complexa nin edición avanzada; só capturar e sacar.",
        ],
        "soon_h": "Proximamente",
        "soon_p": "<strong>En breve na Mac App Store.</strong> Mentres tanto podes seguir as novidades de Stage Apps.",
        "icon_alt": "Icona de Stage Recorder",
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
        "blurb": "Gravadora multipista sinxela (non é un DAW).",
        "detail": "Grava sesións multipista (p. ex. dende unha M32), exporta as pistas ao teu DAW e unha mestura estéreo WAV de referencia. Proximamente na Mac App Store.",
    },
    "ca": {
        "meta": "Enregistradora multipista senzilla per a Mac: captura sessions (p. ex. M32/DN32) i exporta pistes o un WAV estèreo de referència.",
        "title": "Stage Recorder (macOS) — Stage Apps",
        "h1": "Stage Recorder (macOS)",
        "lead": "Stage Recorder no pretén ser un DAW: és una enregistradora multipista senzilla per a Mac. Serveix per obtenir les pistes que després editaràs al teu DAW, o un WAV estèreo L/R de referència.",
        "features_h": "Característiques",
        "features": [
            "Enregistrament multipista senzill: crea una sessió, assigna entrades i grava.",
            "Pensada per a la cabina: captura sortides de taules com M32 / DN32 cap al Mac.",
            "Exporta les pistes individuals per al teu DAW.",
            "Exporta també una barreja estèreo WAV de referència (L/R).",
            "No és un DAW: sense mescla complexa ni edició avançada; només capturar i treure.",
        ],
        "soon_h": "Properament",
        "soon_p": "<strong>Aviat al Mac App Store.</strong> Mentrestant pots seguir les novetats de Stage Apps.",
        "icon_alt": "Icona de Stage Recorder",
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
        "blurb": "Enregistradora multipista senzilla (no és un DAW).",
        "detail": "Enregistra sessions multipista (p. ex. des d’una M32), exporta les pistes al teu DAW i una barreja estèreo WAV de referència. Properament al Mac App Store.",
    },
    "eu": {
        "meta": "Mac-erako multipista grabagailu sinplea: saioak grabatu (adib. M32/DN32) eta pistak edo estereo WAV erreferentzia esportatu.",
        "title": "Stage Recorder (macOS) — Stage Apps",
        "h1": "Stage Recorder (macOS)",
        "lead": "Stage Recorder ez da DAW bat izan nahi: Mac-erako multipista grabagailu sinplea da. Gero DAW-n editatzeko pistak lortzeko, edo L/R estereo WAV erreferentzia baterako.",
        "features_h": "Ezaugarriak",
        "features": [
            "Multipista grabaketa sinplea: sortu saioa, esleitu sarrerak eta grabatu.",
            "Kabinarako pentsatua: M32 / DN32 bezalako mahaien irteerak Mac-era grabatu.",
            "Esportatu pista indibidualak zure DAW-rako.",
            "Esportatu baita estereo WAV mix erreferentzia bat (L/R).",
            "Ez da DAW bat: nahasketa konplexurik edo edizio sakonik gabe — grabatu eta atera.",
        ],
        "soon_h": "Laster",
        "soon_p": "<strong>Laster Mac App Store-n.</strong> Bitartean, jarraitu Stage Apps-en berriak.",
        "icon_alt": "Stage Recorder ikonoa",
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
        "blurb": "Multipista grabagailu sinplea (ez da DAW bat).",
        "detail": "Grabatu multipista saioak (adib. M32 batetik), esportatu pistak zure DAW-ra eta erreferentziako estereo WAV mix bat. Laster Mac App Store-n.",
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
  <link rel="stylesheet" href="../css/styles.css?v=33">
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

    # Wire data-apps href + copy refresh
    for lang in LANGS:
        path = ROOT / f"docs/{lang}/index.html"
        text = path.read_text(encoding="utf-8")
        m = re.search(r'data-apps="([^"]+)"', text)
        apps = json.loads(htmlmod.unescape(m.group(1)))
        for app in apps:
            if app.get("name") == "Stage Recorder":
                app["href"] = HREF
                app["image"] = IMAGE
                app["soon"] = True
                app["blurb"] = COPY[lang]["blurb"]
                app["detail"] = COPY[lang]["detail"]
        encoded = htmlmod.escape(json.dumps(apps, ensure_ascii=False), quote=True)
        text = text[: m.start(1)] + encoded + text[m.end(1) :]
        text = text.replace("app-carousel.js?v=19", "app-carousel.js?v=20")
        text = text.replace("styles.css?v=32", "styles.css?v=33")
        text = text.replace("home-carousel.css?v=42", "home-carousel.css?v=43")
        path.write_text(text, encoding="utf-8")
        print("index", lang)

    # Nav after Transparent Screen
    nav_pat = re.compile(
        r'(<a href="transparent-screen\.html">Transparent Screen</a>)'
        r'(?!\s*\n?\s*<a href="stage-recorder\.html">)'
    )
    nav_count = 0
    for path in (ROOT / "docs").rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if 'href="transparent-screen.html">Transparent Screen</a>' not in text:
            continue
        if 'href="stage-recorder.html">Stage Recorder</a>' in text:
            continue
        new, n = nav_pat.subn(
            r'\1\n            <a href="stage-recorder.html">Stage Recorder</a>',
            text,
        )
        if n:
            path.write_text(new, encoding="utf-8")
            nav_count += n
    print("nav inserts", nav_count)

    # CSS for icon hero
    css_path = ROOT / "docs/css/styles.css"
    css = css_path.read_text(encoding="utf-8")
    if ".app-icon-hero" not in css:
        css += """

.app-icon-hero {
  display: flex;
  justify-content: center;
  margin: 0.5rem auto 1.25rem;
}

.app-icon-hero img {
  width: min(20rem, 72vw);
  height: auto;
  border-radius: 22%;
  border: 1px solid var(--border);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);
}
"""
        css_path.write_text(css, encoding="utf-8")
        print("css icon hero")

    # Allow soon apps to still link to their product page
    js_path = ROOT / "docs/js/app-carousel.js"
    js = js_path.read_text(encoding="utf-8")
    js = js.replace(
        "if (app.href && !app.soon) {\n        html +=",
        "if (app.href) {\n        html +=",
    )
    old_center = """      if (centerLink) {
        if (app.href && !app.soon) {
          centerLink.href = app.href;
          centerLink.setAttribute("aria-label", ui.open + " " + app.name);
          centerLink.removeAttribute("aria-disabled");
          centerLink.classList.remove("is-disabled");
          centerLink.tabIndex = 0;
        } else {
          centerLink.removeAttribute("href");
          centerLink.setAttribute("aria-disabled", "true");
          centerLink.classList.add("is-disabled");
          centerLink.tabIndex = -1;
          centerLink.setAttribute("aria-label", app.name + " (" + ui.soonAria + ")");
        }
      }"""
    new_center = """      if (centerLink) {
        if (app.href) {
          centerLink.href = app.href;
          centerLink.removeAttribute("aria-disabled");
          centerLink.classList.remove("is-disabled");
          centerLink.tabIndex = 0;
          if (app.soon) {
            centerLink.setAttribute("aria-label", app.name + " (" + ui.soonAria + ")");
          } else {
            centerLink.setAttribute("aria-label", ui.open + " " + app.name);
          }
        } else {
          centerLink.removeAttribute("href");
          centerLink.setAttribute("aria-disabled", "true");
          centerLink.classList.add("is-disabled");
          centerLink.tabIndex = -1;
          centerLink.setAttribute("aria-label", app.name + " (" + ui.soonAria + ")");
        }
      }"""
    if old_center not in js:
        raise SystemExit("centerLink block not found")
    js_path.write_text(js.replace(old_center, new_center), encoding="utf-8")
    print("js soon+href ok")
    print("DONE")


if __name__ == "__main__":
    main()
