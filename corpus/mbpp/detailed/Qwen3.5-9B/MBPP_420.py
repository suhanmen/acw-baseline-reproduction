from typing import Union

def _is_positive_integer(value: Union[int, float]) -> bool:
    """
    Helper function to validate that the input is a positive integer.

    A valid input for n must be:
    1. An integer (not a float, even if it looks like one).
    2. Greater than or equal to 1.

    Args:
        value: The value to check.

    Returns:
        True if the value is a positive integer, False otherwise.
    """
    if not isinstance(value, int):
        return False

    if value <= 0:
        return False

    return True

def _generate_first_n_evens(n: int) -> list:
    """
    Helper function to generate the first n even natural numbers.

    Natural numbers typically start from 1. Even natural numbers are 2, 4, 6, ...
    The first n even natural numbers are 2, 4, ..., 2n.

    Args:
        n: The number of even natural numbers to generate.

    Returns:
        A list containing the first n even natural numbers.
    """
    even_numbers = []
    current_even = 2

    for _ in range(n):
        even_numbers.append(current_even)
        current_even += 2

    return even_numbers

def _cube_number(number: int) -> int:
    """
    Helper function to calculate the cube of a number.

    Args:
        number: The number to cube.

    Returns:
        The result of number cubed (number ** 3).
    """
    return number ** 3

def _sum_list(numbers: list) -> int:
    """
    Helper function to calculate the sum of a list of numbers.

    This is an explicit implementation of summation to avoid hidden complexity
    inside built-in functions, adhering to the requirement for explicit steps.

    Args:
        numbers: A list of integers to sum.

    Returns:
        The sum of the integers in the list.
    """
    total_sum = 0

    for number in numbers:
        total_sum = total_sum + number

    return total_sum

def cube_Sum(n: Union[int, float]) -> int:
    """
    Calculate the cube sum of the first n even natural numbers.

    The function computes the sum of the cubes of the first n even natural numbers.
    The sequence of the first n even natural numbers is: 2, 4, 6, ..., 2n.
    We need to calculate: 2^3 + 4^3 + 6^3 + ... + (2n)^3.

    Args:
        n: The count of the first even natural numbers to consider.
           Must be a positive integer.

    Returns:
        The sum of the cubes of the first n even natural numbers as an integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is less than or equal to 0.

    Examples:
        cube_Sum(2) returns 72 (2^3 + 4^3 = 8 + 64)
        cube_Sum(3) returns 288 (2^3 + 4^3 + 6^3 = 8 + 64 + 216)
        cube_Sum(4) returns 800 (2^3 + 4^3 + 6^3 + 8^3 = 8 + 64 + 216 + 512)
    """
    # Step 1: Validate the input explicitly
    if not _is_positive_integer(n):
        if isinstance(n, (int, float)):
            raise TypeError(
                f"Input 'n' must be a positive integer. "
                f"Received type '{type(n).__name__}' with value {n}."
            )
        else:
            raise TypeError(
                f"Input 'n' must be a positive integer. "
                f"Received an object of unknown type '{type(n).__name__}'."
            )

    # Step 2: Generate the list of the first n even natural numbers
    # Explicitly constructing the list allows us to handle edge cases like n=1 clearly.
    even_natural_numbers = _generate_first_n_evens(n)

    # Step 3: Initialize the accumulator for the sum
    # Start with zero to ensure correct accumulation for any list size.
    running_cube_sum = 0

    # Step 4: Iterate through each generated number, cube it, and add to the sum
    for current_number in even_natural_numbers:
        # Calculate the cube of the current even number
        current_cube = _cube_number(current_number)

        # Add the cube to the running total
        running_cube_sum = running_cube_sum + current_cube

    # Step 5: Return the final calculated sum
    return running_cube_sum