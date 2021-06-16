#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import datetime
import tkinter as tk
from tkcalendar import Calendar, DateEntry

from view import View

class CalendarView(View):
    def __init__(self, parent, controller):
        View.__init__(self, parent, controller)
        
        self.mindate = datetime.date.today() - datetime.timedelta(days = 30)

        self.calendar = Calendar(parent, font="Comic_Sans 14", selectmode='day', locale='en_US',
                   mindate=self.mindate, disabledforeground='red',
                   cursor="hand2")

        self.calendar.tag_config('komunia', background = 'yellow', foreground = 'black')
        self.calendar.tag_config('wesele', background = 'red', foreground = 'black')
        self.calendar.tag_config('spotkanie_biznesowe', background = 'blue', foreground = 'white')
        self.calendar.tag_config('urodziny', background = 'black', foreground = 'yellow')

        self.button_frame = tk.Frame(parent)
        self.__build_grid()

        self.grid_columnconfigure(0, weight=1)
    
    def __build_grid(self):
        print('CalendarView::__build_grid')
        self.calendar.grid(column=0, row=0)
        self.button_frame.grid(column=0, row=1)
        