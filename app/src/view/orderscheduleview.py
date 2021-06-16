#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.calendarview import CalendarView

#@TODO poprawić buttony

class OrderScheduleView(CalendarView):
    def __init__(self, parent, controller):
        CalendarView.__init__(self, parent, controller)

        self.__build_buttons()
        self.grid_columnconfigure(0, weight=1)


    def __build_buttons(self):
        button = tk.Button(self.button_frame, text='Add Order')
        button.grid(row=5, column=0)
        button.configure(command=self.on_add_order_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Edit Order')
        button.grid(row=5, column=1)
        button.configure(command=self.on_edit_order_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Delete Order')
        button.grid(row=5, column=2)
        button.configure(command=self.on_delete_order_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Add Employee')
        button.grid(row=5, column=3)
        button.configure(command=self.on_add_employee_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Show Order Info')
        button.grid(row=5, column=4)
        button.configure(command=self.on_show_order_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Main Menu')
        button.grid(row=5, column=5)
        button.configure(command=self.controller.display_control_panel)
        self.buttons.append(button)


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