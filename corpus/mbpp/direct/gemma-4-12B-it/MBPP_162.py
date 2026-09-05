def sum_series(n):
    """
    Calculates the sum of the positive integers in the series
    n + (n-2) + (n-4) + ... until the term becomes <= 0.
    """
    total_sum = 0
    current_value = n
    while current_value > 0:
        total_sum += current_value
        current_value -= 2
    return total_sum

if __name__ == "__main__":
    assert sum_series(6) == 12
    assert sum_series(10) == 30
    assert sum_series(9) == 25