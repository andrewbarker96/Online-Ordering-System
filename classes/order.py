import sys

sys.path.append('.')

from db_inserts import DB_Inserts
from db_selects import DB_Selects
from toppings import Toppings


class Order:
    def __init__(self):
        self.order_date = None
        self.sub_total = 0
        self.cart = []


    def order_appetizer(self, appetizer):
        db_selects = DB_Selects()

        while True:
            print("\nSelect an appetizer:")
            appetizers_list = db_selects.get_appetizers()
            for i, (_, name, cost) in enumerate(appetizers_list, start=1):
                print("({}) {:<40} ${:.2f}".format(i, name, cost))
            try:
                selection = int(input("\n> "))
                if 1 <= selection <= len(appetizers_list):
                    select_appetizer = appetizers_list[selection - 1]
                    appetizer.name = select_appetizer[1]
                    appetizer.cost = select_appetizer[2]
                    break
                else:
                    print("\nInvalid input. Please enter a number within the valid range.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")


    def order_pizza(self, pizza):
        db_selects = DB_Selects()
        toppings = []

        # Pizza Type
        while True:
            print("\nSelect a pizza type:")
            pizza_type_list = db_selects.get_pizza_types()
            for i, (_, name, cost) in enumerate(pizza_type_list, start=1):
                print("({}) {:<40} ${:.2f}".format(i, name, cost))
            try:
                selection = int(input("\n> "))
                if 1 <= selection <= len(pizza_type_list):
                    select_pizza_type = pizza_type_list[selection - 1]
                    pizza.name = select_pizza_type[1]
                    pizza.type_cost = select_pizza_type[2]
                    pizza.add_cost(select_pizza_type[2])
                    break
                else:
                    print("\nInvalid input. Please enter a number within the valid range.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        # Pizza Size
        while True:
            print("\nSelect a pizza size:")
            pizza_size_list = db_selects.get_pizza_sizes()
            for i, (_, name, cost) in enumerate(pizza_size_list, start=1):
                print("({}) {:<40} ${:.2f}".format(i, name, cost))
            try:
                selection = int(input("\n> "))
                if 1 <= selection <= len(pizza_size_list):
                    select_pizza_size = pizza_size_list[selection - 1]
                    pizza.size = select_pizza_size[1]
                    pizza.size_cost = select_pizza_size[2]
                    pizza.add_cost(select_pizza_size[2])
                    break
                else:
                    print("\nInvalid input. Please enter a number within the valid range.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        # Pizza Crust
        while True:
            print("\nSelect a pizza crust:")
            pizza_crust_type = db_selects.get_pizza_crust_types()
            for i, (_, type) in enumerate(pizza_crust_type, start=1):
                print("({}) {:<40}".format(i, type))
            try:
                selection = int(input("\n> "))
                if 1 <= selection <= len(pizza_crust_type):
                    select_pizza_crust = pizza_crust_type[selection - 1]
                    pizza.crust = select_pizza_crust[1]
                    break
                else:
                    print("\nInvalid input. Please enter a number within the valid range.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        # Don't add toppings to a specialty pizza
        if pizza.name.lower() != "custom":
            return

        # Pizza Toppings
        while True:  
            print("\nSelect a pizza toppings:")
            topping = Toppings()
            pizza_topping_list = db_selects.get_pizza_toppings()
            for i, (_, topping_name, cost) in enumerate(pizza_topping_list, start=1):
                print("({}) {:<40} ${:.2f}".format(i, topping_name, cost))
            try:
                selection = int(input("\n> "))
                if 1 <= selection <= len(pizza_topping_list):
                    select_pizza_topping = pizza_topping_list[selection - 1]
                    topping.set_name(select_pizza_topping[1])
                    topping.set_cost(select_pizza_topping[2])
                    if any(existing_topping.get_name() == topping.get_name() for existing_topping in toppings):
                        print("\n" + topping.get_name() + " was already added!")
                    else: 
                        toppings.append(topping)
                else:
                    print("\nInvalid input. Please enter a number within the valid range.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

            print("\nWould you like to add any more toppings? (y/n)")
            selection = input("\n> ").lower()
            if selection == 'n':
                pizza.calculate_toppings_price()
                pizza.set_toppings(toppings)
                break
            elif selection != 'y':
                print("\nInvalid selection. Try again using 'y' or 'n'.")


    def order_dessert(self, dessert):
        db_selects = DB_Selects()
        while True:
            print("\nSelect a dessert:")
            dessert_list = db_selects.get_desserts()
            for i, (_, name, cost) in enumerate(dessert_list, start=1):
                print("({}) {:<40} ${:.2f}".format(i, name, cost))
            try:
                selection = int(input("\n> "))
                if 1 <= selection <= len(dessert_list):
                    select_dessert = dessert_list[selection - 1]
                    dessert.name = select_dessert[1]
                    dessert.cost = select_dessert[2]
                    break
                else:
                    print("\nInvalid input. Please enter a number within the valid range.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")


    def order_drink(self, drink):
        db_selects = DB_Selects()
        while True:
            print("\nSelect a drink:")
            drink_list = db_selects.get_drinks()
            for i, (_, name, cost) in enumerate(drink_list, start=1):
                print("({}) {:<40} ${:.2f}".format(i, name, cost))
            try:
                selection = int(input("\n> "))
                if 1 <= selection <= len(drink_list):
                    select_drink = drink_list[selection - 1]
                    drink.name = select_drink[1]
                    drink.cost = select_drink[2]
                    break
                else:
                    print("\nInvalid input. Please enter a number within the valid range.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")


    def add_cart(self):
        db_inserts = DB_Inserts()
        cart_id = db_inserts.add_cart(self.cart)
        return cart_id
    