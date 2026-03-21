"""
Menubar class for tkinter application.

This handles the menu bar.

Created on 27 Mar 2020

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

from tkinter import Menu

from pymandel.strings import (
    MENUABOUT,
    MENUCAN,
    MENUEXIT,
    MENUEXPORT,
    MENUFILE,
    MENUHELP,
    MENUHIDESB,
    MENUHIDESE,
    MENUHOWTO,
    MENUIMPORT,
    MENUOPTIONS,
    MENUPLOT,
    MENURST,
    MENUSAVE,
    MENUSHOWAX,
    MENUSPIN,
    MENUZOOM,
)


class MenuBar(Menu):
    """
    Menu inheritance class for menu bar.
    """

    def __init__(self, app, *args, **kwargs):
        """
        Constructor
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        Menu.__init__(self, self.__master, *args, **kwargs)

        # Create a pull-down menu for file operations
        self.file_menu = Menu(self, tearoff=False)
        self.file_menu.add_command(
            label=MENUSAVE, underline=1, command=self.__app.frm_settings.save_image
        )
        self.file_menu.add_command(
            label=MENUEXPORT, underline=1, command=self.__app.frm_settings.save_metadata
        )
        self.file_menu.add_command(
            label=MENUIMPORT,
            underline=1,
            command=self.__app.frm_settings.import_metadata,
        )
        self.file_menu.add_command(
            label=MENUEXIT, underline=1, accelerator="Ctrl-Q", command=self.__app.exit
        )
        self.add_cascade(menu=self.file_menu, label=MENUFILE)

        # Create a pull-down menu for options
        self.option_menu = Menu(self, tearoff=False)
        self.option_menu.add_command(
            label=MENUPLOT, underline=1, command=self.__app.frm_fractal.plot
        )
        self.option_menu.add_command(
            label=MENUZOOM, underline=1, command=self.__app.frm_fractal.animate_zoom
        )
        self.option_menu.add_command(
            label=MENUSPIN, underline=1, command=self.__app.frm_fractal.animate_spin
        )
        self.option_menu.add_command(
            label=MENUCAN, underline=1, command=self.__app.frm_fractal.cancel_press
        )
        self.option_menu.add_command(
            label=MENURST, underline=1, command=self.__app.frm_settings.reset
        )
        self.option_menu.add_command(
            label=MENUHIDESE, underline=1, command=self.__app.toggle_settings
        )
        self.option_menu.add_command(
            label=MENUHIDESB, underline=1, command=self.__app.toggle_status
        )
        self.option_menu.add_command(
            label=MENUSHOWAX, underline=1, command=self.__app.toggle_axes
        )
        self.add_cascade(menu=self.option_menu, label=MENUOPTIONS)

        # Create a pull-down menu for help operations
        self.help_menu = Menu(self, tearoff=False)
        self.help_menu.add_command(
            label=MENUHOWTO, underline=1, command=self.__app.howto
        )
        self.help_menu.add_command(
            label=MENUABOUT, underline=1, command=self.__app.about
        )
        self.add_cascade(menu=self.help_menu, label=MENUHELP)
