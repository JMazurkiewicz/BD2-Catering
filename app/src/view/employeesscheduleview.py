#!/usr/bin/env python
# @author Jakub Mazurkiewicz / Konrad  Wojewódzki

from model.employeeschedulemodel import EmployeeScheduleModel
from view.addextracostsview import ExtraCostsView
import tkinter as tk
from view.calendarview import CalendarView

class EmployeesScheduleView(CalendarView):
    def __init__(self, parent, controller):
        CalendarView.__init__(self, parent, controller)

        self.buttons = []
        self.__build_buttons()
        self.set_model(EmployeeScheduleModel())
        
        self.grid_columnconfigure(0, weight=1)

        self.cause = tk.Entry(self, width = 30)
        self.cost = tk.Entry(self, width = 30)


    def __build_buttons(self):
        button = tk.Button(self.button_frame, text='Show Order')
        button.grid(row=0, column=0)
        button.configure(command=self.on_show_order_location_button)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Add extra costs')
        button.grid(row=0, column=1)
        button.configure(command=self.on_add_extra_costs_button)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Main menu')
        button.grid(row=0, column=2)
        button.configure(command=self.controller.display_control_panel)
        self.buttons.append(button)


    def on_show_order_location_button(self):
        print('show order')


    def on_add_extra_costs_button(self):
        description = tk.Label(self, text = "Cost: ")
        description.grid(row = 7, column=0)
        self.cost.grid(row = 8, column=0)

        description = tk.Label(self, text = "Cause: ")
        description.grid(row = 9, column=0)
        self.cause.grid(row = 10, column=0)  

        button = tk.Button(self.button_frame, text='Save')
        button.grid(row=11, column=0)
        button.configure(command=self.save_changes)
        self.buttons.append(button)

    def save_changes(self):
        date = self.get_date()
        cost = self.cost.get()
        cause = self.cause.get()
        self.get_model().add_extra_costs(cost, cause, date)