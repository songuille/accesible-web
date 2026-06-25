#!/usr/bin/env python3
"""Generate stage-with-me-android-privacy.html for all locales."""
from pathlib import Path

FILE = "stage-with-me-android-privacy.html"
LANGS = ["es", "en", "fr", "de", "ca", "gl", "eu"]

CONTENT = {
    "es": {
        "lang": "es", "lang_name": "Español", "emoji": "🇪🇸",
        "title": "Privacidad — Stage With Me (Android)",
        "desc": "Política de privacidad de Stage With Me (StageWithMe) para Android: micrófono, voz sintética y almacenamiento de grabaciones.",
        "h1": "Privacidad — Stage With Me (Android)",
        "meta": "StageWithMe · aplicación de ensayo para Android",
        "nav_aria": "Principal", "lang_aria": "Selector de idioma",
        "footer_support": "Soporte", "footer_privacy": "Privacidad",
        "footer_disclaimer": "QLab es una marca de Figure 53. Este sitio y estas apps son productos independientes y no están afiliados, respaldados ni patrocinados por Figure 53.",
        "footer_made": "Software independiente · Santiago de Compostela",
        "body": """<h2>Alcance</h2>
<p>Esta política se aplica a la aplicación <strong>Stage With Me</strong> (también publicada como <strong>StageWithMe</strong>) para <strong>Android</strong>, desarrollada por Guillermo Vázquez. Describe el uso del <strong>micrófono</strong>, la <strong>voz sintética</strong> (réplicas de ensayo) y el <strong>almacenamiento de grabaciones de audio</strong> en tu dispositivo.</p>
<p>Para otras apps de Stage Apps, consulta la <a href="privacy.html">política general</a>.</p>
<h2>Resumen</h2>
<ul>
<li><strong>No vendemos</strong> tus datos personales ni el contenido de tus ensayos.</li>
<li><strong>No exigimos</strong> crear una cuenta para usar la app.</li>
<li><strong>No subimos</strong> tus grabaciones de voz ni tus textos a servidores del desarrollador.</li>
<li>No conservamos copias de tus guiones ni grabaciones en servidores del desarrollador; no hay periodo de retención en la nube.</li>
<li>Los datos de ensayo y los archivos de audio se guardan <strong>en tu dispositivo</strong>, salvo que tú decidas compartirlos.</li>
</ul>
<h2>Micrófono</h2>
<p>La app solicita permiso de <strong>micrófono</strong> para grabar tu voz durante las sesiones de ensayo. El audio se captura <strong>solo cuando inicias una grabación</strong> dentro de la app.</p>
<ul>
<li>No escuchamos el micrófono en segundo plano con fines ajenos al ensayo.</li>
<li>No enviamos el audio del micrófono a nuestros propios servidores.</li>
<li>Puedes denegar el permiso; no podrás grabar tu voz, pero otras funciones (p. ej. réplicas sintéticas) pueden seguir disponibles.</li>
</ul>
<h2>Voz sintética (réplicas)</h2>
<p>Para las réplicas de otros personajes, el texto se convierte en audio mediante el <strong>motor de voz del sistema</strong> en tu dispositivo (o componentes locales). El procesamiento ocurre <strong>en o desde tu dispositivo</strong>.</p>
<ul>
<li>No usamos tus grabaciones para entrenar modelos de voz ni de IA.</li>
<li>No recopilamos el contenido de tus guiones en nuestros servidores con fines publicitarios.</li>
</ul>
<h2>Almacenamiento de grabaciones</h2>
<p>En el <strong>almacenamiento local</strong> del dispositivo se guardan textos de ensayo, <strong>archivos de audio</strong> de las sesiones que grabas y metadatos (fecha, texto vinculado, etc.).</p>
<p>Puedes <strong>eliminar</strong> textos, sesiones y grabaciones desde la app. Al <strong>desinstalar</strong> la app, Android elimina los datos de la app en el dispositivo (salvo copias que exportes tú).</p>
<h2>Compartir grabaciones</h2>
<p>Si <strong>compartes</strong> una grabación, lo haces tú con el menú «Compartir» de Android hacia la app o contacto que elijas. No controlamos esas apps ni sus políticas.</p>
<h2>Permisos en Android</h2>
<ul>
<li><strong>Micrófono</strong> — grabar tu voz en ensayos.</li>
<li><strong>Almacenamiento / archivos</strong> — guardar, reproducir y exportar grabaciones en el dispositivo.</li>
</ul>
<p>Puedes revocar permisos en Ajustes → Apps → Stage With Me → Permisos.</p>
<h2>Servicios de terceros</h2>
<ul>
<li><strong>Google Play</strong> — distribución, actualizaciones y compras gestionadas por Google.</li>
<li>Sin SDK publicitarios de terceros ni seguimiento publicitario por parte del desarrollador.</li>
</ul>
<h2>Menores</h2>
<p>Puede usarse por estudiantes bajo supervisión de un adulto. No recopilamos datos de menores en servidores del desarrollador (no hay servicio de cuentas en línea).</p>
<h2>Eliminación de datos</h2>
<p>Puedes eliminar textos, sesiones y grabaciones desde la propia app. Si deseas solicitar la eliminación de todos los datos asociados a la aplicación o necesitas ayuda, escríbenos a <a href="mailto:songuille@icloud.com">songuille@icloud.com</a> con el asunto «Eliminación de datos — Stage With Me (Android)». Atenderemos tu solicitud en un plazo razonable.</p>
<p>Como los datos se almacenan en tu dispositivo y no en nuestros servidores, en la mayoría de los casos la forma más rápida de borrarlos por completo es desinstalar la app o eliminar el contenido desde la app.</p>
<h2>Cambios</h2>
<p>Podemos actualizar esta política. La fecha figura al final.</p>
<h2>Contacto</h2>
<p><strong>Guillermo Vázquez</strong><br>
<a href="mailto:songuille@icloud.com">songuille@icloud.com</a> · <a href="support.html">Soporte</a></p>
<p class="muted">Última actualización: mayo de 2026</p>""",
    },
    "en": {
        "lang": "en", "lang_name": "English", "emoji": "🇬🇧",
        "title": "Privacy — Stage With Me (Android)",
        "desc": "Privacy Policy for Stage With Me (StageWithMe) on Android: microphone, synthetic voice, and recording storage.",
        "h1": "Privacy — Stage With Me (Android)",
        "meta": "StageWithMe · rehearsal app for Android",
        "nav_aria": "Main", "lang_aria": "Language selector",
        "footer_support": "Support", "footer_privacy": "Privacy",
        "footer_disclaimer": "QLab is a trademark of Figure 53. This site and these apps are independent and are not affiliated with, endorsed by, or sponsored by Figure 53.",
        "footer_made": "Independent software · Santiago de Compostela, Spain",
        "body": """<h2>Scope</h2>
<p>This policy applies to <strong>Stage With Me</strong> (<strong>StageWithMe</strong>) for <strong>Android</strong>, by Guillermo Vázquez. It covers the <strong>microphone</strong>, <strong>synthetic voice</strong> (line prompts), and <strong>local storage of audio recordings</strong>.</p>
<p>For other Stage Apps products, see the <a href="privacy.html">general privacy policy</a>.</p>
<h2>Summary</h2>
<ul>
<li><strong>We do not sell</strong> your personal data or rehearsal content.</li>
<li><strong>No account</strong> is required.</li>
<li><strong>We do not upload</strong> recordings or scripts to developer servers.</li>
<li>We do not keep copies of your scripts or recordings on developer servers; there is no cloud retention period.</li>
<li>Data stays <strong>on your device</strong> unless you share it.</li>
</ul>
<h2>Microphone</h2>
<p><strong>Microphone</strong> permission records your voice during rehearsal sessions, only when you start a recording in the app.</p>
<ul>
<li>No background microphone use for unrelated purposes.</li>
<li>No upload of microphone audio to our servers.</li>
<li>You may deny permission; recording will be unavailable.</li>
</ul>
<h2>Synthetic voice</h2>
<p>Line prompts use your device’s <strong>system text-to-speech</strong> (or local components), on or from your device.</p>
<ul>
<li>We do not use your recordings to train voice or AI models.</li>
<li>No script collection on our servers for ad profiling.</li>
</ul>
<h2>Recording storage</h2>
<p><strong>Local storage</strong> holds scripts, <strong>audio files</strong>, and session metadata. You can <strong>delete</strong> them in the app. <strong>Uninstalling</strong> removes app data per Android rules.</p>
<h2>Sharing</h2>
<p>Sharing uses Android’s share sheet; we do not control third-party apps you choose.</p>
<h2>Android permissions</h2>
<ul>
<li><strong>Microphone</strong> — rehearsal recordings.</li>
<li><strong>Storage / files</strong> — save and play recordings.</li>
</ul>
<p>Revoke in Settings → Apps → Stage With Me → Permissions.</p>
<h2>Third parties</h2>
<ul>
<li><strong>Google Play</strong> — distribution and billing.</li>
<li>No third-party ad SDKs.</li>
</ul>
<h2>Children</h2>
<p>May be used by students under adult supervision. No knowingly collected children’s data on developer servers.</p>
<h2>Data deletion</h2>
<p>You can delete scripts, sessions, and recordings in the app. To request deletion of all data associated with the app or if you need assistance, email <a href="mailto:songuille@icloud.com">songuille@icloud.com</a> with the subject line “Data deletion — Stage With Me (Android)”. We will respond within a reasonable time.</p>
<p>Because data is stored on your device rather than on our servers, uninstalling the app or deleting content in the app is usually the fastest way to remove it completely.</p>
<h2>Changes</h2>
<p>We may update this policy; date below.</p>
<h2>Contact</h2>
<p><strong>Guillermo Vázquez</strong><br>
<a href="mailto:songuille@icloud.com">songuille@icloud.com</a> · <a href="support.html">Support</a></p>
<p class="muted">Last updated: May 2026</p>""",
    },
}

