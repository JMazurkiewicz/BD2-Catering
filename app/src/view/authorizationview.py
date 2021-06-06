#!/usr/bin/env python
# @author Jakub Mazurkiewicz

import tkinter as tk
from view.formview import FormView

class AuthorizationView(FormView):
    def __init__(self, parent):
        FormView.__init__(self, parent)
    
        self.main_label = tk.Label(self, anchor=tk.CENTER, text='Catering control panel')
        self.add_entry('login').set_description('Login')
        self.add_entry('password').set_description('Password')

        self.login_button = tk.Button(self, text='Log me in')
        self.info_label = tk.Label(self)

        self.__build_grid()
        self.__build_commands()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid(columnspan=10, rowspan=10)


    def __build_grid(self):
        self.main_label.grid(column=0, row=0)
        self.entry_container.grid(column=0, row=1, rowspan=2)
        self.login_button.grid(column=0, row=3)
        self.info_label.grid(column=0, row=4)


    def __build_commands(self):
        self.login_button.configure(command=self.on_button_click)


    def on_button_click(self):
        return None
        login = self.login_entry.get()
        password = self.password_entry.get()

        if len(login) == 0:
            self.__print_error_info('Login cannot be empty')
            return
        elif len(password) == 0:
            self.__print_error_info('Password cannot be empty')
            return
        else:
            self.__print_info('')

        try:
            self.model.set_login(login)
            self.model.set_password(password)
            response = self.model.authorize()
            self.__print_info(response)
        except Exception:
            self.__print_error_info('Authorization error!')
            return


    def __print_error_info(self, str):
        self.info_label.configure(fg='red')
        self.info_label.configure(text=str)


    def __print_info(self, str):
        self.info_label.configure(fg='black')
        self.info_label.config(text=str)
