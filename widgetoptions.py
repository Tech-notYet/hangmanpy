import sys
import typing as tp
from collections import defaultdict, namedtuple
from tkinter import ttk
from tkinter.ttk import tkinter as tk
from pprint import pprint as pp

DDict = tp.DefaultDict[str, tp.Sequence[str]]


class WidgetOptions():
    WIDGETS: tp.Tuple[str, ...] = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'LabeledScale', 'Labelframe',
                                   'Menubutton', 'Notebook', 'OptionMenu', 'PanedWindow', 'Panedwindow', 'Progressbar', 'Radiobutton',
                                   'Scale', 'Scrollbar', 'Separator', 'Sizegrip', 'Spinbox', 'Toplevel', 'Treeview')

    def __init__(self):
        super().__init__()
        self.OPTIONS: DDict = defaultdict(list)

    @classmethod
    def widget_options(cls, widgetname: tp.Optional[str] = None) -> DDict:
        OPTIONS = defaultdict(list)
        wgname = widgetname
        if wgname is None:
            wgname = 'Frame'
        if wgname in cls.WIDGETS:
            source = ''
            try:
                if wgname in ('Canvas', 'Toplevel'):
                    source = 'tk.' + wgname + '().keys()'
                elif wgname == 'OptionMenu':
                    source = 'ttk.' + wgname + '(None, None).keys()'
                else:
                    source = 'ttk.'+wgname+'().keys()'
                obj = eval(compile(source, '<string>', 'eval'))
                OPTIONS[wgname].extend(obj)
            except Exception as e:
                print(f'{wgname}\t{e.args}')
        return OPTIONS[wgname]


if __name__ == '__main__':
    pp(WidgetOptions.widget_options(sys.argv[1]))
    # wg = wo.WIDGETS[sys.argv[1]]
    # wopts = wo._widget_options(wg)
    # canvas = namedtuple(wg, wopts[wg])
    # print(wo)