for code, name, emoji, title, desc, h1, meta, body, nav_aria, lang_aria, footer_support, footer_privacy, footer_made in [
    ("fr", "Français", "🇫🇷",
     "Confidentialité — Stage With Me (Android)",
     "Politique de confidentialité Stage With Me (StageWithMe) pour Android : microphone, voix de synthèse et stockage des enregistrements.",
     "Confidentialité — Stage With Me (Android)", "StageWithMe · application de répétition pour Android",
     """<h2>Champ d'application</h2>
<p>Cette politique s'applique à <strong>Stage With Me</strong> (<strong>StageWithMe</strong>) sur <strong>Android</strong>, par Guillermo Vázquez : <strong>microphone</strong>, <strong>voix de synthèse</strong> et <strong>stockage local des enregistrements audio</strong>.</p>
<p><a href="privacy.html">Politique générale</a> pour les autres produits Stage Apps.</p>
<h2>Résumé</h2>
<ul>
<li>Pas de vente de données. Pas de compte obligatoire. Pas d'envoi de vos enregistrements vers nos serveurs.</li>
<li>Nous ne conservons pas de copies de vos textes ni enregistrements sur nos serveurs ; il n'y a pas de période de conservation dans le cloud.</li>
<li>Données sur l'appareil, sauf partage explicite par vous.</li>
</ul>
<h2>Microphone</h2>
<p>Permission pour enregistrer votre voix pendant les répétitions, uniquement lorsque vous lancez un enregistrement dans l'app. Pas d'écoute en arrière-plan ni d'envoi vers nos serveurs.</p>
<h2>Voix de synthèse</h2>
<p>Répliques via la synthèse vocale du système sur l'appareil. Pas d'entraînement de modèles avec vos enregistrements.</p>
<h2>Stockage</h2>
<p>Textes, fichiers audio et métadonnées en stockage local. Suppression possible dans l'app ; la désinstallation supprime les données de l'app.</p>
<h2>Partage</h2>
<p>Partage via la feuille Android ; nous ne contrôlons pas les apps tierces choisies.</p>
<h2>Permissions Android</h2>
<p>Microphone ; stockage/fichiers. Révocables dans Paramètres → Applications → Stage With Me.</p>
<h2>Tiers</h2>
<p>Google Play pour la distribution. Pas de SDK publicitaires.</p>
<h2>Suppression des données</h2>
<p>Vous pouvez supprimer textes, sessions et enregistrements dans l’app. Pour demander la suppression de toutes les données associées à l’application, écrivez à <a href="mailto:songuille@icloud.com">songuille@icloud.com</a> avec l’objet « Suppression des données — Stage With Me (Android) ». Nous traiterons votre demande dans un délai raisonnable.</p>
<h2>Contact</h2>
<p><strong>Guillermo Vázquez</strong><br>
<a href="mailto:songuille@icloud.com">songuille@icloud.com</a> · <a href="support.html">Support</a></p>
<p class="muted">Dernière mise à jour : mai 2026</p>""",
     "Principal", "Sélecteur de langue", "Support", "Confidentialité",
     "Independent software · Santiago de Compostela, Spain"),
    ("de", "Deutsch", "🇩🇪",
     "Datenschutz — Stage With Me (Android)",
     "Datenschutzerklärung für Stage With Me (StageWithMe) auf Android: Mikrofon, synthetische Stimme und Speicherung von Aufnahmen.",
     "Datenschutz — Stage With Me (Android)", "StageWithMe · Proben-App für Android",
     """<h2>Geltungsbereich</h2>
<p>Diese Erklärung gilt für <strong>Stage With Me</strong> (<strong>StageWithMe</strong>) auf <strong>Android</strong> von Guillermo Vázquez: <strong>Mikrofon</strong>, <strong>synthetische Stimme</strong> und <strong>lokale Speicherung von Audioaufnahmen</strong>.</p>
<p><a href="privacy.html">Allgemeine Datenschutzerklärung</a> für andere Stage Apps.</p>
<h2>Kurzfassung</h2>
<ul>
<li>Kein Verkauf von Daten. Kein Konto erforderlich. Keine Uploads Ihrer Aufnahmen auf unsere Server.</li>
<li>Wir speichern keine Kopien Ihrer Texte oder Aufnahmen auf Entwickler-Servern; es gibt keine Aufbewahrungsfrist in der Cloud.</li>
<li>Daten auf dem Gerät, sofern Sie nicht teilen.</li>
</ul>
<h2>Mikrofon</h2>
<p>Berechtigung zum Aufnehmen Ihrer Stimme bei Proben, nur wenn Sie in der App eine Aufnahme starten.</p>
<h2>Synthetische Stimme</h2>
<p>Stichworte über System-Sprachausgabe auf dem Gerät. Kein Training von Modellen mit Ihren Aufnahmen.</p>
<h2>Speicherung</h2>
<p>Texte, Audiodateien und Metadaten lokal. Löschung in der App möglich; Deinstallation entfernt App-Daten.</p>
<h2>Teilen</h2>
<p>Teilen über Android — von Ihnen gewählte Drittanbieter-Apps.</p>
<h2>Android-Berechtigungen</h2>
<p>Mikrofon; Speicher/Dateien. Widerruf in Einstellungen → Apps → Stage With Me.</p>
<h2>Datenlöschung</h2>
<p>Sie können Texte, Sitzungen und Aufnahmen in der App löschen. Um die Löschung aller mit der App verbundenen Daten zu beantragen, schreiben Sie an <a href="mailto:songuille@icloud.com">songuille@icloud.com</a> mit dem Betreff „Datenlöschung — Stage With Me (Android)“. Wir bearbeiten Ihre Anfrage innerhalb einer angemessenen Frist.</p>
<h2>Kontakt</h2>
<p><strong>Guillermo Vázquez</strong><br>
<a href="mailto:songuille@icloud.com">songuille@icloud.com</a> · <a href="support.html">Support</a></p>
<p class="muted">Stand: Mai 2026</p>""",
     "Haupt", "Sprachauswahl", "Support", "Datenschutz",
     "Independent software · Santiago de Compostela, Spain"),
    ("ca", "Català", None,
     "Privacitat — Stage With Me (Android)",
     "Política de privacitat de Stage With Me (StageWithMe) per a Android: micròfon, veu sintètica i emmagatzematge de gravacions.",
     "Privacitat — Stage With Me (Android)", "StageWithMe · aplicació d'assaig per a Android",
     """<h2>Abast</h2>
<p>Aquesta política s'aplica a <strong>Stage With Me</strong> (<strong>StageWithMe</strong>) per a <strong>Android</strong>, de Guillermo Vázquez: <strong>micròfon</strong>, <strong>veu sintètica</strong> i <strong>emmagatzematge local de gravacions d'àudio</strong>.</p>
<p><a href="privacy.html">Política general</a> d'altres productes Stage Apps.</p>
<h2>Resum</h2>
<ul>
<li>No venem dades. No cal compte. No pujem gravacions als nostres servidors.</li>
<li>No conservem còpies dels teus guions ni gravacions als servidors del desenvolupador; no hi ha període de retenció al núvol.</li>
<li>Dades al dispositiu llevat que comparteixis explícitament.</li>
</ul>
<h2>Micròfon</h2>
<p>Permís per gravar la veu en assajos, només en iniciar una gravació a l'app.</p>
<h2>Veu sintètica</h2>
<p>Rèpliques mitjançant la veu del sistema al dispositiu.</p>
<h2>Emmagatzematge</h2>
<p>Textos, àudio i metadades en emmagatzematge local. Pots esborrar-los; en desinstal·lar s'eliminen les dades de l'app.</p>
<h2>Compartir</h2>
<p>Compartir via Android; no controlem apps de tercers.</p>
<h2>Supressió de dades</h2>
<p>Pots esborrar textos, sessions i gravacions des de l’app. Per sol·licitar l’eliminació de totes les dades associades a l’aplicació, escriu a <a href="mailto:songuille@icloud.com">songuille@icloud.com</a> amb l’assumpte «Supressió de dades — Stage With Me (Android)». Atendrem la sol·licitud en un termini raonable.</p>
<h2>Contacte</h2>
<p><strong>Guillermo Vázquez</strong><br>
<a href="mailto:songuille@icloud.com">songuille@icloud.com</a> · <a href="support.html">Suport</a></p>
<p class="muted">Última actualització: maig de 2026</p>""",
     "Principal", "Selector d'idioma", "Suport", "Privacitat",
     "Software independent · Santiago de Compostela"),
    ("gl", "Galego", None,
     "Privacidade — Stage With Me (Android)",
     "Política de privacidade de Stage With Me (StageWithMe) para Android: micrófono, voz sintética e almacenamento de gravacións.",
     "Privacidade — Stage With Me (Android)", "StageWithMe · aplicación de ensaio para Android",
     """<h2>Alcance</h2>
<p>Esta política aplícase a <strong>Stage With Me</strong> (<strong>StageWithMe</strong>) para <strong>Android</strong>, de Guillermo Vázquez: <strong>micrófono</strong>, <strong>voz sintética</strong> e <strong>almacenamento local de gravacións de audio</strong>.</p>
<p><a href="privacy.html">Política xeral</a> de outras Stage Apps.</p>
<h2>Resumo</h2>
<ul>
<li>Non vendemos datos. Sen conta obrigatoria. Non subimos gravacións aos nosos servidores.</li>
<li>Non conservamos copias dos teus guions nin gravacións nos servidores do desenvolvedor; non hai período de retención na nube.</li>
<li>Datos no dispositivo salvo que compartas.</li>
</ul>
<h2>Micrófono</h2>
<p>Permiso para gravar a túa voz nos ensaios, só ao iniciar unha gravación na app.</p>
<h2>Voz sintética</h2>
<p>Réplicas coa voz do sistema no dispositivo.</p>
<h2>Almacenamento</h2>
<p>Textos, audio e metadatos en almacenamento local. Podes borrar; ao desinstalar elimínase a datos da app.</p>
<h2>Compartir</h2>
<p>Compartir mediante Android; non controlamos terceiras apps.</p>
<h2>Eliminación de datos</h2>
<p>Podes eliminar textos, sesións e gravacións desde a app. Para solicitar a eliminación de todos os datos asociados á aplicación, escribe a <a href="mailto:songuille@icloud.com">songuille@icloud.com</a> co asunto «Eliminación de datos — Stage With Me (Android)». Atenderemos a solicitude nun prazo razoable.</p>
<h2>Contacto</h2>
<p><strong>Guillermo Vázquez</strong><br>
<a href="mailto:songuille@icloud.com">songuille@icloud.com</a> · <a href="support.html">Soporte</a></p>
<p class="muted">Última actualización: maio de 2026</p>""",
     "Principal", "Selector de idioma", "Soporte", "Privacidade",
     "Software independente · Santiago de Compostela"),
    ("eu", "Euskara", None,
     "Pribatutasuna — Stage With Me (Android)",
     "Stage With Me (StageWithMe) Android-erako pribatutasun politika: mikrofonoa, ahots sintetikoa eta grabazioen biltegiratzea.",
     "Pribatutasuna — Stage With Me (Android)", "StageWithMe · Android-erako entsegurako aplikazioa",
     """<h2>Eremua</h2>
<p>Politika hau <strong>Stage With Me</strong> (<strong>StageWithMe</strong>) <strong>Android</strong>-erako da, Guillermo Vázquezek egina: <strong>mikrofonoa</strong>, <strong>ahots sintetikoa</strong> eta <strong>audio-grabazioen biltegiratze lokala</strong>.</p>
<p>Beste Stage Apps produktuetarako: <a href="privacy.html">politika orokorra</a>.</p>
<h2>Laburpena</h2>
<ul>
<li>Ez ditugu zure datuak saltzen. Ez da konturik behar. Ez ditugu grabazioak igotzen gure zerbitzarietara.</li>
<li>Ez gordetzen ditugu zure testu edo grabazioen kopiak garatzailearen zerbitzarietan; ez dago hodeian atxikitzeko eperik.</li>
<li>Datuak gailuan, zuk partekatzen ez baduzu.</li>
</ul>
<h2>Mikrofonoa</h2>
<p>Baimena zure ahotsa entseguetan grabatzeko, aplikazioan grabazioa hasten duzunean soilik.</p>
<h2>Ahots sintetikoa</h2>
<p>Erreplikak gailuko sistemaren ahots sintetikoarekin.</p>
<h2>Biltegiratzea</h2>
<p>Testuak, audio fitxategiak eta metadatuak lokalki. Ezaba ditzakezu aplikaziotik.</p>
<h2>Partekatzea</h2>
<p>Android bidez partekatzen duzu; ez ditugu hirugarrenen aplikazioak kontrolatzen.</p>
<h2>Datuen ezabatzea</h2>
<p>Testuak, saioak eta grabazioak aplikaziotik ezaba ditzakezu. Aplikazioari lotutako datu guztiak ezabatzeko eskaera egiteko, idatzi <a href="mailto:songuille@icloud.com">songuille@icloud.com</a> helbidera «Datuen ezabatzea — Stage With Me (Android)» gaia jarrita. Eskaera arrazoizko epean erantzungo dugu.</p>
<h2>Harremana</h2>
<p><strong>Guillermo Vázquez</strong><br>
<a href="mailto:songuille@icloud.com">songuille@icloud.com</a> · <a href="support.html">Laguntza</a></p>
<p class="muted">Azken eguneraketa: 2026ko maiatza</p>""",
     "Nagusia", "Hizkuntza-hautatzailea", "Laguntza", "Pribatutasuna",
     "Independent software · Santiago de Compostela, Spain"),
]:
    CONTENT[code] = {
        "lang": code, "lang_name": name, "emoji": emoji,
        "title": title, "desc": desc, "h1": h1, "meta": meta,
        "nav_aria": nav_aria, "lang_aria": lang_aria,
        "footer_support": footer_support, "footer_privacy": footer_privacy,
        "footer_disclaimer": CONTENT["en"]["footer_disclaimer"],
        "footer_made": footer_made,
        "body": body,
    }

