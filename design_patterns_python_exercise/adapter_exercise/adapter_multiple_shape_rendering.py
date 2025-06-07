class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


def render_shape(shape):
    print(f"Rendering shape: {shape.get_width()} x {shape.get_height()}")


class ShapeAdapter:
    def __init__(self, shape):
        self.shape = shape
        self.width = 0
        self.height = 0

    def get_width(self):
        if isinstance(self.shape, Rectangle):
            return self.shape.width
        elif isinstance(self.shape, Circle):
            return self.shape.radius * 2

    def get_height(self):
        if isinstance(self.shape, Rectangle):
            return self.shape.height
        elif isinstance(self.shape, Circle):
            return self.shape.radius * 2


rect = Rectangle(4, 10)
circle = Circle(3)

adapter1 = ShapeAdapter(rect)
adapter2 = ShapeAdapter(circle)

render_shape(adapter1)  # Expected: 4 x 10
render_shape(adapter2)  # Expected: 6 x 6
