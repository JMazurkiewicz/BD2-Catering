#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from os import path

from view.formentryview import FormEntryView

class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('Catering app - BD2')
        self.geometry('800x600')

        self.iconphoto(False, tk.PhotoImage(file='view/img/cheese.png'))

        self.x = FormEntryView(self)
        self.x.set_description('TEST')
        self.x.set_error('ERROR :((')
                
