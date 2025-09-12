"""
Literales de cadena de idioma ESPAÑOL para la aplicación PyMandel tkinter

Creado el 22 abr 2020

@autor: semuadmin
"""

# pylint: disable=line-too-long

WIKIURL = "https://en.wikipedia.org/wiki/Mandelbrot_set"
GITHUBURL = "https://github.com/semuconsulting/PyMandel"
CETURL = "https://github.com/holoviz/colorcet/blob/master/LICENSE.txt"
MODULENAME = "pymandel"

COPYRIGHTTXT = "\u00a9 semuadmin (Steve Smith) 2020 \nGPLv3 Licencia. Todos los derechos reservados"

COLORCETTXT = "Mapas de color HoloViz Colorcet disponibles bajo licencia de\nCreative Commons Attribution (CC_BY)"

INTROTXT = "Bienvenido a PyMandel! Use la rueda del mouse o haga clic izquierdo para hacer zoom, haga clic derecho para centrar."

HELPTXT = (
    "Ingrese la configuración manualmente (o impórtela de un archivo de metadatos) y haga clic en TRAZER para crear una imagen fractal con los parámetros especificados.\n\n"
    + "Use la rueda del mouse para acercar y alejar la ubicación actual del cursor.\n"
    + "Clic izquierdo, arrastre y suelte: amplíe un área rectangular dibujada.\n"
    + "Clic izquierdo - acerca la ubicación del cursor por la cantidad de incremento de zoom.\n"
    + "Shift y Clic izquierdo - alejar.\n"
    + "Presione Izquierda \u25c0 o Derecha \u25b6 en modo Julia para rotar el Conjunto Julia sobre su origen.\n\n"
    + "Botón TRAZER - trazar la imagen con la configuración actual.\n"
    + "Botón Guardar: guarda la imagen que se muestra actualmente como un archivo .png junto con sus metadatos asociados como un archivo .json.\n"
    + "Botón Cancelar: cancela la operación de trazado actual.\n"
    + "Botón Restablecer: restablece los parámetros a los valores predeterminados.\n\n"
    + "Botón de zoom: crea automáticamente una secuencia de imágenes con zoom.\n"
    + "Botón Girar: crea automáticamente una secuencia de imágenes giratorias de Julia.\n\n"
    + "Archivo..Configuración de exportación: exporta la configuración actual (metadatos).\n"
    + "Archivo..Configuración de importación: importa metadatos guardados previamente.\n"
    + "Opciones..Ocultar / Mostrar configuración: activa o desactiva el Panel de configuración.\n"
    + "Opciones..Ocultar / Mostrar estado: activa o desactiva la barra de estado.\n"
    + "Ayuda..Cómo: mostrar este cuadro de diálogo Cómo.\n"
    + "Ayuda..Acerca de: muestra el cuadro de diálogo Acerca de."
)

ABOUTTXT = (
    "PyMandel es una aplicación GUI gratuita de código abierto escrita completamente en Python y tkinter con mejoras de rendimiento de Numba.\n\n"
    + "Las instrucciones y el código fuente están disponibles en Github en el siguiente enlace."
)

# Texto de Mensaje
JITTXT = "USO POR PRIMERA VEZ SOLO: espere la compilación y el almacenamiento en caché de JIT"
SETINITTXT = "Configuración inicializada"
VALERROR = "ERROR! Corrija las entradas resaltadas"
SAVEERROR = "ERROR! El archivo no se pudo guardar en el directorio especificado"
METASAVEERROR = (
    "ERROR! El archivo de metadatos no se pudo guardar en el directorio especificado"
)
NOIMGERROR = "ERROR! Se debe crear una imagen antes de guardar"
OPENFILEERROR = "ERROR! El archivo no se pudo abrir"
BADJSONERROR = "ERROR! Archivo de metadatos no válido"
SAVETITLE = "Seleccionar Guardar Directorio"
SELTITLE = "Seleccionar archivo para importar"
METAPROMPTTXT = "importado, haga clic en TRAZER para continuar"
IMGSAVETXT = "Imagen guardada como"
COMPLETETXT = "Operación completada en"
INPROGTXT = "Operación en progreso ..."
OPCANTXT = "Operación cancelada"
COORDTXT = "Coordenadas:"
COORDPOLTXT = "Cordones polares:"
FRMTXT = "Marco"
FRMSTXT = "Marcos"

# Texto de Menú
MENUFILE = "Archivo"
MENUOPTIONS = "Opciones"
MENUSAVE = "Guardar Imagen"
MENUEXPORT = "Exportar Parámetros"
MENUIMPORT = "Importar Parámetros"
MENUEXIT = "Salir"
MENUPLOT = "Trazar Imagen"
MENUZOOM = "Trazar Animación de zoom"
MENUSPIN = "Trazar Animación de Rotación Julia"
MENUCAN = "Cancelar"
MENURST = "Restablecer"
MENUHIDESE = "Ocultar Parámetros"
MENUSHOWSE = "Mostrar Parámetros"
MENUHIDESB = "Ocultar Barra de Estado"
MENUSHOWSB = "Mostrar Barra de Estado"
MENUHIDEAX = "Ocultar Ejes"
MENUSHOWAX = "Mostrar Ejes"
MENUHOWTO = "Cómo"
MENUABOUT = "Acerca de"
MENUHELP = "Ayuda"

# Texto de Botón
BTNPLOT = "TRAZER"
BTNSAVE = "Guardar"
BTNCAN = "Cancelar"
BTNRST = "Restablecer"
BTNZOOM = "Zoom"
BTNSPIN = "Girar"

# Texto de etiqueta
LBLCTL = "Controles"
LBLSET = "Parámetros"
LBLMODE = "Conjunto tipo"
LBLVAR = "Variant"
LBLAUTO = "Animar:"
LBLTHEME = "Tema"
LBLEXP = "Exponente"
LBLRAD = "Escape\nRadio"
LBLSHIFT = "Tema\nCambiar"
LBLITER = "Max\nIteraciones"
LBLZOOM = "Zoom"
LBLZOOMINC = "Zoom\nIncremento"
LBLZXOFF = "ZX Offset"
LBLZYOFF = "ZY Offset"
LBLCX = "Julia CX"
LBLCY = "Julia CY"

# Texto de diálogo
DLGABOUT = "Acerca de PyMandel"
DLGHOWTO = "Cómo usar PyMandel"
