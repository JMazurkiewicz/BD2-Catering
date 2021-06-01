#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from view.view import View
import tkinter as tk

DEFAULT_FORM_ENTRY_WIDTH = 30

class FormEntryView(View):
    def __init__(self, parent, grid_style='default'):
        View.__init__(self, parent)

        self.description = tk.Label()
        self.entry = tk.Entry(width=DEFAULT_FORM_ENTRY_WIDTH)
        self.error_label = tk.Label(fg='red')

        self.validator = lambda: None

        self.__build_grid(grid_style)


    def set_description(self, description):
        self.description.configure(text=description)
        return self


    def set_width(self, new_width):
        self.entry.configure(width=new_width)
        return self


    def set_validator(self, validator):
        self.validator = validator
        return self


    def set_error(self, error_msg):
        self.error_label.configure(text=error_msg)
        return self


    def get_input(self):
        return self.entry.get()


    def __build_grid(self, grid_style):
        if grid_style == 'default':
            self.__build_default_grid()


    def __build_default_grid(self):
        self.description.grid(column=0, columnspan=2, row=0)
        self.entry.grid(column=3, columnspan=5, row=0)
        self.error_label.grid(column=8, columnspan=3, row=0)
