#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from model import Model
from tkcalendar import DateEntry
import datetime

class OrderScheduleModel(Model):
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

    def add_employee_to_event(self, date, name, surname):
        get_order = 'SELECT order_id FROM "Order" WHERE start_date = {}'
        order_id = self.execute_sql(get_order.format(date))

        get_employee = 'SELECT employee_id FROM employee WHERE name = {} AND surname = {}'
        employee_id = self.execute_sql(get_employee.format(name, surname))

        sql = 'INSERT INTO employees_for_order VALUES ({}, {})'
        self.execute_sql(sql.format(employee_id, order_id))

    def delete_order(self, date):
        sql = 'DELETE FROM "Order" WHERE start_date = {}'
        self.execute_sql(sql.format(date))


    def show_order_info(self, date):
        get_address = 'SELECT address_id, base_price FROM "Order" WHERE start_date = {}'
        adress_id, base_price = self.execute_sql(get_address.format(date))

        get_address_info = 'SELECT a.postal_code, a.street_name, a.building_number, a.apartment_number, c.name, c.district FROM address AS a JOIN city AS c ON (c.city_id = a.city_id) WHERE a.address_id = {}'
        address_info = self.execute_sql(get_address_info.format(adress_id))
        print("Adres:", address_info)