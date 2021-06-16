#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.formview import FormView

class NewEmployeeView(FormView):
    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('name').set_description('Name')
        self.add_entry('surname').set_description('Surname')
        self.add_entry('pesel').set_description('Pesel (optional)')
        self.add_entry('phone-number').set_description('Phone number')
        self.add_entry('bank-account-number').set_description('Bank account number')
        
        self.add_entry('street-name').set_description('Street name')
        self.add_entry('building-number').set_description('Building number')
        self.add_entry('apartment-number').set_description('Apartment number (optional)')
        
        self.add_entry('city').set_description('City')
        self.add_entry('disctrict').set_description('District (optional)')

        self.add_button = tk.Button(self, text='Add', command=self.on_add_button_click)
        self.cancel_button = tk.Button(self, text='Cancel', command=self.on_cancel_button_click)

        self.__build_grid()


    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0, columnspan=2)
        self.add_button.grid(column=0, row=1)
        self.cancel_button.grid(column=1, row=1)


    def on_add_button_click(self):
        # TODO: submit 
        self.controller.display_control_panel()

    
    def on_cancel_button_click(self):
        self.controller.display_control_panel()
        