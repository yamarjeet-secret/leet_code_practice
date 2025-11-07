
"""Prototype pattern, is a creational design pattern that allows you to copy existing objects \
    without making your code dependent on their classes. The Prototype Factory typically includes a registry to manage prototypes.\
        
    The Prototype Factory pattern is useful when the cost of creating an object is more expensive or complex than copying an existing instance. \
    It also allows you to add and remove objects at runtime, which can be useful for managing a set of "prototypes" that clients can customize and clone as needed.
"""


import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'

class Employee:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )

# main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
# aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

# john = copy.deepcopy(main_office_employee)
#john.name = "John"
#john.address.suite = 101
#print(john)

# would prefer to write just one line of code
jane = EmployeeFactory.new_aux_office_employee("Jane", 200)
print(jane)







import copy
from abc import ABC, abstractmethod

# Vehicle interface with a clone method
class Vehicle(ABC):
    def __init__(self, source=None):
        if source:
            self.make = source.make
            self.model = source.model
            self.color = source.color

    @abstractmethod
    def clone(self):
        pass

# Concrete implementation of a Car
class Car(Vehicle):
    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.doors = source.doors

    def clone(self):
        return Car(self)

# Concrete implementation of a Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.cc = source.cc

    def clone(self):
        return Motorcycle(self)




class VehicleRegistry:
    def __init__(self):
        self._vehicles = {}

    def register_vehicle(self, name, vehicle):
        self._vehicles[name] = vehicle

    def unregister_vehicle(self, name):
        del self._vehicles[name]

    def get_vehicle(self, name):
        vehicle = self._vehicles.get(name)
        if vehicle:
            return vehicle.clone()
        raise ValueError(f"Vehicle name '{name}' not registered.")





def main():
    registry = VehicleRegistry()

    car = Car()
    car.make = "Toyota"
    car.model = "Corolla"
    car.color = "Blue"
    car.doors = 4

    motorcycle = Motorcycle()
    motorcycle.make = "Harley-Davidson"
    motorcycle.model = "Street 750"
    motorcycle.color = "Black"
    motorcycle.cc = 750

    registry.register_vehicle('BlueCar', car)
    registry.register_vehicle('BlackMotorcycle', motorcycle)

    cloned_car = registry.get_vehicle('BlueCar')
    cloned_motorcycle = registry.get_vehicle('BlackMotorcycle')

    print(cloned_car.__dict__)
    print(cloned_motorcycle.__dict__)

if __name__ == "__main__":
    main()

