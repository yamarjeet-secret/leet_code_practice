from abc import ABC, abstractmethod

"""Paypal uses email addresses for verification, whereas credit and debit cards use security codes.\
    This means we are abusing the Liskov Substitution Principle because we are using a subclass in a \
        way that is not compatible with its parent class.
"""
class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address: str):
        self.email_address = email_address

    def pay(self, order):
        print("Processing paypal payment")
        print(f"Verifying email: {self.email_address}")
        order.status = "paid"


order = Order()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = PaypalPaymentProcessor("hi@arjancodes.com")
processor.pay(order)
print(order.status)

