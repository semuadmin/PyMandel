"""
Status Bar frame class for tkinter application.

This handles the status bar notifications.

Created on 7 Apr 2020

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

from tkinter import E, Frame, Label, StringVar, W


class StatusFrame(Frame):
    """
    Frame inheritance class for _status bar.
    """

    def __init__(self, app, *args, **kwargs):
        """
        Constructor
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        Frame.__init__(self, self.__master, *args, **kwargs)
        self._status = StringVar()

        self.body()

    def body(self):
        """
        Set up frame and widgets.
        """

        self.lbl_status = Label(self, textvariable=self._status, anchor=W)
        self.lbl_status.grid(column=0, row=0, sticky=(W, E))

    def set_status(self, message, color="black"):
        """
        Sets text of status bar.
        """

        self.lbl_status.config(fg=color)
        self._status.set("  " + message)

    def clear_status(self):
        """
        Clears text of status bar.
        """

        self._status.set("")
