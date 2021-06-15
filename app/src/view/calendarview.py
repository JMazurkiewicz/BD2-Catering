#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from tkcalendar import Calendar, DateEntry

from view import View

class CalendarView(View):
    def __init__(self, parent):
        View.__init__(self, parent)
        self.calendar = Calendar(self, selectmode='none')
        self.button_frame = tk.Frame(self)
        self.__build_grid()

    
    def __build_grid(self):
        print('CalendarView::__build_grid')
        self.calendar.grid(row=0, column=0)
        self.button_frame.grid(row=1, column=0)
        