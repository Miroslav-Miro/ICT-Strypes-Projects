class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """
        A class to represent a point in 2D space.
        Args:
            x (int): The x-coordinate. Defaults to 0.
            y (int): The y-coordinate. Defaults to 0.
        """
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        """
        A class to represent a rectangle using top-left and bottom-right points.
        Args:
            top_left (Point): The top-left corner of the rectangle.
            bottom_right (Point): The bottom-right corner of the rectangle.
        """
        self.top_left = top_left
        self.bottom_right = bottom_right

    def deep_copy(self) -> "Rectangle":
        """
        Creates a deep copy of the rectangle.
        Returns:
            Rectangle: A new Rectangle object with copied Point instances.
        """
        # Copy coordinates of the corner points
        top_copy = Point(self.top_left.x, self.top_left.y)
        bottom_copy = Point(self.bottom_right.x, self.bottom_right.y)

        # Return a new Rectangle with the copied points
        return Rectangle(top_copy, bottom_copy)


# Example usage and test
r1 = Rectangle(Point(0, 0), Point(4, 5))
r2 = r1.deep_copy()

# Modify r2 to ensure deep copy works
r2.top_left.x = 10

# Print coordinates to verify independence
print("Rectangle 1 top-left:", r1.top_left.x, r1.top_left.y)  # Should remain (0, 0)
print("Rectangle 2 top-left:", r2.top_left.x, r2.top_left.y)  # Should be (10, 0)
