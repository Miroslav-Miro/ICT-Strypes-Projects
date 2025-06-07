class Singleton:
    """
    A basic Singleton class using the __new__ method to ensure
    only one instance of the class is created.
    """

    _instance: "Singleton" = None  # Holds the single instance of the class

    def __new__(cls) -> "Singleton":
        """
        Overrides object creation. If an instance does not already exist,
        creates one and stores it in the _instance class variable.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Initializes the Singleton instance.
        This method is called every time an instance is created,
        but the object itself is only created once.
        """
        self.name = "Elena"


# Testing the Singleton behavior
s1 = Singleton()
s2 = Singleton()

print(s1.name)  # Elena
print(s2.name)  # Elena

# Check that both variables point to the same instance
print(s1 is s2)  # True

# Changing an attribute through one instance affects the other
s2.name = "Changed"
print(s1.name)  # Changed (because s1 and s2 are the same object)
