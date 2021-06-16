#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from model import Model
import pyodbc

class AuthorizationModel(Model):
    def __init__(self):
        self.login = ''
        self.password = ''
        self.user_type = -1

        self.server = 'bd2-catering.database.windows.net'
        self.database = 'Catering'
        self.driver = '{SQL Server}'


    def set_login(self, login):
        self.login = login


    def set_password(self, password):
        self.password = password


    def authorize(self):
        print('Verification started...')
        str = 'DRIVER={};SERVER={};PORT=1433;DATABASE={};UID={};PWD={}'.format(self.driver, self.server, self.database, self.login, self.password)
        
        self.connection = pyodbc.connect(str)


    def get_user_type(self):
        return self.user_type
        