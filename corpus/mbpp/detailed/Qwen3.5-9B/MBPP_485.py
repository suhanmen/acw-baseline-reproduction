from typing import List, Optional, Union

Number = Union[int, float]

def _is_palindrome(value: Number) -> bool:
    """
    Check if a number is a palindrome.

    Steps:
    1. Convert the number to a string representation.
    2. Check if the string is equal to its reverse.

    This function handles:
    - Positive integers
    - Negative integers (always False because of the minus sign)
    - Floating point numbers (compares string representation directly)
    - Zero (True)
    """
    # Convert the numeric value to a string to check for palindromic property
    string_representation = str(value)

    # Reverse the string representation
    reversed_string = string_representation[::-1]

    # Compare the original string with the reversed string
    return string_representation == reversed_string

def _validate_input(number_list: List[Number], expected_count: int) -> None:
    """
    Validate the input parameters to ensure they meet the problem requirements.

    Checks performed:
    1. Ensure 'number_list' is actually a list.
    2. Ensure the length of the list matches 'expected_count'.
    3. Ensure all elements in the list are numeric types (int or float).
    4. Ensure 'expected_count' is a non-negative integer.

    Raises ValueError if any validation fails.
    """
    # Check if the list is None or not a list
    if not isinstance(number_list, list):
        raise TypeError(f"Expected a list of numbers, but got {type(number_list).__name__}")

    # Check if expected_count is an integer and non-negative
    if not isinstance(expected_count, int) or isinstance(expected_count, bool):
        raise TypeError(f"Expected 'expected_count' to be a non-negative integer, but got {type(expected_count).__name__}")

    if expected_count < 0:
        raise ValueError(f"'expected_count' must be non-negative, but got {expected_count}")

    # Check if the actual length of the list matches the expected count
    actual_length = len(number_list)
    if actual_length != expected_count:
        raise ValueError(
            f"List length mismatch: expected {expected_count} elements, but got {actual_length}"
        )

    # Validate each element in the list
    for index, item in enumerate(number_list):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a valid number: {type(item).__name__} ({item})"
            )

def _find_largest_palindrome_in_list(number_list: List[Number]) -> Optional[Number]:
    """
    Find the largest palindromic number in the given list.

    Steps:
    1. Iterate through each number in the list.
    2. Check if the number is a palindrome using _is_palindrome.
    3. Keep track of the largest palindrome found so far.
    4. Return the largest palindrome or None if no palindrome is found.
    """
    largest_palindrome: Optional[Number] = None

    for number in number_list:
        # Check if the current number is a palindrome
        if _is_palindrome(number):
            # If we haven't found a palindrome yet, this is the first one
            if largest_palindrome is None:
                largest_palindrome = number
            else:
                # If the current palindrome is larger than the existing largest, update it
                if number > largest_palindrome:
                    largest_palindrome = number

    return largest_palindrome

def largest_palindrome(number_list: List[Number], expected_count: int) -> Optional[Number]:
    """
    Find the largest palindromic number in the given array.

    Parameters:
    number_list (List[Number]): A list of numbers to search for palindromes.
    expected_count (int): The expected number of elements in the list (for validation).

    Returns:
    Optional[Number]: The largest palindromic number found in the list.
                      Returns None if no palindromes are found or if the input is invalid.

    Raises:
    TypeError: If inputs are of incorrect types.
    ValueError: If the list length does not match expected_count or count is negative.

    Steps executed by this function:
    1. Validate the input arguments.
    2. Iterate through the validated list.
    3. Identify palindromic numbers.
    4. Determine the maximum among the identified palindromes.
    5. Return the result.
    """
    # Step 1: Validate inputs explicitly
    _validate_input(number_list, expected_count)

    # Step 2-5: Find and return the largest palindrome
    return _find_largest_palindrome_in_list(number_list)