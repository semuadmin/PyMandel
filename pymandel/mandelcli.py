#!/usr/bin/env python
'''
Mandelbrot generator

A command line utility which invokes the Mandelbrot class methods to create a sequence
of Mandelbrot images as .png files. It is the command line equivalent of the GUI
Animate function, but can also be used to generate single, very high resolution images.

Can also import settings from a previously saved metadata file.

Created on 29 Mar 2020

@author: semuadmin
'''

from json import loads
from math import log, sqrt
import sys
from time import time

from mandelbrot import Mandelbrot, MANDELBROT, JULIA

sys.path.append('mandelpy')
sys.path.append('colormaps')


def help_text():
    '''
    Print help text
    '''

    print("Mandelbrot Generator command line utility\n (c) SEMU Consulting - BSD 3 License\n\n",
          "The following keyword parameters can be passed (default):\n\n",
          "settype - 'Mandelbrot' or 'Julia' ('Mandelbrot')\n",
          "width - the width of the image(s) in pixels (1920)\n",
          "height - the height of the image(s) in pixels (1080)\n",
          "zoom - the initial zoom level (0.75)\n",
          "maxiter - the initial maximum iterations (256)\n",
          "zxoffset - the x (Re) axis offset (-0.5)\n",
          "zyoffset - the y (Im) axis offset (0.0)\n",
          "cxoffset - the cx (Re) axis offset for Julia sets (0.0)\n",
          "cyoffset - the cy (Im) axis offset for Julia sets (0.0)\n",
          "escradius - the escape radius (2.0)\n",
          "exponent - the iteration exponent (2)\n",
          "frames - the number of frames to create (1)\n",
          "startframe - the starting frame number (1)\n",
          "zoominc - the zoom increment between frames (1.2)\n",
          "theme - the color rendering theme ('Default')\n",
          "shift - the color theme shift (0)\n",
          "filepath - the path for saved files ($cwd)\n",
          "filename - the name prefix for saved files ('frame')\n\n",
          "import - the full path to a previously saved metadata file ('')\n\n",
          "e.g. python mandelcli.py width=1920 height=1080 import='test.json'")


class BatchMandelbrot():
    '''
    Main class of command line utility
    '''

    # pylint: disable=R0902
    def __init__(self, **kwargs):
        '''
        Command line utility class
        '''

        print("Parameters passed: ", kwargs)
        self._importfile = kwargs.get('import', "")
        if self._importfile != "":
            if not self.import_metadata(self._importfile):
                return
        self._setmode = kwargs.get('settype', "Mandelbrot")
        if self._setmode == "Julia":
            self._settype = JULIA
        else:
            self._settype = MANDELBROT
        self._width = int(kwargs.get('width', 1920))
        self._height = int(kwargs.get('height', 1080))
        self._radius = int(kwargs.get('escradius', 2))
        self._exponent = int(kwargs.get('exponent', 2))
        self._zx_off = float(kwargs.get('zxoffset', -0.5))
        self._zy_off = float(kwargs.get('cyoffset', 0.))
        self._cx_off = float(kwargs.get('cxoffset', 0.))
        self._cy_off = float(kwargs.get('cyoffset', 0.))
        self._filepath = kwargs.get('filepath', ".")
        self._filename = kwargs.get('filename', "image")
        self._frames = int(kwargs.get('frames', 1))
        self._zoominc = float(kwargs.get('zoominc', 1.2))
        self._theme = kwargs.get('theme', "Default")
        self._shift = int(kwargs.get('shift', 0))
        self._startframe = int(kwargs.get('startframe', 1))
        if self._startframe > self._frames:
            self._startframe = self._frames
        self._zoom = float(kwargs.get('zoom', 0.75))
        self._startzoom = float(kwargs.get('startzoom',
                                           self._zoom * pow(self._zoominc,
                                                            self._startframe - 1)))
        self._zoom = self._startzoom
        self._maxiter = int(kwargs.get('maxiter', abs(1000 * log(1 / sqrt(self._zoom)))))

        start = time()

        self.animate()

        end = time()
        print("Sequence of " + str(self._frames - self._startframe + 1) + \
              " frames took " + str(round(end - start, 2)) + " secs")

    def animate(self):
        '''
        Generates and saves a series of frames at a specific point and zoom increment.
        '''

        self.mandelbrot = Mandelbrot(self)
        self.mandelbrot.cancel_plot()  # Cancel any in-flight plot

        for i in range(self._frames):

            self._currframe = i
            fqname = self._filepath + "/" + self._filename + "_" + str(i + 1).zfill(3)
            print("Creating file " + fqname + " ...")

            self.mandelbrot.plot_image(self._settype, self._width, self._height,
                                       self._zoom, self._radius, self._exponent,
                                       self._zx_off, self._zy_off, self._maxiter,
                                       self._theme, self._shift, self._cx_off,
                                       self._cy_off)
            image = self.mandelbrot.get_image()

            try:
                image.save(fqname + ".png", format="png")
            except OSError:
                print("ERROR! File " + fqname + "could not be saved to specified path")
                return

            self._zoom = self._zoom * self._zoominc
            self._maxiter = int(abs(1000 * log(1 / sqrt(self._zoom))))

        print("Animation complete")

    def import_metadata(self, filepath):
        '''
        Import settings from json metadata file.
        '''

        # Read file
        try:
            with open(filepath, 'r') as infile:
                jsondata = infile.read()
        except OSError:
            print("ERROR! Unable to read import file")
            return False

        # Parse file
        settings = loads(jsondata)
        self._settype = settings['mandelbrot']['settype']
        self._zoom = settings['mandelbrot']['zoom']
        self._radius = settings['mandelbrot']['escradius']
        self._exponent = settings['mandelbrot']['exponent']
        self._maxiter = settings['mandelbrot']['maxiter']
        self._zx_off = settings['mandelbrot']['zxoffset']
        self._zy_off = settings['mandelbrot']['zyoffset']
        self._cx_off = settings['mandelbrot']['cxoffset']
        self._cy_off = settings['mandelbrot']['cyoffset']
        self._theme = settings['mandelbrot']['theme']
        self._shift = settings['mandelbrot']['shift']

        return True


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] in {"-h", "--h", "help", "-help", "--help", "-H"}:
            help_text()
            sys.exit()

    BatchMandelbrot(**dict(arg.split('=') for arg in sys.argv[1:]))
