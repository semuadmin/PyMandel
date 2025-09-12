"""
ENGLISH language string literals for PyMandel tkinter application

Created on 22 Apr 2020

@author: semuadmin
"""

# pylint: disable=line-too-long

WIKIURL = "https://en.wikipedia.org/wiki/Mandelbrot_set"
GITHUBURL = "https://github.com/semuconsulting/PyMandel"
CETURL = "https://github.com/holoviz/colorcet/blob/master/LICENSE.txt"
MODULENAME = "pymandel"

COPYRIGHTTXT = "\u00a9 semuadmin (Steve Smith) 2020\nGPLv3 License. All Rights Reserved"

COLORCETTXT = "HoloViz Colorcet color maps available under\nCreative Commons Attribution (CC_BY) license"

INTROTXT = (
    "Welcome to PyMandel! Use mouse wheel or left-click to zoom, right-click to center."
)

HELPTXT = (
    "Enter settings manually (or import them from a metadata file) and click PLOT to create a fractal image with the specified parameters.\n\n"
    + "Mouse wheel - zoom in and out at the current cursor location"
    + " (there may be some lag at high resolutions).\n"
    + "Left-click, drag and release - zoom into a drawn rectangular area.\n"
    + "Left-click momentarily - zoom in at the cursor location by the Zoom Increment amount.\n"
    + "Shift & Left-click - zoom out.\n"
    + "Alt-L or Ctrl-L & Left-click - switch to Julia mode and plot the Julia set corresponding to that cursor (cx, cy offset) location.\n"
    + "Right-click - centre the image at the cursor location.\n"
    + "Press Left \u25c0 or Right \u25b6 arrow keys in Julia mode to rotate the Julia Set about its origin.\n\n"
    + "PLOT button - plot the image using current settings.\n"
    + "Cancel button - cancel the current plot operation.\n"
    + "Reset button - reset the parameters to the default values.\n"
    + "Save button - save the currently displayed image as a .png file along with its associated metadata as a .json file.\n\n"
    + "Zoom button - automatically create a sequence of zooming images.\n"
    + "Spin Button - automatically create a sequence of 'spinning' Julia images.\n\n"
    + "File..Export Settings - export current settings (metadata).\n"
    + "File..Import Settings - import previously saved metadata.\n"
    + "Options..Hide/Show Settings - toggles the Settings Panel on or off.\n"
    + "Options..Hide/Show Status - toggles the Status Bar on or off.\n"
    + "Help..Howto - display this How To dialog.\n"
    + "Help..About - display About dialog."
)

ABOUTTXT = (
    "PyMandel is a free, open-source GUI application written entirely in Python and tkinter with Numba performance enhancements.\n\n"
    + "Instructions and source code are available on Github at the link below."
)

# Message text
JITTXT = "FIRST TIME USE ONLY: Please wait for JIT Compilation and Caching"
SETINITTXT = "Settings initialised"
VALERROR = "ERROR! Please correct highlighted entries"
SAVEERROR = "ERROR! File could not be saved to specified directory"
METASAVEERROR = "ERROR! Metadata file could not be saved to specified directory"
NOIMGERROR = "ERROR! An image must be created before saving"
OPENFILEERROR = "ERROR! File could not be opened"
BADJSONERROR = "ERROR! Invalid metadata file"
SAVETITLE = "Select Save Directory"
SELTITLE = "Select File for Import"
METAPROMPTTXT = " imported, click PLOT to proceed"
IMGSAVETXT = "Image saved as "
COMPLETETXT = "Operation completed in "
INPROGTXT = "Operation in progress..."
OPCANTXT = "Operation Cancelled"
COORDTXT = "Coordinates:"
COORDPOLTXT = "Polar coords:"
FRMTXT = "Frame"
FRMSTXT = "Frames"

# Menu text
MENUFILE = "File"
MENUOPTIONS = "Options"
MENUSAVE = "Save Image"
MENUEXPORT = "Export Settings"
MENUIMPORT = "Import Settings"
MENUEXIT = "Exit"
MENUPLOT = "Plot Image"
MENUZOOM = "Plot Zoom Animation"
MENUSPIN = "Plot Julia Spin Animation"
MENUCAN = "Cancel"
MENURST = "Reset"
MENUHIDESE = "Hide Settings"
MENUSHOWSE = "Show Settings"
MENUHIDESB = "Hide Status Bar"
MENUSHOWSB = "Show Status Bar"
MENUHIDEAX = "Hide Axes"
MENUSHOWAX = "Show Axes"
MENUHOWTO = "How To"
MENUABOUT = "About"
MENUHELP = "Help"

# Button text
BTNPLOT = "PLOT"
BTNSAVE = "Save"
BTNCAN = "Cancel"
BTNRST = "Reset"
BTNZOOM = "Zoom"
BTNSPIN = "Spin"

# Label text
LBLCTL = "Controls"
LBLSET = "Settings"
LBLMODE = "Mode"
LBLVAR = "Variant"
LBLAUTO = "Animate:"
LBLTHEME = "Color\nTheme"
LBLEXP = "Exponent"
LBLRAD = "Escape\nRadius"
LBLSHIFT = "Theme\nShift"
LBLITER = "Max\nIterations"
LBLZOOM = "Zoom"
LBLZOOMINC = "Zoom\nIncrement"
LBLZXOFF = "ZX Offset"
LBLZYOFF = "ZY Offset"
LBLCX = "Julia CX"
LBLCY = "Julia CY"

# Dialog text
DLGABOUT = "About PyMandel"
DLGHOWTO = "How To Use PyMandel"
