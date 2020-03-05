import typing as Tp
from collections import defaultdict, namedtuple
from tkinter import ttk
from tkinter.ttk import tkinter as tk

WIDGETS = ('Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'LabeledScale', 'Labelframe',
            'Menubutton', 'Notebook', 'OptionMenu', 'PanedWindow', 'Panedwindow', 'Progressbar', 'Radiobutton',
            'Scale', 'Scrollbar', 'Separator', 'Sizegrip', 'Spinbox', 'Toplevel', 'Treeview')

def return_widget_options(widgetname: str) -> Tp.Sequence[str]:
        OPTIONS = defaultdict(list)
        if widgetname in WIDGETS:
            source = ''
            try:
                if widgetname == 'Canvas' or widgetname == 'Toplevel':
                    source = 'tk.'+widgetname+'().keys()'
                elif widgetname == 'OptionMenu':
                    source = 'ttk.'+widgetname+'(None, None).keys()'
                else:
                    source = 'ttk.'+widgetname+'().keys()'
                obj = eval(compile(source, '<string>', 'eval'))
                OPTIONS[widgetname].extend(obj)
            except Exception as e:
                print(f'{widgetname}\t{e.args}')
        return OPTIONS[widgetname]

# BUTTON = namedtuple('Button', ['command', 'default', 'takefocus', 'text', 'textvariable',
#                                'underline', 'width', 'image', 'compound', 'padding', 'state', 'cursor', 'style', 'class'])
CANVAS = namedtuple('Canvas', return_widget_options('Canvas'))



def widget_options():

    def __init__(self):
        super().__init__()
        self.OPTIONS = defaultdict(list)

    def return_widget_options(self, widgetnames: Tp.Sequence[str]) -> Tp.Sequence[Tp.Se]:
        OPTIONS = self.OPTIONS
        if widgetname in self.WIDGETS:
            source = ''
            try:
                if widgetname == 'Canvas' or widgetname == 'Toplevel':
                    source = 'tk.'+widgetname+'().keys()'
                elif widgetname == 'OptionMenu':
                    source = 'ttk.'+widgetname+'(None, None).keys()'
                else:
                    source = 'ttk.'+widgetname+'().keys()'
                obj = eval(compile(source, '<string>', 'eval'))
                OPTIONS[widgetname].extend(obj)
            except Exception as e:
                print(f'{widgetname}\t{e.args}')
        return OPTIONS

# Top structure classes


class LeftFrame(ttk.Frame):
    """Child of MainApplication. It contains the Canvas widget"""

    __doc__ = WidgetOptions().return_widget_options()

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.configure(width=400, height=400, padding='0.25i',
                       borderwidth=1, relief=tk.RIDGE)
        self.grid(sticky=tk.NSEW)


class RightFrame(ttk.Frame):
    """Child of MainApplication. It contains the remaining widgets"""

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.configure(width=400, height=400, padding='0.25i',
                       borderwidth=1, relief=tk.GROOVE)
        # 1x3 Grid to fit widgets
        self.rowconfigure([0, 1, 2], weight=1)
        self.columnconfigure(0, weight=1)
        # Grid into column 2 of MainApp
        self.grid(column=1, row=0, sticky=tk.NSEW)


class HangmanCanvas(tk.Canvas):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        opts = {
            'bg': '#f8f8f8',
            'relief': tk.GROOVE,
            'cursor': 'man',
            'height': master['height'] - 50,
            'width': master['width'] - 50
        }
        self.configure(**opts)
        self.pack()
        line = []
        for y in range(5, 125, 5):
            line.append([5, y])
        self.create_line(line)


class GuessesLabel(ttk.Label):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.configure()


class GuessEntry(ttk.Entry):
    def __init__(self, master=None, widget=None, **kw):
        super().__init__(master=master, widget=widget, **kw)


class SubmitButton(ttk.Button):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)


class ClearButton(ttk.Button):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)


class MainApplication(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1, minsize=100)
        top.columnconfigure(0, weight=1, minsize=100)
        self.rowconfigure(0, weight=1, minsize=100)
        self.columnconfigure([0, 1], weight=1, minsize=100)
        self.grid(sticky=tk.NSEW, padx=25, pady=25)

        self.left = LeftFrame(self)
        self.right = RightFrame(self)
        self.hangmanCanvas = HangmanCanvas(self.left)
        self.guessesLabel = GuessesLabel(self.right)
        self.guessEntry = GuessEntry(self.right)
        self.submitButton = SubmitButton(self.right)
        self.clearButton = ClearButton(self.right)


if __name__ == '__main__':
    main = MainApplication()
    main.mainloop()
