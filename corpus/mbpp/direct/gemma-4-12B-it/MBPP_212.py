def fourth_Power_Sum(n):
    """
    Calculates the sum of the fourth powers of the first n natural numbers.
    Formula: Sum(i^4) for i from 1 to n.
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i**4
    return total_sum

if __name__ == "__main__":
    assert fourth_Power_Sum(2) == 17
    assert fourth_Power_Sum(4) == 354
    assert fourth_Power_Sum(6) == 2275