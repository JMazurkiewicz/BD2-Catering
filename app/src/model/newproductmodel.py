#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewProductModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_product(self, catalog, name, price):
        #sql = 'INSERT INTO product VALUES ({},{},{},null,\'A\')'
        sql = 'SELECT * FROM PRODUCT'
        cursor = self.execute_sql(sql.format(catalog, name, price))

        print(cursor)
        

    def __make_order_message(self, order_id, start_date, end_date):
        return "Order id: {}\nStart date: {}\nEnd date: {}".format(order_id, start_date, end_date)
