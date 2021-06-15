#!/usr/bin/env python
# @author Damian Piotrowski

import tkinter as tk
from view.formview import FormView

class NewOrderView(FormView):

    def __init__(self, parent):
        FormView.__init__(self, parent)

        self.add_entry('apetizer').set_description('Apetizer')
        self.add_entry('main_course').set_description('Main Course')
        self.add_entry('soup').set_description('Soup')
        self.add_entry('dessert').set_description('Dessert')
        self.add_entry('snacks').set_description('Snacks')
        self.add_entry('kitchen_hints').set_description('Kitchen Hints')

        self.save_button = tk.Button(self, text='Save')

        self.__build_grid()

    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=0, row=1)