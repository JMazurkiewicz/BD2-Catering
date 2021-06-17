#!/usr/bin/env python
# @author Konrad / Damian

from model import Model
from tkcalendar import DateEntry
import datetime

class NewOrderModel(Model):
    def __init__(self):
        Model.__init__(self)
  
    def insert_new_order(self, date, number_of_ppl, base_price, waiters_needed, client_id):
        get_address = """SELECT address_id
                          FROM client
                          WHERE client_id = \'{}\' """
        address_id_cur = self.execute_sql(get_address.format(client_id))
        address_id = address_id_cur.fetchone()

        #try:
        sql = 'INSERT INTO "Order" VALUES (\'{}\', \'{}\', {}, {}, {}, {}, 1, 1, {})'
        self.execute_sql(sql.format(date, date, number_of_ppl, base_price, waiters_needed, client_id, address_id.address_id)).commit()

        print('Order added!')

        #except Exception as e:
            #print('While adding order error occured'.format(e))
            #return

    def find_person(self, name, surname):
        get_client = """SELECT client_id
                          FROM person
                          WHERE name = \'{}\' AND surname = \'{}\' """
        client_id_cur = self.execute_sql(get_client.format(name, surname))
        return client_id_cur.fetchone()

    def find_business(self, nip):
        get_business = """SELECT client_id
                          FROM business
                          WHERE nip = \'{}\'  """
        business_id_cur = self.execute_sql(get_business.format(nip))
        return business_id_cur.fetchone()

