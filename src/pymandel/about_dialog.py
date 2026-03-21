"""
About Dialog Box class for tkinter application.

Created on 3 Apr 2020

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

import os
from platform import python_version
from tkinter import NW, Button, Canvas, Label, PhotoImage, Toplevel
from webbrowser import open_new_tab

from numba import __version__ as numba_ver
from numpy import __version__ as numpy_ver

from pymandel._version import __version__
from pymandel.strings import (
    ABOUTTXT,
    CETURL,
    COLORCETTXT,
    COPYRIGHTTXT,
    DLGABOUT,
    GITHUBURL,
    WIKIURL,
)

VERSION = __version__
DIRNAME = os.path.dirname(__file__)
THUMBNAIL = os.path.join(DIRNAME, "resources/thumbnail.gif")


class AboutDialog:
    """
    About dialog box class
    """

    def __init__(self, app):
        """
        Initialise Toplevel dialog
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        self._dialog = Toplevel()
        self._dialog.title = DLGABOUT
        self._dialog.geometry(
            f"+{self.__master.winfo_rootx() + 50}+{self.__master.winfo_rooty() + 50}"
        )
        self._dialog.attributes("-topmost", "true")

        self.body()

    def body(self):
        """
        Set up widgets
        """

        # Create widgets
        self.lbl_title = Label(self._dialog, text=DLGABOUT)
        self.lbl_title.config(font=("Verdana", 16))
        self.thumb = PhotoImage(file=THUMBNAIL)
        self.can = Canvas(
            self._dialog,
            width=self.thumb.width(),
            height=self.thumb.height(),
            cursor="hand2",
        )
        self.can.create_image(0, 0, image=self.thumb, anchor=NW)
        self.lbl_desc = Label(self._dialog, text=ABOUTTXT, wraplength=300)
        self.lbl_version = Label(self._dialog, text=f"PyMandel Version: {VERSION}")
        self.lbl_python_version = Label(
            self._dialog, text=f"Python Version: {python_version()}"
        )
        self.lbl_numba_version = Label(self._dialog, text=f"Numba Version: {numba_ver}")
        self.lbl_numpy_version = Label(self._dialog, text=f"Numpy Version: {numpy_ver}")
        self.lbl_copyright = Label(
            self._dialog, text=COPYRIGHTTXT, fg="blue", cursor="hand2"
        )
        self.lbl_colorcet = Label(
            self._dialog, text=COLORCETTXT, fg="blue", cursor="hand2"
        )
        self.btn_ok = Button(self._dialog, text="OK", width=8, command=self.ok_press)

        # Arrange widgets
        self.lbl_title.grid(column=0, row=0, padx=5, pady=5)
        self.can.grid(column=0, row=1, padx=5, pady=5)
        self.lbl_desc.grid(column=0, row=2, padx=5, pady=5)
        self.lbl_version.grid(column=0, row=3, padx=5)
        self.lbl_python_version.grid(column=0, row=4, padx=5)
        self.lbl_numba_version.grid(column=0, row=5, padx=5)
        self.lbl_numpy_version.grid(column=0, row=6, padx=5)
        self.lbl_copyright.grid(column=0, row=7, padx=5, pady=5)
        self.lbl_colorcet.grid(column=0, row=8, padx=5, pady=5)
        self.btn_ok.grid(column=0, row=9, ipadx=3, ipady=3, padx=5, pady=5)

        # Bind commands and hotkeys
        self.can.bind("<Button-1>", lambda e: open_new_tab(WIKIURL))
        self.lbl_copyright.bind("<Button-1>", lambda e: open_new_tab(GITHUBURL))
        self.lbl_colorcet.bind("<Button-1>", lambda e: open_new_tab(CETURL))
        self.btn_ok.bind("<Return>", self.ok_press)
        self.btn_ok.focus_set()

    def ok_press(self, *args, **kwargs):
        """
        Handle OK button press
        """

        self.__master.update_idletasks()
        self._dialog.destroy()
