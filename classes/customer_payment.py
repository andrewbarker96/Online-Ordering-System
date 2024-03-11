import sys

sys.path.append(".")
from classes.customer import Customer


class Payment(Customer):
    def __init__(
        self,
        first_name,
        last_name,
        email,
        phone,
        address,
        zip_code,
        card_number,
        expiration_date,
        cvv,
    ):
        super().__init__(first_name, last_name, email, phone, address, zip_code)
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv
