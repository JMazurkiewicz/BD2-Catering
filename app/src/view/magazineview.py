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
        button.configure(command=self.on_add_product_to_magazine_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Remove product from magazine')
        button.grid(row=1, column=0)
        button.configure(command=self.on_remove_product_from_magazine_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Back to main menu')
        button.grid(row=2, column=0)
        button.configure(command=self.controller.display_control_panel)
        self.buttons.append(button)


    def on_add_product_to_magazine_button_click(self):
        print('on_add_product_to_magazine_button_click')


    def on_remove_product_from_magazine_button_click(self):
        print('on_remove_product_from_magazine_button_click')
