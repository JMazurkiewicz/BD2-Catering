#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.calendarview import CalendarView

class EmployeesScheduleView(CalendarView):
    def __init__(self, parent, controller):
        CalendarView.__init__(self, parent, controller)

        self.show_order_location_button = tk.Button(self.button_frame, text='Show Order')
        self.add_extra_costs_button = tk.Button(self.button_frame, text='Add extra costs')

        self.show_order_location_button.config(command=self.on_show_order_location_button_click)
        self.add_extra_costs_button.config(command=self.on_add_extra_costs_button_click)

        self.show_order_location_button.grid(row=0, column=0)
        self.add_extra_costs_button.grid(row=0, column=1)

    def on_show_order_location_button_click(self):
        print('show order')


    def on_add_extra_costs_button_click(self):
        print('add extra costs')
