"""
Mandelbrot & Julia set class for tkinter application.

This handles the computation of the Mandelbrot or Julia set as a numpy rgb array
which is loaded into a ImageTk.PhotoImage (and ultimately into a Tk.Canvas
for viewing in the GUI).

NB: use of Numba @jit decorators and pranges to improve performance.
For more information refer to http://numba.pydata.org.

Created on 29 Mar 2020

:author: semuadmin
:copyright: semuadmin (Steve Smith) © 2020
:license: GPL-3.0-only

This file is part of PyMandel.

PyMandel is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3
of the License, or (at your option) any later version.

PyMandel is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with PyMandel.
If not, see <https://www.gnu.org/licenses/>.
"""

# pylint: disable=invalid-name

from math import ceil, floor, log, pi, sin, sqrt

import numpy as np
from numba import jit, prange
from PIL import Image

from colormaps.cet_colormap import BlueBrown16, cet_C1, cet_C4s, cet_CBC1, cet_CBTC1
from colormaps.hsv256_colormap import hsv256
from colormaps.landscape256_colormap import landscape256
from colormaps.metallic256_colormap import metallic256
from colormaps.pastels256_colormap import pastels256
from colormaps.tropical_colormap import tropical16, tropical256
from colormaps.twilight256_colormap import twilight256
from colormaps.twilights512_colormap import twilights512

PERIODCHECK = True  # Turn periodicity check optimisation on/off
MANDELBROT = 0
JULIA = 1
STANDARD = 0
BURNINGSHIP = 1
TRICORN = 2
MODES = ("Mandelbrot", "Julia")
VARIANTS = ("Standard", "BurningShip", "Tricorn")
THEMES = [
    "Default",
    "BlueBrown16",
    "Tropical16",
    "Tropical256",
    "Pastels256",
    "Metallic256",
    "Twilight256",
    "Twilights512",
    "Landscape256",
    "Colorcet_CET_C1",
    "Colorcet_CET_CBC1",
    "Colorcet_CET_CBTC1",
    "Colorcet_CET_C4s",
    "HSV256",
    "Monochrome",
    "BasicGrayscale",
    "BasicHue",
    "NormalizedHue",
    "SqrtHue",
    "LogHue",
    "SinHue",
    "SinSqrtHue",
    "BandedRGB",
]


@jit(nopython=True, parallel=True, cache=True)
def plot(
    imagemap,
    settype,
    setvar,
    width,
    height,
    zoom,
    radius,
    exponent,
    zxoff,
    zyoff,
    maxiter,
    theme,
    shift,
    cxoff,
    cyoff,
):
    """
    Plots selected fractal type in the numpy rgb array 'imagemap'
    """

    radius2 = radius**2
    # For each pixel in array
    for x_axis in prange(width):  # pylint: disable=not-an-iterable
        for y_axis in prange(height):  # pylint: disable=not-an-iterable
            # Invoke core algorithm to calculate escape scalars
            i, za = fractal(
                settype,
                setvar,
                width,
                height,
                x_axis,
                y_axis,
                zxoff,
                zyoff,
                zoom,
                maxiter,
                radius2,
                exponent,
                cxoff,
                cyoff,
            )

            # Look up color for these escape scalars and set pixel in imagemap
            imagemap[y_axis, x_axis] = get_color(i, za, radius, maxiter, theme, shift)


@jit(nopython=True, cache=True)
def fractal(
    settype,
    setvar,
    width,
    height,
    x_axis,
    y_axis,
    zxoff,
    zyoff,
    zoom,
    maxiter,
    radius2,
    exponent,
    cxoff,
    cyoff,
):
    """
    Calculates fractal escape scalars i, za for each image pixel
    and returns them for use in color rendering routines.
    """

    zx_coord, zy_coord = ptoc(width, height, x_axis, y_axis, zxoff, zyoff, zoom)
    lastz = complex(0, 0)
    per = 0
    i = 0

    z = complex(zx_coord, zy_coord)
    if settype == JULIA:  # Julia or variant
        c = complex(cxoff, cyoff)
    else:  # Mandelbrot or variant
        c = z

    for i in prange(maxiter + 1):  # pylint: disable=not-an-iterable
        # Iterate till the value z is outside the escape radius.
        if setvar == BURNINGSHIP:
            z = complex(abs(z.real), -abs(z.imag))
        if setvar == TRICORN:
            z = z.conjugate()
        z = z**exponent + c

        # Optimisation - periodicity check speeds
        # up processing of points within set
        if PERIODCHECK:
            if z == lastz:
                i = maxiter
                break
            per += 1
            if per > 20:
                per = 0
                lastz = z
        # ... end of optimisation

        if abs(z) > radius2:
            break

    return i, abs(z)  # i, za


