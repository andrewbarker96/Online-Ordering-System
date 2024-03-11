import time
from db_inserts import DB_Inserts

class Payments:

    def __init__(self, customer_id, cart_id):
        self.customer_id = customer_id
        self.cart_id = cart_id
        self.tax_rate = 0.0575


    def calculate_tax(self, total_cost):
        total_cost += self.tax_rate * total_cost
        return round(total_cost, 2)
    

    def process_card_payment(self):
        # Do intense processing to get payment
        time.sleep(5)


    def add_order(self, total_cost):
        db_insert = DB_Inserts()
        order_id = db_insert.add_order(total_cost, self.cart_id, self.customer_id)
        return order_id
    

    def print_order_receipt(self, cart):
        sub_total = 0

        print("\nHere's your order summary:\n")
        for item in cart:
            item_number, item_details = list(item.items())[0]

            item_name = item_details.get('name', 'Unknown Item')
            type_cost = item_details.get('Cost', 0.0)
            size = item_details.get('Size', '')
            size_cost = item_details.get('Size Cost', 0.0)
            crust = item_details.get('Crust', '')
            crust_cost = item_details.get('Crust Cost', 0.0)
            item_cost = item_details.get('cost', 0.0)

            sub_total += type_cost + size_cost + crust_cost + item_cost

            print(f"Item {item_number}: {item_name} - ${type_cost:.2f}")

            if size and crust:
                print(f"\tSize: {size} - ${size_cost:.2f}\n\tCrust: {crust} - ${crust_cost:.2f}")

            if 'Toppings' in item_details:
                toppings = item_details['Toppings']
                for topping in toppings:
                    topping_name = topping.get('name', 'Unknown Topping')
                    topping_cost = topping.get('cost', 0.0)

                    sub_total += topping_cost

                    print(f"\tTopping: {topping_name} - ${topping_cost:.2f}")

        print("\nSubtotal Cost: ${:.2f}".format(sub_total))
        tax_cost = round(sub_total * self.tax_rate, 2)
        print("Tax cost ({:.2f}%): ${:.2f}".format(self.tax_rate * 100, tax_cost))
        total_cost = self.calculate_tax(sub_total)
        print("Total Cost: ${:.2f}\n".format(total_cost))
        return total_cost