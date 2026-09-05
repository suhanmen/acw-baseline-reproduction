def square_Sum(n):
    """
    Finds the sum of squares of the first n odd natural numbers.
    The first n odd natural numbers are 1, 3, 5, ..., (2n - 1).
    """
    total_sum = 0
    for i in range(1, n + 1):
        odd_number = 2 * i - 1
        total_sum += odd_number ** 2
    return total_sum

if __name__ == "__main__":
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84