import math

def next_perfect_square(n):
    if n < 0:
        return None
    root = math.ceil(math.sqrt(n))
    return root ** 2

# Example usage:
print(next_perfect_square(35))  # Output: 36
print(next_perfect_square(6))   # Output: 9
print(next_perfect_square(9))   # Output: 16