class Cart:

    def __init__(self):
        self.cart = []
        self.sub_total = 0
        self.item_count = 1


    def add_appetizer(self, appetizer):
        appetizer = {'name': appetizer.name, 'Cost': appetizer.cost }
        self.cart.append({self.item_count : appetizer})
        self.item_count += 1


    def add_pizza(self, pizza):
        formatted_toppings = [{'name': topping.name, 'cost': topping.cost} for topping in pizza.toppings]
        pizza = {'name': pizza.name, 'Cost': pizza.type_cost, 'Size': pizza.size, 'Size Cost': pizza.size_cost, 'Crust': pizza.crust, 'Crust Cost': pizza.crust_cost, 'Toppings': formatted_toppings }
        self.cart.append({self.item_count : pizza})
        self.item_count += 1


    def add_dessert(self, dessert):
        dessert = {'name': dessert.name, 'Cost': dessert.cost }
        self.cart.append({self.item_count : dessert})
        self.item_count += 1


    def add_drink(self, drink):
        drink = {'name': drink.name, 'Cost': drink.cost }
        self.cart.append({self.item_count : drink})
        self.item_count += 1


    def get_cart(self):
        print(f"\n Cart Items\n{self.cart}")
        print(f"\n Subtotal: ${self.subtotal:.2f}\n")


    def add_cost(self, cost):
        self.sub_total += round(cost, 2)