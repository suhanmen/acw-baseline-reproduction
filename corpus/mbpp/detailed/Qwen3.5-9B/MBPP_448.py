from typing import Union

Number = Union[int, float]


def is_non_negative_integer(value: Number) -> bool:
    """
    Check if the provided value is a non-negative integer.

    Returns True if value is an int (or a float that is effectively an integer)
    and greater than or equal to 0. Returns False otherwise.
    """
    if isinstance(value, bool):
        return False
    if not isinstance(value, (int, float)):
        return False

    if isinstance(value, float) and not value.is_integer():
        return False

    if value < 0:
        return False

    return True


def validate_input(n: Number) -> None:
    """
    Validate the input argument for the sum of Perrin numbers calculation.

    Raises a ValueError if the input is not a valid non-negative integer.
    """
    if not is_non_negative_integer(n):
        raise ValueError(
            f"Input must be a non-negative integer. "
            f"Received: {n} (type: {type(n).__name__})"
        )


def is_integer(value: Number) -> bool:
    """
    Determine if a numeric value represents an integer.

    This handles both int and float types where the float has no fractional part.
    """
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return value.is_integer()
    return False


def calculate_perrin_numbers_up_to_limit(limit: int) -> list[int]:
    """
    Generate a list of Perrin numbers from index 0 up to and including 'limit'.

    The Perrin sequence is defined by:
      P(0) = 3
      P(1) = 0
      P(2) = 2
      For n >= 3: P(n) = P(n-2) + P(n-3)

    The function returns a list where the element at index i corresponds to P(i).
    If limit is 0, only [3] is returned.
    If limit is 1, [3, 0] is returned.
    If limit is 2, [3, 0, 2] is returned.
    And so on.
    """
    if limit < 0:
        return []

    if limit == 0:
        return [3]

    if limit == 1:
        return [3, 0]

    if limit == 2:
        return [3, 0, 2]

    # Initialize the first three known values
    perrin_0 = 3
    perrin_1 = 0
    perrin_2 = 2

    # Prepare a list to store the results
    result_list = [perrin_0, perrin_1, perrin_2]

    # Calculate subsequent values up to the limit
    # We start calculating P(3) up to P(limit)
    current_index = 3
    while current_index <= limit:
        # P(n) = P(n-2) + P(n-3)
        # In terms of our stored values:
        # P(current_index) = P(current_index - 2) + P(current_index - 3)

        value_minus_2 = result_list[current_index - 2]
        value_minus_3 = result_list[current_index - 3]
        new_value = value_minus_2 + value_minus_3

        result_list.append(new_value)

        # Increment the index to move to the next number to calculate
        current_index += 1

    return result_list


def calculate_sum_of_perrin_numbers(n: Number) -> int:
    """
    Calculate the sum of the first (n+1) Perrin numbers (from P(0) to P(n)).

    Parameters:
    n (Number): The upper limit of the index for Perrin numbers.
                Must be a non-negative integer.

    Returns:
    int: The sum of Perrin numbers P(0) + P(1) + ... + P(n).

    Raises:
    ValueError: If n is not a non-negative integer.
    """
    # Step 1: Validate the input argument strictly
    validate_input(n)

    # Step 2: Cast the validated input to an integer type for indexing
    # Since we validated it is a non-negative integer, this is safe.
    limit_index = int(n)

    # Step 3: Generate the sequence of Perrin numbers up to the given index
    sequence = calculate_perrin_numbers_up_to_limit(limit_index)

    # Step 4: Initialize the accumulator for the sum
    total_sum = 0

    # Step 5: Iterate through the generated sequence and accumulate the sum
    for current_number in sequence:
        total_sum = total_sum + current_number

    # Step 6: Return the calculated sum
    return total_sum


# The following section contains the required function signature exactly as requested,
# aliased for the specific problem constraints, though the logic is encapsulated
# in the more descriptive function above.

def cal_sum(n: int) -> int:
    """
    Calculate the sum of Perrin numbers up to index n.

    Signature kept exactly as requested for compatibility with specific test harnesses.
    """
    return calculate_sum_of_perrin_numbers(n)