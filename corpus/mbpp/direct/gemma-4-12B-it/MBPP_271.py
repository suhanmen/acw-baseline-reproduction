def even_Power_Sum(n):
    """
    Calculates the sum of the fifth power of the first n even natural numbers.
    The first n even numbers are 2, 4, 6, ..., 2n.
    """
    total_sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        total_sum += even_number ** 5
    return total_sum

if __name__ == "__main__":
    assert even_Power_Sum(1) == 32
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832