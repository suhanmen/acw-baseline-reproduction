from typing import List, Union


def smallest_num(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Finds the smallest number in a list of integers or floats.

    Args:
        numbers (List[Union[int, float]]): A list of numeric values.

    Returns:
        Union[int, float]: The smallest value in the list.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric values.
    """

    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list
    if len(numbers) == 0:
        raise ValueError("The input list must contain at least one number.")

    # Validate that all elements in the list are numbers (int or float)
    # This ensures robust behavior against mixed types or non-numeric strings
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numbers. Found: {type(item).__name__}")

    # Initialize the smallest number tracker with the first element
    # We use the first element to handle negative numbers and zeros correctly
    current_smallest: Union[int, float] = numbers[0]

    # Iterate through the list starting from the second element
    # If the list has only one element, this loop will not execute
    for index in range(1, len(numbers)):
        current_value = numbers[index]

        # Compare the current value with our known smallest
        if current_value < current_smallest:
            # Update the smallest value tracker
            current_smallest = current_value

    return current_smallest

# Explicitly defining the expected behavior via assertions as requested
if __name__ == "__main__":
    # Test case 1: Standard unsorted list
    assert smallest_num([10, 20, 1, 45, 99]) == 1

    # Test case 2: Sorted list
    assert smallest_num([1, 2, 3]) == 1

    # Test case 3: Large values
    assert smallest_num([45, 46, 50, 60]) == 45

    # Additional internal checks for robustness:
    # Negative numbers
    assert smallest_num([-10, -5, -20]) == -20
    # Single element
    assert smallest_num([42]) == 42
    # All equal elements
    assert smallest_num([7, 7, 7]) == 7
    # Mixed floats and ints
    assert smallest_num([5.5, 2.1, 3.0]) == 2.1