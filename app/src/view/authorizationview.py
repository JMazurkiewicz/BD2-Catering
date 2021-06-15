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


    def __build_grid(self):
        self.main_label.grid(column=0, row=0)
        self.entry_frame.grid(column=0, row=1, rowspan=2)
        self.login_button.grid(column=0, row=3)
        self.info_label.grid(column=0, row=4)


    def __build_commands(self):
        self.login_button.configure(command=self.on_button_click)


    def on_button_click(self):
        login = self.get_input('login')
        password = self.get_input('password')

        self.reset_all_errors()
        self.info_label.config(text='')

        error_flag = False

        if len(login) == 0:
            self.set_error('login', 'Login cannot be empty')
            error_flag = True
        
        if len(password) == 0:
            self.set_error('password', 'Password cannot be empty')
            error_flag = True

        if error_flag:
            return

        try:
            self.model.set_login(login)
            self.model.set_password(password)
            self.model.authorize()
            print('Success!')
        except Exception as e:
            print('Authorization error: {}'.format(e))
            self.info_label.config(text='Authorization error', fg='red')
            return
