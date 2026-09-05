def cube_Sum(n):
    """
    Calculate the sum of the cubes of the first n even natural numbers.
    First n even numbers: 2, 4, 6, ..., 2*n
    """
    return sum((i * 2) ** 3 for i in range(1, n + 1))