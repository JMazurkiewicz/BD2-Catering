#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from model import Model

class MenuModel(Model):
    def __init__(self):
        Model.__init__(self)
        pass


    def get_inventory_description(self):
        cursor = self.execute_sql('SELECT name, cost FROM item_on_the_menu')
        description = ''
        
        if cursor.rowcount != 0:
            row = cursor.fetchone()
            while row:
                part = '{} ({})\n'.format(row[0], row[1])
                description += part
                row = cursor.fetchone()
        else:
            description = 'No data available'

        cursor.close()
        return description
