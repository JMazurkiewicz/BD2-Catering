#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from view.view import View
import tkinter as tk

DEFAULT_FORM_ENTRY_WIDTH = 30

class FormEntryView(View):
    def __init__(self, parent, row, grid_style='default'):
        View.__init__(self, parent)

        self.description = tk.Label(parent)
        self.entry = tk.Entry(parent, width=DEFAULT_FORM_ENTRY_WIDTH)
        self.error_label = tk.Label(parent, fg='red')
        self.validator = lambda: None

        self.__build_grid(row, grid_style)


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


    def __build_grid(self, row, grid_style):
        if grid_style == 'default':
            self.__build_default_grid(row)
        else:
            raise Exception('FormEntryView: invalid grid style')


    def __build_default_grid(self, row):
        self.description.grid(column=0, row=row)
        self.entry.grid(column=1, row=row)
        self.error_label.grid(column=2, row=row)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
