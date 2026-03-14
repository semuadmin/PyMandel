"""
Mandelbrot generator - Main tkinter application class

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

import os
from tkinter import E, N, PhotoImage, S, W

from pymandel.about_dialog import AboutDialog
from pymandel.fractal_frame import FractalFrame
from pymandel.howto_dialog import HowtoDialog
from pymandel.menu_bar import MenuBar
from pymandel.settings_frame import SettingsFrame
from pymandel.status_frame import StatusFrame
from pymandel.strings import (
    INTROTXT,
    JITTXT,
    MENUHIDEAX,
    MENUHIDESB,
    MENUHIDESE,
    MENUSHOWAX,
    MENUSHOWSB,
    MENUSHOWSE,
)

from ._version import __version__

VERSION = __version__
DIRNAME = os.path.dirname(__file__)
ICON = os.path.join(DIRNAME, "resources/pymandel.png")


class App:
    """
    Main GUI Application Class
    """

    def __init__(self, master):
        """
        Set up main application and add frames
        """

        self.__master = master
        self.__master.columnconfigure(0, weight=1)
        self.__master.rowconfigure(0, weight=1)
        self.__master.protocol("WM_DELETE_WINDOW", self.exit)
        self.__master.title("PyMandel")
        self._show_settings = True  # Flag to toggle settings frame
        self._show_status = True  # Flag to toggle status bar
        self._show_axes = False  # Flag to toggle plot axes
        self.__master.iconphoto(True, PhotoImage(file=ICON))

        self.body()

    def body(self):
        """
        Set up frame and widgets
        """

        self.frm_status = StatusFrame(self, borderwidth=2, relief="groove")
        self.frm_settings = SettingsFrame(self, borderwidth=2, relief="groove")
        self.frm_fractal = FractalFrame(self, borderwidth=2, relief="groove")
        self.frm_fractal.grid(column=0, row=0, padx=2, pady=2, sticky=(N, S, E, W))
        self.frm_settings.grid(column=1, row=0, padx=2, pady=2, sticky=N)
        self.frm_status.grid(
            column=0, row=1, padx=2, pady=2, columnspan=2, sticky=(W, E)
        )

        self.menu = MenuBar(self)
        self.__master.config(menu=self.menu)

        # Set up keyboard hot keys
        self.__master.bind_all("<Control-q>", self.exit)

        self.set_status(JITTXT, "blue")
        self.frm_fractal.can_fractal.update()
        self.frm_fractal.plot()
        self.set_status(INTROTXT, "green")
        self.frm_fractal.focus_set()

    def toggle_settings(self):
        """
        Toggle Settings Frame on or off
        """

        if self._show_settings:
            self.frm_settings.grid_forget()
            self._show_settings = False
            self.menu.option_menu.entryconfig(5, label=MENUSHOWSE)
        else:
            self.frm_settings.grid(column=1, row=0, padx=2, pady=2, sticky=N)
            self._show_settings = True
            self.menu.option_menu.entryconfig(5, label=MENUHIDESE)

    def toggle_status(self):
        """
        Toggle Status Bar on or off
        """

        if self._show_status:
            self.frm_status.grid_forget()
            self._show_status = False
            self.menu.option_menu.entryconfig(6, label=MENUSHOWSB)
        else:
            self.frm_status.grid(column=0, row=1, columnspan=2, sticky=(W, E))
            self._show_status = True
            self.menu.option_menu.entryconfig(6, label=MENUHIDESB)

    def toggle_axes(self):
        """
        Toggle plot axes on or off
        """

        if self._show_axes:
            self.frm_fractal.show_axes = False
            self._show_axes = False
            self.menu.option_menu.entryconfig(7, label=MENUSHOWAX)
        else:
            self.frm_fractal.show_axes = True
            self._show_axes = True
            self.menu.option_menu.entryconfig(7, label=MENUHIDEAX)

    def set_status(self, message, color="black"):
        """
        Sets text of status bar
        """

        self.frm_status.set_status(message, color)

    def get_master(self):
        """
        Returns application master (Tk)
        """

        return self.__master

    def howto(self):
        """
        Open Howto dialog
        """

        HowtoDialog(self)

    def about(self):
        """
        Open About dialog
        """

        AboutDialog(self)

    def exit(self, *args, **kwargs):
        """
        Kill any running processes and quit application
        """

        self.frm_fractal.cancel_press()
        self.__master.destroy()
