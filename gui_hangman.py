import typing as typ
import tkinter as tk
import tkinter.ttk as ttk

# Top-level window


def startup_app():
    APP = tk.Tk()
    spl_props = prepare_splash()


# Splash Window


def get_splash_window(master: typ.Optional[str] = None, **fmt_opts: typ.Dict) -> ttk.Frame:
    if master is None:
        return ttk.Frame(**fmt_opts)
    else:
        return ttk.Frame(master, **fmt_opts)


def prepare_splash() -> typ.Tuple[typ.Tuple]:
    return (('height', 500), ('width', 250), ('padding', 10),
            ('relief', tk.GROOVE), ('name', 'splash_window'))

# Main Activity Window

    # TODO create main window
