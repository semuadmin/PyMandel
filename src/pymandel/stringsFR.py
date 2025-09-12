"""
Littéraux de chaîne de langue FRANCAIS pour l'application PyMandel tkinter

Créé le 22 avr 2020

@author: semuadmin
"""

# pylint: disable=line-too-long

WIKIURL = "https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot"
GITHUBURL = "https://github.com/semuconsulting/PyMandel"
CETURL = "https://github.com/holoviz/colorcet/blob/master/LICENSE.txt"
MODULENAME = "pymandel"

COPYRIGHTTXT = (
    "\u00a9 semuadmin (Steve Smith) 2020\nGPLv3 License. Tous droits réservés"
)

COLORCETTXT = "Cartes de couleurs HoloViz Colorcet disponibles sous la licence\nCreative Commons Attribution (CC_BY)"

INTROTXT = "Bienvenue à PyMandel! Utilisez la molette de la souris ou un clic gauche pour zoomer, un clic droit pour centrer."

HELPTXT = (
    "Entrez les paramètres manuellement (ou importez-les à partir d'un fichier de métadonnées) et cliquez sur TRACER pour créer une image fractale avec les paramètres spécifiés.\n\n"
    + "Utilisez la molette de la souris pour effectuer un zoom avant et arrière à l'emplacement actuel du curseur.\n"
    + "Faites un clic gauche, faites glisser et relâchez - zoomez sur une zone rectangulaire dessinée.\n"
    + "Clic gauche - zoomer à l'emplacement du curseur de la valeur de l'incrément de zoom.\n"
    + "Maj et Clic gauche - zoom arrière.\n"
    + "Appuyez sur Gauche \u25c0 ou Droite \u25b6 en mode Julia pour faire pivoter l'ensemble Julia autour de son origine.\n\n"
    + "Bouton TRACER - trace l'image en utilisant les paramètres actuels.\n"
    + "Bouton Annuler - annule l'opération de tracé en cours.\n"
    + "Bouton de réinitialisation - réinitialise les paramètres aux valeurs par défaut.\n"
    + "Bouton Enregistrer - enregistre l'image actuellement affichée sous forme de fichier .png avec ses métadonnées associées sous forme de fichier .json.\n\n"
    + "Bouton Zoom - crée automatiquement une séquence d'images zoomées.\n"
    + "Bouton de rotation - crée automatiquement une séquence d'images Julia en rotation.\n\n"
    + "Fichier..Paramètres d'exportation - pour exporter les paramètres actuels (métadonnées).\n"
    + "Fichier..Paramètres d'importation - importer les métadonnées précédemment enregistrées.\n"
    + "Options..Masquer / Afficher les paramètres - active ou désactive le panneau des paramètres.\n"
    + "Options..Masquer / Afficher l'état - active ou désactive la barre d'état.\n"
    + "Aide..Comment - afficher cette boîte de dialogue Comment faire.\n"
    + "Aide..À propos - afficher la boîte de dialogue À propos."
)

ABOUTTXT = (
    "PyMandel est une application GUI open-source gratuite entièrement écrite en Python et tkinter avec des améliorations de performances Numba.\n\n"
    + "Les instructions et le code source sont disponibles sur Github au lien ci-dessous."
)

# Texte du message
JITTXT = "PREMIÈRE UTILISATION UNIQUEMENT: veuillez attendre la compilation et la mise en cache JIT"
SETINITTXT = "Paramètres initialisés"
VALERROR = "ERREUR! Veuillez corriger les entrées en surbrillance"
SAVEERROR = "ERREUR! Le fichier n'a pas pu être enregistré dans le répertoire spécifié"
METASAVEERROR = "ERREUR! Le fichier de métadonnées n'a pas pu être enregistré dans le répertoire spécifié"
NOIMGERROR = "ERREUR! Une image doit être créée avant l'enregistrement"
OPENFILEERROR = "ERREUR! Impossible d'ouvrir le fichier"
BADJSONERROR = "ERREUR! Fichier de métadonnées non valide"
SAVETITLE = "Sélectionner le répertoire d'enregistrement"
SELTITLE = "Sélectionner le fichier à importer"
METAPROMPTTXT = "importé, cliquez sur TRACER pour continuer"
IMGSAVETXT = "Image enregistrée sous"
COMPLETETXT = "Opération terminée en"
INPROGTXT = "Opération en cours ..."
OPCANTXT = "Opération annulée"
COORDTXT = "Coordonnées:"
COORDPOLTXT = "Coordonnées polaires:"
FRMTXT = "Cadre"
FRMSTXT = "Cadres"

# Texte du menu
MENUFILE = "Fichier"
MENUOPTIONS = "Options"
MENUSAVE = "Enregistrer l'image"
MENUEXPORT = "Exporter les paramètres"
MENUIMPORT = "Importer les paramètres"
MENUEXIT = "Quitter"
MENUPLOT = "TRACER Image"
MENUZOOM = "TRACER Zoom Animation"
MENUSPIN = "TRACER Julia Spin Animation"
MENUCAN = "Annuler"
MENURST = "Réinitialiser"
MENUHIDESE = "Masquer les paramètres"
MENUSHOWSE = "Afficher les paramètres"
MENUHIDESB = "Masquer la barre d'état"
MENUSHOWSB = "Afficher la barre d'état"
MENUHIDEAX = "Masquer les axes"
MENUSHOWAX = "Afficher les axes"
MENUHOWTO = "Comment faire"
MENUABOUT = "À propos"
MENUHELP = "Aide"

# Texte du bouton
BTNPLOT = "TRACER"
BTNSAVE = "Enregistrer"
BTNCAN = "Annuler"
BTNRST = "Réinitialiser"
BTNZOOM = "Zoom"
BTNSPIN = "Spin"

# Texte d'étiquette
LBLCTL = "Contrôles"
LBLSET = "Paramètres"
LBLMODE = "Définir le type"
LBLVAR = "Variant"
LBLAUTO = "Animer:"
LBLTHEME = "Thème\nCouleur"
LBLEXP = "Exposant"
LBLRAD = "Escape\nRadius"
LBLSHIFT = "Thème\nMaj"
LBLITER = "Max\nItérations"
LBLZOOM = "Zoom"
LBLZOOMINC = "Zoom\nIncrément"
LBLZXOFF = "Décalage ZX"
LBLZYOFF = "Décalage ZY"
LBLCX = "Julia CX"
LBLCY = "Julia CY"

# Texte de dialogue
DLGABOUT = "À propos de PyMandel"
DLGHOWTO = "Comment utiliser PyMandel"
