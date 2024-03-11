from db_handler import DB_Handler
from datetime import datetime
import json


class DB_Inserts:

    def __init__(self):
        db_handler_instance = DB_Handler()
        self.connection = db_handler_instance.get_connection()
        self.cursor = self.connection.cursor()


    def add_customer(self, first_name, last_name, email):
        customer = (first_name, last_name, email)
        self.connection.execute('''
                                INSERT INTO customers (first_name, last_name, email)
                                VALUES(?, ?, ?)
                                ''', customer)
        self.connection.commit()

        # Get the last inserted row ID (customer_id)
        self.cursor.execute('''
                            SELECT id
                            FROM customers
                            ORDER BY id DESC
                            LIMIT 1 
                            ''')
        
        row = self.cursor.fetchone()
        id = row[0] if row is not None else None
        return id

    def add_cart(self, items):
        self.connection.execute(
                                '''
                                INSERT INTO cart (items)
                                VALUES (?)
                                ''', (json.dumps(items, indent=2),))
        self.connection.commit()

        # Get the last inserted row ID (cart_id)
        self.cursor.execute('''
                            SELECT id
                            FROM cart
                            ORDER BY id DESC
                            LIMIT 1 
                            ''')
        
        row = self.cursor.fetchone()
        id = row[0] if row is not None else None
        return id


    def add_order(self, total_cost, cart_id, customer_id):
        self.connection.execute('''
                                INSERT INTO orders (order_date, total_cost, cart_id, customer_id)
                                VALUES (?, ?, ?, ?)
                                ''', (datetime.now(), total_cost, cart_id, customer_id))
        self.connection.commit()

        # Get the last inserted row ID (order_id)
        self.cursor.execute('''
                            SELECT id
                            FROM orders
                            ORDER BY id DESC
                            LIMIT 1 
                            ''')
        
        row = self.cursor.fetchone()
        id = row[0] if row is not None else None
        return id
    