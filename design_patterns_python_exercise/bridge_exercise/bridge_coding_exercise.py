from abc import ABC


class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Triangle"


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Square"


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"


print(str(Triangle(VectorRenderer())))  # should print: Drawing Triangle as lines
print(str(Square(RasterRenderer())))  # should print: Drawing Square as pixels
