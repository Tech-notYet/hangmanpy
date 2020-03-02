import typing as typ
import tkinter as tk
import tkinter.ttk as ttk

# Top-level window


def startup_app():
    # Top level window
    APP = tk.Tk()
    APP.title('Hangman In Python')
    APP.rowconfigure(0, minsize=800, weight=1)
    APP.columnconfigure([0, 1, 2], weight=1)

    initialize_frame(APP)


def initialize_frame(names: typ.Tuple[str], positions: typ.Tuple[int], master: tk.Widget = None) -> ttk.Frame:
    """Take a name, master, and int (0,1,2 representing left-center-right),
    and return the specific Frame widget"""

    if position == 0:
        # Left Frame containing the canvas widget
        left_parent = ttk.Frame(master, class_='ParentFrame', height=800, width=700, padding=15,
                            relief=tk.GROOVE, name=name, borderwidth=1)
    if position == 1:
        # Center Frame containing the canvas widget
        right_parent = ttk.Frame(master, class_='ParentFrame', height=800, width=700, padding=15,
                            relief=tk.GROOVE, name=name, borderwidth=1)
    if position == 2:
        # Right Frame containing the canvas widget
        left_parent = ttk.Frame(master, class_='ParentFrame', height=800, width=700, padding=15,
                            relief=tk.GROOVE, name=name, borderwidth=1)
