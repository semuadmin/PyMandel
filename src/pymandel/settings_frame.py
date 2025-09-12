"""
Settings frame class for tkinter application.

This handles all the settings and file storage/retrieval.

Created on 3 Apr 2020

:author: semuadmin
:copyright: SEMU Consulting © 2020
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
from json import dump, loads
from re import match
from time import gmtime, strftime
from tkinter import (
    DISABLED,
    HORIZONTAL,
    LEFT,
    NORMAL,
    RIGHT,
    VERTICAL,
    Button,
    Checkbutton,
    DoubleVar,
    E,
    Entry,
    Frame,
    IntVar,
    Label,
    Listbox,
    N,
    S,
    Scale,
    Scrollbar,
    Spinbox,
    StringVar,
    W,
    filedialog,
    ttk,
)

from pymandel.mandelbrot import JULIA, MANDELBROT, MODES, THEMES, VARIANTS
from pymandel.strings import (
    BADJSONERROR,
    BTNCAN,
    BTNPLOT,
    BTNRST,
    BTNSAVE,
    BTNSPIN,
    BTNZOOM,
    FRMSTXT,
    IMGSAVETXT,
    LBLAUTO,
    LBLCX,
    LBLCY,
    LBLEXP,
    LBLITER,
    LBLMODE,
    LBLRAD,
    LBLSHIFT,
    LBLTHEME,
    LBLVAR,
    LBLZOOM,
    LBLZOOMINC,
    LBLZXOFF,
    LBLZYOFF,
    METAPROMPTTXT,
    METASAVEERROR,
    MODULENAME,
    NOIMGERROR,
    OPENFILEERROR,
    SAVEERROR,
    SAVETITLE,
    SELTITLE,
    SETINITTXT,
    VALERROR,
)

# Global variables for Entry widget validation
GOOD = "azure"
BAD = "pink1"


class SettingsFrame(Frame):
    """
    Frame inheritance class for application settings and controls.
    """

    def __init__(self, app, *args, **kwargs):
        """
        Constructor
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        Frame.__init__(self, self.__master, *args, **kwargs)

        #  Initialise up key variables
        self._image_num = 0
        self._image_name = "image"
        self._settype = StringVar()
        self._setvar = StringVar()
        self._zoom = DoubleVar()
        self._radius = DoubleVar()
        self._exponent = DoubleVar()
        self._zx_off = DoubleVar()
        self._zy_off = DoubleVar()
        self._cx_off = DoubleVar()
        self._cy_off = DoubleVar()
        self._maxiter = IntVar()
        self._zx_coord = DoubleVar()
        self._zy_coord = DoubleVar()
        self._theme = StringVar()
        self._shift = IntVar()
        self._themes = None
        self._filename = StringVar()
        self._filepath = None
        self._frames = IntVar()
        self._zoominc = DoubleVar()
        self._autoiter = IntVar()
        self._autosave = IntVar()
        self._validsettings = True

        self.body()

    def body(self):
        """
        Set up frame and widgets.
        """

        # Create settings panel widgets
        # pylint: disable=W0108
        self.lbl_settype = Label(self, text=LBLMODE)
        self.spn_settype = Spinbox(
            self,
            values=MODES,
            width=8,
            bg=GOOD,
            wrap=True,
            textvariable=self._settype,
        )
        self.lbl_setvar = Label(self, text=LBLVAR)
        self.spn_setvar = Spinbox(
            self,
            values=VARIANTS,
            width=8,
            bg=GOOD,
            wrap=True,
            textvariable=self._setvar,
        )
        self.lbl_zoom = Label(self, text=LBLZOOM)
        self.ent_zoom = Entry(
            self,
            border=2,
            relief="sunken",
            width=12,
            bg=GOOD,
            justify=RIGHT,
            textvariable=self._zoom,
        )
        self.lbl_zoominc = Label(self, text=LBLZOOMINC, justify=LEFT)
        self.ent_zoominc = Entry(
            self, width=5, border=2, bg=GOOD, justify=RIGHT, textvariable=self._zoominc
        )
        self.lbl_zx_off = Label(self, text=LBLZXOFF)
        self.ent_zx_off = Entry(
            self,
            border=2,
            relief="sunken",
            width=12,
            bg=GOOD,
            justify=RIGHT,
            textvariable=self._zx_off,
        )
        self.lbl_zy_off = Label(self, text=LBLZYOFF)
        self.ent_zy_off = Entry(
            self,
            border=2,
            relief="sunken",
            width=12,
            bg=GOOD,
            justify=RIGHT,
            textvariable=self._zy_off,
        )
        self.lbl_cx_off = Label(self, text=LBLCX)
        self.ent_cx_off = Entry(
            self,
            border=2,
            relief="sunken",
            width=12,
            bg=GOOD,
            justify=RIGHT,
            textvariable=self._cx_off,
            state=DISABLED,
        )
        self.lbl_cy_off = Label(self, text=LBLCY)
        self.ent_cy_off = Entry(
            self,
            border=2,
            relief="sunken",
            width=12,
            bg=GOOD,
            justify=RIGHT,
            textvariable=self._cy_off,
            state=DISABLED,
        )
        self.lbl_niter = Label(self, text=LBLITER, justify=LEFT)
        self.ent_maxiter = Entry(
            self,
            border=2,
            relief="sunken",
            bg=GOOD,
            width=8,
            justify=RIGHT,
            textvariable=self._maxiter,
        )
        self.chk_autoiter = Checkbutton(
            self, text="Auto", variable=self._autoiter, onvalue=1, offvalue=0
        )
        self.lbl_theme = Label(self, text=LBLTHEME, justify=LEFT)
        self.lbl_radius = Label(self, text=LBLRAD, justify=LEFT)
        self.ent_radius = Entry(
            self,
            border=2,
            relief="sunken",
            bg=GOOD,
            width=8,
            justify=RIGHT,
            textvariable=self._radius,
        )
        self.lbl_exp = Label(self, text=LBLEXP)
        self.ent_exp = Entry(
            self,
            border=2,
            relief="sunken",
            bg=GOOD,
            width=8,
            justify=RIGHT,
            textvariable=self._exponent,
        )
        self.sep_1 = ttk.Separator(
            self,
            orient=HORIZONTAL,
        )
        self.lbx_theme = Listbox(
            self,
            border=2,
            relief="sunken",
            bg=GOOD,
            width=6,
            height=5,
            justify=LEFT,
            exportselection=False,
        )
        self.lbl_shift = Label(self, text=LBLSHIFT, justify=LEFT)
        self.scl_shift = Scale(
            self,
            from_=0,
            to=100,
            orient=HORIZONTAL,
            variable=self._shift,
            border=2,
            relief="sunken",
            sliderlength=20,
            troughcolor=GOOD,
        )
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.lbx_theme.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lbx_theme.yview)
        self.lbx_theme.select_set(0)
        self.lbx_theme.event_generate("<<ListboxSelect>>")
        self.lbl_coords = Label(self, text="Re, Im", fg="grey")
        self.btn_plot = Button(
            self,
            text=BTNPLOT,
            width=8,
            fg="green",
            command=lambda: self.__app.frm_fractal.plot(),
        )
        self.btn_cancel = Button(
            self,
            text=BTNCAN,
            width=8,
            command=lambda: self.__app.frm_fractal.cancel_press(),
        )
        self.btn_reset = Button(self, text=BTNRST, width=8, command=self.reset)
        self.ent_save = Entry(
            self,
            textvariable=self._filename,
            width=6,
            border=2,
            relief="sunken",
            bg=GOOD,
            justify=LEFT,
        )
        self._filename.set(self._image_name + str(self._image_num))
        self.btn_save = Button(self, text=BTNSAVE, width=8, command=self.save_image)
        self.lbl_auto = Label(self, text=LBLAUTO, justify=LEFT)
        self.btn_autozoom = Button(
            self,
            text=BTNZOOM,
            width=8,
            command=lambda: self.__app.frm_fractal.animate_zoom(),
        )
        self.btn_autospin = Button(
            self,
            text=BTNSPIN,
            width=8,
            command=lambda: self.__app.frm_fractal.animate_spin(),
            state=DISABLED,
        )
        self.chk_autosave = Checkbutton(
            self, text=BTNSAVE, variable=self._autosave, onvalue=1, offvalue=0
        )
        self.lbl_frames = Label(self, text=FRMSTXT)
        self.ent_frames = Entry(
            self, width=5, border=2, bg=GOOD, justify=RIGHT, textvariable=self._frames
        )

        # Get list of available themes
        for idx, theme in enumerate(THEMES):
            self.lbx_theme.insert(idx, theme)

        self.body_arrange()  # Position all widgets in frame

        self.reset()  # Reset all settings to their defaults

        self.set_traces()  # Trace entry variables for validation and event handling

    def body_arrange(self):
        """
        Position widgets in frame
        """

        # Position all widgets in their parent frames
        self.btn_plot.grid(column=0, row=1, ipadx=3, ipady=3, sticky=W, padx=3, pady=3)
        self.btn_cancel.grid(
            column=1, row=1, ipadx=3, ipady=3, sticky=W, padx=3, pady=3
        )
        self.btn_reset.grid(column=2, row=1, ipadx=3, ipady=3, sticky=W, padx=3, pady=3)
        self.ent_save.grid(column=0, row=2, columnspan=2, sticky=(W, E), padx=3, pady=3)
        self.btn_save.grid(column=2, row=2, ipadx=3, ipady=3, sticky=W, padx=3, pady=3)
        self.lbl_auto.grid(column=0, row=3, sticky=W)
        self.btn_autozoom.grid(
            column=1, row=3, ipadx=3, ipady=3, sticky=W, padx=3, pady=3
        )
        self.btn_autospin.grid(
            column=2, row=3, ipadx=3, ipady=3, sticky=W, padx=3, pady=3
        )
        self.lbl_frames.grid(column=0, row=4, sticky=W)
        self.ent_frames.grid(column=1, row=4, sticky=W, padx=3, pady=3)
        self.chk_autosave.grid(column=2, row=4, sticky=W, padx=3, pady=3)
        self.sep_1.grid(column=0, row=5, columnspan=3, pady=5, sticky=(W, E))
        self.lbl_settype.grid(column=0, row=6, sticky=W)
        self.spn_settype.grid(
            column=1, row=6, columnspan=2, sticky=(W, E), padx=3, pady=3
        )
        self.lbl_setvar.grid(column=0, row=7, sticky=W)
        self.spn_setvar.grid(
            column=1, row=7, columnspan=2, sticky=(W, E), padx=3, pady=3
        )
        self.lbl_zoom.grid(column=0, row=8, sticky=W)
        self.ent_zoom.grid(column=1, row=8, columnspan=2, sticky=(W, E), padx=3, pady=3)
        self.lbl_zoominc.grid(column=0, row=9, sticky=W)
        self.ent_zoominc.grid(column=1, row=9, sticky=W, padx=3, pady=3)
        self.lbl_zx_off.grid(column=0, row=10, sticky=W)
        self.ent_zx_off.grid(
            column=1, row=10, columnspan=2, sticky=(W, E), padx=3, pady=3
        )
        self.lbl_zy_off.grid(column=0, row=11, sticky=W)
        self.ent_zy_off.grid(
            column=1, row=11, columnspan=2, sticky=(W, E), padx=3, pady=3
        )
        self.lbl_cx_off.grid(column=0, row=12, sticky=W)
        self.ent_cx_off.grid(
            column=1, row=12, columnspan=2, sticky=(W, E), padx=3, pady=3
        )
        self.lbl_cy_off.grid(column=0, row=13, sticky=W)
        self.ent_cy_off.grid(
            column=1, row=13, columnspan=2, sticky=(W, E), padx=3, pady=3
        )
        self.lbl_niter.grid(column=0, row=14, sticky=W)
        self.ent_maxiter.grid(column=1, row=14, sticky=W, padx=3, pady=3)
        self.chk_autoiter.grid(column=2, row=14, sticky=W, padx=3, pady=3)
        self.lbl_radius.grid(column=0, row=15, sticky=W)
        self.ent_radius.grid(column=1, row=15, sticky=W, padx=3, pady=3)
        self.lbl_exp.grid(column=0, row=16, sticky=W)
        self.ent_exp.grid(column=1, row=16, sticky=W, padx=3, pady=3)
        self.lbl_theme.grid(column=0, row=17, sticky=W)
        self.lbx_theme.grid(
            column=1, row=17, padx=3, pady=3, columnspan=2, sticky=(N, S, W, E)
        )
        self.scrollbar.grid(column=2, row=17, sticky=(N, S, E))
        self.lbl_shift.grid(column=0, row=18, sticky=W)
        self.scl_shift.grid(
            column=1, row=18, columnspan=2, padx=3, pady=3, sticky=(W, E)
        )
        self.lbx_theme.bind("<<ListboxSelect>>", self.get_sel_theme)

    def set_traces(self):
        """
        Set up entry variable traces for validation and event handling
        """

        self._validsettings = True
        self._settype.trace_add("write", self.val_settings)
        self._setvar.trace_add("write", self.val_settings)
        self._zoom.trace_add("write", self.val_settings)
        self._zx_off.trace_add("write", self.val_settings)
        self._zy_off.trace_add("write", self.val_settings)
        self._cx_off.trace_add("write", self.val_settings)
        self._cy_off.trace_add("write", self.val_settings)
        self._maxiter.trace_add("write", self.val_settings)
        self._radius.trace_add("write", self.val_settings)
        self._exponent.trace_add("write", self.val_settings)
        self._filename.trace_add("write", self.val_settings)
        self._frames.trace_add("write", self.val_settings)
        self._zoominc.trace_add("write", self.val_settings)

    def val_settings(self, *args, **kwargs):
        """
        Validate all user-entered settings.
        (A personal choice but I find this user experience more intuitive
        than the standard validatecommand method for Entry widgets)
        """

        self._validsettings = True
        self.__app.set_status("")

        if self.is_float(self.ent_zoom.get()) and self._zoom.get() > 0:
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_zoom, flg)

        if self.is_float(self.ent_zx_off.get()):
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_zx_off, flg)

        if self.is_float(self.ent_zy_off.get()):
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_zy_off, flg)

        if self.is_float(self.ent_cx_off.get()):
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_cx_off, flg)

        if self.is_float(self.ent_cy_off.get()):
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_cy_off, flg)

        if self.is_integer(self.ent_maxiter.get()) and self._maxiter.get() > 0:
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_maxiter, flg)

        if self.is_float(self.ent_radius.get()) and self._radius.get() > 0:
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_radius, flg)

        if self.is_float(self.ent_exp.get()) and self._exponent.get() >= 1:
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_exp, flg)

        if self.is_integer(self.ent_frames.get()) and self._frames.get() > 0:
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_frames, flg)

        if self.is_float(self.ent_zoominc.get()) and self._zoominc.get() > 0:
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_zoominc, flg)

        if self.is_filename(self.ent_save.get()):
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.ent_save, flg)

        if self.spn_settype.get() == MODES[MANDELBROT]:
            self.btn_autospin.config(state=DISABLED)
            self.ent_cx_off.config(state=DISABLED)
            self.ent_cy_off.config(state=DISABLED)
            self._cx_off.set(0)
            self._cy_off.set(0)
            flg = GOOD
        elif self.spn_settype.get() == MODES[JULIA]:
            self.btn_autospin.config(state=NORMAL)
            self.ent_cx_off.config(state=NORMAL)
            self.ent_cy_off.config(state=NORMAL)
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.spn_settype, flg)

        if self.spn_setvar.get() in VARIANTS:
            flg = GOOD
        else:
            flg = BAD
        self.flag_entry(self.spn_setvar, flg)

    def flag_entry(self, ent, flag):
        """
        Flag entry field as valid or invalid and set global validity status flag.
        This flag is used throughout to determine whether functions can proceed
        or not.
        """

        ent.config(bg=flag)
        if flag == BAD:
            self._validsettings = False
            self.__app.set_status(VALERROR, "red")

    def is_float(self, flag):
        """
        Validate if entry is a float.
        """

        try:
            float(flag)
            return True
        except ValueError:
            return False

    def is_integer(self, flag):
        """
        Validate if entry is a positive integer.
        """

        try:
            int(flag)
            if int(flag) > 0:
                return True
            return False
        except ValueError:
            return False

    def is_filename(self, flag):
        """
        Validate if entry represents a valid filename using a regexp.
        """

        return match(r"^[\w\-. ]+$", flag) and flag != ""

    def reset(self):
        """
        Reset settings to defaults.
        """

        self._settype.set(MODES[0])
        self._setvar.set(VARIANTS[0])
        self._zoom.set(0.75)
        self._zx_off.set(-0.5)
        self._zy_off.set(0.0)
        self._cx_off.set(0.0)
        self._cy_off.set(0.0)
        self._maxiter.set(128)
        self._radius.set(2)
        self._exponent.set(2)
        self._frames.set(10)
        self._zoominc.set(2.0)
        self._autoiter.set(1)
        self._autosave.set(0)
        self._theme.set("Default")
        self._filename.set("image0")
        self._shift.set(0)
        self.set_sel_theme()

        self.__app.set_status(SETINITTXT)

    def get_sel_theme(self, *args, **kwargs):
        """
        Get selected theme from listbox and set global variable.
        """

        idx = self.lbx_theme.curselection()
        if idx == "":
            idx = 0
        self._theme.set(self.lbx_theme.get(idx))

    def set_sel_theme(self):
        """
        Lookup index of selected theme and highlight that listbox position.
        NB: this requires 'exportselection=False' option to be set on listbox to
        work properly.
        """

        for idx, theme in enumerate(THEMES):
            if theme == self._theme.get():
                self.lbx_theme.activate(idx)
                self.lbx_theme.see(idx)
                break

    def get_settings(self):
        """
        Return all current settings as a dict.
        """

        if not self._validsettings:
            settings = {"valid": self._validsettings}
            return settings

        settings = {
            "settype": self._settype.get(),
            "setvar": self._setvar.get(),
            "zoom": self._zoom.get(),
            "zxoffset": self._zx_off.get(),
            "zyoffset": self._zy_off.get(),
            "cxoffset": self._cx_off.get(),
            "cyoffset": self._cy_off.get(),
            "maxiter": self._maxiter.get(),
            "autoiter": self._autoiter.get(),
            "autosave": self._autosave.get(),
            "radius": self._radius.get(),
            "exponent": self._exponent.get(),
            "theme": self._theme.get(),
            "shift": self._shift.get(),
            "filepath": self._filepath,
            "filename": self._filename.get(),
            "frames": self._frames.get(),
            "zoominc": self._zoominc.get(),
            "valid": self._validsettings,
        }
        return settings

    def update_settings(self, **kwargs):
        """
        Update settings from keyword parms.
        """

        if "settype" in kwargs:
            self._settype.set(kwargs["settype"])
        if "setvar" in kwargs:
            self._setvar.set(kwargs["setvar"])
        if "zoom" in kwargs:
            self._zoom.set(kwargs["zoom"])
        if "zxoffset" in kwargs:
            self._zx_off.set(kwargs["zxoffset"])
        if "zyoffset" in kwargs:
            self._zy_off.set(kwargs["zyoffset"])
        if "cxoffset" in kwargs:
            self._cx_off.set(kwargs["cxoffset"])
        if "cyoffset" in kwargs:
            self._cy_off.set(kwargs["cyoffset"])
        if "maxiter" in kwargs:
            self._maxiter.set(kwargs["maxiter"])
        if "autoiter" in kwargs:
            self._autoiter.set(kwargs["autoiter"])
        if "autosave" in kwargs:
            self._autosave.set(kwargs["autosave"])
        if "radius" in kwargs:
            self._radius.set(kwargs["radius"])
        if "exponent" in kwargs:
            self._exponent.set(kwargs["exponent"])
        if "filepath" in kwargs:
            self._filepath.set(kwargs["filepath"])
        if "filename" in kwargs:
            self._filename.set(kwargs["filename"])
        if "frames" in kwargs:
            self._frames.set(kwargs["frames"])
        if "zoominc" in kwargs:
            self._zoominc.set(kwargs["zoominc"])
        if "theme" in kwargs:
            self._theme.set(kwargs["theme"])
            self.set_sel_theme()
        if "shift" in kwargs:
            self._shift.set(kwargs["shift"])

    def set_filepath(self):
        """
        Sets filepath for saved files for the duration of this session.
        """

        default = os.getcwd()  # Default _filepath is current working directory
        if self._filepath is None:
            self._filepath = filedialog.askdirectory(
                title=SAVETITLE, initialdir=default, mustexist=True
            )
            if self._filepath == "":
                self._filepath = None  # User cancelled

        return self._filepath

    def save_image(self):
        """
        Save image as PNG file to selected filepath and automatically increment default
        image name. NB: currently this will overwrite any existing file of the same
        name without warning.
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings["valid"]:
            return

        # Check if image has been created
        image = self.__app.frm_fractal.mandelbrot.get_image()
        if image is None:
            self.__app.set_status(NOIMGERROR, "red")
            return

        # Set _filename and path
        if self.set_filepath() is None:  # User cancelled
            return
        fname = self._filename.get()
        fqname = self._filepath + "/" + fname

        # Save the image along with its metadata
        try:
            # image.write(fqname + ".png", format="png")
            image.save(fqname + ".png", format="png")
            self.save_metadata()
        except OSError:
            self.__app.set_status(SAVEERROR, "red")
            self._filepath = None
            return

        self._image_num += 1
        self._filename.set(self._image_name + str(self._image_num))
        self.__app.set_status(IMGSAVETXT + fqname + ".png", "green")

        # Return focus to image frame
        self.__app.frm_fractal.focus_set()

    def save_metadata(self):
        """
        Save json file containing meta data associated with image,
        allowing it to be imported and reproduced.
        """

        if self._filepath is None:
            if self.set_filepath() is None:  # User cancelled
                return

        fname = self._filename.get()
        fqname = self._filepath + "/" + fname
        filename = fqname + ".json"
        createtime = strftime("%b %d %Y %H:%M:%S %Z", gmtime())

        jsondata = {
            MODULENAME: {
                "filename": fqname + ".png",
                "created": createtime,
                "settype": self._settype.get(),
                "setvar": self._setvar.get(),
                "zoom": self._zoom.get(),
                "zoominc": self._zoominc.get(),
                "frames": self._frames.get(),
                "escradius": self._radius.get(),
                "exponent": self._exponent.get(),
                "maxiter": self._maxiter.get(),
                "zxoffset": self._zx_off.get(),
                "zyoffset": self._zy_off.get(),
                "cxoffset": self._cx_off.get(),
                "cyoffset": self._cy_off.get(),
                "theme": self._theme.get(),
                "shift": self._shift.get(),
            }
        }

        try:
            with open(filename, "w", encoding="utf-8") as outfile:
                dump(jsondata, outfile)
        except OSError:
            self.__app.set_status(METASAVEERROR, "red")
            self._filepath = None

        # Return focus to image frame
        self.__app.frm_fractal.focus_set()

    def import_metadata(self):
        """
        Update settings from imported json metadata file.
        """

        # Select and read file
        try:
            default = os.getcwd()
            filepath = filedialog.askopenfilename(
                initialdir=default,
                title=SELTITLE,
                filetypes=(("json files", "*.json"), ("all files", "*.*")),
            )
            if filepath == "":  # User cancelled
                return
            with open(filepath, "r", encoding="utf-8") as infile:
                jsondata = infile.read()
        except OSError:
            self.__app.set_status(OPENFILEERROR, "red")
            return

        # Parse file
        try:
            settings = loads(jsondata).get(MODULENAME)

            # Set plot parameters
            self._settype.set(settings.get("settype", "Mandelbrot"))
            self._setvar.set(settings.get("setvar", "Standard"))
            self._zoom.set(settings.get("zoom", 1))
            self._zoominc.set(settings.get("zoominc", 2.0))
            self._frames.set(settings.get("frames", 10))
            self._radius.set(settings.get("escradius", 2.0))
            self._exponent.set(settings.get("exponent", 2))
            self._maxiter.set(settings.get("maxiter", 256))
            self._zx_off.set(settings.get("zxoffset", 0))
            self._zy_off.set(settings.get("zyoffset", 0))
            self._cx_off.set(settings.get("cxoffset", 0))
            self._cy_off.set(settings.get("cyoffset", 0))
            self._theme.set(settings.get("theme", "Default"))
            self._shift.set(settings.get("shift", 0))

        except OSError:
            self.__app.set_status(BADJSONERROR, "red")
            return

        self.set_sel_theme()

        fbase = os.path.basename(filepath)
        filename, fileext = os.path.splitext(fbase)
        self.__app.set_status(
            "Metadata file " + filename + fileext + METAPROMPTTXT, "green"
        )

        # Return focus to image frame
        self.__app.frm_fractal.focus_set()
