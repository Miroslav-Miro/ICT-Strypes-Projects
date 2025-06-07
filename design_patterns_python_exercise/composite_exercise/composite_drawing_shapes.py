from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Graphic):
    def draw(self):
        print("Drawing Circle")


class Square(Graphic):
    def draw(self):
        print("Drawing Square")


class Group(Graphic):
    def __init__(self):
        self.storage = []

    def add(self, shape):
        self.storage.append(shape)

    def draw(self):
        print("Drawing Group:")
        for graphic_element in self.storage:
            graphic_element.draw()


# circle = Circle()
# square = Square()

# circle.draw()  # Expected: Drawing Circle
# square.draw()  # Expected: Drawing Square

# 2nd test
# group = Group()
# group.add(Circle())
# group.add(Square())

# group.draw()

# 3th test
group1 = Group()
group1.add(Circle())

group2 = Group()
group2.add(Square())
group2.add(group1)

group3 = Group()
group3.add(Square())
group3.add(group2)
group3.add(group1)


group3.draw()
