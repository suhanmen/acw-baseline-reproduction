def sumofFactors(n):
    """
    Calculate the sum of even factors of a given number n.

    Parameters:
    n (int): The number for which to find even factors.

    Returns:
    int: The sum of even factors of n, or 0 if n is 0 or 1 (no even factors).

    Raises:
    ValueError: If n is a negative number.
    """
    # Handle invalid input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Number cannot be negative.")

    # Handle edge cases
    if n == 0 or n == 1:
        return 0

    # Extract the power of 2 from n
    k = 0
    temp = n
    while temp % 2 == 0:
        temp = temp // 2
        k += 1

    # If there are no even factors (n is odd)
    if k == 0:
        return 0

    # Now, compute the sum of factors of the remaining part (which is odd)
    sum_odd = 1
    i = 3
    max_factor = (temp ** 0.5)  # Using sqrt for efficiency

    while i <= max_factor:
        if i * i > temp:
            break  # No more factors

        if temp % i == 0:
            sum_odd *= (i ** (exponent(temp, i) + 1) - 1)
            max_factor = max(max_factor, exponent(temp, i))

        i += 2  # Increment by 2 to skip even numbers

    # Calculate the sum using the formula
    sum_even = 2 * sum_odd * (2 ** k - 1)

    return sum_even

def exponent(number, factor):
    """
    Calculate the highest power of a factor that divides a number.

    Parameters:
    number (int): The number to factorize.
    factor (int): The prime factor to find the exponent for.

    Returns:
    int: The highest exponent such that factor^exponent divides the number.
    """
    exponent = 0
    while number % factor == 0:
        exponent += 1
        number = number // factor
    return exponent