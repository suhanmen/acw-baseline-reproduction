def zigzag(n, k):
    """
    Compute the entringer number e(n, k).

    The function calculates the sum of the first k positive integers
    that are less than or equal to n. If k exceeds n, it adjusts by 
    subtracting the excess from n.
    """
    if n < 0 or k < 0:
        raise ValueError("Negative values for n or k are not allowed.")

    # Ensure k is not greater than n
    if k > n:
        k = n

    # Calculate the sum of the first k integers up to n
    total = (k * (k + 1)) // 2
    # Adjust if k exceeds n
    if k > n:
        total -= (k - n) * (k - n + 1) // 2

    return total