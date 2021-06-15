#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view import View

class ControlPanelView(View):
    def __init__(self, parent, controller):
        View.__init__(self, parent, controller)

        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=0, column=0)

        self.buttons = []
        self.__build_buttons()
        self.grid_columnconfigure(0, weight=1)

    
    def __build_buttons(self):
        button = tk.Button(self.button_frame, text='Products')
        button.grid(row=0, column=0)
        self.buttons.append(button)


        button = tk.Button(self.button_frame, text='Vehicles')
        button.grid(row=0, column=1)
        self.buttons.append(button)


        button = tk.Button(self.button_frame, text='Magazine')
        button.grid(row=0, column=2)
        self.buttons.append(button)


        button = tk.Button(self.button_frame, text='Menu')
        button.grid(row=0, column=3)
        self.buttons.append(button)


        button = tk.Button(self.button_frame, text='Edit employees')
        button.grid(row=1, column=0)
        self.buttons.append(button)


        button = tk.Button(self.button_frame, text='Add employee')
        button.grid(row=1, column=1)
        self.buttons.append(button)


        button = tk.Button(self.button_frame, text='Order calendar')
        button.grid(row=1, column=2)
        self.buttons.append(button)


        button = tk.Button(self.button_frame, text='Employee calendar')
        button.grid(row=1, column=3)
        self.buttons.append(button)


    def __add_button(self, text, command):
        button = tk.Button(self.button_frame, text=text, command=command)
        
