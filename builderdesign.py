class Pizza:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushroom = False
        self.bacon = False

    def __str__(self):
        return (f"Size: {self.size}, Cheese: {'Yes' if self.cheese else 'No'}, "
                f"Pepperoni: {'Yes' if self.pepperoni else 'No'}, "
                f"Mushroom: {'Yes' if self.mushroom else 'No'}, "
                f"Bacon: {'Yes' if self.bacon else 'No'}")




class PizzaBuilder:
    def __init__(self, size):
        self.pizza = Pizza(size)

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushroom(self):
        self.pizza.mushroom = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


"""The PizzaBuilder class provides methods for adding toppings to the Pizza object. Each method returns the PizzaBuilder object itself,\
    allowing for method chaining. The build() method returns the final Pizza object.
"""

def main():
    pizza_builder = PizzaBuilder(size="Large")
    pizza = (pizza_builder
             .add_cheese()
             .add_pepperoni()
             .add_mushroom()
             .build())
    print(pizza)

if __name__ == "__main__":
    main()
