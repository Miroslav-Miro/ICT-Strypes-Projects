from abc import ABC


class Shape(ABC):
    def __init__(self, color):
        self.color = color
        self.name = None

    def describe(self):
        return f"Drawing a {self.name} in {self.color}"


class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Circle"


class Square(Shape):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Square"


class Rectangle(Shape):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Rectangle"


class Color:
    def __str__(self):
        return "some color"


class Red(Color):
    def __str__(self):
        return "red"


class Blue(Color):
    def __str__(self):
        return "blue"


class Purple(Color):
    def __str__(self):
        return "purple"


circle = Circle(Red())
square = Square(Blue())

print(circle.describe())  # Drawing a Circle in red
print(square.describe())  # Drawing a Square in blue
