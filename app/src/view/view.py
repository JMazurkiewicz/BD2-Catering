#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk

class View(tk.Frame):
    def __init__(self):
        self.model = None

    
    def set_model(self, model):
        self.model = model
