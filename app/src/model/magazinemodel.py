#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from model import Model

class MagazineModel(Model):
    def __init__(self):
        pass

        
    def get_inventory_description(self):
        sql = """
            SELECT catalog_number, batch_number, products.name, available_amount, expiration_date, storage.name
            FROM products RIGHT JOIN stored_products LEFT JOIN storage ON 
            ORDER BY expiration_date DESCENDING
        """

        cursor = self.execute_sql(sql)
        description = ''
        
        row = cursor.fetchone()
        while row:
            part = '[{}:{}] {}, amount: {}, expiration date: {} (in {})\n'.format(row[0], row[1], row[2], row[3], row[4], row[5])
            description += part
            row = cursor.fetchone()

        return description

