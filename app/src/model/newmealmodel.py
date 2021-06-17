#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewMealModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_meal(self, name, weight, ingridient):
        try:
            sql = 'INSERT INTO meals VALUES ({},{},{})'
            self.execute_sql(sql.format(name, weight, ingridient))
            print('Meal added!')

        except Exception as e:
            print('While adding meal error occured'.format(e))
            return

        

