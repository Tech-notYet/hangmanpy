import typing as tp
from collections import defaultdict, namedtuple
from tkinter import ttk
import tkinter as tk

WIDGETTYPES: tp.Tuple[str, ...] = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label',
                                   'LabelFrame', 'LabeledScale', 'Labelframe', 'Menubutton', 'Notebook',
                                   'OptionMenu', 'PanedWindow', 'Panedwindow', 'Progressbar', 'Radiobutton',
                                   'Scale', 'Scrollbar', 'Separator', 'Sizegrip', 'Spinbox', 'Toplevel', 'Treeview')
DDICT = tp.DefaultDict[str, tp.Sequence[str]]


class LeftFrame(ttk.Frame):
    """Child of MainApplication. It contains the Canvas widget"""

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.configure(borderwidth=0, width=500, height=500, padding=(25, 25))
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, anchor=tk.CENTER)


class RightFrame(ttk.Frame):
    """Child of MainApplication. It contains the remaining widgets"""

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.configure(relief=tk.RIDGE, width=500,
                       height=500, padding=(25, 0, 0, 0))
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, anchor=tk.CENTER)


class HangmanCanvas(tk.Canvas):
    """Canvas Widget used to draw the hangman image
    for each incorrect guess by the player"""

    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        opts = {
            'bg': '#f8f8f8',
            'borderwidth': 1,
            'relief': tk.RIDGE
        }
        self.configure(**opts)
        self.pack(fill=tk.Y, expand=True, anchor=tk.N,
                  padx=2, pady=2)
        line = []
        for y in range(5, 125, 5):
            line.append([5, y])
        self.create_line(line)


class GuessesLabelframe(ttk.Labelframe):
    """Labelframe to contain a Label Widget which displays players previous guesses"""

    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.configure(text='Previous Guesses:', labelanchor=tk.NW, style='TLabelframe')
        self.pack(anchor=tk.N, fill=tk.X, expand=True,
                  ipadx=5, ipady=5, padx=25, pady=10)


class GuessesLabel(ttk.Label):
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.guess_list = set()
        self.guesses = tk.StringVar()
        self.configure(textvariable=self.guesses, style='TLabel')
        self.pack(anchor=tk.CENTER, fill=tk.X, expand=True, padx=25, pady=25)


class GuessEntry(ttk.Entry):
    def __init__(self, master, widget=None, **kw):
        super().__init__(master=master, **kw)
        self.configure(width=50, style='TEntry')
        self.pack(ipadx=5, ipady=5, padx=25, pady=25, anchor=tk.N,
                  fill=tk.X, expand=True)


class SubmitButton(ttk.Button):

    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)


class ClearButton(ttk.Button):
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)


class MainApplication():
    def __init__(self):
        # top = self.winfo_toplevel()
        # top.rowconfigure(0, weight=1, minsize=100)
        # top.columnconfigure(0, weight=1, minsize=100)
        # self.rowconfigure(0, weight=1, minsize=100)
        # self.columnconfigure([0, 1], weight=1, minsize=100)
        # self.pack_configure(anchor=tk.CENTER, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.root = tk.Tk()
        self.style = ttk.Style(self.root)
        self.set_default_styles()
        self.left = LeftFrame(self.root)
        self.right = RightFrame(self.root)
        self.hangmanCanvas = HangmanCanvas(self.left)
        self.guessesLFrame = GuessesLabelframe(self.right)
        self.guessesLabel = GuessesLabel(self.guessesLFrame)
        self.guessEntry = GuessEntry(self.right)
        # self.submitButton = SubmitButton(self.right)
        # self.clearButton = ClearButton(self.right)

    def set_default_styles(self):
        self.style.theme_use('default')


# if __name__ == '__main__':
#     main = MainApplication()
#     main.root.mainloop()
