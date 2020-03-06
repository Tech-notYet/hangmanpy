import sys
import typing as tp
from collections import defaultdict, namedtuple
from tkinter import ttk
from tkinter.ttk import tkinter as tk
from pprint import pprint as pp

DDICT = tp.DefaultDict[str, tp.Sequence[str]]

WIDGETS: tp.Tuple[str, ...] = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'LabeledScale', 'Labelframe',
                                'Menubutton', 'Notebook', 'OptionMenu', 'PanedWindow', 'Panedwindow', 'Progressbar', 'Radiobutton',
                                'Scale', 'Scrollbar', 'Separator', 'Sizegrip', 'Spinbox', 'Toplevel', 'Treeview')

class WidgetOptions():
    OPTIONS: DDICT

    def __new__(cls):
        cls.OPTIONS = cls.widget_options()
        return cls
    def __init__(self):
        self.OPTIONS = self.widget_options()
    
    @staticmethod
    def widget_options() -> DDICT:
        OPTIONS = defaultdict(list)
        for wgname in WIDGETS:
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
        return OPTIONS


if __name__ == '__main__':
    wo = WidgetOptions()
    for wg in wo.OPTIONS:
        print(f"({wg}, {wo.OPTIONS[wg]})")
    # opt_set = [set(wo.OPTIONS[wg]) for wg in wo.OPTIONS]
    # for opt in opt_set:
    #     if set_ > opt:
    #         opt_set.intersection_update()
    #     print({wg: dict((w,None) for w in _)})
        # print(f"namedtuple({wg}, '{' '.join(wo.OPTIONS[wg])}')")
    # pp(WidgetOptions.widget_options(sys.argv[1]))
    # wg = wo.WIDGETS[sys.argv[1]]
    # wopts = wo._widget_options(wg)
    # canvas = namedtuple(wg, wopts[wg])
    # print(wo)
