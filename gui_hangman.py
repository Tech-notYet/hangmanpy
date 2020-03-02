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

    left_parent, center_parent, right_parent = initialize_frame(('left_parent', 'center_parent', 'right_parent'), APP)
    for parent in left_parent, center_parent, right_parent:
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        parent.grid(sticky=tk.NSEW)
    
    APP.mainloop()



def initialize_frame(names: typ.Tuple[str], master: typ.Optional[tk.Toplevel] = None) -> typ.Tuple[ttk.Frame]:
    """Take names and master ordering as left-center-right),
    and return a tuple of Frame widgets"""

    try:
        # Left Frame containing the canvas widget
        _left = ttk.Frame(master, class_='ParentFrame', height=800, width=700, padding=15,
                          relief=tk.GROOVE, name=names[0], borderwidth=1)
        # Center Frame containing the Text widget to display previous choices
        _center = ttk.Frame(master, class_='ParentFrame', width=500, padding=15,
                            name=names[1], borderwidth=1)
        # Right Frame containing the canvas widget
        _right = ttk.Frame(master, class_='ParentFrame', width=500, padding=15,
                           relief=tk.SUNKEN, name=names[3], borderwidth=1)
    except IndexError:
        print('3 names needed for frames')
        return tuple()

    return tuple(_left, _center, _right)

if __name__ == '__main__':
    startup_app()