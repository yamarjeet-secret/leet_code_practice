""" Let's consider a scenario where we have a Car class that our application uses to accelerate vehicles. \
    However, we now want to integrate a Bicycle that has a different interface for increasing speed. Instead\
    of refactoring the entire application to support the bicycle's interface, we can create an adapter.
"""
class Car:
    def accelerate(self):
        print("Car is accelerating")

class Bicycle:
    def pedal_harder(self):
        print("Bicycle speed is increasing by pedaling harder")


class BicycleAdapter:
    def __init__(self, bicycle:Bicycle):
        self.bicycle = bicycle

    def accelerate(self):
        # The adapter calls the new interface method
        self.bicycle.pedal_harder()


# Existing application code
def start_race(vehicle):
    vehicle.accelerate()

# Car usage
car = Car()
start_race(car)

# Bicycle usage with adapter
bicycle = Bicycle()
bicycle_adapter = BicycleAdapter(bicycle)
start_race(bicycle_adapter)
