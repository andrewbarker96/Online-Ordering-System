from classes.order import Order


class Promotion:
    def __init__(self, promotion_name, discount_code, discount=float):
        self.discount_code = discount_code
        self.promotion_name = promotion_name
        self.discount = discount

    def get_promotion_name(self):
        return self.promotion_name

    def get_discount(self):
        return Order.total_cost - (self.discount * Order.total_cost)

    def __str__(self):
        return self.discount
