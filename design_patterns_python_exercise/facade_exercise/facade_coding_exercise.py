import random


class Generator:
    def generate(self, size):
        return [random.randint(1, 9) for _ in range(size * size)]


class Splitter:
    def split(self, square):
        size = len(square)
        result = []

        # Rows
        for row in square:
            result.append(row)

        # Columns
        for col in range(size):
            result.append([square[row][col] for row in range(size)])

        # Diagonal top-left to bottom-right
        result.append([square[i][i] for i in range(size)])

        # Diagonal top-right to bottom-left
        result.append([square[i][size - i - 1] for i in range(size)])

        return result


class Verifier:
    def verify(self, sublists):
        if not sublists:
            return False

        expected_sum = sum(sublists[0])
        return all(sum(sublist) == expected_sum for sublist in sublists)


class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            data = self.generator.generate(size)
            square = [data[i * size : (i + 1) * size] for i in range(size)]
            parts = self.splitter.split(square)

            if self.verifier.verify(parts):
                return square
