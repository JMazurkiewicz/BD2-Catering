#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.calendarview import CalendarView
from view import View

class OrderScheduleView(CalendarView):
    def __init__(self, parent, controller):
        CalendarView.__init__(self, parent, controller)

        self.add_order_button = tk.Button(self.button_frame, text='Add order')
        self.edit_order_button = tk.Button(self.button_frame, text='Edit selected order')
        self.delete_order_button = tk.Button(self.button_frame, text='Delete selected order')
        self.add_employee_button = tk.Button(self.button_frame, text='Add employee to selected order')
        self.show_order_button = tk.Button(self.button_frame, text='Show info about selected order')

        self.add_order_button.config(command=self.on_add_order_button_click)
        self.edit_order_button.config(command=self.on_edit_order_button_click)
        self.delete_order_button.config(command=self.on_delete_order_button_click)
        self.add_employee_button.config(command=self.on_add_employee_button_click)
        self.show_order_button.config(command=self.on_show_order_button_click)

        self.add_order_button.grid(row=0, column=0)
        self.edit_order_button.grid(row=0, column=1)
        self.delete_order_button.grid(row=0, column=2)
        self.add_employee_button.grid(row=0, column=3)
        self.show_order_button.grid(row=0, column=4)


    def on_add_order_button_click(self):
        print('add order')


    def on_edit_order_button_click(self):
        print('edit order')

    
    def on_delete_order_button_click(self):
        print('delete order')

    def on_add_employee_button_click(self):
        print('add employee to order')


    def on_show_order_button_click(self):
        print('show order info')