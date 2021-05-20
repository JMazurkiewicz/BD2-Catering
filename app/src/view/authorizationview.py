#!/usr/bin/env python
# @author: Jakub Mazurkiewicz

import tkinter as tk
from model import AuthorizationModel

ENTRY_WIDTH = 30
WELCOME = 'Cathering control panel'

class AuthorizationView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.model = AuthorizationModel()
        self.main_label = tk.Label(self, anchor=tk.CENTER, text=WELCOME)

        self.login_label = tk.Label(self, text='Login')
        self.login_entry = tk.Entry(self, width=ENTRY_WIDTH)

        self.password_label = tk.Label(self, text='Password')
        self.password_entry = tk.Entry(self, show='*', width=ENTRY_WIDTH)

        self.login_button = tk.Button(self, text='Log me in')
        self.error_label = tk.Label(self, fg='red')
        
        self.__build_gui()
        self.__build_commands()
        
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        self.pack()
        

    def __build_gui(self):
        self.main_label.grid(column=0, columnspan=3, row=0)

        self.login_label.grid(column=0, row=1)
        self.login_entry.grid(column=1, columnspan=2, row=1)

        self.password_label.grid(column=0, row=2)
        self.password_entry.grid(column=1, columnspan=2, row=2)

        self.login_button.grid(column=1, row=3)
        self.error_label.grid(column=0, columnspan=3, row=4)


    def __build_commands(self):
        self.login_button.configure(command=self.on_button_click)


    def on_button_click(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        if len(login) == 0:
            self.error_label.configure(text = 'Login cannot be empty')
            return
        elif len(password) == 0:
            self.error_label.configure(text = 'Password cannot be empty')
            return

        self.model.set_login(login)
        self.model.set_password(password)
        self.model.authorize()
