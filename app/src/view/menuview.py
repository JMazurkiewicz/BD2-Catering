#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.inventoryview import InventoryView

class MenuView(InventoryView):
    def __init__(self, parent, controller):
        InventoryView.__init__(self, parent, controller)
        self.__build_buttons()
        self.description.configure(text='Loading data from external DB...')


    def __build_buttons(self):
        button = tk.Button(self.button_frame, text='Add new meal')
        button.grid(row=0, column=0)
        button.configure(command=self.on_add_new_meal_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Delete meal')
        button.grid(row=1, column=0)
        button.configure(command=self.on_delete_meal_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Edit meal')
        button.grid(row=2, column=0)
        button.configure(command=self.on_edit_meal_button_click)
        self.buttons.append(button)


    def on_add_new_meal_button_click(self):
        print('on_add_new_meal_button_click')


    def on_delete_meal_button_click(self):
        print('on_delete_meal_button_click')

    
    def on_edit_meal_button_click(self):
        print('on_edit_meal_button_click')
