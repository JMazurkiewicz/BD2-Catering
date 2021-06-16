#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewMealModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_meal(self, name, weight, ingridient):
        sql = 'INSERT INTO meals VALUES ({},{},{})'
        #sql = 'SELECT * FROM PRODUCT'
        self.execute_sql(sql.format(name, weight, ingridient))

        

