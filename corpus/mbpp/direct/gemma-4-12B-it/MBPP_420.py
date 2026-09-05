def cube_Sum(n):
    """
    Finds the sum of the cubes of the first n even natural numbers.
    The first n even natural numbers are 2, 4, 6, ..., 2n.
    The sum is (2^3) + (4^3) + (6^3) + ... + (2n^3).

    Mathematical simplification:
    Sum = sum_{i=1}^n (2i)^3 = sum_{i=1}^n 8i^3 = 8 * sum_{i=1}^n i^3.
    The formula for the sum of the first n cubes is [n(n+1)/2]^2.
    So, Sum = 8 * [n(n+1)/2]^2 = 8 * [n^2(n+1)^2 / 4] = 2 * n^2 * (n+1)^2.
    """
    total_sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        total_sum += even_number ** 3
    return total_sum

if __name__ == "__main__":
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800