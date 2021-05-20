#!/usr/bin/env python
# @author: Jakub Mazurkiewicz

class AuthorizationModel:
    def __init__(self):
        self.login = ''
        self.password = ''
        self.user_type = -1 # todo: add user types

    def set_login(self, login):
        self.login = login


    def set_password(self, password):
        self.password = password


    def authorize(self):
        # do some password verification
        print('password verification started')
        return True


    def get_user_type(self):
        return self.user_type
        