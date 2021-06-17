#!/usr/bin/env python
# @author Jakub Mazurkiewicz / Konrad Wojewódzki

from view.formview import FormView
from view.neworderview import NewOrderView
import tkinter as tk
import datetime
from view.calendarview import CalendarView
from model.orderschedulemodel import OrderScheduleModel

#@TODO poprawić buttony

class OrderScheduleView(CalendarView):
    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)
        CalendarView.__init__(self, parent, controller)

        self.set_model(OrderScheduleModel())
        self.__build_buttons()
        self.grid_columnconfigure(0, weight=1)

        
        self.name = tk.Entry(self, width = 30)
        self.surname = tk.Entry(self, width = 30)



    def __build_buttons(self):
        button = tk.Button(self.button_frame, text='Add Order')
        button.grid(row=5, column=0)
        button.configure(command=self.on_add_order_button_click)
        self.buttons.append(button)

        button = tk.Button(self.button_frame, text='Show Event')
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
        self.__set_events()
        print('edit order (TODO)')

    
    def on_delete_order_button_click(self):
        date = self.get_date()
        self.get_model().delete_order(date)
        print('delete order')


    def on_add_employee_button_click(self):
        

        description = tk.Label(self, text = "Name: ")
        description.grid(row = 7, column=0)
        self.name.grid(row = 8, column=0)

        description = tk.Label(self, text = "Surname: ")
        description.grid(row = 9, column=0)
        self.surname.grid(row = 10, column=0)  

        button = tk.Button(self.button_frame, text='Save')
        button.grid(row=11, column=0)
        button.configure(command=self.save_changes)
        self.buttons.append(button)

        print('add employee to order')


    def on_show_order_button_click(self):
        date = self.get_date()
        cursor = self.get_model().show_order_info(date)
        description = ''
        
        row = cursor.fetchone()
        for i in range(0, len(row)):
            description += str(row[i]) + ' '

        description = tk.Label(self, text = description)
        description.grid(row = 7, column=0)

        print('show order info')

    def save_changes(self):
        date = self.get_date()
        name = self.name.get()
        surname = self.surname.get()
        print('adding...')
        self.get_model().add_employee_to_event(date, name, surname)

    def __set_events(self):
        cursor = self.get_model().get_date_and_type()
        info = cursor.fetchone()
        while info:
            date = datetime.date(year=int(info.year), month=int(info.month), day=int(info.day))
            self.calendar.calevent_create(date, info.event_name ,info.event_name)
            info = cursor.fetchone()

