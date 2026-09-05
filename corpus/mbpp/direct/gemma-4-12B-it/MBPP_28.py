import math

def binomial_Coeff(n, k):
    """
    Calculates the binomial coefficient C(n, k) which represents
    the number of ways to choose k items from n items without regard to order.

    The formula is: n! / (k! * (n - k)!)
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k

    # Using the multiplicative formula for efficiency
    # C(n, k) = (n * (n-1) * ... * (n-k+1)) / (k * (k-1) * ... * 1)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (n - i)
        denominator *= (i + 1)

    return numerator // denominator

if __name__ == "__main__":
    assert binomial_Coeff(5, 2) == 10
    assert binomial_Coeff(4, 3) == 4
    assert binomial_Coeff(3, 2) == 3