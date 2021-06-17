#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.inventoryview import InventoryView
from model.menumodel import MenuModel

class MenuView(InventoryView):
    def __init__(self, parent, controller):
        InventoryView.__init__(self, parent, controller)
        self.__build_buttons()
        self.description.configure(text='Loading data from external DB...')
        self.set_model(MenuModel())


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

        button = tk.Button(self.button_frame, text='Back to main menu')
        button.grid(row=3, column=0)
        button.configure(command=self.controller.display_control_panel)
        self.buttons.append(button)


    def update(self):
        self.description.configure(text=self.get_model().get_inventory_description())


    def on_add_new_meal_button_click(self):
        print('Niezaimplementowane :(')
        #self.controller.display_view()


    def on_delete_meal_button_click(self):
        print('Niezaimplementowane :(')

    
    def on_edit_meal_button_click(self):
        print('Niezaimplementowane :(')
