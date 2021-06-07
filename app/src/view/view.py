#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk

class View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.model = None

    
    def set_model(self, model):
        self.model = model


    def update(self):
        pass