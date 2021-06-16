#!/usr/bin/env python
# @author Damian Piotrowski / Konrad Wojewódzki

from model import Model

class NewClientModel(Model):
    def __init__(self):
        Model.__init__(self)

  
    def add_person(self, costs, cause):
        sql = 'INSERT INTO client VALUES (\'P\', )'
        get_id = 'SELECT order_id FROM "Order" WHERE start_date = GETDATE()'

        order_id = self.execute_sql(get_id.format())      
        self.execute_sql(sql.format(costs, cause, order_id))

    def add_business(self):
        return

    def get_address(self, city, street, building):
        sql = 'SELECT a.address_id FROM address AS a JOIN city AS c ON (a.city_id = c.city_id) WHERE c.name = \'{}\' AND a.street_name = \'{}\' AND a.building_number = \'{}\''
        return self.execute_sql(sql.format(city, street, building))