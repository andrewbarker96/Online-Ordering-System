import sqlite3


def initialize_tables(connection):
    cursor = connection.cursor()

    # Customer Table
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE  
        )         
    """
    )

    # Orders Table
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            order_date TEXT NOT NULL,
            total_cost REAL NOT NULL,
            cart_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (cart_id) REFERENCES cart(id)
        )         
    """
    )

    # Cart Table
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY,
            items TEXT NOT NULL
        )         
    """
    )

    # Pizza Types Table
    try:
        cursor.execute("SELECT COUNT(*) FROM pizza_types")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS pizza_types (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cost REAL NOT NULL
        )         
    """
    )

    if row_count < 1:
        pizzas = [
            ("Pepperoni", 11.99),
            ("Sausage", 11.99),
            ("Bacon", 11.99),
            ("Hamburger", 11.99),
            ("Cheese", 10.99),
            ("Veggie", 11.99),
            ("Meat Lovers", 13.99),
            ("Supreme", 13.99),
            ("Hawaiian", 13.99),
            ("BBQ Chicken", 13.99),
            ("Buffalo Chicken", 13.99),
            ("Custom", 10.99),
        ]

        connection.executemany(
            "INSERT INTO pizza_types (name, cost) VALUES(?, ?)", pizzas
        )
        connection.commit()

    # Pizza Sizes Table
    try:
        cursor.execute("SELECT COUNT(*) FROM pizza_sizes")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS pizza_sizes (
            id INTEGER PRIMARY KEY,
            size TEXT NOT NULL,
            cost REAL NOT NULL
        )           
    """
    )

    if row_count < 1:
        pizza_sizes = [("Small", 2), ("Medium", 4), ("Large", 6), ("X-Large", 8)]

        connection.executemany(
            "INSERT INTO pizza_sizes (size, cost) VALUES(?, ?)", pizza_sizes
        )
        connection.commit()

    # Pizza Crust Types Table
    try:
        cursor.execute("SELECT COUNT(*) FROM pizza_crust_types")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS pizza_crust_types (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL
        )           
    """
    )

    if row_count < 1:
        crust_types = [
            ("Thin",),
            ("Hand Tossed",),
            ("Pan",),
            ("Deep Dish",),
            ("Stuffed Crust",),
            ("Gluten-Free",),
        ]

        connection.executemany(
            "INSERT INTO pizza_crust_types (type) VALUES(?)", crust_types
        )
        connection.commit()

    # Pizza Toppings Table
    try:
        cursor.execute("SELECT COUNT(*) FROM pizza_toppings")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS pizza_toppings (
            id INTEGER PRIMARY KEY,
            topping_name TEXT NOT NULL,
            cost REAL NOT NULL
        )       
    """
    )

    if row_count < 1:
        pizza_toppings = [
            ("Pepperoni", 1.99),
            ("Sausage", 1.99),
            ("Bacon", 1.99),
            ("Ham", 1.99),
            ("Hamburger", 1.99),
            ("Mushrooms", 1.99),
            ("Onions", 1.99),
            ("Green Peppers", 1.99),
            ("Black Olives", 1.99),
            ("Pineapple", 1.99),
            ("Tomatoes", 1.99),
            ("Jalapenos", 1.99),
            ("Extra Cheese", 1.99),
        ]

        connection.executemany(
            "INSERT INTO pizza_toppings (topping_name, cost) VALUES(?, ?)",
            pizza_toppings,
        )
        connection.commit()

    # Appetizers Table
    try:
        cursor.execute("SELECT COUNT(*) FROM appetizers")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS appetizers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cost REAL NOT NULL
        )       
    """
    )

    if row_count < 1:
        appetizers = [
            ("Breadsticks", 6.99),
            ("Cheesesticks", 8.79),
            ("BBQ Wings", 11.49),
            ("Buffalo Wings", 11.49),
            ("Honey Chipotle Boneless Wings", 9.49),
        ]

        connection.executemany(
            "INSERT INTO appetizers (name, cost) VALUES(?, ?)", appetizers
        )
        connection.commit()

    # Desserts Table
    try:
        cursor.execute("SELECT COUNT(*) FROM desserts")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS desserts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cost REAL NOT NULL
        )       
    """
    )

    if row_count < 1:
        desserts = [
            ("Cinnamon Pull Aparts", 8.29),
            ("Chocolate Chip Cookie", 3.39),
            ("Double Chocolate Chip Brownie", 3.39),
        ]

        connection.executemany(
            "INSERT INTO desserts (name, cost) VALUES(?, ?)", desserts
        )
        connection.commit()

    # Drinks Table
    try:
        cursor.execute("SELECT COUNT(*) FROM drinks")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cost REAL NOT NULL
        )       
    """
    )

    if row_count < 1:
        drinks = [
            ("Pepsi", 3.39),
            ("Mountain Dew", 3.39),
            ("Diet Pepsi", 3.39),
            ("Fiji Water", 3.39),
            ("Vodka on Tap", 1.39),
            ("Pepsi Zero Sugar", 3.39),
            ("Starry", 3.39),
            ("Mug Root Beer", 3.39),
            ("Pepsi Wild Cherry", 3.39),
        ]

        connection.executemany("INSERT INTO drinks (name, cost) VALUES(?, ?)", drinks)
        connection.commit()

    # Promotions Table
    try:
        cursor.execute("SELECT COUNT(*) FROM promotions")
        row_count = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        row_count = 0

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS promotions (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            discount_code TEXT NOT NULL,
            discount REAL NOT NULL
        )       
    """
    )

    if row_count < 1:
        promotions = [
            ("Hoppy Easter!", "HOP!", 40),
            ("Buy 2 Pizzas Get One Free (a Dance @ LF)", "BOGO", 100),
        ]

        connection.executemany(
            "INSERT INTO promotions (name, discount_code, discount) VALUES(?, ?, ?)",
            promotions,
        )
        connection.commit()
