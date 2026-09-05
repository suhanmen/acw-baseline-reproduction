def _is_positive_integer(value):
    """
    Helper function to check if the input is a positive integer (natural number).

    Args:
        value: The value to check.

    Returns:
        bool: True if value is a positive integer, False otherwise.
    """
    if not isinstance(value, int):
        return False
    if value <= 0:
        return False
    return True


def _calculate_cube(n):
    """
    Helper function to calculate the cube of a given number.

    Args:
        n (int): The number to be cubed.

    Returns:
        int: The cube of the number.
    """
    result = n * n * n
    return result


def sum_Of_Series(n):
    """
    Calculates the sum of the cubes of the first n natural numbers.

    The problem defines natural numbers as starting from 1.
    For n = 5, the sum is 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225.

    Args:
        n (int): The number of terms to consider from the sequence of natural numbers (1, 2, 3...).

    Returns:
        int: The sum of the cubes of the first n natural numbers.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not a positive integer (n <= 0).
    """
    # Step 1: Validate the input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Step 2: Validate the input value constraints (must be a positive integer)
    if n <= 0:
        raise ValueError(f"Input must be a positive integer (natural number), got {n}")

    # Step 3: Initialize the accumulator variable for the sum
    total_sum = 0

    # Step 4: Iterate through the first n natural numbers (1 to n inclusive)
    current_number = 1

    while current_number <= n:
        # Step 5: Calculate the cube of the current number
        cube_value = _calculate_cube(current_number)

        # Step 6: Add the cube value to the running total
        total_sum = total_sum + cube_value

        # Step 7: Move to the next natural number
        current_number = current_number + 1

    # Step 8: Return the calculated sum
    return total_sum