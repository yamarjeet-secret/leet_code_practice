
"""The Observer design pattern is a behavioral design pattern that defines a one-to-many dependency between objects so \
    that when one object changes state, all its dependents are notified and updated automatically. This pattern is often \
        used to implement distributed event handling systems, where the subject is the object that holds the state, \
    and the observers are the objects that receive the notification when there's a change in the subject's state. 
"""


class Product:
    """Let's consider a more practical example where we have a Product class as the subject, and it notifies observers\
        when its price changes. We'll have two types of observers: EmailAlert \
        and MobileAlert, which simulate sending an email and a mobile notification, respectively, when the product price changes.
    """

    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price != self._price:
            self._price = new_price
            self._notify()

class Observer:
    def update(self, subject):
        raise NotImplementedError("Subclasses must override update() method")

class EmailAlert(Observer):
    def update(self, product):
        print(f"Email Alert: The price of {product._name} has changed to ${product._price}!")

class MobileAlert(Observer):
    def update(self, product):
        print(f"Mobile Alert: The price of {product._name} has changed to ${product._price}!")

# Usage
product = Product('Python Design Patterns Book', 29.99)

email_alert = EmailAlert()
mobile_alert = MobileAlert()

product.attach(email_alert)
product.attach(mobile_alert)

# Change the price, which triggers notifications
product.price = 24.99

# Detach the email alert and change the price again
product.detach(email_alert)
product.price = 19.99

