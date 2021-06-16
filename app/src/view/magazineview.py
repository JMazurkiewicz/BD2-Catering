#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.inventoryview import InventoryView

class MagazineView(InventoryView):
    def __init__(self, parent, controller):
        InventoryView.__init__(self, parent, controller)
        self.__build_buttons()
        self.description.configure(text='Loading data from external DB...')


    def __build_buttons(self):
        button = tk.Button(self.button_frame, text='Add product to magazine')
        button.grid(row=0, column=0)
        button.configure(command=None) # TODO
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Remove product from magazine')
        button.grid(row=1, column=0)
        button.configure(command=None) # TODO
        self.buttons.append(button)
