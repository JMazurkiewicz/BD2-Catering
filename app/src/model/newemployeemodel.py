#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewEmployeeModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_employee(self, name, surname, pesel, phone_nbumber, bank_acc_number, postal_code, street_name, building_number, apartment_number, city, district):
        try:
            sql1 = 'INSERT INTO address VALUES ({},{})'
            self.execute_sql(sql1.format(city, district))

            get_city = """SELECT city_id
                          FROM city
                          WHERE name = \'{}\' """
            city_id_cur = self.execute_sql(get_city.format(city))
            city_id = city_id_cur.fetchone()

            sql2 = 'INSERT INTO address VALUES ({},{},{}, {})'
            self.execute_sql(sql2.format(postal_code, street_name, building_number, apartment_number, city_id))

            get_address = """SELECT address_id
                          FROM address
                          WHERE postal_code = \'{}\' AND street_name = \'{}\' AND building_number = \'{}\' """
            address_id_cur = self.execute_sql(get_address.format(postal_code, street_name, building_number))
            address_id = address_id_cur.fetchone()

            sql3 = 'INSERT INTO employee VALUES ({},{},{},{},{},{},1)'
            self.execute_sql(sql3.format(name, surname, pesel, phone_nbumber, bank_acc_number, address_id))
            print('Employee added!')

        except Exception as e:
            print('While adding employee error occured'.format(e))
            return

        

