#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewOrderModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_order(self, apetizer, main_course, soup, dessert, snacks, kitchen_hints):
        try:
            sql = 'INSERT INTO "Order" VALUES ({},{},{},{},{},{})'
            self.execute_sql(sql.format(apetizer, main_course, soup, dessert, snacks, kitchen_hints))
            print('Order added!')

        except Exception as e:
            print('While adding order error occured'.format(e))
            return

        

