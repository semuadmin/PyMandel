"""
DEUTSCHE Sprachzeichenfolgenliterale für die PyMandel tkinter-Anwendung

Erstellt am 22. April 2020

@author: semuadmin
"""

# pylint: disable=line-too-long

WIKIURL = "https://de.wikipedia.org/wiki/Mandelbrot-Menge"
GITHUBURL = "https://github.com/semuconsulting/PyMandel"
CETURL = "https://github.com/holoviz/colorcet/blob/master/LICENSE.txt"
MODULENAME = "pymandel"

COPYRIGHTTXT = (
    "\u00a9 semuadmin (Steve Smith) 2020\nGPLv3 lizenz. Alle Rechte vorbehalten"
)

COLORCETTXT = "HoloViz Colorcet-Farbkarten verfügbar unter der Lizenz\nCreative Commons Attribution (CC_BY)"

INTROTXT = "Willkommen bei PyMandel! Verwenden Sie das Mausrad oder klicken Sie mit der linken Maustaste, um zu zoomen, und klicken Sie mit der rechten Maustaste, um zu zentrieren."

HELPTXT = (
    "Geben Sie die Einstellungen manuell ein (oder importieren Sie sie aus einer Metadatendatei) und klicken Sie auf ZEICHNEN, um ein Fraktalbild mit den angegebenen Parametern zu erstellen.\n\n"
    + "Verwenden Sie das Mausrad, um an der aktuellen Cursorposition hinein- und herauszuzoomen.\n"
    + "Klicken Sie mit der linken Maustaste, ziehen Sie sie und lassen Sie sie los - zoomen Sie in einen gezeichneten rechteckigen Bereich.\n"
    + "Linksklick - Vergrößern Sie die Cursorposition um den Betrag des Zoominkrements.\n"
    + "Umschalt & Linksklick - Verkleinern.\n"
    + "Drücken Sie im Julia-Modus nach links \u25c0 oder rechts \u25b6, um das Julia-Set um seinen Ursprung zu drehen.\n\n"
    + "ZEICHNEN-Taste - Plotten Sie das Bild mit den aktuellen Einstellungen.\n"
    + "Abbrechen-Schaltfläche - Bricht den aktuellen Plotvorgang ab.\n"
    + "Reset-Taste - Setzt die Parameter auf die Standardwerte zurück.\n"
    + "Speichern - Speichern Sie das aktuell angezeigte Bild als PNG-Datei zusammen mit den zugehörigen Metadaten als JSON-Datei.\n\n"
    + "Zoom-Schaltfläche - Erstellt automatisch eine Folge von Zoom-Bildern.\n"
    + "Drehknopf - Erstellt automatisch eine Folge von 'sich drehenden' Julia-Bildern.\n\n"
    + "Datei..Exporteinstellungen - Aktuelle Einstellungen (Metadaten) exportieren.\n"
    + "Datei..Importeinstellungen - Importieren Sie zuvor gespeicherte Metadaten.\n"
    + "Optionen..Einstellungen ein- / ausblenden - Schaltet das Einstellungsfeld ein oder aus.\n"
    + "Optionen..Status ein- / ausblenden - Schaltet die Statusleiste ein oder aus.\n"
    + "Hilfe..Anleitung - Zeigen Sie diesen Dialog an.\n"
    + "Hilfe..Über - Dialogfeld Info anzeigen"
)

ABOUTTXT = (
    "PyMandel ist eine kostenlose Open-Source-GUI-Anwendung, die vollständig in Python und tkinter mit Numba-Leistungsverbesserungen geschrieben wurde.\n\n"
    + "Anweisungen und Quellcode sind auf Github unter dem folgenden Link verfügbar."
)

# Nachrichtentext
JITTXT = "NUR FÜR DEN ERSTEN GEBRAUCH: Bitte warten Sie auf JIT Compilation and Caching"
SETINITTXT = "Einstellungen initialisiert"
VALERROR = "FEHLER! Bitte hervorgehobene Einträge korrigieren"
SAVEERROR = "FEHLER! Datei konnte nicht im angegebenen Verzeichnis gespeichert werden"
METASAVEERROR = (
    "FEHLER! Metadatendatei konnte nicht im angegebenen Verzeichnis gespeichert werden"
)
NOIMGERROR = "FEHLER! Vor dem Speichern muss ein Bild erstellt werden."
OPENFILEERROR = "FEHLER! Datei konnte nicht geöffnet werden"
BADJSONERROR = "FEHLER! Ungültige Metadatendatei"
SAVETITLE = "Verzeichnis speichern auswählen"
SELTITLE = "Datei zum Importieren auswählen"
METAPROMPTTXT = "importiert, klicken Sie auf ZEICHNEN, um fortzufahren"
IMGSAVETXT = "Bild gespeichert als"
COMPLETETXT = "Vorgang abgeschlossen in"
INPROGTXT = "Operation läuft ..."
OPCANTXT = "Vorgang abgebrochen"
COORDTXT = "Koordinaten:"
COORDPOLTXT = "Polarkoordinaten:"
FRMTXT = "Rahmen"
FRMSTXT = "Rahmen"

# Menütext
MENUFILE = "Datei"
MENUOPTIONS = "Optionen"
MENUSAVE = "Bild speichern"
MENUEXPORT = "Exporteinstellungen"
MENUIMPORT = "Importeinstellungen"
MENUEXIT = "Beenden"
MENUPLOT = "Bild zeichnen"
MENUZOOM = "Zeichnen Zoom Animation"
MENUSPIN = "Zeichnen Julia Rotieren Animation"
MENUCAN = "Abbrechen"
MENURST = "Zurücksetzen"
MENUHIDESE = "Einstellungen ausblenden"
MENUSHOWSE = "Einstellungen anzeigen"
MENUHIDESB = "Statusleiste ausblenden"
MENUSHOWSB = "Statusleiste anzeigen"
MENUHIDEAX = "Achsen ausblenden"
MENUSHOWAX = "Achsen anzeigen"
MENUHOWTO = "Verwendun"
MENUABOUT = "Über"
MENUHELP = "Hilfe"

# Schaltflächentext
BTNPLOT = "ZEICHNEN"
BTNSAVE = "Speichern"
BTNCAN = "Abbrechen"
BTNRST = "Zurücksetzen"
BTNZOOM = "Zoom"
BTNSPIN = "Rotieren"

# Beschriftungstext
LBLCTL = "Kontrollen"
LBLSET = "Einstellungen"
LBLMODE = "Serietyp"
LBLVAR = "Variant"
LBLAUTO = "Animieren:"
LBLTHEME = "Thema"
LBLEXP = "Exponent"
LBLRAD = "Escape\nRadius"
LBLSHIFT = "Thema\nVerschiebung"
LBLITER = "Max\nIterationen"
LBLZOOM = "Zoom"
LBLZOOMINC = "Zoom\nInkrement"
LBLZXOFF = "ZX Versatz"
LBLZYOFF = "ZY Versatz"
LBLCX = "Julia CX"
LBLCY = "Julia CY"

# Dialogtext
DLGABOUT = "Über PyMandel"
DLGHOWTO = "Verwendung von PyMandel"
