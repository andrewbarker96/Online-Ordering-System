# SWDV 630 Final Project

This project encompasses a full text-based "Online Ordering System".

Within this project, a user can "Order" food items from a restaurant. These food items entail:

- Pizzas
- Appetizers
- Drinks
- Desserts

The food items are all stored in a SQLite database along with their pricing. When selecting items, the various classes are used to call upon those items, append to order list, and calculate subtotal for customer.

At the beginning of the ordering process, customers are asked if they would prefer to have their order "Delivery" or "Carryout". This is saved for later as if a user selects "Delivery" then a delivery driver would be assigned after order has been purchased.

## Class Usage

1. Appetizer(MenuItem) - appetizer items (subclass of MenuItem)
2. Cart - can add/remove items to the cart, calculate subtotal costs.
3. Customer - gathers customer information
4. Payment(Customer) - collects payment information from the customer.
5. Dessert(MenuItem) - labels dessert items
6. Drink(MenuItem) - labels drink items.
7. Menu - displays full menu along with pricing. Can retrieve sectional items as well i.e., appetizer items, pizza types, pizza crusts.
8. Promotion - promotions can be added by the customer which reduce cost of the subtotal.
9. Size(Pizza) - user selects the size they want for their pizza
10. Toppings - set the toppings on the pizza that they want.
11. DB_Handler - establishes the connection to the database.
12. DB_Inserts - inserts items from the database.
13. DB_Selects - selects items from the database.

## Use-Cases

1. New User Registration:

   - Description: A new user visits the online food ordering platform and registers for an account.
   - Steps:
   - User provides necessary information (name, email, password).
     System verifies and stores the user's details.

2. Browsing and Menu Exploration:

   - Description: A registered user logs in and explores menu and sub-menus.
   - Steps: User navigates to the restaurant and retrieves menu items by selecting "Menu". System displays restaurant details and menu options.

3. Placing a New Order:

   - Description: User selects "Add to Order" on specific item selections, this adds items to the cart, allows an order to be placed.

   - Steps: User chooses a restaurant and browses the menu.
     Items are added to the cart, and the user proceeds to checkout.
     System confirms the order, and user provides delivery details.

4. Customizing Order:

   - Description: User customizes food items in the order by adding toppings, changing crust types, and sizes of pizzas.
   - Steps: User selects a pizza type and customizes options (e.g., toppings, crust type, size, adding additional menu items).
     System updates the order details based on user preferences.

5. Promotions and Discounts:

   - Description: User applies a promotion code or discounts during the checkout process.
   - Steps: User enters a promotion code. System validates and applies the discount to the order.

6. Payment Processing:

   - Description: User completes the payment for the order.
   - Steps: User selects a payment method (credit card, online wallet). System securely processes the payment.

7. Order Tracking:

   - Description: User tracks the status of their order in real-time.
     Steps:
   - User accesses the order tracking feature.
     System provides real-time updates on order preparation, dispatch, and delivery.

8. Order Saving:

   - Description: User saves order before processing and can return to it later. User can view past orders to make same order as previous.
   - System saves current orders and past orders to user account. User must provide email first to create account.

9. Restaurant Management:

   - Description: Restaurant owners/managers update their menu, availability, and operating hours.
   - Steps: Restaurant owner logs into the management portal. System allows updates to the menu, availability, and operating hours.

10. Delivery Driver Assignment:

    - Description: When User selects "Delivery" a driver is assigned to the job.
    - Steps: User places an order, delivery driver assigned based on availability and drivers on shift.
      System provides navigation and updates on assigned orders.

11. Create Account:

    - Description: User creates an account.
    - Steps: User clicks "profile" or "account".
      Also user begins creating an order and before submitting order is asked to provide first name, last name, email, and password. Or can login. This would be asked as part to entail the user to save their order.

12. Customer service:
    - Description: User contacts restaurant for assistance.
    - Steps: Phone number provided for user to make contact with store regarding their order.
