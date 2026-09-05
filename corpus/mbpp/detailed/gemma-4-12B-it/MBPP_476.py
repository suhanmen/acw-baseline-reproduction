from typing import List, Union

def big_sum(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculates the sum of the largest and smallest values in a list of numbers.

    Args:
        numbers: A list of integers or floats.

    Returns:
        The sum of the maximum and minimum values in the list.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric types.
    """
    # Validate that the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list
    if len(numbers) == 0:
        raise ValueError("The input list cannot be empty.")

    # Validate that all elements in the list are numbers (int or float)
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numeric. Found: {type(item).__name__}")

    # Handle the case of a single element
    # The largest and smallest value are both the same element.
    if len(numbers) == 1:
        single_value = numbers[0]
        return single_value + single_value

    # Find the smallest value
    # We initialize with the first element to handle all-equal or negative cases correctly.
    smallest_value = numbers[0]
    for current_number in numbers:
        if current_number < smallest_value:
            smallest_value = current_number

    # Find the largest value
    largest_value = numbers[0]
    for current_number in numbers:
        if current_number > largest_value:
            largest_value = current_number

    # Calculate the result
    total_sum = smallest_value + largest_value

    return total_sum

if __name__ == "__main__":
    # The following assertions are provided in the problem description
    assert big_sum([1, 2, 3]) == 4
    assert big_sum([-1, 2, 3, 4]) == 3
    assert big_sum([2, 3, 6]) == 8