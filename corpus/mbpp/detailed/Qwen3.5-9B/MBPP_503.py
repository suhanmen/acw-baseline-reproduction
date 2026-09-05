from typing import List, Union

Number = Union[int, float]

def _validate_input_list(input_list: List[Number]) -> List[Number]:
    """
    Validates that the input is a list containing only numbers (int or float).
    Raises a TypeError if validation fails.
    Returns the validated list.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list, but received {type(input_list).__name__}.")

    if len(input_list) == 0:
        return []

    for index, item in enumerate(input_list):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"All elements must be numbers. "
                f"Found element at index {index} with type {type(item).__name__} "
                f"and value {repr(item)}."
            )

    return input_list

def _add_consecutive_pairs(nums: List[Number]) -> List[Number]:
    """
    Iterates through the validated list of numbers and creates a new list
    where each element is the sum of the current number and the next number.

    Logic:
    1. Initialize an empty result list.
    2. Iterate from index 0 up to (length of nums) - 2.
    3. Calculate sum of nums[i] and nums[i+1].
    4. Append the sum to the result list.

    If the list has 0 or 1 element, the loop range is empty, returning an empty list.
    """
    result: List[Number] = []

    # Determine the stopping index. We stop at len(nums) - 2 because we access i + 1.
    # If len(nums) is 0 or 1, range will be empty (start >= stop).
    limit_index = len(nums) - 1
    current_index = 0

    while current_index < limit_index:
        first_value = nums[current_index]
        second_value = nums[current_index + 1]
        pair_sum = first_value + second_value
        result.append(pair_sum)
        current_index += 1

    return result

def add_consecutive_nums(input_list: List[Number]) -> List[Number]:
    """
    Adds consecutive numbers from the given list.
    The function takes a list of numbers and returns a new list containing
    the sum of each adjacent pair of numbers.

    Example:
    Input: [1, 2, 3, 4]
    Output: [3, 5, 7] (1+2, 2+3, 3+4)

    Edge Cases Handled:
    - Empty list: Returns an empty list.
    - Single element list: Returns an empty list (no pairs exist).
    - Lists with all equal elements: Works correctly.
    - Negative numbers, zero, and floats: Work correctly.

    :param input_list: A list of numbers (int or float).
    :return: A list of summed consecutive pairs.
    :raises TypeError: If input is not a list or contains non-numeric elements.
    """
    # Step 1: Validate the input structure and contents
    validated_list = _validate_input_list(input_list)

    # Step 2: Perform the addition of consecutive pairs on the validated list
    result_list = _add_consecutive_pairs(validated_list)

    return result_list