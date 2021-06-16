#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewProductModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_product(self, catalog, name, price):
        
        try:
            sql = 'INSERT INTO product VALUES (\'{}\',{},{},null,\'A\')'
            self.execute_sql(sql.format(catalog, name, price))
            print('Product added!')
        except Exception as e:
            print('While adding product error occured'.format(e))
            return