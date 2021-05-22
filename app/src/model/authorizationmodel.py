#!/usr/bin/env python
# @author: Jakub Mazurkiewicz

import pyodbc

class AuthorizationModel:
    def __init__(self):
        self.login = ''
        self.password = ''
        self.user_type = -1

        self.server = 'bd2-grupa11.database.windows.net'
        self.database = 'BD2'
        self.driver = '{SQL Server}'


    def set_login(self, login):
        self.login = login


    def set_password(self, password):
        self.password = password


    def authorize(self):
        print('password verification started')
        conn = 'DRIVER={};SERVER={};PORT=1433;DATABASE={};UID={};PWD={}'.format(self.driver, self.server, self.database, self.login, self.password)
        
        try:
            with pyodbc.connect(conn) as connection:
                with connection.cursor() as cursor:
                    cursor.execute('select * from test')
                    row = cursor.fetchone()
                    while row:
                        print('{} + {}', row[0], row[1])
                        row = cursor.fetchone()

            return True
        except Exception:
            print('fatal error')
            raise


    def get_user_type(self):
        return self.user_type
        