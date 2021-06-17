#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from model.newemployeemodel import NewEmployeeModel
import tkinter as tk
from view.formview import FormView

class NewEmployeeView(FormView):
    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('name').set_description('Name')
        self.add_entry('surname').set_description('Surname')
        self.add_entry('pesel').set_description('Pesel (optional)')
        self.add_entry('phone_number').set_description('Phone number')
        self.add_entry('bank_account_number').set_description('Bank account number')
        
        self.add_entry('postal_code').set_description('Postal code')
        self.add_entry('street_name').set_description('Street name')
        self.add_entry('building_number').set_description('Building number')
        self.add_entry('apartment_number').set_description('Apartment number (optional)')
        
        self.add_entry('city').set_description('City')
        self.add_entry('disctrict').set_description('District (optional)')

        self.add_button = tk.Button(self, text='Add', command=self.on_add_button_click)
        self.cancel_button = tk.Button(self, text='Cancel', command=self.on_cancel_button_click)

        self.__build_grid()
        self.set_model(NewEmployeeModel())


    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0, columnspan=2)
        self.add_button.grid(column=0, row=1)
        self.cancel_button.grid(column=1, row=1)


    def on_add_button_click(self):
        name = self.get_input('name')
        surname = self.get_input('surname')
        pesel = self.get_input('pesel')
        phone_number = self.get_input('phone_number')
        bank_account_number = self.get_input('bank_account_number')
        postal_code = self.get_input('postal_code')
        street_name = self.get_input('street_name')
        building_number = self.get_input('building_number')
        apartment_number = self.get_input('apartment_number')
        city = self.get_input('city')
        disctrict = self.get_input('disctrict')
        self.get_model().insert_new_employee(name, surname, pesel, phone_number, bank_account_number, postal_code, street_name, building_number, apartment_number, city, disctrict)
        #self.controller.display_control_panel()

    
    def on_cancel_button_click(self):
        self.controller.display_control_panel()
        