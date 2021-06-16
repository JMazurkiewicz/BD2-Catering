#!/usr/bin/env python
# @author Jakub Mazurkiewicz


import tkinter as tk
from view.addextracostsview import ExtraCostsView
from view.newemployeeview import NewEmployeeView
from view.magazineview import MagazineView
from view.authorizationview import AuthorizationView
from view.newmealview import NewMealView
from view.neworderview import NewOrderView
from view.newproductview import NewProductView
from view.newstorageentryview import NewStorageEntryView
from view.controlpanelview import ControlPanelView
from view.calendarview import CalendarView
from view.employeesscheduleview import EmployeesScheduleView
from view.orderscheduleview import OrderScheduleView
from view.menuview import MenuView

# Class that represents main view AND main controller
class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.title('Catering app - BD2')
        self.geometry('800x600')
        self.iconphoto(False, tk.PhotoImage(file='view/img/cheese.png'))
        
        self.main_container = tk.Frame(self)
        self.main_container.pack(side='top', fill='both', expand=True)

        # List of views
        self.views = {}

        # Database connection
        self.connection = None

        for V in (AuthorizationView, ControlPanelView, NewMealView, NewOrderView, NewProductView, EmployeesScheduleView, OrderScheduleView, MagazineView, MenuView, NewStorageEntryView, NewEmployeeView, ExtraCostsView):
            view = V(self.main_container, self)

            print (V)

            if not isinstance(view, AuthorizationView):
                view.get_model().set_connection(self.connection)

            self.views[V] = view
            view.grid(row=0, column=0, sticky='nsew')

        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)

        self.display_view(AuthorizationView)
        
    
    def display_view(self, V):
        view = self.views[V]
        view.tkraise()
        

    def display_control_panel(self):
        self.display_view(ControlPanelView)

    
    def update_connection(self, connection):
        self.connection = connection
