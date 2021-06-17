#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class EmployeeScheduleModel(Model):
    def __init__(self):
        self.date_entries = {}
  
    def load_month(self, month, year):
        sql = 'SELECT order_id, start_date, end_date FROM order WHERE MONTH(start_date) = {} AND YEAR(start_date) = {}'
        cursor = self.execute_sql(sql.format(month, year))

        #date_entries = []

        row = cursor.fetchone()
        while row:
            date = datetime.date(row[1])
            message = self.__make_order_message(row[0], row[1], row[2])

            entry = (date, message)
            self.date_entries.append(entry)

    def __make_order_message(self, order_id, start_date, end_date):
        return "Order id: {}\nStart date: {}\nEnd date: {}".format(order_id, start_date, end_date)

    def add_extra_costs(self, costs, cause, date):
        sql = 'INSERT INTO additional_costs VALUES ({},\'{}\',{})'
        get_id = 'SELECT order_id FROM "Order" WHERE start_date = \'{}\''

        order_id = self.execute_sql(get_id.format(date)) 
        order_id = order_id.fetchone() 
        
        self.execute_sql(sql.format(costs, cause, order_id.order_id)).commit()
