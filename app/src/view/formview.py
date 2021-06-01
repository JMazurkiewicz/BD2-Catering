#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from view import View

class FormView(View):
    def __init__(self):
        print('FormView()')
        self.entries = {}


    def add_entry(self, entry, entry_name):
        self.entries[entry_name] = entry


    def get_input(self, entry_name):
        self.entries[entry_name].get_input()


    def set_error(self, entry_name, error_msg):
        self.entries[entry_name].set_error(error_msg)


    def update_grid(self):
        for row_index, entry in enumerate(self.entries.values()):
            entry.grid(row=row_index, column=0)
