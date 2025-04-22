"""
Section 13: Problem 3

This script demonstrates iteration over a string using both a for-loop and manual iteration
with the iter() and next() functions.
"""

s = "hello"

# Using for-loop iteration
for char in s:
    print(char)

print("\n")

# Using iter() and next()
print("iter use -->")
word_iter = iter(s)

try:
    print(next(word_iter))
    print(next(word_iter))
    print(next(word_iter))
    print(next(word_iter))
    print(next(word_iter))
except StopIteration:
    print("End of string reached.")
