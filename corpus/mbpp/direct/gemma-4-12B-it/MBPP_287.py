def square_Sum(n):
    """
    Finds the sum of squares of the first n even natural numbers.
    The first n even natural numbers are 2, 4, 6, ..., 2n.
    """
    total_sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        total_sum += even_number ** 2
    return total_sum

if __name__ == "__main__":
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120