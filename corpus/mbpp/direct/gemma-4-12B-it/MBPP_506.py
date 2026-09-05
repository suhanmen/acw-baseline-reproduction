def permutation_coefficient(n, k):
    """
    Calculates the permutation coefficient P(n, k) = n! / (n - k)!
    which is equal to n * (n - 1) * ... * (n - k + 1).
    """
    if k < 0 or k > n:
        return 0

    coefficient = 1
    for i in range(k):
        coefficient *= (n - i)

    return coefficient

if __name__ == "__main__":
    assert permutation_coefficient(10, 2) == 90
    assert permutation_coefficient(10, 3) == 720
    assert permutation_coefficient(10, 1) == 10