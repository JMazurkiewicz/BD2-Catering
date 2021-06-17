#!/usr/bin/env python
# @author Damian Piotrowski / Konrad Wojewódzki

from model import Model

class NewClientModel(Model):
    def __init__(self):
        Model.__init__(self)

  
    def add_person(self, name, surname, phone_nbumber, email, postal_code, street_name, building_number, apartment_number, city, district):
        #try:
        address_id = self.add_address(postal_code, street_name, building_number, apartment_number, city, district)

        sql3 = 'INSERT INTO client VALUES (\'P\', {} )'
        self.execute_sql(sql3.format(address_id.address_id )).commit()

        get_client = 'SELECT client_id FROM client WHERE address_id = {}'
        client_id_cur = self.execute_sql(get_client.format(address_id.address_id))
        client_id = client_id_cur.fetchone()
        print(client_id.client_id)

        sql4 = 'INSERT INTO person VALUES ({}, \'{}\', \'{}\', \'{}\', \'{}\')'
        self.execute_sql(sql4.format(client_id.client_id, name, surname, phone_nbumber,email)).commit()
        print('Person added!')


    def add_business(self, postal_code, street_name, building_number, apartment_number, city, district, nip):
        address_id = self.add_address(postal_code, street_name, building_number, apartment_number, city, district)
        sql3 = 'INSERT INTO client VALUES (\'B\', {} )'
        self.execute_sql(sql3.format(address_id.address_id )).commit()

        get_client = 'SELECT client_id FROM client WHERE address_id = {}'
        client_id_cur = self.execute_sql(get_client.format(address_id.address_id))
        client_id = client_id_cur.fetchone()

        sql4 = 'INSERT INTO business VALUES ({}, \'{}\')'
        self.execute_sql(sql4.format(client_id.client_id, nip)).commit()
        print('Business added!')


    def add_address(self, postal_code, street_name, building_number, apartment_number, city, district):
        sql1 = 'INSERT INTO city VALUES (\'{}\',\'{}\')'
        self.execute_sql(sql1.format(city, district)).commit()

        get_city = """SELECT city_id
                          FROM city
                          WHERE name = \'{}\' """
        city_id_cur = self.execute_sql(get_city.format(city))
        city_id = city_id_cur.fetchone()

        sql2 = 'INSERT INTO address VALUES (\'{}\', \'{}\', {}, {}, {})'
        self.execute_sql(sql2.format(postal_code, street_name, building_number, apartment_number, city_id.city_id)).commit()

        get_address = """SELECT address_id
                          FROM address
                          WHERE postal_code = \'{}\' AND street_name = \'{}\' AND building_number = \'{}\' """
        address_id_cur = self.execute_sql(get_address.format(postal_code, street_name, building_number))
        return address_id_cur.fetchone()