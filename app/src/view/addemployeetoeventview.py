#!/usr/bin/env python
# @author Konrad Wojewódzki

from model.orderschedulemodel import OrderScheduleModel
import tkinter as tk
from view.formview import FormView

class AddEmployeeToOrder(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('name').set_description('Name')
        self.add_entry('surname').set_description('Surname')

        self.save_button = tk.Button(self, text='Save')
        self.save_button.configure(command=self.on_save_button)

        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.display_control_panel)

        self.__build_grid()

        self.set_model(OrderScheduleModel())


    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=1, row=1)
        self.go_back_button.grid(column=0, row=1)

    def on_save_button(self):
        name = self.get_input('name')
        surname = self.get_input('surname')

        self.get_model().insert_new_product(name, surname)