NAV_INDEX = {
    "es": "Inicio", "en": "Home", "fr": "Accueil", "de": "Start",
    "ca": "Inici", "gl": "Inicio", "eu": "Hasiera",
}
NAV_EXTRA = {
    "es": ("Comparativa", "Recursos", "Soporte"),
    "en": ("Compare", "Resources", "Support"),
    "fr": ("Comparatif", "Ressources", "Support"),
    "de": ("Vergleich", "Ressourcen", "Support"),
    "ca": ("Comparativa", "Recursos", "Suport"),
    "gl": ("Comparativa", "Recursos", "Soporte"),
    "eu": ("Konparaketa", "Baliabideak", "Laguntza"),
}
LABELS = {
    "es": "Español", "en": "English", "fr": "Français", "de": "Deutsch",
    "eu": "Euskara", "gl": "Galego", "ca": "Català",
}
EMOJIS = {"es": "🇪🇸", "en": "🇬🇧", "fr": "🇫🇷", "de": "🇩🇪"}
FLAGS = {"eu": "eu", "gl": "gl", "ca": "ca"}


def lang_menu(current):
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


def render_page(code):
    t = CONTENT[code]
    hreflangs = "\n".join(
        f'  <link rel="alternate" hreflang="{c}" href="../{c}/{FILE}">' for c in LANGS
    )
    n = NAV_EXTRA[code]
    if code in FLAGS:
        summary_inner = (
            f'<img class="lang-dropdown-flag" src="../assets/flags/{FLAGS[code]}.svg" alt="" decoding="async"> '
            f'<span class="lang-dropdown-label">{t["lang_name"]}</span>'
        )
    else:
        summary_inner = (
            f'<span class="lang-emoji" aria-hidden="true">{t["emoji"]}</span> '
            f'<span class="lang-dropdown-label">{t["lang_name"]}</span>'
        )
    return f"""<!DOCTYPE html>
<html lang="{t["lang"]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{t["desc"]}">
  <title>{t["title"]}</title>
{hreflangs}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css?v=11">
</head>
<body>
  <div class="page">
    <header class="site-header">
      <div class="wrap inner">
        <a class="logo" href="index.html"><img class="logo-mark" src="/assets/images/stageapps-mark.png?v=2" alt="" width="36" height="36" decoding="async"><span class="logo-text">StageApps</span></a>
        <div class="header-right">
          <nav class="nav" aria-label="{t["nav_aria"]}">
            <a href="index.html">{NAV_INDEX[code]}</a>
            <a href="stage-with-me.html">Stage With Me</a>
            <a href="compare.html">{n[0]}</a>
            <a href="resources.html">{n[1]}</a>
            <a href="faq.html">FAQ</a>
            <a href="support.html">{n[2]}</a>
          </nav>
          <div class="lang-dropdown" role="navigation" aria-label="{t["lang_aria"]}">
  <details>
    <summary>
      {summary_inner}
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
        <h1>{t["h1"]}</h1>
        <p class="meta">{t["meta"]}</p>
      </section>
      <section>
        <div class="wrap prose">
          {t["body"]}
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="wrap inner">
        <span>© <span id="y"></span> Stage Apps</span>
        <div class="links">
          <a href="support.html">{t["footer_support"]}</a>
          <a href="privacy.html">{t["footer_privacy"]}</a>
        </div>
      </div>
      <p class="wrap footer-disclaimer">{t["footer_disclaimer"]}</p>
      <p class="wrap footer-made-in">{t["footer_made"]}</p>
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


if __name__ == "__main__":
    root = Path(__file__).parent
    for code in LANGS:
        path = root / code / FILE
        path.write_text(render_page(code), encoding="utf-8")
        print("wrote", path)
