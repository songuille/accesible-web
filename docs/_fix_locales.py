#!/usr/bin/env python3
"""One-off: fix mixed-language content in fr/de/eu/gl/ca Stage Apps pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Shared aria labels per locale (not Spanish)
ARIA = {
    "eu": {"nav": "Menu nagusia", "lang": "Hizkuntza-hautatzailea"},
    "ca": {"nav": "Navegació principal", "lang": "Selector d’idioma"},
    "gl": {"nav": "Navegación principal", "lang": "Selector de lingua"},
    "fr": {"nav": "Navigation principale", "lang": "Sélecteur de langue"},
    "de": {"nav": "Hauptnavigation", "lang": "Sprachauswahl"},
}

# App detail h2 title
H2_FEATURES = {
    "eu": "Ezaugarriak",
    "ca": "Característiques",
    "gl": "Características",
    "fr": "Fonctionnalités",
    "de": "Funktionen",
}

CONTENT = {
    "eu": {
        "compare_thead": '<tr><th>App</th><th>Onena honetarako</th><th>Protokoloak</th><th>Plataforma</th></tr>',
        "compare_rows": """                <tr><td>Accesible</td><td>Irisgarritasun zerbitzuak ikuskizunetan</td><td>OSC, HTTP/WebSocket</td><td>macOS</td></tr>
                <tr><td>Shutter PJ-OSC</td><td>Proiektorearen shutter eta energia automatizatuak</td><td>PJLink, OSC</td><td>macOS</td></tr>
                <tr><td>Shutter PJLINK</td><td>Proiektoreko urruneko kontrol eskuzkoa</td><td>PJLink</td><td>iOS</td></tr>
                <tr><td>MIDItoOSC</td><td>Nahasgailua eta show softwarearen arteko zubia</td><td>MIDI, OSC</td><td>macOS</td></tr>""",
        "use_h2": ("1. kasua", "2. kasua", "3. kasua"),
        "use_p": (
            "QLab-eko cue-ak erabili Accesible-n azpitituluak jartzeko eta Shutter PJ-OSC-rekin proiektorearen shutter ekintzak eszena aldaketetan.",
            "MIDItoOSC erabili nahasgailuko mugimenduetatik OSC aginduak sortzeko eta show softwarean audio snapshot-ak automatizatzeko.",
            "Shutter PJLINK erabili iOS-en eskuzko kontrol gisa, FOH-k macOS-en OSC automatizazioa martxan duen bitartean.",
        ),
        "res_h2a": "Konfigurazio azkarreko zerrenda",
        "res_li": (
            "Ahal denean IP finkoak esleitu proiektoreei eta nahasgailuko gailuei.",
            "OSC atak dokumentatu gailu eta aplikazio bakoitzeko.",
            "Cue kritikoetarako eskuzko babes-ekintzak prestatu.",
            "Sarearen portaera probatu show-karga errealarekin.",
        ),
        "res_h2b": "Gomendatutako lan-fluxua",
        "res_p": "Lehenik sortu cue-ak QLab-en edo zure kontrol softwarean, gero mapatu gailu-mailako ekintzak aplikazio bakoitzean eta balioztatu entseguan.",
        "faq": (
            ("QLab behar dute app guztiek?", "Ez. QLab ohikoa da antzerki-fluxuetan, baina app-ak OSC/PJLink/MIDI bateragarriak diren edozein fluxutan erabil daitezke."),
            ("Hainbat app aldi berean erabil ditzaket?", "Bai. Ohiko konfigurazioek irisgarritasuna, proiekzioa eta nahasgailu automatizazioa ekoizpen berean uztartzen dituzte."),
            ("Zein plataforma daude?", "Une honetan macOS eta iOS. Integrazio gehiago gehitu daitezke denborarekin."),
        ),
        "sup_meta": "Laguntza teknikoa, konfigurazio gida eta proiektu-galderak.",
        "sup_desc": "Laguntza teknikoa Stage Apps aplikazioetarako.",
        "sup_h2": "Zer sartu laguntza-eskaera batean",
        "sup_email_h2": "E-posta",
        "sup_li": (
            "App-aren izena eta bertsioa.",
            "macOS/iOS bertsioa eta hardware xehetasunak.",
            "Fluxu-kontextua (QLab, Resolume, nahasgailu eredua, proiektore eredua).",
            "Espero den portaera, benetako portaera eta berrezartzeko urratsak.",
        ),
        "priv_meta": "Stage Apps produktuen pribatutasun-informazioa.",
        "priv_intro": "Orrialde honek gure aplikazioetarako datuen tratamenduaren printzipio orokorrak deskribatzen ditu. Politika legal ofizial gisa erabili aurretik aholkularitza legalarekin berrikusi.",
        "priv_h2a": "Datuen tratamendua",
        "priv_pa": "Proiektuak eta konfigurazioak gailuan bertan kudeatzen dira nagusiki. Funtzio batzuek sare lokalekin edo hirugarrenen zerbitzuekin komunika daitezke erabiltzailearen konfigurazioaren arabera.",
        "priv_h2b": "Harpidetzak eta fakturazioa",
        "priv_pb": "Harpidetzak daudenean, fakturazioa eta kontu-kudeaketa Apple-k egiten ditu bere politikak arabera.",
        "priv_h2c": "Harremana",
        "shutter_osc": (
            "Shutter ireki/ixteko eta proiektorea piztu/itzaltzeko komandoak.",
            "Proiektore bat edo gehiago aukeratu ekintza berean.",
            "OSC jaso QLab, Resolume edo OSC igorle batetik.",
            "Ikuskizun zuzeneko proiekzio-fluxua automatizatzeko diseinatua.",
        ),
        "shutter_ios": (
            "Kontrol azkarra iPhone/iPad ukipen-interfacetik.",
            "Shutter PJ-OSC-rekin filosofia bera.",
            "OSC geruza gabe: botoi bidezko urruneko kontrol hutsa.",
            "Aretoan mugitzen diren teknikarientzat erabilgarria.",
        ),
        "midi": (
            "Nahasgailuaren parametroak irakurri, fader eta mute bezala.",
            "OSC komando errazak sortu QLab-era kopiatu edo arrastatzeko.",
            "Mix cue automatizatuen programazioa azkartu.",
            "Nahasgailu eredu gehiago gehitzeko prest dagoen arkitektura.",
        ),
        "footer_note": "QLab Figure 53-ren marka da. Webgune hau eta app hauek independenteak dira eta ez daude Figure 53-rekin lotuta edo babestuta.",
    },
    "ca": {
        "compare_thead": '<tr><th>App</th><th>Millor per a</th><th>Protocols</th><th>Plataforma</th></tr>',
        "compare_rows": """                <tr><td>Accesible</td><td>Serveis d’accessibilitat durant l’espectacle</td><td>OSC, HTTP/WebSocket</td><td>macOS</td></tr>
                <tr><td>Shutter PJ-OSC</td><td>Automatització del shutter i l’energia del projector</td><td>PJLink, OSC</td><td>macOS</td></tr>
                <tr><td>Shutter PJLINK</td><td>Control remot manual del projector</td><td>PJLink</td><td>iOS</td></tr>
                <tr><td>MIDItoOSC</td><td>Pont entre la mescla i el control de l’espectacle</td><td>MIDI, OSC</td><td>macOS</td></tr>""",
        "use_h2": ("Cas 1", "Cas 2", "Cas 3"),
        "use_p": (
            "Fes servir cues de QLab per llançar subtítols a Accesible i accions de shutter del projector amb Shutter PJ-OSC en els canvis d’escena.",
            "Fes servir MIDItoOSC per generar ordres OSC des dels moviments de la mescla i automatitzar snapshots d’àudio al programari de l’espectacle.",
            "Fes servir Shutter PJLINK a iOS com a control manual mentre la FOH manté l’automatització OSC a macOS.",
        ),
        "res_h2a": "Llista ràpida de configuració",
        "res_li": (
            "Assigna IPs fixes als projectors i dispositius de la mescla quan sigui possible.",
            "Documenta els ports OSC per equip i per aplicació.",
            "Prepara accions manuals de reserva per als cues crítics.",
            "Prova el comportament de la xarxa amb càrrega real d’espectacle.",
        ),
        "res_h2b": "Flux de treball recomanat",
        "res_p": "Primer construeix els cues a QLab o al teu programari de control, després mapeja les accions de dispositiu a cada app i valida-ho a l’assaig.",
        "faq": (
            ("Totes les apps requereixen QLab?", "No. QLab és habitual en fluxos de teatre, però les apps es poden utilitzar amb qualsevol flux compatible OSC/PJLink/MIDI."),
            ("Puc usar diverses apps alhora?", "Sí. Les configuracions típiques combinen accessibilitat, projecció i automatització de la mescla en la mateixa producció."),
            ("Quines plataformes cobreix?", "Actualment inclou macOS i iOS. Es poden afegir més integracions amb el temps."),
        ),
        "sup_meta": "Ajuda tècnica, guia de configuració i dubtes de projecte.",
        "sup_desc": "Informació de suport per a productes Stage Apps.",
        "sup_h2": "Què incloure en una sol·licitud de suport",
        "sup_email_h2": "Correu electrònic",
        "sup_li": (
            "Nom de l’app i versió.",
            "Versió de macOS/iOS i detalls del maquinari.",
            "Context del flux (QLab, Resolume, model de mescla, model de projector).",
            "Comportament esperat, comportament real i passos per reproduir.",
        ),
        "priv_meta": "Informació de privacitat per als productes Stage Apps.",
        "priv_intro": "Aquesta pàgina descriu principis generals de tractament de dades per a les nostres apps. Revisa-la amb assessorament legal abans d’usar-la com a política oficial.",
        "priv_h2a": "Tractament de dades",
        "priv_pa": "Els projectes i configuracions es gestionen principalment al dispositiu. Algunes funcions poden comunicar-se amb xarxes locals o serveis de tercers segons la configuració de l’usuari.",
        "priv_h2b": "Subscripcions i facturació",
        "priv_pb": "Quan hi ha subscripcions, la facturació i la gestió del compte les fa Apple segons les seves polítiques.",
        "priv_h2c": "Contacte",
        "shutter_osc": (
            "Envia ordres per obrir/tancar el shutter i encendre/apagar el projector.",
            "Selecciona un o diversos projectors en la mateixa acció.",
            "Rep OSC des de QLab, Resolume o qualsevol emissor OSC.",
            "Dissenyada per automatitzar el flux de projecció en espectacles en directe.",
        ),
        "shutter_ios": (
            "Control ràpid des de la interfície tàctil d’iPhone/iPad.",
            "La mateixa filosofia de control que Shutter PJ-OSC.",
            "Sense capa OSC: control remot només amb botons.",
            "Útil per a tècnics que es mouen per la sala.",
        ),
        "midi": (
            "Llegeix paràmetres de la mescla com faders i mute.",
            "Genera ordres OSC fàcils de copiar o arrossegar a QLab.",
            "Accelera la programació de cues de mescla automatitzats.",
            "Arquitectura preparada per ampliar més models de mescla.",
        ),
        "footer_note": "QLab és una marca comercial de Figure 53. Aquest lloc i aquestes apps són productes independents i no estan afiliats, avalats ni patrocinats per Figure 53.",
    },
    "gl": {
        "compare_thead": '<tr><th>App</th><th>Mellor para</th><th>Protocolos</th><th>Plataforma</th></tr>',
        "compare_rows": """                <tr><td>Accesible</td><td>Servizos de accesibilidade durante o espectáculo</td><td>OSC, HTTP/WebSocket</td><td>macOS</td></tr>
                <tr><td>Shutter PJ-OSC</td><td>Automatización do shutter e da enerxía do proxector</td><td>PJLink, OSC</td><td>macOS</td></tr>
                <tr><td>Shutter PJLINK</td><td>Control remoto manual do proxector</td><td>PJLink</td><td>iOS</td></tr>
                <tr><td>MIDItoOSC</td><td>Ponte entre a mesa de mestura e o control do show</td><td>MIDI, OSC</td><td>macOS</td></tr>""",
        "use_h2": ("Primeiro caso", "Segundo caso", "Terceiro caso"),
        "use_p": (
            "Emprega os cues de QLab para subtítulos en Accesible e accións de obturador do proxector con Shutter PJ-OSC nos trocos de escena.",
            "Emprega MIDItoOSC para xerar comandos OSC a partir dos movementos da mesa e automatizar instantáneas de audio no software do espectáculo.",
            "Emprega Shutter PJLINK en iOS como control manual mentres a FOH mantén a automatización OSC en macOS.",
        ),
        "res_h2a": "Lista rápida de configuración",
        "res_li": (
            "Asigna IPs fixas a proxectores e dispositivos da mesa cando sexa posible.",
            "Documenta os portos OSC por equipo e por app.",
            "Prepara accións manuais de respaldo para cues críticos.",
            "Proba o comportamento da rede con carga real de show.",
        ),
        "res_h2b": "Fluxo de traballo recomendado",
        "res_p": "Primeiro constrúe os cues en QLab ou no teu software de control, despois mapea as accións de dispositivo en cada app e valídao no ensaio.",
        "faq": (
            ("Todas as apps requiren QLab?", "Non. QLab é habitual en fluxos de teatro, pero as apps pódense usar con calquera fluxo compatible OSC/PJLink/MIDI."),
            ("Podo usar varias apps á vez?", "Si. As configuracións típicas combinan accesibilidade, proxección e automatización da mesma na mesma produción."),
            ("Que plataformas cubre?", "Actualmente inclúe macOS e iOS. Pódense engadir máis integracións co tempo."),
        ),
        "sup_meta": "Axuda técnica, guía de configuración e dúbidas de proxecto.",
        "sup_desc": "Información de soporte para produtos Stage Apps.",
        "sup_h2": "Que incluír nunha solicitude de soporte",
        "sup_email_h2": "Correo electrónico",
        "sup_li": (
            "Nome da app e versión.",
            "Versión de macOS/iOS e detalles do hardware.",
            "Contexto de fluxo (QLab, Resolume, modelo de mesa, modelo de proxector).",
            "Comportamento esperado, comportamento real e pasos para reproducir.",
        ),
        "priv_meta": "Información de privacidade para produtos Stage Apps.",
        "priv_intro": "Esta páxina describe principios xerais de tratamento de datos para as nosas apps. Revísa cun asesoramento legal antes de usala como política oficial.",
        "priv_h2a": "Tratamento de datos",
        "priv_pa": "Os proxectos e configuracións xestionanse principalmente no dispositivo. Algunhas funcións poden comunicarse con redes locais ou servizos de terceiros segundo a configuración do usuario.",
        "priv_h2b": "Subscricións e facturación",
        "priv_pb": "Cando existan subscricións, a facturación e a xestión de conta faina Apple segundo as súas políticas.",
        "priv_h2c": "Contacto",
        "shutter_osc": (
            "Envía ordes para abrir/pechar o shutter e acender/apagar o proxector.",
            "Selecciona un ou varios proxectores na mesma acción.",
            "Recibe OSC desde QLab, Resolume ou calquera emisor OSC.",
            "Deseñada para automatizar o fluxo de proxección en shows en vivo.",
        ),
        "shutter_ios": (
            "Control rápido desde a interface táctil de iPhone/iPad.",
            "A mesma filosofía de control que Shutter PJ-OSC.",
            "Sen capa OSC: control remoto só con botóns.",
            "Útil para técnicos que se moven polo recinto.",
        ),
        "midi": (
            "Le parámetros da mesa como faders e mutes.",
            "Xera comandos OSC fáciles de copiar ou arrastrar a QLab.",
            "Acelera a programación de cues automatizados de mestura.",
            "Arquitectura preparada para ampliar máis modelos de mesa.",
        ),
        "footer_note": "QLab é unha marca de Figure 53. Este sitio e estas apps son independentes e non están afiliados, respaldados nin patrocinados por Figure 53.",
    },
    "fr": {
        "compare_thead": '<tr><th>App</th><th>Idéal pour</th><th>Protocoles</th><th>Plateforme</th></tr>',
        "compare_rows": """                <tr><td>Accesible</td><td>Services d’accessibilité pendant le spectacle</td><td>OSC, HTTP/WebSocket</td><td>macOS</td></tr>
                <tr><td>Shutter PJ-OSC</td><td>Automatisation du volet et de l’alimentation du projeteur</td><td>PJLink, OSC</td><td>macOS</td></tr>
                <tr><td>Shutter PJLINK</td><td>Contrôle à distance manuel du projeteur</td><td>PJLink</td><td>iOS</td></tr>
                <tr><td>MIDItoOSC</td><td>Pont entre la console et le logiciel de spectacle</td><td>MIDI, OSC</td><td>macOS</td></tr>""",
        "use_h2": ("Cas 1", "Cas 2", "Cas 3"),
        "use_p": (
            "Utilisez les cues QLab pour déclencher les sous-titres dans Accesible et les actions d’obturateur avec Shutter PJ-OSC lors des changements de scène.",
            "Utilisez MIDItoOSC pour générer des commandes OSC à partir des mouvements de console et automatiser les snapshots audio dans le logiciel de spectacle.",
            "Utilisez Shutter PJLINK sur iOS comme contrôle manuel pendant que la FOH garde l’automatisation OSC sur macOS.",
        ),
        "res_h2a": "Liste de contrôle rapide",
        "res_li": (
            "Attribuez des IP fixes aux projecteurs et à la console lorsque c’est possible.",
            "Documentez les ports OSC par machine et par application.",
            "Préparez des actions manuelles de secours pour les cues critiques.",
            "Testez le réseau sous charge réelle de spectacle.",
        ),
        "res_h2b": "Flux de travail recommandé",
        "res_p": "Construisez d’abord les cues dans QLab ou votre logiciel de contrôle, puis mappez les actions matérielles dans chaque app et validez en répétition.",
        "faq": (
            ("Toutes les apps exigent-elles QLab ?", "Non. QLab est courant en théâtre, mais les apps fonctionnent avec tout flux compatible OSC/PJLink/MIDI."),
            ("Puis-je utiliser plusieurs apps à la fois ?", "Oui. Les configurations typiques combinent accessibilité, projection et automatisation de console en une même production."),
            ("Quelles plateformes sont couvertes ?", "Actuellement macOS et iOS. D’autres intégrations peuvent être ajoutées."),
        ),
        "sup_meta": "Aide technique, guide de configuration et questions projet.",
        "sup_desc": "Support et aide technique pour Stage Apps.",
        "sup_h2": "Que inclure dans une demande de support",
        "sup_email_h2": "Courriel",
        "sup_li": (
            "Nom de l’app et version.",
            "Version macOS/iOS et détails matériels.",
            "Contexte de flux (QLab, Resolume, modèle de console, modèle de projecteur).",
            "Comportement attendu, comportement réel et étapes de reproduction.",
        ),
        "priv_meta": "Informations de confidentialité pour les produits Stage Apps.",
        "priv_intro": "Cette page décrit les principes généraux de traitement des données pour nos apps. Faites-la relire par un conseil juridique avant toute politique officielle.",
        "priv_h2a": "Traitement des données",
        "priv_pa": "Les projets et configurations sont gérés principalement sur l’appareil. Certaines fonctions peuvent communiquer avec des réseaux locaux ou des services tiers selon la configuration.",
        "priv_h2b": "Abonnements et facturation",
        "priv_pb": "Lorsqu’il existe des abonnements, la facturation et le compte sont gérés par Apple selon ses politiques.",
        "priv_h2c": "Contact",
        "shutter_osc": (
            "Déclenchez les commandes d’ouverture/fermeture du volet et marche/arrêt du projecteur.",
            "Sélectionnez un ou plusieurs projecteurs dans la même action.",
            "Recevez l’OSC depuis QLab, Resolume ou tout émetteur OSC.",
            "Conçue pour automatiser le flux de projection en spectacle vivant.",
        ),
        "shutter_ios": (
            "Contrôle rapide depuis l’interface tactile iPhone/iPad.",
            "Même philosophie que Shutter PJ-OSC.",
            "Sans couche OSC : télécommande pure par boutons.",
            "Utile pour les techniciens en déplacement dans la salle.",
        ),
        "midi": (
            "Lit les paramètres du mélangeur (faders, mutes, etc.).",
            "Génère des commandes OSC faciles à copier ou glisser vers QLab.",
            "Accélère la programmation des cues de mix automatisés.",
            "Architecture prête à étendre d’autres modèles de consoles.",
        ),
        "footer_note": "QLab est une marque de Figure 53. Ce site et ces apps sont indépendants et ne sont ni affiliés, ni approuvés, ni sponsorisés par Figure 53.",
    },
    "de": {
        "compare_thead": '<tr><th>App</th><th>Am besten für</th><th>Protokolle</th><th>Plattform</th></tr>',
        "compare_rows": """                <tr><td>Accesible</td><td>Barrierefreiheit während der Show</td><td>OSC, HTTP/WebSocket</td><td>macOS</td></tr>
                <tr><td>Shutter PJ-OSC</td><td>Automatisierung von Shutter und Stromversorgung des Projektors</td><td>PJLink, OSC</td><td>macOS</td></tr>
                <tr><td>Shutter PJLINK</td><td>Manuelle Fernsteuerung des Projektors</td><td>PJLink</td><td>iOS</td></tr>
                <tr><td>MIDItoOSC</td><td>Brücke zwischen Mixer und Show-Steuerung</td><td>MIDI, OSC</td><td>macOS</td></tr>""",
        "use_h2": ("Fall 1", "Fall 2", "Fall 3"),
        "use_p": (
            "QLab-Cues nutzen, um Untertitel in Accesible auszulösen und Shutter-Aktionen mit Shutter PJ-OSC bei Szenenwechseln.",
            "MIDItoOSC nutzen, um OSC-Befehle aus Mixer-Bewegungen zu erzeugen und Audio-Snapshots in der Show-Software zu automatisieren.",
            "Shutter PJLINK auf iOS als manuelle Steuerung nutzen, während FOH die OSC-Automatisierung auf macOS läuft.",
        ),
        "res_h2a": "Schnelle Checkliste",
        "res_li": (
            "Wo möglich feste IPs für Projektoren und Mixer-Geräte vergeben.",
            "OSC-Ports pro Gerät und App dokumentieren.",
            "Manuelle Fallback-Aktionen für kritische Cues vorbereiten.",
            "Netzwerk unter realer Show-Last testen.",
        ),
        "res_h2b": "Empfohlener Workflow",
        "res_p": "Zuerst Cues in QLab oder in Ihrer Steuer-Software erstellen, dann Geräteaktionen in jeder App mappen und in der Probe validieren.",
        "faq": (
            ("Benötigen alle Apps QLab?", "Nein. QLab ist im Theater üblich, aber die Apps funktionieren mit jedem OSC/PJLink/MIDI-kompatiblen Workflow."),
            ("Kann ich mehrere Apps gleichzeitig nutzen?", "Ja. Typische Setups kombinieren Barrierefreiheit, Projektion und Mixer-Automatisierung in einer Produktion."),
            ("Welche Plattformen?", "Aktuell macOS und iOS. Weitere Integrationen können folgen."),
        ),
        "sup_meta": "Technische Hilfe, Einrichtungsanleitung und Projektfragen.",
        "sup_desc": "Support und technische Hilfe für Stage Apps.",
        "sup_h2": "Was in eine Support-Anfrage gehört",
        "sup_email_h2": "E-Mail",
        "sup_li": (
            "App-Name und Version.",
            "macOS/iOS-Version und Hardware-Details.",
            "Workflow-Kontext (QLab, Resolume, Mixer-Modell, Projektor-Modell).",
            "Erwartetes Verhalten, tatsächliches Verhalten und Reproduktionsschritte.",
        ),
        "priv_meta": "Datenschutzhinweise für Stage-Apps-Produkte.",
        "priv_intro": "Diese Seite beschreibt allgemeine Grundsätze zur Datenverarbeitung für unsere Apps. Bitte mit rechtlicher Beratung prüfen, bevor Sie sie als offizielle Richtlinie veröffentlichen.",
        "priv_h2a": "Datenverarbeitung",
        "priv_pa": "Projekte und Konfigurationen werden primär auf dem Gerät verarbeitet. Einige Funktionen können je nach Nutzerkonfiguration mit lokalen Netzwerken oder Drittanbietern kommunizieren.",
        "priv_h2b": "Abonnements und Abrechnung",
        "priv_pb": "Wenn Abonnements vorhanden sind, erfolgen Abrechnung und Kontoverwaltung über Apple gemäß dessen Richtlinien.",
        "priv_h2c": "Kontakt",
        "shutter_osc": (
            "Befehle zum Öffnen/Schließen des Shutters und Ein-/Ausschalten des Projektors.",
            "Einen oder mehrere Projektoren in derselben Aktion auswählen.",
            "OSC von QLab, Resolume oder jedem OSC-Sender empfangen.",
            "Entwickelt, um den Projektionsablauf in Live-Shows zu automatisieren.",
        ),
        "shutter_ios": (
            "Schnelle Steuerung über die iPhone/iPad-Touch-Oberfläche.",
            "Gleiche Steuerphilosophie wie Shutter PJ-OSC.",
            "Ohne OSC-Schicht: reine Fernbedienung per Tasten.",
            "Nützlich für Techniker, die sich im Raum bewegen.",
        ),
        "midi": (
            "Mixer-Parameter wie Fader und Mutes lesen.",
            "Einfache OSC-Befehle erzeugen, die kopiert oder nach QLab gezogen werden können.",
            "Programmierung automatisierter Mix-Cues beschleunigen.",
            "Architektur für weitere Mixer-Modelle erweiterbar.",
        ),
        "footer_note": "QLab ist eine Marke von Figure 53. Diese Website und diese Apps sind unabhängig und nicht mit Figure 53 verbunden, von ihr unterstützt oder gesponsert.",
    },
}


def patch_common_headers(html: str, lang: str) -> str:
    a = ARIA[lang]
    html = html.replace('aria-label="Principal"', f'aria-label="{a["nav"]}"')
    html = html.replace('aria-label="Selector de idioma"', f'aria-label="{a["lang"]}"')
    # leftover English nav label from mixed edits
    html = html.replace('aria-label="Main"', f'aria-label="{a["nav"]}"')
    return html


def replace_between(html: str, start: str, end: str, new_body: str) -> str:
    i = html.find(start)
    j = html.find(end, i)
    if i == -1 or j == -1:
        return html
    return html[: i + len(start)] + "\n" + new_body + "\n" + html[j:]


def fix_compare(path: Path, lang: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    html = re.sub(
        r"<thead>\s*<tr>.*?</tr>\s*</thead>",
        f"<thead>\n              {c['compare_thead']}\n              </thead>",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r"<tbody>\s*.*?</tbody>",
        f"<tbody>\n{c['compare_rows']}\n              </tbody>",
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def fix_use_cases(path: Path, lang: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    block = f"""          <h2>{c['use_h2'][0]}</h2>
          <p>{c['use_p'][0]}</p>
          <h2>{c['use_h2'][1]}</h2>
          <p>{c['use_p'][1]}</p>
          <h2>{c['use_h2'][2]}</h2>
          <p>{c['use_p'][2]}</p>"""
    html = re.sub(
        r"<div class=\"wrap prose\">\s*.*?</div>\s*</section>",
        f'<div class="wrap prose">\n{block}\n        </div>\n      </section>',
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def fix_resources(path: Path, lang: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    lis = "\n".join(f"            <li>{x}</li>" for x in c["res_li"])
    block = f"""          <h2>{c['res_h2a']}</h2>
          <ul>
{lis}
          </ul>
          <h2>{c['res_h2b']}</h2>
          <p>{c['res_p']}</p>"""
    html = re.sub(
        r"<div class=\"wrap prose\">\s*.*?</div>\s*</section>",
        f'<div class="wrap prose">\n{block}\n        </div>\n      </section>',
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def fix_faq(path: Path, lang: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    qas = "\n".join(
        f"          <h2>{q}</h2>\n          <p>{a}</p>" for q, a in c["faq"]
    )
    block = f"""<div class="wrap prose">
{qas}
        </div>"""
    html = re.sub(
        r"<div class=\"wrap prose\">\s*.*?</div>\s*</section>",
        block + "\n      </section>",
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def fix_support(path: Path, lang: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    # meta description
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{c["sup_desc"]}">',
        html,
        count=1,
    )
    lis = "\n".join(f"            <li>{x}</li>" for x in c["sup_li"])
    h1 = {"eu": "Laguntza", "ca": "Suport", "gl": "Soporte", "fr": "Support", "de": "Support"}[lang]
    block = f"""      <section class="page-hero wrap">
        <h1>{h1}</h1>
        <p class="meta">{c['sup_meta']}</p>
      </section>
      <section>
        <div class="wrap prose">
          <h2>{c.get('sup_email_h2', 'Email')}</h2>
          <p><a href="mailto:songuille@icloud.com">songuille@icloud.com</a></p>
          <h2>{c['sup_h2']}</h2>
          <ul>
{lis}
          </ul>
        </div>
      </section>"""
    html = re.sub(
        r"<main>\s*.*?</main>",
        f"<main>\n{block}\n    </main>",
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def fix_privacy(path: Path, lang: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{c["priv_meta"]}">',
        html,
        count=1,
    )
    h1 = {"eu": "Pribatutasuna", "ca": "Privacitat", "gl": "Privacidade", "fr": "Confidentialité", "de": "Datenschutz"}[lang]
    block = f"""      <section class="page-hero wrap">
        <h1>{h1}</h1>
        <p class="meta">{c['priv_meta'].split('.')[0]}.</p>
      </section>
      <section>
        <div class="wrap prose">
          <p>{c['priv_intro']}</p>
          <h2>{c['priv_h2a']}</h2>
          <p>{c['priv_pa']}</p>
          <h2>{c['priv_h2b']}</h2>
          <p>{c['priv_pb']}</p>
          <h2>{c['priv_h2c']}</h2>
          <p><a href="mailto:songuille@icloud.com">songuille@icloud.com</a></p>
        </div>
      </section>"""
    html = re.sub(
        r"<main>\s*.*?</main>",
        f"<main>\n{block}\n    </main>",
        html,
        count=1,
        flags=re.S,
    )
    # footer disclaimer
    html = re.sub(
        r'<p class="wrap footer-disclaimer">.*?</p>',
        f'<p class="wrap footer-disclaimer">{c["footer_note"]}</p>',
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def fix_app_page(path: Path, lang: str, kind: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    h2 = H2_FEATURES[lang]
    if kind == "osc":
        bullets = c["shutter_osc"]
    elif kind == "ios":
        bullets = c["shutter_ios"]
    else:
        bullets = c["midi"]
    lis = "\n".join(f"            <li>{b}</li>" for b in bullets)
    html = re.sub(
        r"<h2>.*?</h2>\s*<ul>.*?</ul>",
        f"<h2>{h2}</h2>\n          <ul>\n{lis}\n          </ul>",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'<p class="wrap footer-disclaimer">.*?</p>',
        f'<p class="wrap footer-disclaimer">{c["footer_note"]}</p>',
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def fix_index_footer(path: Path, lang: str) -> None:
    c = CONTENT[lang]
    html = path.read_text(encoding="utf-8")
    html = patch_common_headers(html, lang)
    html = re.sub(
        r'<p class="wrap footer-disclaimer">.*?</p>',
        f'<p class="wrap footer-disclaimer">{c["footer_note"]}</p>',
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")


def main():
    for lang in ("eu", "ca", "gl", "fr", "de"):
        d = ROOT / lang
        fix_compare(d / "compare.html", lang)
        fix_use_cases(d / "use-cases.html", lang)
        fix_resources(d / "resources.html", lang)
        fix_faq(d / "faq.html", lang)
        fix_support(d / "support.html", lang)
        fix_privacy(d / "privacy.html", lang)
        fix_app_page(d / "shutter-pj-osc.html", lang, "osc")
        fix_app_page(d / "shutter-pjlink-ios.html", lang, "ios")
        fix_app_page(d / "miditoosc.html", lang, "midi")
        fix_index_footer(d / "index.html", lang)
        # other pages with footer: compare, use-cases, resources, faq, support already; compare footer
        for name in ("compare.html", "use-cases.html", "resources.html", "faq.html"):
            p = d / name
            t = p.read_text(encoding="utf-8")
            t = re.sub(
                r'<p class="wrap footer-disclaimer">.*?</p>',
                f'<p class="wrap footer-disclaimer">{CONTENT[lang]["footer_note"]}</p>',
                t,
                count=1,
                flags=re.S,
            )
            p.write_text(t, encoding="utf-8")

    # accesible pages: only aria
    for lang in ("eu", "ca", "gl", "fr", "de"):
        p = ROOT / lang / "accesible.html"
        t = p.read_text(encoding="utf-8")
        t = patch_common_headers(t, lang)
        p.write_text(t, encoding="utf-8")

    print("done")


if __name__ == "__main__":
    main()
