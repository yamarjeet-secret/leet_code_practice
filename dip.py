"""The Dependency Inversion Principle states that high-level modules should not depend on low-level modules,\
    but both should depend on abstractions. This means that you should not have to change other sections of\
        your code when you change the implementation of a class.

In practice, this means that our payment processor shouldn’t be concerned \
    with how its payment is validated, whether that be by SMS, a robot check, or an email.
"""

from abc import ABC, abstractmethod


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


class Authorizer(ABC):
    @abstractmethod
    def is_authenticated(self):
        ...


class SMSAuthorizer(Authorizer):
    def __init__(self):
        self.authenticated = False

    def verify_code(self, code: str):
        print("Verifying code")
        self.authenticated = True

    def is_authenticated(self):
        return self.authenticated


class NotARobotAuthorizer(Authorizer):
    def __init__(self):
        self.authenticated = False

    def ask(self):
        print("Are you a robot?!!! [┐∵]┘")
        self.authenticated = True

    def is_authenticated(self):
        return self.authenticated


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order: Order):
        if not self.authorizer.is_authenticated():
            raise Exception("Not authenticated")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order: Order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


order = Order()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

authorizer = NotARobotAuthorizer()

authorizer.ask()

processor = DebitPaymentProcessor("0372846", authorizer)

processor.pay(order)

print(order.status)
