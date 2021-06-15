#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from os import path

from model import AuthorizationModel
from view.authorizationview import AuthorizationView
from view.newmealview import NewMealView
from view.neworderview import NewOrderView
from view.newproductview import NewProductView

class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('Catering app - BD2')
        self.geometry('800x600')

        self.iconphoto(False, tk.PhotoImage(file='view/img/cheese.png'))

        #self.authorization_model = AuthorizationModel()
        #self.authorization_view = AuthorizationView(self)
        self.newmeal_view = NewMealView(self)
        #self.neworder_view = NewOrderView(self)
        #self.newproduct_view = NewProductView(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #self.autorization_view.set_model(self.authorization_model)
        