@jit(nopython=True, cache=True)
def ptoc(width, height, x, y, zxoff, zyoff, zoom):
    """
    Converts actual pixel coordinates to complex space coordinates
    (zxoff, zyoff are always the complex offsets).
    """

    zx_coord = zxoff + ((width / height) * (x - width / 2) / (zoom * width / 2))
    zy_coord = zyoff + (-1 * (y - height / 2) / (zoom * height / 2))
    return zx_coord, zy_coord


@jit(nopython=True, cache=True)
def ctop(width, height, zx_coord, zy_coord, zxoff, zyoff, zoom):
    """
    Converts complex space coordinates to actual pixel coordinates
    (zxoff, zyoff are always the complex offsets).
    """

    x_coord = (zx_coord + zxoff) * zoom * width / 2 / (width / height)
    y_coord = (zy_coord + zyoff) * zoom * height / 2
    return x_coord, y_coord


@jit(nopython=True, cache=True)
def get_color(i, za, radius, maxiter, theme, shift):
    """
    Uses escape scalars i, za from the fractal algorithm to drive a variety
    of color rendering algorithms or 'themes'.

    NB: If you want to add more rendering algorithms, this is where to add them,
    but you'll need to ensure they are 'Numba friendly' (i.e. limited to
    Numba-recognised data types and suitably decorated library functions).
    """

    if i == maxiter and theme != "BasicGrayscale":  # Inside Mandelbrot set, so black
        return 0, 0, 0

    if theme == "Default":
        theme = "BlueBrown16"

    if theme == "Monochrome":
        if shift == 0:
            h = 0.0
            s = 0.0
        else:
            h = 0.5 + shift / -200
            s = 1.0
        r, g, b = hsv_to_rgb(h, s, 1.0)
    elif theme == "BasicGrayscale":
        if i == maxiter:
            return 255, 255, 255
        r = 256 * i / maxiter
        b = g = r
    elif theme == "BasicHue":
        h = ((i / maxiter) + (shift / 100)) % 1
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "BandedRGB":
        bands = [0, 32, 96, 192]
        r = bands[(i // 4) % 4]
        g = bands[i % 4]
        b = bands[(i // 16) % 4]
    elif theme == "NormalizedHue":
        h = ((normalize(i, za, radius) / maxiter) + (shift / 100)) % 1
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "SqrtHue":
        h = ((normalize(i, za, radius) / sqrt(maxiter)) + (shift / 100)) % 1
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "LogHue":
        h = ((normalize(i, za, radius) / log(maxiter)) + (shift / 100)) % 1
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "SinHue":
        h = normalize(i, za, radius) * sin(((shift + 1) / 100) * pi / 2)
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "SinSqrtHue":
        steps = 1 + shift / 100
        h = 1 - (sin((normalize(i, za, radius) / sqrt(maxiter) * steps) + 1) / 2)
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    else:  # Indexed colormap arrays
        r, g, b = sel_colormap(i, za, radius, shift, theme)
    return r, g, b


@jit(nopython=True, cache=True)
def sel_colormap(i, za, radius, shift, theme):
    """
    Select from indexed colormap theme
    """

    r = g = b = 0
    if theme == "Colorcet_CET_CBC1":
        r, g, b = get_colormap(i, za, radius, shift, cet_CBC1)
    elif theme == "Colorcet_CET_CBTC1":
        r, g, b = get_colormap(i, za, radius, shift, cet_CBTC1)
    elif theme == "Colorcet_CET_C1":
        r, g, b = get_colormap(i, za, radius, shift, cet_C1)
    elif theme == "Colorcet_CET_C4s":
        r, g, b = get_colormap(i, za, radius, shift, cet_C4s)
    elif theme == "BlueBrown16":
        r, g, b = get_colormap(i, za, radius, shift, BlueBrown16)
    elif theme == "Tropical16":
        r, g, b = get_colormap(i, za, radius, shift, tropical16)
    elif theme == "Tropical256":
        r, g, b = get_colormap(i, za, radius, shift, tropical256)
    elif theme == "Pastels256":
        r, g, b = get_colormap(i, za, radius, shift, pastels256)
    elif theme == "Metallic256":
        r, g, b = get_colormap(i, za, radius, shift, metallic256)
    elif theme == "Twilight256":
        r, g, b = get_colormap(i, za, radius, shift, twilight256)
    elif theme == "Twilights512":
        r, g, b = get_colormap(i, za, radius, shift, twilights512)
    elif theme == "Landscape256":
        r, g, b = get_colormap(i, za, radius, shift, landscape256)
    elif theme == "HSV256":
        r, g, b = get_colormap(i, za, radius, shift, hsv256)

    return r, g, b


@jit(nopython=True, cache=True)
def get_colormap(i, za, radius, shift, colmap):
    """
    Get pixel color from colormap
    """

    ni = normalize(i, za, radius)  # normalised iteration count
    sh = ceil(shift * len(colmap) / 100)  # palette shift
    col1 = colmap[(floor(ni) + sh) % len(colmap)]
    col2 = colmap[(floor(ni) + sh + 1) % len(colmap)]
    return interpolate(col1, col2, ni)


@jit(nopython=True, cache=True)
def normalize(i, za, radius):
    """
    Normalize iteration count from escape scalars to produce
    smoother color gradients.
    """

    lzn = log(za**2) / 2
    nu = log(lzn / log(radius)) / log(2)
    return i + 1 - nu


@jit(nopython=True, cache=True)
def interpolate(col1, col2, ni):
    """
    Linear interpolation between two adjacent colors in color palette.
    """

    f = ni % 1  # fractional part of ni
    r = (col2[0] - col1[0]) * f + col1[0]
    g = (col2[1] - col1[1]) * f + col1[1]
    b = (col2[2] - col1[2]) * f + col1[2]
    return [r, g, b]


@jit(nopython=True, cache=True)
def hsv_to_rgb(h, s, v):
    """
    Convert HSV values (in range 0-1) to RGB (in range 0-255).
    """

    r = g = b = 0
    v = int(v * 255)
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = int(v * (1.0 - s))
    q = int(v * (1.0 - s * f))
    t = int(v * (1.0 - s * (1.0 - f)))
    i %= 6
    if i == 0:
        r, g, b = v, t, p
    if i == 1:
        r, g, b = q, v, p
    if i == 2:
        r, g, b = p, v, t
    if i == 3:
        r, g, b = p, q, v
    if i == 4:
        r, g, b = t, p, v
    if i == 5:
        r, g, b = v, p, q

    return r, g, b


class Mandelbrot:
    """
    Main computation and imaging class.
    """

    def __init__(self, master):
        """
        Constructor
        """

        self.__master = master
        self._kill = False
        self._image = None

    def plot_image(
        self,
        settype,
        setvar,
        width,
        height,
        zoom,
        radius,
        exp,
        zxoff,
        zyoff,
        maxiter,
        theme,
        shift,
        cxoff,
        cyoff,
    ):
        """
        Creates empty numpy rgb array, passes it to fractal calculation routine for
        populating, then loads populated array into an ImageTk.PhotoImage.
        """

        self._kill = False
        imagemap = np.zeros((height, width, 3), dtype=np.uint8)
        plot(
            imagemap,
            settype,
            setvar,
            width,
            height,
            zoom,
            radius,
            exp,
            zxoff,
            zyoff,
            maxiter,
            theme,
            shift,
            cxoff,
            cyoff,
        )
        self._image = Image.fromarray(imagemap, "RGB")

    def get_image(self):
        """
        Return populated PhotoImage for display or saving.
        """

        return self._image

    def get_cancel(self):
        """
        Return kill flag.
        """

        return self._kill

    def cancel_plot(self):
        """
        Cancel in-flight plot operation (plot is normally so quick this is
        largely redundant).
        """

        self._kill = True
