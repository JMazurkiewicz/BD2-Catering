#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from os import path

from model import AuthorizationModel
from view.authorizationview import AuthorizationView

class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('Catering app - BD2')
        self.geometry('800x600')

        self.iconphoto(False, tk.PhotoImage(file='view/img/cheese.png'))

        #self.authorization_model = AuthorizationModel()
        self.authorization_view = AuthorizationView(self)
        #self.autorization_view.set_model(self.authorization_model)
        