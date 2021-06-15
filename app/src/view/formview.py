#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.formentryview import FormEntryView
from view import View

class FormView(View):
    def __init__(self, parent, controller):
        View.__init__(self, parent, controller)

        self.entry_frame = tk.Frame(self)
        self.entry_frame.grid_rowconfigure(0, weight=1)
        self.entry_frame.grid_columnconfigure(0, weight=1)

        self.entries = {}


    def add_entry(self, entry_name):
        row_index = len(self.entries)
        self.entries[entry_name] = FormEntryView(self.entry_frame, row_index)

        self.grid(rowspan=row_index+1)

        return self.entries[entry_name]


    def get_input(self, entry_name):
        return self.entries[entry_name].get_input()


    def set_error(self, entry_name, error_msg):
        self.entries[entry_name].set_error(error_msg)


    def reset_all_errors(self):
        for entry in self.entries.values():
            entry.set_error('')
