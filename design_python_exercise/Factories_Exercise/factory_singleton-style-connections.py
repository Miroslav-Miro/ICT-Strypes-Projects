class Connection:
    """
    Represents a connection identified by a unique name.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a new Connection instance.

        Args:
            name (str): The name identifying the connection.
        """
        self.name = name


class ConnectionFactory:
    """
    Factory that manages and reuses Connection instances by name.
    Implements a basic flyweight pattern.
    """

    def __init__(self) -> None:
        """
        Initialize the factory with an empty connection pool.
        """
        self.connections: dict[str, Connection] = {}

    def get_connection(self, name: str) -> Connection:
        """
        Retrieve an existing connection by name or create a new one if not found.

        Args:
            name (str): The name of the connection.

        Returns:
            Connection: A shared or newly created Connection object.
        """
        if name not in self.connections:
            self.connections[name] = Connection(name)
        return self.connections[name]


# Example usage
factory = ConnectionFactory()

c1 = factory.get_connection("main_db")
c2 = factory.get_connection("cache")
c3 = factory.get_connection("main_db")

print(c1 is c3)  # True, reused
print(c1.name)  # "main_db"
print(c2.name)  # "cache"
