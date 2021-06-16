#!/usr/bin/env python
# @author Damian Piotrowski / Konrad Wojewódzki

from tkcalendar.calendar_ import Calendar
from model import Model
from tkcalendar import DateEntry
import datetime

class ExtraCostsModel(Model):
    def __init__(self):
        Model.__init__(self)

  
    def add_extra_cost(self, costs, cause):
        sql = 'INSERT INTO additional_costs VALUES ({},{},{})'
        get_id = 'SELECT order_id FROM "Order" WHERE start_date = GETDATE()'

        order_id = self.execute_sql(get_id.format())      
        self.execute_sql(sql.format(costs, cause, order_id))
