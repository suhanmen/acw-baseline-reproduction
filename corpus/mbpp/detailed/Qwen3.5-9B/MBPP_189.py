import typing

def _is_valid_input_sequence(input_list: typing.Any, expected_type: typing.Type[typing.List]) -> bool:
    """
    Validates that the input is exactly a list.

    This function checks two things:
    1. The type of the input is exactly 'list'.
    2. The function signature requires the input to be a list, 
       so we reject tuples, sets, or other sequence types.
    """
    return isinstance(input_list, list)


def _is_integer(value: typing.Any) -> bool:
    """
    Checks if a value is an integer (or a float with no fractional part, 
    effectively treating it as an integer for this context, 
    but strictly we will rely on `isinstance(x, int)` to be safe 
    and exclude booleans which are a subclass of int in Python).
    """
    # Booleans are a subclass of int in Python, so we must explicitly exclude them.
    if isinstance(value, bool):
        return False
    return isinstance(value, int)


def _filter_positive_integers(input_list: list) -> list:
    """
    Filters the input list to return only positive integers.

    Returns a new list containing only the elements that are:
    - Integers
    - Greater than 0
    """
    filtered_result: list = []
    for element in input_list:
        is_integer_val: bool = _is_integer(element)
        if is_integer_val:
            is_positive: bool = element > 0
            if is_positive:
                filtered_result.append(element)
    return filtered_result


def _generate_set_of_input_numbers(filtered_numbers: list) -> typing.Set:
    """
    Converts the filtered list of positive integers into a set.

    This allows for O(1) average-time complexity lookups later on.
    """
    return set(filtered_numbers)


def _determine_necessary_range(n_elements: int) -> int:
    """
    Calculates the maximum necessary number to check for missingness.

    If we have N positive integers, the smallest possible missing positive
    integer is bounded by N + 1.
    Example:
    - [1, 2, 3] -> N=3, max needed to check is 4.
    - [1] -> N=1, max needed to check is 2.
    - [] -> N=0, max needed to check is 1.

    We need to check numbers from 1 up to (and including) n_elements + 1.
    """
    return n_elements + 1


def _find_first_missing_in_range(numbers_set: typing.Set, max_check_value: int) -> int:
    """
    Iterates through the range [1, max_check_value] and finds the first integer
    that is not present in the provided set of numbers.
    """
    current_number: int = 1
    while current_number <= max_check_value:
        if current_number not in numbers_set:
            return current_number
        current_number += 1
    # If no missing number is found within the expected range [1, N],
    # the answer must be N + 1.
    return max_check_value


def first_Missing_Positive(input_list: list, expected_n: int) -> int:
    """
    Finds the first missing positive integer in the given list.

    The function expects a list of integers (including negative numbers and zero).
    The 'expected_n' parameter in the signature is preserved but not logically 
    required for the core algorithm's correctness regarding the missing value,
    as the missing value is derived purely from the presence of numbers in the list.
    However, strictly following the requirement to keep the signature, it is included.

    Edge cases handled:
    - Empty list: Returns 1.
    - List with no positive integers: Returns 1.
    - List containing all integers from 1 to N: Returns N + 1.
    - Duplicate positive integers: Handled by converting to a set.

    Args:
        input_list (list): The list of integers to search.
        expected_n (int): An integer parameter kept for signature compliance.

    Returns:
        int: The first missing positive integer.

    Raises:
        TypeError: If input_list is not a list.
        TypeError: If any element in input_list is not an integer (excluding booleans).
    """
    # Step 1: Validate the input structure
    if not _is_valid_input_sequence(input_list, list):
        raise TypeError("The input argument must be a list.")

    # Step 2: Validate element types
    for idx, element in enumerate(input_list):
        if not _is_integer(element):
            raise TypeError(f"Element at index {idx} is not an integer.")

    # Step 3: Filter for relevant data (positive integers)
    positive_integers: list = _filter_positive_integers(input_list)

    # Step 4: Create a set for O(1) lookup
    unique_positive_numbers: typing.Set = _generate_set_of_input_numbers(positive_integers)

    # Step 5: Determine the range we need to check.
    # The first missing positive number cannot exceed the count of positive integers + 1.
    count_of_positives: int = len(positive_integers)
    limit_value: int = _determine_necessary_range(count_of_positives)

    # Step 6: Find the first missing number in the range [1, limit_value]
    result: int = _find_first_missing_in_range(unique_positive_numbers, limit_value)

    return result