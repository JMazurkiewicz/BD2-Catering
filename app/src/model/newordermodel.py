#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewOrderModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_order(self, apetizer, main_course, soup, dessert, snacks, kitchen_hints):
        sql = 'INSERT INTO "Order" VALUES ({},{},{},{},{},{})'
        #sql = 'SELECT * FROM PRODUCT'
        self.execute_sql(sql.format(apetizer, main_course, soup, dessert, snacks, kitchen_hints))

        

