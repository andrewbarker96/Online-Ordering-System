import sys

sys.path.append(".")
from db_inserts import DB_Inserts


class Customer:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    def AddCustomer(self):
        db_insert = DB_Inserts()
        customer_id = db_insert.add_customer(self.first_name, self.last_name, self.email)
        return customer_id
            