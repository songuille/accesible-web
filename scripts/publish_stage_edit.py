#!/usr/bin/env python3
"""Add Stage Edit (coming soon) to the Stage Apps site."""
import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "../assets/images/stage-edit-square-1080.png"
HREF = "stage-edit.html"
LANGS = ["es", "en", "fr", "de", "gl", "ca", "eu"]

COPY = {
    "es": {
        "meta": "Editor de dos pistas dual-mono para Mac: grabar, editar ondas y exportar sin un DAW completo.",
        "title": "Stage Edit (macOS) — Stage Apps",
        "h1": "Stage Edit (macOS)",
        "lead": "Stage Edit es un editor de dos pistas dual-mono para Mac: grabar, editar ondas y exportar sin la complejidad de un DAW completo.",
        "features_h": "Características",
        "features": [
            "Dos pistas dual-mono: ideal para escena, ensayo y podcast.",
            "Captura HAL (AUHAL) estable para tomas largas.",
            "Edición de onda: zoom, selección, cortar/copiar/pegar, fades, ganancia y normalizar.",
            "EQ, compresor y reducción de ruido offline; inserts Audio Unit por pista.",
            "Importa audio y exporta WAV o AIFF; proyectos .stageedit con autosave.",
        ],
        "soon_h": "Próximamente",
        "soon_p": "<strong>En breve en la Mac App Store.</strong> Mientras tanto puedes seguir las novedades de Stage Apps.",
        "icon_alt": "Icono de Stage Edit",
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
        "blurb": "Editor de 2 pistas dual-mono para Mac.",
        "detail": "Graba, edita ondas y exporta WAV/AIFF sin un DAW completo. Dos pistas dual-mono para Mac. Próximamente en la Mac App Store.",
        "compare_best": "Editar dos pistas dual-mono y exportar WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS · próximamente",
    },
    "en": {
        "meta": "Two-track dual-mono editor for Mac: record, edit waveforms and export without a full DAW.",
        "title": "Stage Edit (macOS) — Stage Apps",
        "h1": "Stage Edit (macOS)",
        "lead": "Stage Edit is a two-track dual-mono editor for Mac: record, edit waveforms and export without full DAW complexity.",
        "features_h": "Features",
        "features": [
            "Two dual-mono tracks: great for stage, rehearsal and podcasts.",
            "Stable HAL (AUHAL) capture for long takes.",
            "Waveform editing: zoom, selection, cut/copy/paste, fades, gain and normalize.",
            "Offline EQ, compressor and noise reduction; per-track Audio Unit inserts.",
            "Import audio and export WAV or AIFF; .stageedit projects with autosave.",
        ],
        "soon_h": "Coming soon",
        "soon_p": "<strong>Coming soon to the Mac App Store.</strong> Follow Stage Apps for updates.",
        "icon_alt": "Stage Edit icon",
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
        "blurb": "2-track dual-mono editor for Mac.",
        "detail": "Record, edit waveforms and export WAV/AIFF without a full DAW. Two dual-mono tracks for Mac. Coming soon to the Mac App Store.",
        "compare_best": "Edit two dual-mono tracks and export WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS · coming soon",
    },
    "fr": {
        "meta": "Éditeur deux pistes dual-mono pour Mac : enregistrer, éditer les formes d’onde et exporter sans un DAW complet.",
        "title": "Stage Edit (macOS) — Stage Apps",
        "h1": "Stage Edit (macOS)",
        "lead": "Stage Edit est un éditeur deux pistes dual-mono pour Mac : enregistrer, éditer les formes d’onde et exporter sans la complexité d’un DAW.",
        "features_h": "Fonctionnalités",
        "features": [
            "Deux pistes dual-mono : idéal pour la scène, les répétitions et le podcast.",
            "Capture HAL (AUHAL) stable pour les prises longues.",
            "Édition d’onde : zoom, sélection, couper/copier/coller, fades, gain et normalisation.",
            "EQ, compresseur et réduction de bruit hors ligne ; inserts Audio Unit par piste.",
            "Importez l’audio et exportez WAV ou AIFF ; projets .stageedit avec autosave.",
        ],
        "soon_h": "Bientôt",
        "soon_p": "<strong>Bientôt sur le Mac App Store.</strong> Suivez Stage Apps pour les nouveautés.",
        "icon_alt": "Icône Stage Edit",
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
        "blurb": "Éditeur 2 pistes dual-mono pour Mac.",
        "detail": "Enregistrez, éditez les formes d’onde et exportez WAV/AIFF sans un DAW complet. Deux pistes dual-mono pour Mac. Bientôt sur le Mac App Store.",
        "compare_best": "Éditer deux pistes dual-mono et exporter WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS · bientôt",
    },
    "de": {
        "meta": "Zwei-Spur Dual-Mono-Editor für den Mac: aufnehmen, Wellenform bearbeiten und exportieren ohne volles DAW.",
        "title": "Stage Edit (macOS) — Stage Apps",
        "h1": "Stage Edit (macOS)",
        "lead": "Stage Edit ist ein Zwei-Spur Dual-Mono-Editor für den Mac: aufnehmen, Wellenformen bearbeiten und exportieren ohne DAW-Komplexität.",
        "features_h": "Funktionen",
        "features": [
            "Zwei Dual-Mono-Spuren: ideal für Bühne, Probe und Podcast.",
            "Stabile HAL-(AUHAL)-Aufnahme für lange Takes.",
            "Wellenform-Editing: Zoom, Auswahl, Ausschneiden/Kopieren/Einfügen, Fades, Gain und Normalisieren.",
            "Offline-EQ, Kompressor und Rauschreduktion; Audio-Unit-Inserts pro Spur.",
            "Audio importieren und WAV oder AIFF exportieren; .stageedit-Projekte mit Autosave.",
        ],
        "soon_h": "Demnächst",
        "soon_p": "<strong>Demnächst im Mac App Store.</strong> Folgen Sie Stage Apps für Neuigkeiten.",
        "icon_alt": "Stage-Edit-Symbol",
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
        "blurb": "2-Spur Dual-Mono-Editor für den Mac.",
        "detail": "Aufnehmen, Wellenformen bearbeiten und WAV/AIFF exportieren ohne volles DAW. Zwei Dual-Mono-Spuren für den Mac. Demnächst im Mac App Store.",
        "compare_best": "Zwei Dual-Mono-Spuren bearbeiten und WAV/AIFF exportieren",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS · demnächst",
    },
    "gl": {
        "meta": "Editor de dúas pistas dual-mono para Mac: gravar, editar ondas e exportar sen un DAW completo.",
        "title": "Stage Edit (macOS) — Stage Apps",
        "h1": "Stage Edit (macOS)",
        "lead": "Stage Edit é un editor de dúas pistas dual-mono para Mac: gravar, editar ondas e exportar sen a complexidade dun DAW completo.",
        "features_h": "Características",
        "features": [
            "Dúas pistas dual-mono: ideal para escena, ensaio e podcast.",
            "Captura HAL (AUHAL) estábel para tomas longas.",
            "Edición de onda: zoom, selección, cortar/copiar/pegar, fades, gañancia e normalizar.",
            "EQ, compresor e redución de ruído offline; inserts Audio Unit por pista.",
            "Importa audio e exporta WAV ou AIFF; proxectos .stageedit con autosave.",
        ],
        "soon_h": "Proximamente",
        "soon_p": "<strong>En breve na Mac App Store.</strong> Mentres tanto podes seguir as novidades de Stage Apps.",
        "icon_alt": "Icona de Stage Edit",
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
        "blurb": "Editor de 2 pistas dual-mono para Mac.",
        "detail": "Grava, edita ondas e exporta WAV/AIFF sen un DAW completo. Dúas pistas dual-mono para Mac. Proximamente na Mac App Store.",
        "compare_best": "Editar dúas pistas dual-mono e exportar WAV/AIFF",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS · proximamente",
    },
    "ca": {
        "meta": "Editor de dues pistes dual-mono per a Mac: gravar, editar ones i exportar sense un DAW complet.",
        "title": "Stage Edit (macOS) — Stage Apps",
        "h1": "Stage Edit (macOS)",
        "lead": "Stage Edit és un editor de dues pistes dual-mono per a Mac: gravar, editar ones i exportar sense la complexitat d’un DAW complet.",
        "features_h": "Característiques",
        "features": [
            "Dues pistes dual-mono: ideal per a escena, assaig i podcast.",
            "Captura HAL (AUHAL) estable per a preses llargues.",
            "Edició d’ona: zoom, selecció, tallar/copiar/enganxar, fades, guany i normalitzar.",
            "EQ, compressor i reducció de soroll offline; inserts Audio Unit per pista.",
            "Importa àudio i exporta WAV o AIFF; projectes .stageedit amb autosave.",
        ],
        "soon_h": "Properament",
        "soon_p": "<strong>Aviat al Mac App Store.</strong> Mentrestant pots seguir les novetats de Stage Apps.",
        "icon_alt": "Icona de Stage Edit",
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
        "blurb": "Editor de 2 pistes dual-mono per a Mac.",
        "detail": "Grava, edita ones i exporta WAV/AIFF sense un DAW complet. Dues pistes dual-mono per a Mac. Properament al Mac App Store.",
        "compare_best": "Editar dues pistes dual-mono i exportar WAV/AIFF",
        "compare_proto": "Àudio / WAV · AIFF",
        "compare_plat": "macOS · properament",
    },
    "eu": {
        "meta": "Mac-erako bi pistako dual-mono editorea: grabatu, uhinak editatu eta esportatu DAW osorik gabe.",
        "title": "Stage Edit (macOS) — Stage Apps",
        "h1": "Stage Edit (macOS)",
        "lead": "Stage Edit Mac-erako bi pistako dual-mono editorea da: grabatu, uhinak editatu eta esportatu DAW osorik gabe.",
        "features_h": "Ezaugarriak",
        "features": [
            "Bi dual-mono pista: eszenarako, entseguetarako eta podcastetarako aproposa.",
            "HAL (AUHAL) captura egonkorra hartze luzeetarako.",
            "Uhin-edizioa: zoom, hautaketa, moztu/kopiatu/itsatsi, fades, gain eta normalizatu.",
            "EQ, konpresore eta zarata-murrizketa offline; Audio Unit insertak pistaka.",
            "Inportatu audioa eta esportatu WAV edo AIFF; .stageedit proiektuak autosave-rekin.",
        ],
        "soon_h": "Laster",
        "soon_p": "<strong>Laster Mac App Store-n.</strong> Bitartean, jarraitu Stage Apps-en berriak.",
        "icon_alt": "Stage Edit ikonoa",
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
        "blurb": "Mac-erako 2 pistako dual-mono editorea.",
        "detail": "Grabatu, editatu uhinak eta esportatu WAV/AIFF DAW osorik gabe. Bi dual-mono pista Mac-erako. Laster Mac App Store-n.",
        "compare_best": "Bi dual-mono pista editatu eta WAV/AIFF esportatu",
        "compare_proto": "Audio / WAV · AIFF",
        "compare_plat": "macOS · laster",
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
  <link rel="stylesheet" href="../css/styles.css?v=34">
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

    planet_btn = (
        f'<button type="button" class="app-orbit-planet" data-orbit-planet '
        f'aria-label="Stage Edit"><img src="{IMAGE}" alt=""></button>'
    )

    for lang in LANGS:
        path = ROOT / f"docs/{lang}/index.html"
        text = path.read_text(encoding="utf-8")
        m = re.search(r'data-apps="([^"]+)"', text)
        apps = json.loads(htmlmod.unescape(m.group(1)))
        if not any(a.get("name") == "Stage Edit" for a in apps):
            apps.append(
                {
                    "name": "Stage Edit",
                    "blurb": COPY[lang]["blurb"],
                    "detail": COPY[lang]["detail"],
                    "soon": True,
                    "image": IMAGE,
                    "href": HREF,
                }
            )
        else:
            for app in apps:
                if app.get("name") == "Stage Edit":
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

        if 'aria-label="Stage Edit"' not in text:
            marker = 'aria-label="Stage Recorder"'
            i = text.find(marker)
            if i < 0:
                raise SystemExit(f"no Stage Recorder planet {lang}")
            btn_end = text.find("</button>", i) + len("</button>")
            text = text[:btn_end] + "\n              " + planet_btn + text[btn_end:]

        text = text.replace(">1 / 9</p>", ">1 / 10</p>")
        text = text.replace("home-carousel.css?v=46", "home-carousel.css?v=47")
        text = text.replace("app-carousel.js?v=21", "app-carousel.js?v=22")
        text = text.replace("styles.css?v=33", "styles.css?v=34")
        path.write_text(text, encoding="utf-8")
        print("index", lang, "apps", len(apps))

        cpath = ROOT / f"docs/{lang}/compare.html"
        if cpath.exists():
            ctext = cpath.read_text(encoding="utf-8")
            if "<td>Stage Edit</td>" not in ctext:
                row = (
                    f'<tr><td>Stage Edit</td><td>{COPY[lang]["compare_best"]}</td>'
                    f'<td>{COPY[lang]["compare_proto"]}</td>'
                    f'<td>{COPY[lang]["compare_plat"]}</td></tr>'
                )
                ctext = ctext.replace("</tbody>", f"                {row}\n              </tbody>", 1)
                cpath.write_text(ctext, encoding="utf-8")
                print("compare", lang)

    nav_pat = re.compile(
        r'(<a href="stage-recorder\.html">Stage Recorder</a>)'
        r'(?!\s*\n?\s*<a href="stage-edit\.html">)'
    )
    nav_count = 0
    for path in (ROOT / "docs").rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if 'href="stage-recorder.html">Stage Recorder</a>' not in text:
            continue
        if 'href="stage-edit.html">Stage Edit</a>' in text:
            continue
        new, n = nav_pat.subn(
            r'\1\n            <a href="stage-edit.html">Stage Edit</a>',
            text,
        )
        if n:
            path.write_text(new, encoding="utf-8")
            nav_count += n
    print("nav inserts", nav_count)

    js_path = ROOT / "docs/js/app-carousel.js"
    js = js_path.read_text(encoding="utf-8")
    if 'app.name === "Stage Edit"' not in js:
        old = '''      } else if (app.name === "Stage Recorder") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Recorder"));
      } else {
        label.textContent = app.name;
      }'''
        new = '''      } else if (app.name === "Stage Recorder") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Recorder"));
      } else if (app.name === "Stage Edit") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Stage"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Edit"));
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
