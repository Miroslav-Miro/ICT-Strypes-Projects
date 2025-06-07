class Circle:
    def __init__(self, radius):
        self.radius = radius


def get_shape_area(shape):
    return shape.width * shape.height  # expects width & height


class CircleAdapter:
    def __init__(self, circle):
        self.width = circle.radius * 2
        self.height = circle.radius * 2


circle = Circle(5)
adapter = CircleAdapter(circle)
print(get_shape_area(adapter))  # Expected output: 100
