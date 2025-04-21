class Person:
    """
    A class representing a person with a unique ID and name.
    """
    def __init__(self, id: int, name: str) -> None:
        """
        Initialize a new Person instance.
        Args:
            id (int): The unique identifier for the person.
            name (str): The name of the person.
        """
        self.id = id
        self.name = name


class PersonFactory:
    """
    A factory class to create Person instances with unique IDs.
    """
    def __init__(self) -> None:
        """
        Initialize the factory with a counter starting at 0.
        """
        self.counter = 0

    def create_person(self, name: str) -> Person:
        """
        Create a new Person instance with a unique ID and given name.
        Args:
            name (str): The name of the person to create.
        Returns:
            Person: A new Person object with a unique ID.
        """
        p = Person(self.counter, name)
        self.counter += 1
        return p
