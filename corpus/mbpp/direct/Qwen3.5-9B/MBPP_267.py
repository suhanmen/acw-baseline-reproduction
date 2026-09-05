def square_Sum(n):
    """Return the sum of squares of the first n odd natural numbers."""
    return sum((2 * i + 1) ** 2 for i in range(n))