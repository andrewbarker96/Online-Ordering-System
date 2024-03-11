class MenuItem:
    def __init__(self):
        self.name = None
        self.cost = 0

    # Getter and Setter for name
    def get_name(self):
        return self.name


    def set_name(self, value):
        if isinstance(value, str):
            self.name = value
        else:
            raise ValueError("Pizza name must be of type string.")


    # Getter and Setter for cost
    def get_cost(self):
        return self.cost


    def add_cost(self, price):
        self.cost += round(price, 2)
