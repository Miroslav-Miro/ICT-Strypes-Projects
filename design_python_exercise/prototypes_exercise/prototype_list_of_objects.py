import copy
from typing import List

class Person: 
    def __init__(self, name: str, age: int) -> None:
        """
        A class representing a person.
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name: str = name  # Person's name
        self.age: int = age    # Person's age


class Group: 
    def __init__(self, persons: List[Person]) -> None:
        """
        A class representing a group of persons.
        Args:
            persons (List[Person]): A list of Person objects.
        """
        self.persons: List[Person] = persons  # List of persons in the group

    def deep_copy(self) -> 'Group':
        """
        Creates a deep copy of the group.
        Returns:
            Group: A new Group instance with deeply copied Person objects.
        """
        copied_persons: List[Person] = copy.deepcopy(self.persons)  # Deep copy of the persons list
        return Group(copied_persons)  # Return a new Group instance


# Example usage and test
g1 = Group([Person("Alice", 30), Person("Bob", 25)])  # Original group
g2 = g1.deep_copy()  # Deep copy of the group

# Modify the name of the first person in the copied group
g2.persons[0].name = "Charlie"

# Should still be "Alice" in the original group
print("g1 name:", g1.persons[0].name)  # Output: Alice

# Should be "Charlie" in the copied group
print("g2 name:", g2.persons[0].name)  # Output: Charlie