def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even."""
    product = 1
    for d in str(n):
        digit = int(d)
        if digit % 2 != 0:
            product *= digit
    return product if product != 1 else 0