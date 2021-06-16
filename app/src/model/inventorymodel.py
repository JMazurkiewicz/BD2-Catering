#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from model import Model

class InventoryModel(Model):
    def __init__(self):
        pass

        
    def get_inventory_description(self):
        sql = """
            SELECT batch_number, available_amount, expiration_date
            FROM stored_products LEFT JOIN storage ON 
            ORDER BY expiration_date DESCENDING
        """
        cursor = self.execute_sql(sql)

        description = ''

        row = cursor.fetchone()
        while row:
            message = self.__make_order_message(row[0], row[1], row[2])

            row = cursor.fetchone()

        return description

    
    def __make_order_message(self, order_id, start_date, end_date):
        return "Order id: {}\nStart date: {}\nEnd date: {}".format(order_id, start_date, end_date)
