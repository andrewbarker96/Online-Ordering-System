from db_handler import DB_Handler


class DB_Selects:

    def __init__(self):
        db_handler_instance = DB_Handler()
        self.connection = db_handler_instance.get_connection()
        self.cursor = self.connection.cursor()


    def get_pizzas(self):
        self.cursor.execute('''
                            SELECT * FROM pizzas
                            ''')
        pizzas = self.cursor.fetchall()
        return pizzas


    def get_pizza_types(self):
        self.cursor.execute('''
                            SELECT * FROM pizza_types
                            ''')
        pizza_types = self.cursor.fetchall()
        return pizza_types


    def get_pizza_sizes(self):
        self.cursor.execute('''
                            SELECT * FROM pizza_sizes
                            ''')
        pizza_sizes = self.cursor.fetchall()
        return pizza_sizes


    def get_pizza_crust_types(self):
        self.cursor.execute('''
                            SELECT * FROM pizza_crust_types
                            ''')
        crust_types = self.cursor.fetchall()
        return crust_types


    def get_pizza_toppings(self):
        self.cursor.execute('''
                            SELECT * FROM pizza_toppings
                            ''')
        pizza_toppings = self.cursor.fetchall()
        return pizza_toppings


    def get_appetizers(self):
        self.cursor.execute('''
                            SELECT * FROM appetizers
                            ''')
        appetizers = self.cursor.fetchall()
        return appetizers


    def get_desserts(self):
        self.cursor.execute('''
                            SELECT * FROM desserts
                            ''')
        desserts = self.cursor.fetchall()
        return desserts


    def get_drinks(self):
        self.cursor.execute('''
                            SELECT * FROM drinks
                            ''')
        drinks = self.cursor.fetchall()
        return drinks
    

    def get_promotions(self):
        self.cursor.execute('''
                            SELECT * FROM promotions
                            ''')
        promotions = self.cursor.fetchall()
        return promotions
    
    def get_customer(self, customer_id):
        self.cursor.execute('''
                            SELECT * FROM customers
                            WHERE id = ?
                            ''', (customer_id,))
        customers = self.cursor.fetchall()
        return customers[0]
        

    def get_cart(self, cart_id):
        self.cursor.execute('''
                            SELECT * FROM cart
                            WHERE id = ?
                            ''', (cart_id,))
        cart = self.cursor.fetchall()
        return cart[0]


    def get_order_status(self, order_id):
        self.cursor.execute('''
                            SELECT * FROM orders
                            WHERE id = ?
                            ''', (order_id,))
        order = self.cursor.fetchall()

        # Check if any order was found
        if order:
            return order[0]
        else:
            return None

    