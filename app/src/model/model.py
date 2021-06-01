#!/usr/bin/env python
# @author Jakub Mazurkiewicz

#from view import View

class Model:
    def __init__(self):
        self.views = []


    def test_connection(self):
        pass


    def execute_sql(self, sql):
        pass
        

    def add_view(self, view):
        self.views.add(view)


    def remove_view(self, view):
        self.views.add(view)
