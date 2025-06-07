class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.height = square.side
        self.width = square.side


sq = Square(11)
adapter = SquareToRectangleAdapter(sq)
print(calculate_area(adapter))  # should print 25
