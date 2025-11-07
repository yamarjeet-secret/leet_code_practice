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


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        ...

    @abstractmethod
    def auth_sms(self, order, code: str):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code
        self.authenticated = False

    def pay(self, order):
        if not self.authenticated:
            raise Exception("Not authenticated")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

    def auth_sms(self, order, code: str):
        print("Authenticating via SMS")
        self.authenticated = True


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

    def auth_sms(self, order, code: str):
        raise Exception("Not implemented")


order = Order()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = DebitPaymentProcessor("0372846")
processor.auth_sms(order, "12345")
processor.pay(order)
print(order.status)


"""
    This code violates the ISP because the CreditPaymentProcessor class is forced to implement \
    the auth_sms method, even though it does not use it. This not only means we end up \
    writing more code, but it could potentially cause bugs if we forget to implement the method.
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


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        ...


class SmsPaymentProcessor(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, order: Order, code: str):
        ...


class DebitPaymentProcessor(SmsPaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code
        self.authenticated = False

    def pay(self, order):
        if not self.authenticated:
            raise Exception("Not authenticated")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

    def auth_sms(self, order, code: str):
        print("Authenticating via SMS")
        self.authenticated = True


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


order = Order()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = DebitPaymentProcessor("0372846")
processor.auth_sms(order, "12345")
processor.pay(order)

print(order.status)
