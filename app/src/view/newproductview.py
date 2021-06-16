#!/usr/bin/env python
# @author Damian Piotrowski

import tkinter as tk
from model.newproductmodel import NewProductModel
from view.formview import FormView

class NewProductView(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('catalog_number').set_description('Catalog Number')
        self.add_entry('name').set_description('Name')
        self.add_entry('price').set_description('Price')

        self.save_button = tk.Button(self, text='Save')
        self.save_button.configure(command=self.on_save_click)
        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.display_control_panel)

        self.set_model(NewProductModel())
        self.__build_grid()

    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=1, row=1)
        self.go_back_button.grid(column=0, row=1)

    def on_save_click(self):
        catalog_number = self.get_input('catalog_number')
        name = self.get_input('name')
        price = self.get_input('price')
        self.get_model().insert_new_product(catalog_number, name, price)

