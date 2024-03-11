import sys
sys.path.append('.')

from db_selects import DB_Selects

class Menu:
    def __init__(self):
        self.db_select = DB_Selects()

    def get_pizza_types(self):
        pizza_types = self.db_select.get_pizza_types()
        pizzas = [{"name": name, "cost": cost} for _, name, cost in pizza_types]
        print("\nPizza Menu:\n")
        print("{:<25} {:<10}".format("Name", "Price"))
        print("-" * 35)
        for pizza in pizzas:
            name = pizza["name"]
            cost = pizza["cost"]
            print("{:<25} ${:.2f}".format(name, cost))

    def get_pizza_sizes(self):
        pizza_sizes = self.db_select.get_pizza_sizes()
        sizes = [{"size": size, "cost": cost} for _, size, cost in pizza_sizes]
        print("\nPizza Sizes:\n")
        print("{:<15} {:<21}".format("Size", "Additional Price"))
        print("-" * 36)
        for size in sizes:
            name = size["size"]
            cost = size["cost"]
            print("{:<15} ${:.2f}".format(name, cost))

    def get_pizza_crust_types(self):
        crust_types = self.db_select.get_pizza_crust_types()
        types = [{"type": type} for _, type in crust_types]
        print("\nCrust Types:\n")
        print("{:<25}".format("Type"))
        print("-" * 25)
        for type in types:
            crust_type = type["type"]
            print("{:<25}".format(crust_type))

    def get_pizza_toppings(self):
        pizza_toppings = self.db_select.get_pizza_toppings()
        toppings = [{"name": name, "cost": cost} for _, name, cost in pizza_toppings]
        print("\nPizza Toppings:\n")
        print("{:<25} {:<21}".format("Name", "+ Cost"))
        print("-" * 46)
        for topping in toppings:
            name = topping["name"]
            cost = topping["cost"]
            print("{:<25} ${:.2f}".format(name, cost))

    def get_appetizers(self):
        appetizers = self.db_select.get_appetizers()
        apps = [{"name": name, "cost": cost} for _, name, cost in appetizers]
        print("\nAppetizers:\n")
        print("{:<35} {:<10}".format("Name", "Price"))
        print("-" * 45)
        for app in apps:
            name = app["name"]
            cost = app["cost"]
            print("{:<35} ${:.2f}".format(name, cost))

    def get_desserts(self):
        desserts = self.db_select.get_desserts()
        desserts = [{"name": name, "cost": cost} for _, name, cost in desserts]
        print("\Desserts:\n")
        print("{:<35} {:<10}".format("Name", "Price"))
        print("-" * 45)
        for dessert in desserts:
            name = dessert["name"]
            cost = dessert["cost"]
            print("{:<35} ${:.2f}".format(name, cost))

    def get_drinks(self):
        drinks = self.db_select.get_drinks()
        drinks = [{"name": name, "cost": cost} for _, name, cost in drinks]
        print("\nDrinks:\n")
        print("{:<35} {:<10}".format("Name", "Price"))
        print("-" * 45)
        for drink in drinks:
            name = drink["name"]
            cost = drink["cost"]
            print("{:<35} ${:.2f}".format(name, cost))
