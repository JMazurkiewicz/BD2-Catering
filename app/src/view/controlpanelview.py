#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view import View

class ControlPanelView(View):
    def __init__(self, parent, controller):
        View.__init__(self, parent, controller)

        self.button_frame = tk.Frame(self)
        self.buttons = []
        self.__build_buttons()

    
    def __build_buttons(self):
        self.__add_button(text='Show orders')
        self.__add_button(text='New order')
        self.__add_button(text='xD')

    
    def __add_button(self, *args, **kwargs):
        button = tk.Button(self.button_frame, *args, **kwargs);
        column_index = len(self.buttons)
        button.grid(row=0, column=column_index)
        self.buttons.append(button)
