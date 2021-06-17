#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewProductModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_product(self, catalog, name, price):       
        sql = 'INSERT INTO product VALUES (\'{}\',\'{}\',{},null,\'A\')'
        self.execute_sql(sql.format(catalog, name, price)).commit()
        print('Product added!')

