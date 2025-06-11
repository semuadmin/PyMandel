# PyMandel Release Notes

### RELEASE 1.0.15

CHANGES:

1. Remove pinned numpy dependency.

### RELEASE 1.0.14

CHANGES:

1. Support for Python 3.13 added - numba>=0.61 now supports 3.13

### RELEASE 1.0.13

CHANGES:

1. Support for Python 3.12 added - numba>=0.59 now supports 3.12

### RELEASE 1.0.12

CHANGES:

1. Support for Python 3.11 added - numba now supports 3.11
1. Support for Python 3.7 dropped - now end of life

### RELEASE 1.0.11

CHANGES:

1. VSCode and GHA workflows updated - Bandit security analysis added.
1. Project URLS corrected in pyproject.toml.
1. No functional changes.

### RELEASE 1.0.10

ENHANCEMENTS:

1. Update project structure and test framework to use pyproject.toml (instead of setup.py) with pytest and pytest-cov. No functional changes to application.

### RELEASE 1.0.9

FIXES:

1. Fixed maxiter error when zooming using pymandelcli. Fixes [#3](https://github.com/semuconsulting/PyMandel/issues/3)

CHANGES:

1. CLI utilities `pymandelcli.py` and `make_colormap.py` updated to use standard `argparse` library. Arguments should now be passed in the format `pymandelcli --width 800 --height 600` rather than `pymandelcli width=800 height=600`. Type `pymandelcli -h` for help.

### RELEASE 1.0.8

CHANGES:

1. License changed to GPLv3. No other functional changes.

### RELEASE 1.0.7

CHANGES:

1. Minimum versions of numba, numpy and Pillow updated.
2. shields.io build status badge URL updated.

No other functional changes.


### RELEASE 1.0.6

ENHANCEMENTS:

Number of significant enhancements in this release:
1. Set mode and variant categories separated, allowing Mandelbrot and Julia modes for each variation Standard, Burning Ship and Tricorn. Julias mapped from the Burning Ship's 'keel' are particularly attractive.
2. Linear color interpolation added to colormap rendering, producing much smoother color gradients.
3. Periodicity checking added to fractal calculation routine, dramatically improving rendering times for plots
which feature substantial 'in set' (black) points.

### RELEASE 1.0.5

FIXES:

1. Fixed bug in `mandelpycli` command line utility that was skewing the zyoffset coordinate. Also minor improvements to metadata import. 

**NB:** If you have old (pre 0v1.0.0) metadata json files, they'll need amending to change the 
header element from `mandelpy` to `pymandel` - see examples in `images` folder.

### RELEASE 1.0.4

ENHANCEMENTS:

1. Further console script entry points added for pymandelcli and make_colormap CLI utilities. These utilities
can now be launched via simple `pymandelcli` and `make_colormap` commands.

### RELEASE 1.0.3

ENHANCEMENTS:

1. Console script entry point added to `setup.py`, so application can now be launched via a simple `pymandel` command as an alternative to `python -m pymandel`, provided the Python 3 scripts/bin folder is in the user's PATH.

### RELEASE 1.0.2

ENHANCEMENTS:

1. Numba now supports Python 3.9. Minimum numba version updated to 0.53.0.
2. Numba & numpy versions cited in About dialog.
