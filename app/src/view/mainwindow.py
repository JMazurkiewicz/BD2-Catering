#!/usr/bin/env python
# @author: Jakub Mazurkiewicz

import tkinter as tk

from view.authorizationview import AuthorizationView

class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('Catering app - BD2')
        self.geometry('800x600')

        self.authorization_view = AuthorizationView(self)
                
