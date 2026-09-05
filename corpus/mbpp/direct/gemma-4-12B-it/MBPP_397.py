def median_numbers(a, b, c):
    """
    Returns the median of three numbers.
    """
    numbers = [a, b, c]
    numbers.sort()
    return float(numbers[1])

if __name__ == "__main__":
    assert median_numbers(25, 55, 65) == 55.0
    assert median_numbers(20, 10, 30) == 20.0
    assert median_numbers(15, 45, 75) == 45.0