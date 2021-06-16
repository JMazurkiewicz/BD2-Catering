#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewMealModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_employee(self, name, surname, pesel, phone_nbumber, bank_acc_number, street_name, building_number, apartment_number, city, district):
        #sql = 'SELECT * FROM PRODUCT'
        sql1 = 'INSERT INTO employee VALUES ({},{},{},{},{})'
        self.execute_sql(sql1.format(name, surname, pesel, phone_nbumber, bank_acc_number))

        sql2 = 'INSERT INTO address VALUES ({},{},{})'
        self.execute_sql(sql2.format(street_name, building_number, apartment_number))

        sql3 = 'INSERT INTO address VALUES ({},{})'
        self.execute_sql(sql3.format(city, district))

        

