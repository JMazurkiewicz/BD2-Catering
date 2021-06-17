#!/usr/bin/env python
# @author Jakub Mazurkiewicz / Konrad Wojewódzki

from view.addemployeetoeventview import AddEmployeeToOrder
from view.formview import FormView
from view.neworderview import NewOrderView
import tkinter as tk
from view.calendarview import CalendarView
from model.orderschedulemodel import OrderScheduleModel

#@TODO poprawić buttony

class OrderScheduleView(CalendarView):
    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)
        CalendarView.__init__(self, parent, controller)

        self.__build_buttons()
        self.grid_columnconfigure(0, weight=1)
        
        self.set_model(OrderScheduleModel())

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
        self.controller.display_view(NewOrderView)


    def on_edit_order_button_click(self):
        print('edit order (TODO)')

    
    def on_delete_order_button_click(self):
        date = self.get_date()
        self.get_model().delete_order(date)
        print('delete order')


    def on_add_employee_button_click(self):
        name = tk.Entry(self, width = 30)
        surname = tk.Entry(self, width = 30)
        
        description = tk.Label(self, text = "Name: ")
        description.grid(row = 7, column=0)
        name.grid(row = 8, column=0)

        description = tk.Label(self, text = "Surname: ")
        description.grid(row = 9, column=0)
        surname.grid(row = 10, column=0)

        button = tk.Button(self.button_frame, text='Main Menu')
        button.grid(row=5, column=5)
        button.configure(command=self.controller.display_control_panel)
        self.buttons.append(button)
        print('add employee to order')


    def on_show_order_button_click(self):
        date = self.get_date()
        self.get_model().show_order_info(date)
        print('show order info')