from abc import ABC


class ValueContainer(ABC):
    @property
    def sum(self):
        return sum(x for x in self)


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(ValueContainer, list):
    def __iter__(self):
        for item in super().__iter__():  # iterates the list
            if hasattr(item, "__iter__") and not isinstance(item, (str, bytes)):
                yield from item
            else:
                yield item
