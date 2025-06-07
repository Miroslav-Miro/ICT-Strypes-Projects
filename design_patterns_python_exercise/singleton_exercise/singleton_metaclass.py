from typing import Any, Dict, Type


class SingletonMeta(type):
    """
    Metaclass that implements the Singleton design pattern.
    Ensures only one instance of any class using this metaclass exists.
    """

    _instance: Dict[Type, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Overrides the __call__ method to control the instantiation process.
        If an instance of the class doesn't already exist, it creates one.
        Otherwise, it returns the existing instance.
        """
        if cls not in cls._instance:
            # Create a new instance and store it in the _instance dictionary
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=SingletonMeta):
    """
    Example class that simulates a database connection.
    Uses SingletonMeta to ensure only one instance is created.
    """

    def __init__(self) -> None:
        print("Connecting to database...")


# Testing the singleton behavior
db1 = Database()
db2 = Database()

# This should print True
print(db1 is db2)
