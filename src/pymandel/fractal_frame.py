"""
Fractal frame class for tkinter application.

This handles all the user interaction (mouse and key clicks) and image mechanics.

Created on 3 Apr 2020

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

from cmath import polar
from math import cos, log, pi, sin, sqrt
from platform import system
from time import time
from tkinter import BOTH, NW, YES, Canvas, Frame

from PIL import ImageTk

from pymandel.mandelbrot import (
    BURNINGSHIP,
    JULIA,
    MANDELBROT,
    MODES,
    STANDARD,
    TRICORN,
    VARIANTS,
    Mandelbrot,
    ctop,
    ptoc,
)
from pymandel.strings import (
    COMPLETETXT,
    COORDTXT,
    FRMTXT,
    INPROGTXT,
    OPCANTXT,
    SAVEERROR,
)

ZOOM = 0
SPIN = 1
ZOOMOUT = 0
ZOOMIN = 1
GOJULIA = 2


class FractalFrame(Frame):
    """
    Frame inheritance class for plotting area.
    """

    def __init__(self, app, *args, **kwargs):
        """
        Constructor.
        """

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)

        Frame.__init__(self, self.__master, *args, **kwargs)

        self._fractal = None  # Must be instance variable to persist after use
        self._animating = False
        self._setmode = MANDELBROT
        self._setvar = STANDARD
        self._leftclickmode = ZOOMIN
        self.show_axes = False
        self._zoom_rect = None
        self._x_start = None
        self._y_start = None
        self._xaxis = self._yaxis = 0

        self.mandelbrot = None

        self.body()

    def body(self):
        """
        Set up frame and widgets.
        """

        self.__master.update_idletasks()
        plot_height = self.__app.frm_settings.winfo_reqheight() - 8
        self.can_fractal = Canvas(
            self, width=plot_height * 1.5, height=plot_height, cursor="tcross"
        )
        self.can_fractal.pack(fill=BOTH, expand=YES)
        self.can_fractal.bind("<Motion>", self.get_coords)
        self.can_fractal.bind("<Button-1>", self.on_left_click)  # Left-click zoom
        self.can_fractal.bind("<Button-3>", self.on_right_click)  # Right-click center
        self.can_fractal.bind(
            "<Button-2>", self.on_right_click
        )  # Right-click center (MacOS)
        self.can_fractal.bind_all("<KeyPress>", self.on_key_down)
        self.can_fractal.bind_all("<KeyRelease>", self.on_key_release)
        self.can_fractal.bind("<MouseWheel>", self.on_mouse_wheel)  # Mousewheel zoom
        self.can_fractal.bind("<ButtonPress-1>", self.on_button_down)  # Left-down
        self.can_fractal.bind("<B1-Motion>", self.on_button_drag)  # Left-drag
        self.can_fractal.bind(
            "<ButtonRelease-1>", self.on_button_release
        )  # Left-release

    def plot(self):
        """
        Plot Mandelbrot set as an ImageTk.PhotoImage and load
        this into the GUI's Canvas widget for display.
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings.get("valid"):
            return

        # Apply the current settings
        width, height = self.get_size()
        setmode = settings.get("settype")
        if setmode == "Julia":
            self._setmode = JULIA
        else:
            self._setmode = MANDELBROT
        setvar = settings.get("setvar")
        if setvar == VARIANTS[TRICORN]:
            self._setvar = TRICORN
        elif setvar == VARIANTS[BURNINGSHIP]:
            self._setvar = BURNINGSHIP
        else:
            self._setvar = STANDARD
        zoom = settings.get("zoom")
        radius = settings.get("radius")
        exponent = settings.get("exponent")
        if settings.get("autoiter"):
            maxiter = self.get_autoiter(zoom)
            self.__app.frm_settings.update_settings(maxiter=maxiter)
        else:
            maxiter = settings.get("maxiter")
        zx_off = settings.get("zxoffset")
        zy_off = settings.get("zyoffset")
        cx_off = settings.get("cxoffset")
        cy_off = settings.get("cyoffset")
        theme = settings.get("theme")
        shift = settings.get("shift")

        if not self._animating:
            self.__app.set_status(INPROGTXT)
        self.__master.update_idletasks()
        start = time()

        self.mandelbrot = Mandelbrot(self)
        self.mandelbrot.plot_image(
            self._setmode,
            self._setvar,
            width,
            height,
            zoom,
            radius,
            exponent,
            zx_off,
            zy_off,
            maxiter,
            theme,
            shift,
            cx_off,
            cy_off,
        )
        self._fractal = ImageTk.PhotoImage(self.mandelbrot.get_image())
        self.can_fractal.create_image(
            0, 0, image=self._fractal, state="normal", anchor=NW
        )

        if self.show_axes:
            self.axes(width, height)
        self.can_fractal.update()

        if (
            not self.mandelbrot.get_cancel() and not self._animating
        ):  # If plot wasn't cancelled
            end = time()
            self.__app.set_status(COMPLETETXT + str(round(end - start, 2)) + " seconds")

    def axes(self, width, height):
        """
        Draw complex space axes on plot.
        Bit simple - only really works at low magnifications
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings.get("valid"):
            return

        zoom = settings.get("zoom")
        zxoff = settings.get("zxoffset")
        zyoff = settings.get("zyoffset")
        tki = [-2.5, -2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2, 2.5]
        tick = 10
        xoff, yoff = ctop(width, height, 0, 0, zxoff, zyoff, zoom)
        xline = [0, height / 2 + yoff, width, height / 2 + yoff]
        yline = [width / 2 - xoff, 0, width / 2 - xoff, height]
        self.can_fractal.create_line(xline, fill="gray")
        self.can_fractal.create_text(
            0 + 40, height / 2 + yoff + 20, text="Re[c] (X)", fill="gray", anchor="n"
        )
        self.can_fractal.create_line(yline, fill="gray")
        self.can_fractal.create_text(
            width / 2 - xoff + 20, 0 + 20, text="Im[c] (Y)", fill="gray", anchor="w"
        )

        for x_axis in tki:
            xoff, yoff = ctop(width, height, x_axis, 0, zxoff, zyoff, zoom)
            yline = [
                width / 2 - xoff,
                height / 2 - tick + yoff,
                width / 2 - xoff,
                height / 2 + tick + yoff,
            ]
            self.can_fractal.create_line(yline, fill="gray")
            self.can_fractal.create_text(
                width / 2 - xoff,
                height / 2 - tick + yoff - 10,
                text=x_axis * -1,
                fill="gray",
            )
        for y_axis in tki:
            xoff, yoff = ctop(width, height, 0, y_axis, zxoff, zyoff, zoom)
            xline = [
                width / 2 - tick - xoff,
                height / 2 + yoff,
                width / 2 + tick - xoff,
                height / 2 + yoff,
            ]
            self.can_fractal.create_line(xline, fill="gray")
            self.can_fractal.create_text(
                width / 2 - tick - xoff - 10,
                height / 2 + yoff,
                text=y_axis * -1,
                fill="gray",
                anchor="e",
            )
        self.can_fractal.update()

    def get_autoiter(self, zoom):
        """
        Arbitrary algorithm to derive 'optimal' max iterations from zoom level.
        """

        settype = self.__app.frm_settings.get_settings().get("settype")
        if settype == MODES[JULIA]:
            miniter = 500
        else:
            miniter = 100
        maxiter = max(miniter, int(abs(1000 * log(1 / sqrt(zoom)))))
        return maxiter

    def cancel_press(self):
        """
        Cancel in-progress plot.
        """

        self.mandelbrot.cancel_plot()
        self._animating = False
        self.__app.set_status(OPCANTXT, "red")

    def get_size(self):
        """
        Get current canvas size.
        """

        self.update_idletasks()  # Make sure we know about any resizing
        width = self.can_fractal.winfo_width()
        height = self.can_fractal.winfo_height()
        return (width, height)

    def get_coords(self, event):
        """
        Get and display complex space coordinates of current mouse location.
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings.get("valid"):
            return (0, 0)

        # Get actual screen dimensions and mouse location
        width, height = self.get_size()
        x_pos = event.x
        y_pos = event.y
        zoom = settings.get("zoom")
        zxoff = settings.get("zxoffset")
        zyoff = settings.get("zyoffset")

        # Convert to complex space coordinates (offsets are expressed in z space)
        zx_coord, zy_coord = ptoc(width, height, x_pos, y_pos, zxoff, zyoff, zoom)

        self.__app.set_status(
            COORDTXT + " Re[c] (X): " + str(zx_coord) + ",  Im[c] (Y): " + str(zy_coord)
        )
        return (zx_coord, zy_coord)

    def on_mouse_wheel(self, event):
        """
        Zoom in and out using mouse wheel

        Mouse wheel event.delta increment differs between Windows and
        MacOS/Linux platforms. These settings seem to work OK for Logitech
        and Apple wireless mice but may need to be tweaked for other devices
        """

        if system() == "Windows":
            sensitivity = 0.015
        else:
            sensitivity = 1.5
        self.cancel_press()
        zx_coord, zy_coord = self.get_coords(event)
        zoom = self.__app.frm_settings.get_settings().get("zoom")

        if event.delta > 0:
            zoom = zoom * (event.delta * sensitivity)
        else:
            zoom = zoom / (event.delta * -sensitivity)

        self.__app.frm_settings.update_settings(
            zoom=zoom, zxoffset=zx_coord, zyoffset=zy_coord
        )
        self.__master.update_idletasks()

        self.plot()

    def on_right_click(self, event):
        """
        Right-Click - center and redraw image at mouse position.
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings.get("valid"):
            return

        self.cancel_press()
        zx_coord, zy_coord = self.get_coords(event)
        self.__app.frm_settings.update_settings(zxoffset=zx_coord, zyoffset=zy_coord)

        self.plot()

    def on_left_click(self, event):
        """
        Left-click - zoom in at cursor position (ZOOMIN mode).
        Left-click & Shift - zoom out (ZOOMOUT mode).
        Left-click & Ctrl-L or Alt-L - switch to Julia mode and plot Julia set
        corresponding to current cursor (cx, cy) position (GOJULIA mode).
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings.get("valid"):
            return

        self.cancel_press()
        zx_coord, zy_coord = self.get_coords(event)
        zoom = settings.get("zoom")
        zoominc = settings.get("zoominc")
        if self._leftclickmode == ZOOMIN:
            zoom = zoom * zoominc
            self.__app.frm_settings.update_settings(
                zoom=zoom, zxoffset=zx_coord, zyoffset=zy_coord
            )
        if self._leftclickmode == ZOOMOUT:
            zoom = zoom / zoominc
            self.__app.frm_settings.update_settings(
                zoom=zoom, zxoffset=zx_coord, zyoffset=zy_coord
            )
        if self._leftclickmode == GOJULIA:
            self.__app.frm_settings.update_settings(
                settype=MODES[JULIA],
                zxoffset=0,
                zyoffset=0,
                cxoffset=zx_coord,
                cyoffset=zy_coord,
            )

        self.plot()

    def on_key_down(self, event):
        """
        Left-click - zoom in at cursor position (ZOOMIN mode).
        Left-click & Shift - zoom out (ZOOMOUT mode).
        Left-click & Ctrl-L or Alt-L - switch to Julia mode and plot Julia set
        corresponding to current cursor (cx, cy) position (GOJULIA mode).
        Left or Right Arrow keys - in Julia mode, rotate Julia set about its origin

        (for some reason tkinter doesn't appear to recognise an Alt-L event on all
        Windows platforms)
        """

        if event.keysym == "Shift_L":
            self._leftclickmode = ZOOMOUT
            self.can_fractal.config(cursor="sizing")

        if event.keysym in ("Alt_L", "Control_L"):
            self._leftclickmode = GOJULIA
            self._setmode = JULIA
            self.can_fractal.config(cursor="target")

        # Pressing Left or Right button in Julia mode will rotate the Julia Set clockwise
        # or anti-clockwise about its origin
        if (event.keysym in ("Left", "Right")) and self._setmode == JULIA:
            if event.keysym == "Left":
                self.rotate_julia(0.01)
            else:
                self.rotate_julia(-0.01)

            self.plot()

    def on_key_release(self, event):
        """
        Revert to normal left-click mode (ZOOMIN)
        """

        self._leftclickmode = ZOOMIN
        self.can_fractal.config(cursor="tcross")

    def on_button_down(self, event):
        """
        Left-click - start to draw zoom area
        """

        self._x_start = event.x
        self._y_start = event.y
        if not self._zoom_rect:
            self._zoom_rect = self.can_fractal.create_rectangle(
                self._xaxis, self._yaxis, 1, 1, outline="yellow", width=2
            )

    def on_button_drag(self, event):
        """
        Left-drag - extend drawn zoom area
        """

        self.can_fractal.coords(
            self._zoom_rect, self._x_start, self._y_start, event.x, event.y
        )

    def on_button_release(self, event):
        """
        Left-release - zoom to drawn area
        """

        if not self._zoom_rect:
            return

        # Bug out if settings invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings["valid"]:
            return

        zxoff = settings.get("zxoffset")
        zyoff = settings.get("zyoffset")
        zoom = settings.get("zoom")
        width, height = self.get_size()
        x_0, y_0, x_1, y_1 = self.can_fractal.coords(self._zoom_rect)

        # If rectangle is less than two pixels wide, treat as momentary left-click
        # and simply zoom in by Zoom Increment amount
        if abs(x_1 - x_0) <= 2:
            self._zoom_rect = None
            self.on_left_click(event)
            return

        # Find the complex coordinates of the centre of the drawn rectangle
        x_pos = x_0 + ((x_1 - x_0) / 2)
        y_pos = y_0 + ((y_1 - y_0) / 2)
        zx_coord, zy_coord = ptoc(width, height, x_pos, y_pos, zxoff, zyoff, zoom)
        # Base zoom on x-axis only to maintain current canvas aspect ratio
        zoom = zoom * width / (x_1 - x_0)
        self.__app.frm_settings.update_settings(
            zoom=zoom, zxoffset=zx_coord, zyoffset=zy_coord
        )

        self.plot()
        self._zoom_rect = None

    def rotate_julia(self, angle):
        """
        Rotate Julia set about its origin by the angle in radians
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings["valid"]:
            return

        cx_off = settings.get("cxoffset")
        cy_off = settings.get("cyoffset")
        rds, phi = polar(complex(cx_off, cy_off))
        angle = phi + angle
        cx_off = rds * cos(angle)
        cy_off = rds * sin(angle)
        self.__app.frm_settings.update_settings(cxoffset=cx_off, cyoffset=cy_off)

    def animate_zoom(self):
        """
        Animate Julia spin mode
        """
        self.animate(ZOOM)

    def animate_spin(self):
        """
        Animate zoom mode
        """
        self.animate(SPIN)

    def animate(self, animatemode):
        """
        Generates and saves a series of frames at a specified offset.
        The individual frames can then be assembled into e.g. an
        animated .gif or short video using external tools.

        Also used to generate a 'Spinning Julia' animation, rotating
        a Julia Set anti-clockwise around its origin.
        """

        # Bug out if the settings are invalid
        settings = self.__app.frm_settings.get_settings()
        if not settings.get("valid"):
            return

        # If autosave is on, set filepath if not already set
        if settings.get("autosave"):
            filepath = self.__app.frm_settings.set_filepath()
            if filepath is None:  # User cancelled
                return

        zoom = settings.get("zoom")
        if settings.get("autoiter"):
            maxiter = self.get_autoiter(zoom)
            self.__app.frm_settings.update_settings(maxiter=maxiter)
        else:
            maxiter = settings.get("maxiter")
        frames = settings.get("frames")
        zoominc = settings.get("zoominc")
        name = settings.get("filename")
        width, height = self.get_size()

        self.mandelbrot = Mandelbrot(self)
        self.mandelbrot.cancel_plot()  # Cancel any in-flight plot
        self._animating = True

        start = time()
        for i in range(frames):
            self.__app.set_status(FRMTXT + " " + str(i) + " / " + str(frames) + " ...")
            self.can_fractal.update()

            if animatemode == SPIN:  # Spinning Julia animation
                self.rotate_julia((1 / frames) * 2 * pi)

            self.plot()

            if self.show_axes:
                self.axes(width, height)
            self.can_fractal.update()

            if self.mandelbrot.get_cancel():
                return

            if settings.get("autosave"):
                fqname = filepath + "/" + name + "_" + str(i + 1).zfill(3)
                try:
                    image = self.mandelbrot.get_image()
                    image.save(fqname + ".png", format="png")
                except OSError:
                    self.__app.set_status(SAVEERROR, "red")
                    self.__app.filepath = None
                    return

            if animatemode == ZOOM:
                zoom = zoom * zoominc
                maxiter = self.get_autoiter(zoom)
                self.__app.frm_settings.update_settings(zoom=zoom, maxiter=maxiter)

        end = time()
        self.__app.set_status(COMPLETETXT + str(round(end - start, 2)) + " seconds")
        self._animating = False
