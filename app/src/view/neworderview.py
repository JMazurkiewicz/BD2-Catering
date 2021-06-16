#!/usr/bin/env python
# @author Damian Piotrowski

import tkinter as tk
from view.formview import FormView

class NewOrderView(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('apetizer').set_description('Apetizer')
        self.add_entry('main_course').set_description('Main Course')
        self.add_entry('soup').set_description('Soup')
        self.add_entry('dessert').set_description('Dessert')
        self.add_entry('snacks').set_description('Snacks')
        self.add_entry('kitchen_hints').set_description('Kitchen Hints')

        self.save_button = tk.Button(self, text='Save')
        self.save_button.configure(command=self.on_save_button)

        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.display_control_panel)

        self.__build_grid()


    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=1, row=1)
        self.go_back_button.grid(column=0, row=1)

    def on_save_button(self):
        apetizer = self.get_input('apetizer')
        main_course = self.get_input('main_course')
        soup = self.get_input('soup')
        dessert = self.get_input('dessert')
        snacks = self.get_input('snacks')
        kitchen_hints = self.get_input('kitchen_hints')
        self.get_model().insert_new_product(apetizer, main_course, soup, dessert, snacks, kitchen_hints)