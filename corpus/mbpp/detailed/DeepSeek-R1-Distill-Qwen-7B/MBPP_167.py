def next_Power_Of_2(n):
    """
    Find the smallest power of 2 that is greater than or equal to n.
    """
    # Handle the case where n is 0
    if n == 0:
        return 1

    # Handle the case where n is a positive integer
    n = int(n)
    if n <= 0:
        return 1

    # Calculate the logarithm base 2 of n
    log_n = math.log(n, 2)

    # Take the ceiling of the logarithm to get the smallest integer exponent
    exponent = math.ceil(log_n)

    # Calculate the smallest power of 2 greater than or equal to n
    result = 2 ** exponent

    return result