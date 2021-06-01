#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from view import View
import tkinter as tk

class FromEntryView(View):
    def __init__(self, parent, name, grid_style='default'):
        super.__init__(self, parent)

        self.entry = tk.Entry()
        self.description = tk.Label()
        self.error_label = tk.Label()

        self.entry_name = name
        self.validator = lambda: None

        self.__build_grid(grid_style)


    def set_validator(self, validator):
        self.validator = validator


    def get_input(self):
        return self.entry.get()


    def set_error(self, error_msg):
        self.error_label.configure(text=error_msg)


    def __build_grid(self, grid_style):
        if grid_style == 'default':
            self.__build_default_grid()


    def __build_default_grid(self):
        self.entry.grid(column=0, columnspan=2)
        self.description.grid(column=2, columnspan=5)
        self.description.grid(column=7, columnspan=3)
