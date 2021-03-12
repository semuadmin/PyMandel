"""
Mandelbrot & Julia set class for tkinter application

This handles the computation of the Mandelbrot or Julia set as a numpy rgb array
which is loaded into a ImageTk.PhotoImage (and ultimately into a Tk.Canvas
for viewing in the GUI).

NB: use of Numba @jit decorators and pranges to improve performance.
For more information refer to http://numba.pydata.org.

Created on 29 Mar 2020

@author: semuadmin
"""
# pylint: disable=invalid-name

from math import log, sin, sqrt, pi

from PIL import Image
from numba import jit, prange
import numpy as np

from colormaps.cet_colormap import cet_CBC1, cet_CBTC1, cet_C1, cet_C4s, BlueBrown16
from colormaps.landscape256_colormap import landscape256
from colormaps.metallic256_colormap import metallic256
from colormaps.pastels256_colormap import pastels256
from colormaps.tropical_colormap import tropical16, tropical256
from colormaps.twilight256_colormap import twilight256

MANDELBROT = 0
JULIA = 1
TRICORN = 2
BURNINGSHIP = 3

THEMES = [
    "Default",
    "Monochrome",
    "BasicGrayscale",
    "BasicHue",
    "NormalizedHue",
    "SqrtHue",
    "LogHue",
    "SinHue",
    "SinSqrtHue",
    "BandedRGB",
    "BlueBrown16",
    "Tropical16",
    "Tropical256",
    "Pastels256",
    "Metallic256",
    "Twilight256",
    "Landscape256",
    "Colorcet_CET_C1",
    "Colorcet_CET_CBC1",
    "Colorcet_CET_CBTC1",
    "Colorcet_CET_C4s",
]


@jit(nopython=True, parallel=True, cache=True)
def plot(
    imagemap,
    settype,
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

    # For each pixel in array
    for x_axis in prange(width):  # pylint: disable=not-an-iterable
        for y_axis in prange(height):  # pylint: disable=not-an-iterable

            # Invoke core algorithm to calculate escape scalars
            i, z = fractal(
                settype,
                width,
                height,
                x_axis,
                y_axis,
                zxoff,
                zyoff,
                zoom,
                maxiter,
                radius,
                exponent,
                cxoff,
                cyoff,
            )

            # Look up color for these escape scalars and set pixel in imagemap
            imagemap[y_axis, x_axis] = get_color(i, z, maxiter, theme, shift)


@jit(nopython=True, cache=True)
def fractal(
    settype,
    width,
    height,
    x_axis,
    y_axis,
    zxoff,
    zyoff,
    zoom,
    maxiter,
    radius,
    exponent,
    cxoff,
    cyoff,
):
    """
    Calculates fractal escape scalars i, z for each image pixel
    and returns them for use in color rendering routines.

    YES! - just 10 lines of codes produces such infinite complexity - cool, huh?
    """

    zx_coord, zy_coord = ptoc(width, height, x_axis, y_axis, zxoff, zyoff, zoom)

    z = complex(zx_coord, zy_coord)
    if settype == JULIA:  # Julia or variant
        c = complex(cxoff, cyoff)
    else:  # Mandelbrot or variant
        c = z

    for i in prange(maxiter):  # pylint: disable=not-an-iterable
        # Iterate till the point c is outside the escape radius.
        if settype == BURNINGSHIP:
            z = complex(abs(z.real), -abs(z.imag))
        if settype == TRICORN:
            z = z.conjugate()
        z = z ** exponent + c

        if abs(z) > radius ** 2:
            break

    return i, z


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
def get_color(i, z, maxiter, theme, shift):
    """
    Uses escape scalars i, z from the fractal algorithm to drive a variety
    of color rendering algorithms or 'themes'.

    NB: If you want to add more rendering algorithms, this is where to add them,
    but you'll need to ensure they are 'Numba friendly' (i.e. limited to
    Numba-recognised data types and suitably decorated library functions).
    """

    if (
        i == maxiter - 1 and theme != "BasicGrayscale"
    ):  # Inside Mandelbrot set, so black
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
        if i == maxiter - 1:
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
        h = ((normalize(i, z) / maxiter) + (shift / 100)) % 1
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "SqrtHue":
        h = ((normalize(i, z) / sqrt(maxiter)) + (shift / 100)) % 1
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "LogHue":
        h = ((normalize(i, z) / log(maxiter)) + (shift / 100)) % 1
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "SinHue":
        h = normalize(i, z) * sin(((shift + 1) / 100) * pi / 2)
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    elif theme == "SinSqrtHue":
        steps = 1 + shift / 100
        h = 1 - (sin((normalize(i, z) / sqrt(maxiter) * steps) + 1) / 2)
        r, g, b = hsv_to_rgb(h, 0.75, 1)
    else:  # Indexed colormap arrays
        r, g, b = sel_colormap(i, z, shift, theme)
    return r, g, b


@jit(nopython=True, cache=True)
def sel_colormap(i, z, shift, theme):
    """
    Select from indexed colormap theme
    """

    if theme == "Colorcet_CET_CBC1":
        r, g, b = get_colormap(i, z, shift, cet_CBC1)
    if theme == "Colorcet_CET_CBTC1":
        r, g, b = get_colormap(i, z, shift, cet_CBTC1)
    if theme == "Colorcet_CET_C1":
        r, g, b = get_colormap(i, z, shift, cet_C1)
    if theme == "Colorcet_CET_C4s":
        r, g, b = get_colormap(i, z, shift, cet_C4s)
    if theme == "BlueBrown16":
        r, g, b = get_colormap(i, z, shift, BlueBrown16)
    if theme == "Tropical16":
        r, g, b = get_colormap(i, z, shift, tropical16)
    if theme == "Tropical256":
        r, g, b = get_colormap(i, z, shift, tropical256)
    if theme == "Pastels256":
        r, g, b = get_colormap(i, z, shift, pastels256)
    if theme == "Metallic256":
        r, g, b = get_colormap(i, z, shift, metallic256)
    if theme == "Twilight256":
        r, g, b = get_colormap(i, z, shift, twilight256)
    if theme == "Landscape256":
        r, g, b = get_colormap(i, z, shift, landscape256)

    return r, g, b


@jit(nopython=True, cache=True)
def get_colormap(i, z, shift, colmap):
    """
    Get pixel color from colormap
    """

    col = int((normalize(i, z)) + (shift * len(colmap) / 100)) % len(colmap)
    return colmap[col]


@jit(nopython=True, cache=True)
def normalize(i, z):
    """
    Normalize iteration count from escape scalars.
    (NB: should ideally be (log(log2(abs(z))) but Numba doesn't currently handle log2)
    """

    return i + 1 - (log(log(abs(z))) / log(2.0))


@jit(nopython=True, cache=True)
def hsv_to_rgb(h, s, v):
    """
    Convert HSV values (in range 0-1) to RGB (in range 0-255).
    """

    if s == 0.0:
        v = int(v * 255)
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
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

    r, g, b = int(r * 255), int(g * 255), int(b * 255)
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
