import sys
from toppings import Toppings
from menu_item import MenuItem

sys.path.append(".")

class Pizza(MenuItem):
    def __init__(self):
        # Type is the name which is defined in parent class.
        super().__init__()
        self.type_cost = 0
        self.size = None
        self.size_cost = 0
        self.crust = None
        self.crust_cost = 0
        self.toppings = []


    # Getter and Setter for size
    def get_size(self):
        return self.size


    def set_size(self, value):
        if isinstance(value, str):
            self.size = value
        else:
            raise ValueError("Pizza size must be of type string.")


    # Getter and Setter for crust
    def get_crust(self):
        return self.crust


    def set_crust(self, value):
        if isinstance(value, str):
            self.crust = value
        else:
            raise ValueError("Crust type must be of type string.")
        

    # Getter and Setter for toppings
    def get_toppings(self):
        return self.toppings


    def set_toppings(self, toppings):
        self.toppings = toppings


    def calculate_toppings_price(self):
        for topping in self.toppings:
            self.add_cost(topping.cost)
        