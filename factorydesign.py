from abc import ABC, abstractmethod

# Shape interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete implementation of a Circle
class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

# Concrete implementation of a Square
class Square(Shape):
    def draw(self):
        print("Drawing a square.")

# Concrete implementation of a Rectangle
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle.")

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type.lower() == 'circle':
            return Circle()
        elif shape_type.lower() == 'square':
            return Square()
        elif shape_type.lower() == 'rectangle':
            return Rectangle()
        else:
            raise ValueError(f"Shape type '{shape_type}' not supported.")

def main():
    circle = ShapeFactory.get_shape('circle')
    circle.draw()

    square = ShapeFactory.get_shape('square')
    square.draw()

    rectangle = ShapeFactory.get_shape('rectangle')
    rectangle.draw()

    # This will raise an error as the shape type 'triangle' is not supported
    # triangle = ShapeFactory.get_shape('triangle')
    # triangle.draw()

if __name__ == "__main__":
    main()
