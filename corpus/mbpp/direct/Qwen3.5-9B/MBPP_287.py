def square_Sum(n):
    """
    Returns the sum of squares of the first n even natural numbers.
    Even numbers: 2, 4, 6, ...
    Square of 2nd even number (4) is 16.
    """
    total = 0
    for i in range(1, n + 1):
        even_num = 2 * i
        total += even_num ** 2
    return total