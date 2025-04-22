from typing import Optional


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """
        A class representing a point in 2D space.
        Args:
            x (int): The x-coordinate. Defaults to 0.
            y (int): The y-coordinate. Defaults to 0.
        """
        self.x = x
        self.y = y


class Line:
    def __init__(
        self, start: Optional[Point] = None, end: Optional[Point] = None
    ) -> None:
        """
        A class representing a line segment in 2D space, defined by two Points.
        Args:
            start (Point): The starting point of the line. Defaults to (0, 0).
            end (Point): The ending point of the line. Defaults to (0, 0)
        """
        self.start = start if start else Point()
        self.end = end if end else Point()

    def deep_copy(self) -> "Line":
        """
        Creates a deep copy of the Line object.
        Returns:
            Line: A new Line object with copied Point instances for start and end.
        """
        # Correctly create new Point instances with copied coordinates
        start_point = Point(self.start.x, self.start.y)
        end_point = Point(self.end.x, self.end.y)

        # Create a new Line object with the copied points
        copied_line = Line(start_point, end_point)

        return copied_line


# Test case
line1 = Line(Point(1, 2), Point(3, 4))
line2 = line1.deep_copy()

# Modify line2's start point
line2.start.x = 9
line2.start.y = 9

# Should be 1, 2
print("Line 1 start:", line1.start.x, line1.start.y)

# Should be 9, 9
print("Line 2 start:", line2.start.x, line2.start.y)
