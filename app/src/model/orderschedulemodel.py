#!/usr/bin/env python
# @author Jakub Mazurkiewicz / Konrad Wojewódzki

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
        get_order = 'SELECT order_id FROM "Order" WHERE start_date = \'{}\''
        order_id_cur = self.execute_sql(get_order.format(date))
        order_id = order_id_cur.fetchone()

        get_employee = 'SELECT employee_id FROM employee WHERE name = \'{}\' AND surname = \'{}\''
        employee_id_cur = self.execute_sql(get_employee.format(name, surname))
        employee_id = employee_id_cur.fetchone()

        sql = 'INSERT INTO employees_for_order VALUES ({}, {})'
        self.execute_sql(sql.format(employee_id.employee_id, order_id.order_id)).commit()


    def delete_order(self, date):
        sql = 'DELETE FROM "Order" WHERE start_date = \'{}\''
        self.execute_sql(sql.format(date)).commit


    def show_order_info(self, date):
        get_address = """SELECT address_id 
                         FROM "Order"
                         WHERE start_date = \'{}\'"""
        adress_id_cur = self.execute_sql(get_address.format(date))
        adress_id = adress_id_cur.fetchone()

        get_address_info = """SELECT a.postal_code, a.street_name, a.building_number, a.apartment_number, c.name, c.district 
                                FROM address AS a 
                                JOIN city AS c 
                                ON (c.city_id = a.city_id) 
                                WHERE a.address_id = {}"""
        address_info_cur = self.execute_sql(get_address_info.format(adress_id[0]))

        address_info =  address_info_cur.fetchone()
        while address_info:
            print("Adres:", address_info.postal_code, address_info.street_name, address_info.building_number, address_info.apartment_number, address_info.name, address_info.district)
            address_info =  address_info_cur.fetchone()


    def get_date_and_type(self):
        sql = """SELECT e.event_name, year(o.start_date) AS year, month(o.start_date) AS month, day(o.start_date) AS day
                FROM event_type AS e
                JOIN "Order" AS o
                ON (o.event_type_id = e.event_type_id) """
        cursor = self.execute_sql(sql)
        return cursor