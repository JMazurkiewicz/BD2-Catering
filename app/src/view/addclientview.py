#!/usr/bin/env python
# @author Damian Piotrowski


import tkinter as tk
from view.formview import FormView
from model.addclientmodel import NewClientModel

class NewClientView(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('type').set_description('Person or Business')
        self.add_entry('name').set_description('Name')
        self.add_entry('surname').set_description('Surname')
        self.add_entry('phone').set_description('Phone Number')
        self.add_entry('email').set_description('E-mail address')
        self.add_entry('nip').set_description('NIP (if needed)')

        self.add_entry('city').set_description('City')
        self.add_entry('district').set_description('Ditstrict')
        self.add_entry('postal').set_description('Postal code')
        self.add_entry('street').set_description('Street')
        self.add_entry('building').set_description('Building Number')
        self.add_entry('apartment').set_description('Apartment Number')

        self.save_button = tk.Button(self, text='Save')
        self.save_button.configure(command=self.on_save_click)
        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.display_control_panel)

        self.set_model(NewClientModel())
        self.__build_grid()


    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=1, row=1)
        self.go_back_button.grid(column=0, row=1)

    def on_save_click(self):
        city = self.get_input('city')
        street = self.get_input('street')
        building = self.get_input('building')
        apartment = self.get_input('apartment')
        postal = self.get_input('postal')
        district = self.get_input('district')

        if self.get_input('type') in ('Person', 'person', 'PERSON'):
            name = self.get_input('name')
            surname = self.get_input('surname')
            phone = self.get_input('phone')
            email = self.get_input('email')

            self.get_model().add_person(name, surname, phone, email, postal, street, building, apartment, city, district)
        

        elif  self.get_input('type') in ('Business', 'business', 'BUSINESS'):
            nip = self.get_input('nip')
            self.get_model().add_business(postal, street, building, apartment, city, district, nip)



        #self.get_model().insert_new_product(catalog_number, name, price)

