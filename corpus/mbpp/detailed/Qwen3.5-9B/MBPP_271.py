def even_Power_Sum(n: int) -> int:
    """
    Calculate the sum of the fifth powers of the first n even natural numbers.

    The first n even natural numbers are: 2, 4, 6, ..., 2*n.
    For example:
    - If n = 1, the number is 2. Result: 2**5 = 32.
    - If n = 2, the numbers are 2, 4. Result: 2**5 + 4**5 = 32 + 1024 = 1056.
    - If n = 3, the numbers are 2, 4, 6. Result: 32 + 1024 + 7776 = 8832.

    Parameters:
        n (int): The count of the first even natural numbers to consider. Must be non-negative.

    Returns:
        int: The sum of the fifth powers of the first n even natural numbers.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """

    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer, got {type(n).__name__}")

    # Validate input range (natural numbers count must be non-negative)
    if n < 0:
        raise ValueError(f"Input 'n' must be non-negative, got {n}")

    # Handle the edge case where n is 0 (no numbers to sum)
    if n == 0:
        return 0

    total_sum = 0

    # Loop from 1 to n (inclusive) to generate the first n even numbers
    # We use an index i from 1 to n to calculate the i-th even number as (2 * i)
    for i in range(1, n + 1):
        # Calculate the current even number
        current_even_number = 2 * i

        # Calculate the fifth power of the current even number
        # We explicitly do this step instead of using a one-liner inside the loop
        fifth_power = current_even_number ** 5

        # Add the fifth power to the running total
        total_sum = total_sum + fifth_power

    # Return the final accumulated sum
    return total_sum