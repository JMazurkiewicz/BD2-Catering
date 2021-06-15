#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from os import path

from view.authorizationview import AuthorizationView
from view.controlpanelview import ControlPanelView
from model.connectionmodel import ConnectionModel

# Class that represents main view AND main controller
class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.title('Catering app - BD2')
        self.geometry('800x600')
        self.iconphoto(False, tk.PhotoImage(file='view/img/cheese.png'))

        self.main_container = tk.Frame(self)
        self.main_container.pack(side='top', fill='both', expand=True)

        # List of views
        self.views = {}

        # SQL connection
        self.connection = ConnectionModel() 

        for V in (AuthorizationView, ControlPanelView):
            view = V(self.main_container, self)

            if not isinstance(view, AuthorizationView):
                view.set_model(self.connection)

            self.views[V] = view
            view.grid(row=0, column=0, sticky='nsew')

        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)

        self.display_view(AuthorizationView)
        
    
    def display_view(self, V):
        view = self.views[V]
        view.tkraise()
