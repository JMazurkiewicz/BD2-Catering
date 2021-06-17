#!/usr/bin/env python
# @author Damian Piotrowski

from model.newordermodel import NewOrderModel
import tkinter as tk
from view.formview import FormView

class NewOrderView(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.type = ""

        self.add_entry('date').set_description('Date')
        self.add_entry('number_of_ppl').set_description('Number of people')
        self.add_entry('base_price').set_description('Base price')
        self.add_entry('waiters_needed').set_description('Waiters needed')

        self.save_button = tk.Button(self, text='Save')
        self.save_button.configure(command=self.on_save_button)

        self.person = tk.Button(self, text='Add person')
        self.person.configure(command=self.on_person_button)
        
        self.business = tk.Button(self, text='Add business')
        self.business.configure(command=self.on_business_button)

        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.display_control_panel)

        self.__build_grid()
        self.set_model(NewOrderModel())


    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=0, row=1)
        self.person.grid(column=1, row=1)
        self.business.grid(column=2, row=1)
        self.go_back_button.grid(column=3, row=1)
        

    def on_save_button(self):
        date = self.get_input('date')
        number_of_ppl = self.get_input('number_of_ppl')
        base_price = self.get_input('base_price')
        waiters_needed = self.get_input('waiters_needed')
        if(self.type == "Person"):
            client_id = self.get_model().find_person(self.get_input('name'), self.get_input('surname'))
        elif(self.type == "Business"):
            client_id = self.get_model().find_business(self.get_input('business'))

        self.get_model().insert_new_order(date, number_of_ppl, base_price, waiters_needed, client_id.client_id)


    def on_person_button(self):
        self.add_entry('name').set_description('Name')
        self.add_entry('surname').set_description('Surname')
        self.type = "Person"
        self.entry_frame.grid(column=0, row=0)
        

    def on_business_button(self):
        self.add_entry('business').set_description('NIP')
        self.type = "Business"
        self.entry_frame.grid(column=0, row=0)