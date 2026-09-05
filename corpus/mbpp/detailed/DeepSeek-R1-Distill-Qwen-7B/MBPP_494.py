# Valid binary tuples
print(binary_to_integer((1, 1, 0, 1, 0, 0, 1)))  # Output: 105
print(binary_to_integer((0, 1, 1, 0, 0, 1, 0, 1)))  # Output: 101
print(binary_to_integer((1, 1, 0, 1, 0, 1)))  # Output: 53

# Invalid binary tuple
print(binary_to_integer((2, 3, 4)))  # Raises ValueError

# Empty tuple
print(binary_to_integer(()))  # Output: 0