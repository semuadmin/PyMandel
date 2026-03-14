#!/usr/bin/env python
"""
Mandelbrot generator

A command line utility which invokes the Mandelbrot class methods to create a sequence
of Mandelbrot images as .png files. It is the command line equivalent of the GUI
Animate function, but can also be used to generate single, very high resolution images.

Can also import settings from a previously saved metadata file.

Created on 29 Mar 2020

:author: semuadmin
:copyright: semuadmin (Steve Smith) © 2020
:license: GPL3

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

import sys
from argparse import SUPPRESS, ArgumentDefaultsHelpFormatter, ArgumentParser
from json import loads
from math import log, sqrt
from time import time

from pymandel._version import __version__ as VERSION
from pymandel.mandelbrot import JULIA, MANDELBROT, Mandelbrot
from pymandel.strings import MODULENAME

sys.path.append("pymandel")
sys.path.append("colormaps")

EPILOG = (
    "© 2021 SEMU Consulting GPLv3 license - https://github.com/semuconsulting/PyMandel/"
)


class BatchMandelbrot:
    """
    Main class of command line utility
    """

    def __init__(self, **kwargs):
        """
        Command line utility class
        """

        print("Parameters passed: ", kwargs)
        self._setmode = kwargs.get("settype", "Mandelbrot")
        if self._setmode == "Julia":
            self._settype = JULIA
        else:
            self._settype = MANDELBROT
        self._setvar = kwargs.get("setvar", "Standard")
        self._width = int(kwargs.get("width", 1920))
        self._height = int(kwargs.get("height", 1080))
        self._radius = int(kwargs.get("escradius", 2))
        self._exponent = int(kwargs.get("exponent", 2))
        self._zx_off = float(kwargs.get("zxoffset", -0.5))
        self._zy_off = float(kwargs.get("zyoffset", 0.0))
        self._cx_off = float(kwargs.get("cxoffset", 0.0))
        self._cy_off = float(kwargs.get("cyoffset", 0.0))
        self._filepath = kwargs.get("filepath", ".")
        self._filename = kwargs.get("filename", "image")
        self._frames = int(kwargs.get("frames", 1))
        self._zoominc = float(kwargs.get("zoominc", 1.2))
        self._theme = kwargs.get("theme", "Default")
        self._shift = int(kwargs.get("shift", 0))
        self._startframe = int(kwargs.get("startframe", 1))
        self._startframe = min(self._startframe, self._frames)
        self._zoom = float(kwargs.get("zoom", 0.75))
        self._startzoom = float(
            kwargs.get(
                "startzoom", self._zoom * pow(self._zoominc, self._startframe - 1)
            )
        )
        self._zoom = self._startzoom
        self._maxiter = int(
            kwargs.get("maxiter", abs(1000 * log(1 / sqrt(self._zoom))))
        )

        self._importfile = kwargs.get("import", "")
        if self._importfile != "":
            if not self.import_metadata(self._importfile):
                return

        start = time()

        i = self.animate()

        end = time()
        print(f"Sequence of {i+1} frames took {round(end - start, 2)} secs")

    def animate(self) -> int:
        """
        Generates and saves a series of frames at a specific point and zoom increment.
        """

        i = 0
        try:
            self.mandelbrot = Mandelbrot(self)
            self.mandelbrot.cancel_plot()  # Cancel any in-flight plot

            for i in range(self._frames):
                self._currframe = i
                fqname = f"{self._filepath}/{self._filename}_{(i + 1):03d}"
                print(f"Creating file {fqname} ...")

                self.mandelbrot.plot_image(
                    self._settype,
                    self._setvar,
                    self._width,
                    self._height,
                    self._zoom,
                    self._radius,
                    self._exponent,
                    self._zx_off,
                    self._zy_off,
                    self._maxiter,
                    self._theme,
                    self._shift,
                    self._cx_off,
                    self._cy_off,
                )
                image = self.mandelbrot.get_image()

                try:
                    image.save(f"{fqname}.png", format="png")
                except OSError:
                    print(f"ERROR! File {fqname} could not be saved to specified path")
                    return i

                self._zoom = self._zoom * self._zoominc
                self._maxiter = self.get_autoiter(self._zoom)
        except KeyboardInterrupt:
            print("Animation interrupted by user")

        print("Animation complete")
        return i

    def import_metadata(self, filepath):
        """
        Import settings from json metadata file.
        """

        # Read file
        try:
            with open(filepath, "r", encoding="utf-8") as infile:
                jsondata = infile.read()
        except OSError:
            print("ERROR! Unable to read import file")
            return False

        # Parse file
        settings = loads(jsondata)
        self._settype = settings[MODULENAME]["settype"]
        self._setvar = settings[MODULENAME]["setvar"]
        self._zoom = float(settings[MODULENAME]["zoom"])
        self._radius = float(settings[MODULENAME]["escradius"])
        self._exponent = int(settings[MODULENAME]["exponent"])
        self._maxiter = int(settings[MODULENAME]["maxiter"])
        self._zx_off = float(settings[MODULENAME]["zxoffset"])
        self._zy_off = float(settings[MODULENAME]["zyoffset"])
        self._cx_off = float(settings[MODULENAME]["cxoffset"])
        self._cy_off = float(settings[MODULENAME]["cyoffset"])
        self._theme = settings[MODULENAME]["theme"]
        self._shift = int(settings[MODULENAME]["shift"])
        self._frames = int(settings[MODULENAME]["frames"])

        return True

    def get_autoiter(self, zoom):
        """
        Arbitrary algorithm to derive 'optimal' max iterations from zoom level.
        """

        if self._settype == JULIA:
            miniter = 500
        else:
            miniter = 100
        maxiter = max(miniter, int(abs(1000 * log(1 / sqrt(zoom)))))
        return maxiter


def main():
    """Entry point for CLI."""

    arp = ArgumentParser(
        epilog=EPILOG,
        formatter_class=ArgumentDefaultsHelpFormatter,
        argument_default=SUPPRESS,
    )
    arp.add_argument("-V", "--version", action="version", version="%(prog)s " + VERSION)
    arp.add_argument(
        "--settype",
        help="Set Type",
        choices=["Mandelbrot", "Julia"],
        default="Mandelbrot",
    )
    arp.add_argument(
        "--setvar",
        help="Set Variant",
        choices=["Standard", "BurningShip", "Tricorn"],
        default="Standard",
    )
    arp.add_argument(
        "--width", help="Width of the image(s) in pixels", type=int, default=1920
    )
    arp.add_argument(
        "--height", help="Height of the image(s) in pixels", type=int, default=1080
    )
    arp.add_argument("--zoom", help="Initial zoom level", type=float, default=0.75)
    arp.add_argument(
        "--maxiter", help="Initial maximum iterations", type=int, default=256
    )
    arp.add_argument("--zxoffset", help="X (Re) axis offset", type=float, default=-0.5)
    arp.add_argument("--zyoffset", help="Y (Im) axis offset", type=float, default=0.0)
    arp.add_argument(
        "--cxoffset", help="CX (Re) axis offset for Julia sets", type=float, default=0.0
    )
    arp.add_argument(
        "--cyoffset", help="CY (Im) axis offset for Julia sets", type=float, default=0.0
    )
    arp.add_argument("--escradius", help="Escape radius", type=float, default=2.0)
    arp.add_argument("--exponent", help="Iteration exponent", type=int, default=2)
    arp.add_argument("--frames", help="Number of frames to create", type=int, default=1)
    arp.add_argument("--startframe", help="Starting frame number", type=int, default=1)
    arp.add_argument(
        "--zoominc", help="Zoom increment between frames", type=float, default=1.2
    )
    arp.add_argument("--theme", help="Color rendering theme", default="Default")
    arp.add_argument("--shift", help="Color theme shift", type=int, default=0)
    arp.add_argument("--filepath", help="Path for saved files", default=".")
    arp.add_argument("--filename", help="Name prefix for saved files", default="frame")
    arp.add_argument(
        "--import", help="Fully qualified path to a previously saved metadata file"
    )

    kwargs = vars(arp.parse_args())
    BatchMandelbrot(**kwargs)


if __name__ == "__main__":
    sys.exit(main())
