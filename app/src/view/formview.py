#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.formentryview import FormEntryView
from view import View

class FormView(View):
    def __init__(self, parent):
        View.__init__(self, parent)
        
        self.entry_container = tk.Frame(self)
        self.entries = {}


    def add_entry(self, entry_name):
        self.entries[entry_name] = FormEntryView(self.entry_container)

        row_index = len(self.entries)
        self.entries[entry_name].grid(row=row_index-1, column=0)

        self.grid(rowspan=row_index)

        return self.entries[entry_name]


    def get_input(self, entry_name):
        self.entries[entry_name].get_input()


    def set_error(self, entry_name, error_msg):
        self.entries[entry_name].set_error(error_msg)
