from typing import Callable, Any


def is_singleton(factory: Callable[[], Any]) -> bool:
    """
    Checks whether the given factory function returns a singleton instance.
    Args:
        factory: A zero-argument callable (class or factory function) that returns an instance of an object.
    Returns:
        True if the factory returns the same instance on multiple calls,
        False otherwise.
    """
    factory1 = factory()
    factory2 = factory()

    # Compare the two instances to check if they are the same object
    return factory1 is factory2
