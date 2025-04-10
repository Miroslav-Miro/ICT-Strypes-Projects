import random

"""
Section 13: Problem 2

This script defines a generator function that yields a specified number of random integers
within a given inclusive range and prints them one by one.
"""

def rand_num(low, high, n):
    """
    Generates a sequence of 'n' random integers between 'low' and 'high'.

    Parameters:
    low (int): The lower bound of the random number range.
    high (int): The upper bound of the random number range.
    n (int): The number of random integers to generate.
    Yields:
    int: A random integer between 'low' and 'high'.
    """
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)
