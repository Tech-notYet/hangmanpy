import sys
import typing as Tp
from collections import defaultdict, namedtuple
from tkinter import ttk
from tkinter.ttk import tkinter as tk
from pprint import pprint as pp


class WidgetOptions():
    _WIDGETS = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'LabeledScale', 'Labelframe',
               'Menubutton', 'Notebook', 'OptionMenu', 'PanedWindow', 'Panedwindow', 'Progressbar', 'Radiobutton',
               'Scale', 'Scrollbar', 'Separator', 'Sizegrip', 'Spinbox', 'Toplevel', 'Treeview')

    def __new__(cls):
        cls.__setattr__('OPTIONS', defaultdict(list))
        pass

    # def __init__(self):
    #     super().__init__()
    #     self.WIDGETS = {w: w for w in self._WIDGETS}

    def return_widget_options(self, widgetname: str) -> Tp.Mapping[str, Tp.Sequence[str]]:
        OPTIONS = self.OPTIONS
        wgname = widgetname
        if wgname is None:
            wgname = 'Frame'
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

if __name__ == '__main__':
    wo = WidgetOptions()
    wg = wo.WIDGETS[sys.argv[1]]
    wopts = wo.return_widget_options(wg)
    canvas = namedtuple(wg, wopts[wg])
    print(canvas)
