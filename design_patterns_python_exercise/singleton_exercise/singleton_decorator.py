from typing import Any, Callable, Dict, TypeVar, Type

T = TypeVar("T")


def singleton(cls: Type[T]) -> Callable[..., T]:
    """
    A decorator that makes a class a Singleton.
    Ensures that only one instance of the class is created.
    Args:
        cls: The class to be turned into a Singleton.
    Returns:
        A function that returns the singleton instance of the class.
    """
    instances: Dict[Type, T] = {}

    def get_instance(*args: Any, **kwargs: Any) -> T:
        """
        Returns the singleton instance of the decorated class.
        Creates a new one if it doesn't already exist.
        """
        if cls not in instances:
            # Instantiate and cache the instance
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Logger:
    """
    Example class that demonstrates the Singleton behavior.
    This class will only be instantiated once.
    """

    def __init__(self) -> None:
        print("Logger created")


# Testing the singleton behavior
l1 = Logger()
l2 = Logger()

# This should print True
print(l1 is l2)
