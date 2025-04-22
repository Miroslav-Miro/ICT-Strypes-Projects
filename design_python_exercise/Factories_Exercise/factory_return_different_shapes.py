from typing import Union


class Shape:
    """
    Base class for all shapes.
    """

    def __init__(self) -> None:
        pass


class Square(Shape):
    """
    A class representing a square shape.
    """

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "Square"


class Circle(Shape):
    """
    A class representing a circle shape.
    """

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "Circle"


class ShapeFactory:
    """
    Factory class to create shape instances based on shape type.
    """

    def create_shape(self, shape_type: str) -> Union[Shape, None]:
        """
        Create and return a shape instance based on the shape_type.
        Args:
            shape_type (str): The type of shape to create ('Circle' or 'Square').
        Returns:
            Shape: An instance of Circle or Square.
            None: If the shape_type is not recognized.
        """
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        return None
