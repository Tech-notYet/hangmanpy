import tkinter.ttk as ttk
from tkinter.ttk import tkinter as tk
from typing import *

GenericWidget = TypeVar('GenericWidget',
                        ttk.Button,
                        ttk.Checkbutton,
                        ttk.Combobox,
                        ttk.Entry,
                        ttk.Frame,
                        ttk.Label,
                        ttk.Labelframe,
                        ttk.LabelFrame,
                        ttk.Menubutton,
                        ttk.Notebook,
                        ttk.Panedwindow,
                        ttk.PanedWindow,
                        ttk.Progressbar,
                        ttk.Radiobutton,
                        ttk.Scale,
                        ttk.Scrollbar,
                        ttk.Separator,
                        ttk.Sizegrip,
                        ttk.Spinbox,
                        ttk.Style,
                        ttk.Treeview,
                        ttk.LabeledScale,
                        ttk.OptionMenu)

WidgetOpts = NewType('WidgetOpts', Mapping[str, Union[str, int]])

def startup_app() -> None:
    APP_ROWS = [0]
    APP_COLS = [0, 1, 2]

    # Left and Center Frames consist of 1x1 row, col
    LP_ROWS = [0]
    LP_COLS = [0]
    CP_ROWS = [0]
    CP_COLS = [0]
    # Right Frames contains input, buttons, text; it consists of 2x1 row, col
    RP_ROWS = [0, 1]
    RP_COLS = [0]

    # Top level window
    APP = tk.Tk()
    APP.title('Hangman In Python')
    APP.rowconfigure(APP_ROWS, weight=1, minsize=400)
    APP.columnconfigure(APP_COLS, weight=1, minsize=400)

    left_parent, center_parent, right_parent = initialize_frame(['left_parent', 'center_parent', 'right_parent'], APP)
    for parent in left_parent, center_parent, right_parent:
        if parent.winfo_name() == 'left_parent':
            parent.rowconfigure(LP_ROWS, weight=1)
            parent.columnconfigure(LP_COLS, weight=1)
            parent.grid(sticky=tk.NSEW, row=APP_ROWS, column=APP_COLS[0])
        elif parent.winfo_name() == 'center_parent':
            parent.rowconfigure(CP_ROWS, weight=1)
            parent.columnconfigure(CP_COLS, weight=1)
            parent.grid(sticky=tk.NSEW, row=APP_ROWS, column=APP_COLS[1])
        else:
            parent.rowconfigure(RP_ROWS, weight=1)
            parent.columnconfigure(RP_COLS, weight=1)
            parent.grid(sticky=tk.NSEW, row=APP_ROWS, column=APP_COLS[2])

    APP.mainloop()


def grid_widgets(widget: Type[GenericWidget], widget_opts: Mapping[str, Type[Sequence]]) -> None:
    widget.grid_configure(**widget_opts)


def initialize_frame(names: List[str], master: Optional[tk.Tk] = None) -> Tuple[ttk.Frame]:
    """Take names and master ordering as left-center-right),
    and return a tuple of Frame widgets"""

    try:
        # Left Frame containing the canvas widget
        left = ttk.Frame(master, class_='ParentFrame', height=600, width=500, padding=15,
                         relief=tk.GROOVE, name=names[0], borderwidth=1)
        # Center Frame containing the Text widget to display previous choices
        center = ttk.Frame(master, class_='ParentFrame', width=500, padding=15,
                           name=names[1], borderwidth=1)
        # Right Frame containing the canvas widget
        right = ttk.Frame(master, class_='ParentFrame', width=500, padding=15,
                          relief=tk.SUNKEN, name=names[2], borderwidth=1)
    except IndexError:
        print('3 names needed for frames')
        return tuple()

    return (left, center, right)


if __name__ == '__main__':
    startup_app()
