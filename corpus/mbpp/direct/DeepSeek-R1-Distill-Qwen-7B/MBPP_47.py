def compute_Last_Digit(a, b):
    """
    Find the last digit when factorial of a divides factorial of b.
    """
    from math import factorial

    if a > b:
        return 0
    fact_a = factorial(a)
    fact_b = factorial(b)
    quotient = fact_b // fact_a
    return quotient % 10

# Example usage:
# assert compute_Last_Digit(2,4) == 2
# assert compute_Last_Digit(6,8) == 6
# assert compute_Last_Digit(1,2) == 2