#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view import View

class InventoryView(View):
    def __init__(self, parent, controller):
        View.__init__(self, parent, controller)

        self.scroll_frame = tk.Scrollbar(self)
        self.description = tk.Label(self)

        self.button_frame = tk.Frame(self)
        self.buttons = []
        self.__build_grid()
        

    def __build_grid(self):
        self.description.grid(row=0, column=0, padx=(0, 50))
        self.button_frame.grid(row=0, column=1)
