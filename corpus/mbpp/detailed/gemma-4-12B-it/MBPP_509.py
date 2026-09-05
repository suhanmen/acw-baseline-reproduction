from typing import List, Union

def average_Odd(n: int) -> float:
    """
    Calculates the average of all odd numbers from 1 up to and including 
    the given odd number 'n'.

    The function follows these steps:
    1. Validates that the input is an integer.
    2. Validates that the input is an odd number.
    3. Validates that the input is positive (as the sequence starts from 1).
    4. Identifies all odd integers in the range [1, n].
    5. Calculates the sum and count of these integers.
    6. Computes and returns the arithmetic mean.
    """

    # --- Input Validation ---

    # Check if the input is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    # Check if the input is an odd number
    # An odd number leaves a remainder of 1 (or -1) when divided by 2
    if n % 2 == 0:
        raise ValueError(f"Input must be an odd number. Received: {n}")

    # Check for positive bounds
    # Based on the examples (9, 5, 11), the sequence implies positive odd integers.
    if n < 1:
        raise ValueError(f"Input must be a positive odd number. Received: {n}")

    # --- Logic ---

    # Identify the odd numbers in the range [1, n]
    # Since we know 'n' is odd and the sequence starts at 1,
    # we can iterate through all integers and collect the odd ones.
    odd_numbers_list: List[int] = []

    for current_number in range(1, n + 1):
        if current_number % 2 != 0:
            odd_numbers_list.append(current_number)

    # Handle the case of an empty list, though with n >= 1 and n odd, 
    # this list will always contain at least [1].
    if not odd_numbers_list:
        return 0.0

    # Calculate the sum of the identified odd numbers
    total_sum: int = sum(odd_numbers_list)

    # Calculate the count of the identified odd numbers
    count: int = len(odd_numbers_list)

    # Calculate the average
    # We use float conversion to ensure precise division
    average: float = float(total_sum) / float(count)

    # The problem asserts imply the result can be returned as an integer/float
    # where 5.0 == 5. To match the exact assertion types, we can return it.
    return average

# The following block would be used for internal verification against the provided assertions
if __name__ == "__main__":
    # Assertions provided in the problem description
    assert average_Odd(9) == 5
    assert average_Odd(5) == 3
    assert average_Odd(11) == 6