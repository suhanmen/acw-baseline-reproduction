from typing import List

def get_sum_of_digits(number: int) -> int:
    """
    Calculates the sum of the digits of an integer.
    For negative numbers, the negative sign is ignored and the 
    digits are summed as positive values.

    Example:
    -12 -> 1 + 2 = 3
    11  -> 1 + 1 = 2
    """
    # Take the absolute value to handle negative numbers
    abs_value = abs(number)

    total_sum = 0
    # Handle the case for 0 explicitly, though the loop handles it naturally
    if abs_value == 0:
        return 0

    current_val = abs_value
    while current_val > 0:
        digit = current_val % 10
        total_sum += digit
        current_val //= 10

    return total_sum

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Validation: Ensure the input is a list
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")

    # Edge case: Empty list
    if len(nums) == 0:
        return []

    # Validation: Ensure all elements in the list are integers
    for item in nums:
        if not isinstance(item, int):
            raise ValueError(f"All elements in the list must be integers. Found: {type(item)}")

    # We need to store:
    # 1. The original value
    # 2. The calculated sum of digits
    # 3. The original index (to maintain stability/ordering)

    # Create a list of tuples to hold our metadata
    # Tuple structure: (original_value, digit_sum, original_index)
    indexed_data = []

    for index, value in enumerate(nums):
        digit_sum = get_sum_of_digits(value)
        indexed_data.append({
            "value": value,
            "digit_sum": digit_sum,
            "original_index": index
        })

    # Sort the list of dictionaries.
    # Python's sort is stable, but we will be explicit about the keys.
    # Primary key: digit_sum (ascending)
    # Secondary key: original_index (ascending)

    # We use a lambda to define the sort priority clearly.
    # Because Python's sort is stable, if we only sorted by digit_sum, 
    # the original order would be preserved automatically. 
    # However, explicit keys are preferred for production-grade clarity.

    indexed_data.sort(key=lambda item: (item["digit_sum"], item["original_index"]))

    # Extract the sorted values into a new list
    sorted_results = []
    for item in indexed_data:
        sorted_results.append(item["value"])

    return sorted_results