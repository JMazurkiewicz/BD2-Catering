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
