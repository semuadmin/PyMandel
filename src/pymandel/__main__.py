"""
Entry point for PyMandel Application.

Created on 12 Sep 2020

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
from tkinter import Tk

from pymandel.app import App


def main():
    """The main tkinter loop."""

    ROOT = Tk()
    APP = App(ROOT)
    ROOT.mainloop()


if __name__ == "__main__":
    sys.exit(main())
