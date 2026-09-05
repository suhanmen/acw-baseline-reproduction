from collections import Counter
from typing import List, Union

def _validate_input_type(input_list: List, target_value: Union[int, float]) -> None:
    """
    Validates that the input list is indeed a list and the target value is a number.
    Raises a TypeError if validation fails.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list as the first argument, got '{type(input_list).__name__}'")

    if not isinstance(target_value, (int, float)):
        raise TypeError(f"Expected a number (int or float) as the second argument, got '{type(target_value).__name__}'")

def _count_element_occurrences(input_list: List, target_value: Union[int, float]) -> int:
    """
    Counts how many times the target_value appears in the input_list.
    Returns 0 if the list is empty or the value does not exist.
    """
    count = 0
    for element in input_list:
        if element == target_value:
            count += 1
    return count

def _find_sum_of_repeated_elements(input_list: List, target_value: Union[int, float]) -> Union[int, float]:
    """
    Helper function that calculates the sum of all occurrences of a specific target value
    in the input list. This is the core logic separated for clarity.

    If the target_value appears 'n' times, this function returns (target_value * n).
    """
    occurrence_count = _count_element_occurrences(input_list, target_value)

    if occurrence_count <= 0:
        # If the element is not present or not repeated at all (count is 0), sum is 0.
        # Note: The problem implies we sum the element value for every occurrence found.
        return 0

    return target_value * occurrence_count

def find_Sum(input_array: List, target_value: Union[int, float]) -> Union[int, float]:
    """
    Finds the sum of repeated elements in a given array based on a specified target value.

    Logic:
    1. Validate that input_array is a list and target_value is a number.
    2. Count the number of times target_value appears in input_array.
    3. If the count is greater than zero, multiply the target_value by the count.
    4. Return the calculated sum.

    Edge cases handled:
    - Empty input list: returns 0.
    - Single element list: checks if it matches target_value.
    - All-equal elements: counts all and multiplies.
    - Zero or negative numbers: handled correctly by equality check.
    - Invalid types: raises TypeError.

    Args:
        input_array (List): The list of numbers to search within.
        target_value (Union[int, float]): The specific number to look for and sum.

    Returns:
        Union[int, float]: The sum of all occurrences of target_value in the list.

    Raises:
        TypeError: If input arguments are of incorrect types.
    """
    # Step 1: Explicit Input Validation
    _validate_input_type(input_array, target_value)

    # Step 2: Explicit Logic Execution
    # We need to find the sum of the target_value for every time it appears in the list.
    # This effectively means: count occurrences * target_value.

    # Calculate occurrences explicitly
    count = _count_element_occurrences(input_array, target_value)

    # Calculate final sum
    total_sum = count * target_value

    return total_sum