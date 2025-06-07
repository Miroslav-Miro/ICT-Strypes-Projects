from typing import List, Dict


class Router:
    """
    Represents a network router.
    Attributes:
        ip (str): The IP address of the router.
    """

    def __init__(self, ip: str) -> None:
        """
        Initialize a Router instance.

        Args:
            ip (str): The IP address of the router.
        """
        self.ip = ip


class Computer:
    """
    Represents a computer connected to a router.
    Attributes:
        name (str): The name of the computer.
        router (Router): The router this computer is connected to.
    """

    def __init__(self, name: str, router: Router) -> None:
        """
        Initialize a Computer instance.
        Args:
            name (str): The name of the computer.
            router (Router): The router the computer is connected to.
        """
        self.name = name
        self.router = router


class Network:
    """
    Represents a network of computers.
    Attributes:
        computers (List[Computer]): List of computers in the network.
    """

    def __init__(self, computers: List[Computer]) -> None:
        """
        Initialize a Network instance.
        Args:
            computers (List[Computer]): List of Computer objects.
        """
        self.computers = computers

    def deep_copy(self) -> "Network":
        """
        Create a deep copy of the network.
        Returns:
            Network: A new Network instance with copied computers and routers.
        """
        new_computers: List[Computer] = []

        router_mapping: Dict[Router, Router] = {}

        # First, copy each unique router only once
        for computer in self.computers:
            if computer.router not in router_mapping:
                router_mapping[computer.router] = Router(computer.router.ip)

        # Then, copy each computer and assign the copied router
        for computer in self.computers:
            new_router = router_mapping[computer.router]
            new_computer = Computer(computer.name, new_router)
            new_computers.append(new_computer)

        return Network(new_computers)


# Example usage:
router1 = Router("192.168.1.1")
router2 = Router("10.0.0.1")

# Create initial network with computers connected to routers
net1 = Network(
    [
        Computer("Comp1", router1),
        Computer("Comp2", router1),
        Computer("Comp3", router2),
        Computer("Comp4", router2),
    ]
)

# Create a deep copy of the network
net2 = net1.deep_copy()

# Modify the router in the copied network
net2.computers[0].router.ip = "8.8.8.8"

# The original network should remain unchanged
print(net1.computers[0].router.ip)  # Output: 192.168.1.1
print(net1.computers[1].router.ip)  # Output: 192.168.1.1

# The copied network reflects the change
print(net2.computers[0].router.ip)  # Output: 8.8.8.8
print(net2.computers[1].router.ip)  # Output: 8.8.8.8

# Computers 3 and 4 share the second router copy
print(net2.computers[2].router.ip)  # Output: 10.0.0.1
print(net2.computers[3].router.ip)  # Output: 10.0.0.1
