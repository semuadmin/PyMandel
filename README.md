# PyMandel

[Current Status](#currentstatus) |
[Installation](#installation) |
[How to Use](#howto) |
[Command Line Utility](#cli) |
[Author & License](#author)

PyMandel is a free, open-source graphical Mandelbrot and Julia Set rendering application written entirely in Python 3 and tkinter 8.6, with metadata import/export, basic animation functionality and performance enhancement via [Numba](http://numba.pydata.org/) JIT compilation, parallelisation and caching.

![MacOS screenshot](https://github.com/semuconsulting/PyMandel/blob/main/images/burning_julia.png?raw=true)

The application plots fractals in an expandable window and allows the user to save the image as a .png file. It automatically saves the metadata (settings) associated with an image and provides a facility to import that metadata at a later date to reproduce it. It supports popular variants such as 'Burning Ship' and 'Tricorn'.

![image0](https://github.com/semuconsulting/PyMandel/blob/main/images/image0.png?raw=true)
![image1](https://github.com/semuconsulting/PyMandel/blob/main/images/image1.png?raw=true)
![image2](https://github.com/semuconsulting/PyMandel/blob/main/images/image2.png?raw=true)

![image3](https://github.com/semuconsulting/PyMandel/blob/main/images/image3.png?raw=true)
![image5](https://github.com/semuconsulting/PyMandel/blob/main/images/image5.png?raw=true)
![image6](https://github.com/semuconsulting/PyMandel/blob/main/images/image6.png?raw=true)

It also includes both GUI and command line facilities to automatically create sequences of 'deep zoom' or 'spinning Julia Set' images which can be converted into animated GIF files or short videos using external open source tools (e.g. GIMP or OpenShot).

## <a name="currentstatus">Current Status</a>

![Status](https://img.shields.io/pypi/status/PyMandel)
![Release](https://img.shields.io/github/v/release/semuconsulting/PyMandel)
![Build](https://img.shields.io/github/actions/workflow/status/semuconsulting/PyMandel/main.yml?branch=master)
![Release Date](https://img.shields.io/github/release-date-pre/semuconsulting/PyMandel)
![Last Commit](https://img.shields.io/github/last-commit/semuconsulting/PyMandel)
![Contributors](https://img.shields.io/github/contributors/semuconsulting/PyMandel.svg)
![Open Issues](https://img.shields.io/github/issues-raw/semuconsulting/PyMandel)

PyMandel is intended as free, open-source educational fun. We're not looking to compete with the likes of Ultra Fractal © here, but contributions are very welcome - please refer to [CONTRIBUTING.MD](https://github.com/semuconsulting/PyMandel/blob/main/CONTRIBUTING.md).

### Animated Mandelbrot Zoom sequence

This 178 frame, 10 fps sequence was automatically generated using the `mandelcli` command line utility and converted into an animated GIF file using GIMP. The entire sequence took about 35 seconds to render and save.

```shell
mandelcli --filename zoom --width 400 --height 300 --frames 178 --zoom 0.75 --zoominc 1.2 --zxoffset -0.743643887037158704752191506114774 --zyoffset 0.131825904205311970493132056385139 --theme Colorcet_CET_C1
```

![Zoom Animation](https://github.com/semuconsulting/PyMandel/blob/main/images/zoom.gif?raw=true)

### Animated Julia Spin sequences

These 400 frame, 20 fps sequences were automatically generated using the GUI's SPIN function and converted into animated GIF files using GIMP. The second sequence illustrates a Julia Set with exponent = 3.


![Spin Animation](https://github.com/semuconsulting/PyMandel/blob/main/images/juliaspin.gif?raw=true) ![Spin Animation Exponent = 3](https://github.com/semuconsulting/PyMandel/blob/main/images/juliaspin_exp3.gif?raw=true)

### Sample Metadata

```
{"pymandel": {
    "filename": "C:/Users/myuser/Downloads/mandela.png", 
    "created": "Apr 08 2020 19:43:41 GMT Standard Time", 
    "settype": "Mandelbrot",
    "setvar": "Standard",
    "zoom": 7500000000.0,
    "zoominc": 1.2,
    "frames": 10,
    "escradius": 2,
    "exponent": 2,
    "maxiter": 20000, 
    "zxoffset": -0.7491649396736062, 
    "zyoffset": 0.071803172645556,
    "cxoffset": 0, 
    "cyoffset": 0, 
    "theme": "Colorcet_CET_C1",
    "shift": 0
    }
}
```

## <a name="installation">Installation</a>

In the following, `python` & `pip` refer to the Python 3 executables. You may need to type 
`python3` or `pip3`, depending on your particular environment. It is also recommended that 
the Python 3 scripts (bin) and site_packages directories are included in your PATH (*most standard Python installation packages should do this automatically*).

### Dependencies

PyMandel is compatible with Python 3.9 - 3.13.

On Windows and MacOS, pip, tkinter and the necessary imaging libraries are generally packaged with Python.  On some Linux distributions like Ubuntu 18+ and Raspberry Pi OS, they may need to be installed separately, e.g.:

```shell
sudo apt install python3-pip python3-tk python3-pil python3-pil.imagetk libjpeg-dev zlib1g-dev
```

If you're installing Python 3 from source, you may also need to install the tkinter development library (refer to http://wiki.python.org/moin/TkInter for further details):

```shell
sudo apt install tk-devel
```

### 1. Install using pip

![Python version](https://img.shields.io/pypi/pyversions/PyMandel.svg?style=flat)
[![PyPI version](https://img.shields.io/pypi/v/PyMandel.svg?style=flat)](https://pypi.org/project/PyMandel/)
![PyPI downloads](https://img.shields.io/pypi/dm/PyMandel.svg?style=flat)

The easiest way to install the latest version of PyMandel is via [pip](http://pypi.python.org/pypi/pip/):

```shell
python3 -m pip install --upgrade pymandel
```

If required, `PyMandel` can also be installed into a virtual environment, e.g.

```shell
python3 -m pip install --user --upgrade virtualenv
python3 -m virtualenv env
source env/bin/activate (or env\Scripts\activate on Windows)
(env) python3 -m pip install --upgrade pymandel
...
deactivate
```

To run the application, if the Python 3 scripts (bin) directory is in your PATH, simply type (all lowercase):
```shell
pymandel
```

If desired, you can add a shortcut to this command to your desktop or favourites menu.

Alternatively, if the Python 3 site_packages directory is in your PATH, you can type (all lowercase):
```shell
python3 -m pymandel
```

**NB:** if the Python 3 scripts (bin) or site_packages directories are *not* in your PATH, you will need
to add the fully-qualified path to `pymandel` in the commands above.

**Tip**: to find the site_packages location, type `pip3 show pymandel` and look for the `Location:` entry in the response, e.g.

- Linux: `Location: /home/username/.local/lib/python3.12/site-packages`
- MacOS: `Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages`
- Windows: `Location: c:\users\username\appdata\roaming\python\python312\lib\site-packages`

**Tip:** To create an application launcher for linux distributions like Ubuntu, create a text file named `pymandel.desktop` with the following content (*edited for your particular environment*) and copy this to the `/home/user/.local/share/applications` folder, e.g.

```
[Desktop Entry]
Type=Application
Terminal=false
Name=PyMandel
Icon=/home/user/.local/lib/python3.11/site-packages/pygpsclient/resources/pymandel.png
Exec=/home/user/.local/bin/pymandel
```

### Performance Optimisations

The application makes use of [Numba](http://numba.pydata.org/) just in time (jit) compilation, caching and parallelisation techniques, in conjunction with Numpy image arrays, to dramatically improve calculation and rendering times relative to standard Python, particularly on multi-core CPUs. 

**NB:**

1. The very first time the program is used after installation, jit compilation and caching will delay the first plot by a couple of seconds, but thereafter the rendering should start instantly.

## <a name="howto">How To Use</a>

* Settings can be entered manually (or imported from a previously saved metadata file) to plot a fractal image using the specified parameters.

* Use the mouse wheel to zoom in and out at the current cursor location. There may be some lag at very high resolutions or where a substantial part of the image is within the set (i.e. black).

* Left-click, drag and release to zoom into a drawn rectangular area.

* Left-click momentarily to zoom in at the current cursor location by the Zoom Increment amount (e.g. a Zoom Increment of 10 will zoom in tenfold)

* Shift & Left-click to zoom out by the same amount.

* Right-clicking anywhere in the plot area will centre the image at that point using the currently specified zoom level.

* **NB:** Pressing Alt-L (left-hand Alt key) or Ctrl-L (left-hand Ctrl key) while left-clicking in Mandelbrot mode will automatically switch to Julia mode and plot the Julia Set corresponding to the cx, cy offset at the cursor location. Useful points of interest can be found anywhere around the perimeter of the Mandelbrot set.

* Pressing the Left &#9664; or Right &#9654; arrow keys in Julia mode will rotate the Julia Set clockwise or anti-clockwise about its origin (*the SPIN animation function does this automatically*).

* PLOT button - plot the image using current settings. 

* Cancel button - cancel the current plot operation.

* Reset button - reset the parameters to the default values.

* Save button - save the currently displayed image as a PNG file. You will be prompted for a directory on first use. A corresponding metadata json file will also be saved containing the parameters that were used to create the image, allowing it to be reproduced at a later date.

* File..Import Settings - import previously saved metadata. You will be prompted to select a json file to import. Some sample *.json files can be found in the [Images](https://github.com/semuconsulting/PyMandel/blob/main/images) folder

* Zoom button - automatically create and save a sequence of images at increasing zoom levels, which can be converted externally into an animation (e.g. GIF or short video).

* Spin button - in Julia mode only, automatically creates and saves a 360 degree 'spinning Julia Set' sequence. Increasing the number of frames will result in a slower but more detailed spin animation.

* Options..Hide/Show Status - toggles the Status Bar on or off.

* Options..Hide/Show Settings - toggles the Settings panel on or off.

* Help..How To - display how to use instructions.

* Help..About - display help screen with links to license and source code.

*Settings:*

* Set Type (Mode). Select from Mandelbrot or Julia.

* Set Variant. Select from Standard, Tricorn or BurningShip.

* Zoom level. The application currently uses standard 64-bit double precision and the maximum practical zoom level before floating-point errors cause pixelation is around 2 x 10<sup>13</sup> (20 million million).

* ZX axis offset in Real or 'Re' dimensional units (typically in the range -2.0 to 1.2).

* ZY axis offset in Imaginary or 'Im' dimensional units (typically in the range -1.2 to 1.2).

* CX axis offset of the Julia Set in Real or 'Re' dimensional units.

* CY axis offset of the Julia Set in Imaginary or 'Im' dimensional units.

* Max Iterations. Maximum number of iterations, which broadly equates to the fineness or resolution of the image. It will also affect the colour rendition in most themes. Higher zoom levels will typically require a higher number of iterations to produce a detailed image.

* Auto. If checked, maximum iterations will be automatically calculated according to the current zoom level.

* Escape Radius. The escape radius (defaults to 2, but higher values can produce more expansive color gradients).

* Exponent. The iteration exponent (normally 2 for the classic Mandelbrot, but higher exponents yield other radially symmetric forms at the cost of increased rendering time).

* Theme - a list of color rendering themes is provided. These are based on a variety of rendering algorithms, including cyclic colormap indexing; HSV derivations; banded RGB maps and simple grayscale. The code allows additional algorithms to be easily added.

* Theme Shift - this modifies the characteristics of certain themes, typically by shifting the hue along the spectrum or color map index. Its effect will depend on the specific rendering algorithm used.

* An image filename for saved images, metadata and animation frames.

* Frames. The number of animation frames to create.

* Zoom Increment. The zoom increment between frames (e.g. an increment of 1.5 means each successive frame is zoomed in 1.5x as much as the previous one; set Zoom Increment < 1 to zoom out). Used for left-click zooms and animations. For animations, the number of iterations is also automatically increased with the zoom level in accordance with a predefined algorithm.

## <a name="cli">Command Line Utilities</a>

### mandelcli.py

`mandelcli` is a command line equivalent to the GUI's Animate function. If PyMandel has been installed using `pip` and the Python 3 scripts (bin) directory is in the user's PATH, it can be invoked thus:

```shell
mandelcli --width 480 --height 480 --frames 20
``` 
This will produce a sequence of 20 .png images. Type `mandelcli -h` for a list of available parameters.

It can import settings from a previously saved metadata file using the import parameter e.g. `--import filename.json`.

In addition to producing animated sequences, the command line utility can be used to create single images at a much higher pixel resolution than would be available via the GUI application on a standard monitor, though render time may be significant e.g. this example produces an 8K resolution image which takes about a minute to render:

```shell
mandelcli --filename 8kres --width 7680 --height 4320 --zoom 207011 --maxiter 7000 --zxoffset -0.7428301078839413 --zyoffset 0.14078514286474172 --theme Tropical256 
```

**Suggestion** Use the PyMandel GUI at moderate resolutions to explore fractals and find a location and configuration you like, save the image & metadata, and then use the `mandelcli` command line utility to import the metadata and create a much higher resolution version of the same image e.g for desktop wallpaper, printing or sharing.

### make_colormap.py

`make_colormap` is a simple command line utility for generating PyMandel-compatible numpy RGB arrays from image files containing suitable color gradients (e.g. created using GIMP's gradient tool) or even photographs with interesting color palettes. If PyMandel has been installed using `pip` and the Python 3 scripts (bin) directory is in the user's PATH, it can be invoked thus:

```shell
make_colormap --mapname mymap --input image.png --output mymap_colormap.py --levels 256
```

Pass `-h` or `-help` for a list of available parameters.

## <a name="author">Author and License</a>

![License](https://img.shields.io/github/license/semuconsulting/PyMandel.svg)

GPLv3 License

Copyright (c) 2020, SEMU Consulting
All rights reserved.
semuadmin@semuconsulting.com

The HoloViz [Colorcet color maps](https://github.com/holoviz/colorcet) library has been harvested for some of the color rendering themes. These color maps are released under a Creative Commons Attribution 4.0 International Public License (CC-BY) - see [Colorcet License Conditions](https://github.com/holoviz/colorcet/blob/main/LICENSE.txt) for details. ***NB:*** for convenience the selected Colorcet assets (256-depth cyclic color maps) were converted into numpy rgb arrays in colormaps.py and the library itself is not actually used at runtime.

`PyMandel` is maintained entirely by volunteers. If you find it useful, a small donation would be greatly appreciated!

[![Donations](https://www.paypalobjects.com/en_GB/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?business=UL24WUA4XHNRY&no_recurring=1&item_name=Any+donations%2C+however+small%2C+will+help+further+the+development+of+these+projects.+Many+thanks%21&currency_code=GBP)


You may also like this - an online [JavaScript version of a Fractal Generator](https://github.com/semuadmin/fractal-generator) with similar functionality:

https://www.algolvariables.com/fractals/index.html
