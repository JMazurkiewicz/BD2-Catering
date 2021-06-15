#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk

class View(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent_view = None
        self.model = None
        self.controller = controller


    def set_model(self, model):
        self.model = model


    def set_parent_view(self, parent_view):
        self.parent_view = parent_view


    def update(self):
        pass