#!/usr/bin/env python
# @author Damian Piotrowski

import tkinter as tk
from view.formview import FormView

class NewProductView(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('catalog_number').set_description('Catalog Number')
        self.add_entry('name').set_description('Name')
        self.add_entry('price').set_description('Price')

        self.save_button = tk.Button(self, text='Save')
        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.go_to_control_panel)

        self.__build_grid()

    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=1, row=1)
        self.go_back_button.grid(column=0, row=1)