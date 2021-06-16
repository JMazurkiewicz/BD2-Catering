#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.calendarview import CalendarView

class EmployeesScheduleView(CalendarView):
    def __init__(self, parent, controller):
        CalendarView.__init__(self, parent, controller)

        self.buttons = []
        self.__build_buttons()
        
        self.grid_columnconfigure(0, weight=1)


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
        button.configure(command=self.controller.go_to_control_panel)
        self.buttons.append(button)


    def on_show_order_location_button(self):
        print('show order')


    def on_add_extra_costs_button(self):
        print('add extra costs')
