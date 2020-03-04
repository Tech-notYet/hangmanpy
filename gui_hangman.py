import typing as Tp
from tkinter import ttk as ttk
from tkinter.ttk import tkinter as tk
from itertools import starmap


class LayoutManager():
    def __init__(self):
        self.APP = tk.Tk()
        self.APP.title('Hangman In Python')
        self.APP.rowconfigure(0, weight=1, pad=15, minsize=400)
        self.APP.columnconfigure([0, 1], weight=1, pad=15, minsize=400)

        self.LEFT = ttk.Frame(self.APP, name='lFrame')
        self.RIGHT = ttk.Frame(self.APP, name='rFrame')
        # Left Frame containing the canvas widget
        left = {'height': 600, 'width': 500, 'padding': 15,
                'relief': tk.SUNKEN, 'borderwidth': 1}
        # Right Frame containing the canvas widget
        right = {'height': 600, 'width': 500, 'padding': 15,
                 'relief': tk.GROOVE, 'borderwidth': 1}

        self.initialize_frame(self.LEFT, left)
        self.initialize_frame(self.RIGHT, right)

    def set_frame_grids(self, parent: Tp.Type[ttk.Frame]) -> None:
        # Left and Center Frames consist of 1x1 row, col
        # Right Frames contains input, buttons, text; it consists of 2x1 row, col
        cnfg = ('weight', 1), ('minsize', 400), ('pad', 15)
        if parent.winfo_name() == 'LFrame':
            parent.rowconfigure(0, dict(cnfg))
            parent.columnconfigure(0, dict(cnfg))
            parent.grid(sticky=tk.NSEW, row=0, column=0, padx=15, pady=15)
        else:
            parent.rowconfigure([0, 1], dict(cnfg))
            parent.columnconfigure(0, dict(cnfg))
            parent.grid(sticky=tk.NSEW, row=0, column=1, padx=15, pady=15)

    def initialize_frame(self, frame: Tp.Type[ttk.Frame], frame_opts: Tp.Mapping[str, Tp.Any]) -> None:
        """Configure Frame widgets configured with frame_opts"""
        for opt in frame_opts:
            frame[opt] = frame_opts[opt]
        self.set_frame_grids(frame)

    def start_app(self):
        self.APP.mainloop()


if __name__ == '__main__':
    lm = LayoutManager()
    lm.start_app()
