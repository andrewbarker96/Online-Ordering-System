import sys

sys.path.append("./classes")
from classes.appetizer import Appetizer
from classes.pizza import Pizza
from classes.dessert import Dessert
from classes.drink import Drink
from classes.payments import Payments
from classes.separator import Separator
from classes.customer import Customer
from classes.order import Order
from classes.cart import Cart
from classes.menu import Menu
from db_handler import DB_Handler
from db_selects import DB_Selects
from datetime import datetime, timedelta

def get_order():
    order = Order()
    cart = Cart()

    print("\nWhat would you like to order?\n")
    print("(1) Appetizer")
    print("(2) Pizza")
    print("(3) Dessert")
    print("(4) Drink")
    print("(5) Cancel order")

    while True:
        try:
            selection = int(input("\n> "))
            if selection == 1:
                appetizer = Appetizer()
                order.order_appetizer(appetizer)
                cart.add_cost(appetizer.cost)
                cart.add_appetizer(appetizer)
            elif selection == 2:
                pizza = Pizza()
                order.order_pizza(pizza)
                cart.add_cost(pizza.cost)
                cart.add_pizza(pizza)   
            elif selection == 3:
                dessert = Dessert()
                order.order_dessert(dessert)
                cart.add_cost(dessert.cost)
                cart.add_dessert(dessert)
            elif selection == 4:
                drink = Drink()
                order.order_drink(drink)
                cart.add_cost(drink.cost)
                cart.add_drink(drink)
            elif selection == 5:
                return
            else:
                print("\nInvalid input. Please enter a valid number.\n")
           
            while True:
                print("\nWould you like to add anything else to your order? (y/n)")
                selection = input("\n> ").lower()
                if selection == "n":
                    # Get customer info
                    print("\nLet's get your contact information.\n")
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name: ")
                    email = input("Enter your email: ")
                    customer = Customer(first_name, last_name, email)
                    customer_id = customer.AddCustomer()

                    # Get order total
                    order.cart = cart.cart
                    cart_id = order.add_cart()
                    payment = Payments(customer_id, cart_id)
                    order.sub_total = cart.sub_total
                    total_cost = payment.print_order_receipt(order.cart)

                    while True:
                        print("Would you like to pay with:")
                        print("(1) Cash")
                        print("(2) Card")
                        print("(3) Cancel order")
                        try:
                            selection = int(input("\n> "))
                            if selection == 1:
                                order_id = payment.add_order(total_cost)
                                print("\nThank you! Your order has been placed and will be ready in 20 minutes."
                                    " Please pay when you arrive to pickup your order."
                                    " For your reference, your order # is ({}).\n".format(order_id))
                                return
                            elif selection == 2:
                                order_id = payment.add_order(total_cost)
                                input("\nPlease enter the name exactly as shown on your card: ")
                                input("Please enter your card's 16 digit number: ")
                                input("Please enter the expiration date on your card: ")
                                input("Please enter the CVC number on your card: ")
                                print("\nProcessing payment...")
                                payment.process_card_payment()
                                print("\nSuccess! Your order has been placed and will be ready in 20 minutes."
                                    " For your refernece, your order # is ({}).\n".format(order_id))
                                return
                            elif selection == 3:
                                return
                            else:
                                print("\nInvalid input. Please enter a valid number.\n")
                        except ValueError:
                            print("\nInvalid input. Please enter a valid number.\n")
                elif selection != 'y':
                    print("\nInvalid selection. Try again using 'y' or 'n'.")
                else:
                    break

            print("\nWhat else would you like to order?\n")
            print("(1) Appetizer")
            print("(2) Pizza")
            print("(3) Dessert")
            print("(4) Drink")
            print("(5) Cancel order")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print('Error: ' + e)


def check_order_status():
    print("\nOrder Status (type 'back' to go back):")
    while True:
        order_id = input("Enter your order id: ")
        try:
            if order_id.lower() == 'back':
                break
            else:
                order_id = int(order_id)
                db_select = DB_Selects()
                order = db_select.get_order_status(order_id)

                if order == None:
                    print("Order not found.")
                    continue

                order_time = datetime.strptime(order[1], '%Y-%m-%d %H:%M:%S.%f') 

                print("\nYour order was placed on: " + order_time.strftime('%A, %B %d, %Y %I:%M:%S %p'))

                twenty_minutes_after = order_time + timedelta(minutes=20)
                if datetime.now() < twenty_minutes_after:
                    print("Your order is still being made. It will be ready on: " 
                        + twenty_minutes_after.strftime('%A, %B %d, %Y %I:%M:%S %p'))
                else:
                    print("Your order is ready for pickup! We look forward to seeing you!\n")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


def view_menu():
    menu = Menu()
    menu.get_pizza_types()
    menu.get_pizza_sizes()
    menu.get_pizza_crust_types()
    menu.get_pizza_toppings()
    menu.get_appetizers()
    menu.get_desserts()


def main():
    Separator()
    while True:
        try:
            print("Welcome to Pitchfork Eatery!\n")
            print("(1) Place an order")
            print("(2) Check order status")
            print("(3) View menu")
            print("(4) Exit\n")

            selection = int(input("> "))
            if selection == 1:
                get_order()
            elif selection == 2:
                check_order_status()
            elif selection == 3:
                view_menu()
            elif selection == 4:
                break
            else:
                print(
                    "\nOption not recognized. Please choose from the following options.\n"
                )
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print("Error: " + str(e))
            break

    # Close DB connection
    Separator()
    db_handler_instance = DB_Handler()
    db_handler_instance.close_connection()
    sys.exit(0)


if __name__ == "__main__":
    main()
