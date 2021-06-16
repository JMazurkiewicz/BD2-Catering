#!/usr/bin/env python
# @author Damian Piotrowski

import tkinter as tk
from view.formview import FormView

class NewStorageEntryView(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('catalog_number').set_description('Catalog Number')
        self.add_entry('amount').set_description('Amount')
        self.add_entry('expiration_date').set_description('Expiration Date')
        self.add_entry('batch_number').set_description('Batch Number')

        self.save_button = tk.Button(self, text='Save')
        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.display_control_panel)

        self.__build_grid()
        self.__build_commands

    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=0, row=1)
        self.go_back_button.grid(column=1, row=1)

    def __build_commands(self):
        self.save_button.configure(command=self.on_button_click)

    def on_button_click(self):
        return None

        