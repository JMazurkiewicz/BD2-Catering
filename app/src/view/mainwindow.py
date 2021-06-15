#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from os import path

from model import AuthorizationModel
from view.authorizationview import AuthorizationView
from view.orderscheduleview import OrderScheduleView
from view.employeesscheduleview import EmployeesScheduleView
from view.calendarview import CalendarView

class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('Catering app - BD2')
        self.geometry('800x600')

        self.iconphoto(False, tk.PhotoImage(file='view/img/cheese.png'))

        #self.authorization_model = AuthorizationModel()
        #self.authorization_view = AuthorizationView(self)
        #self.employees_schedule_view = EmployeesScheduleView(self)
        self.order_schedule_view = OrderScheduleView(self)
        
        #self.authorization_view.set_model(self.authorization_model)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        