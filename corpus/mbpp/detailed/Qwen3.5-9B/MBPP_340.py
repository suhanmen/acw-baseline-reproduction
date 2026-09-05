from typing import List, Union

def is_positive_number(value: Union[int, float]) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Args:
        value: A numeric value (int or float).

    Returns:
        True if the number is greater than zero, False otherwise.
    """
    return isinstance(value, (int, float)) and value > 0

def validate_input_list(numbers: List) -> List:
    """
    Validate the input list and extract positive numbers.

    This function performs several checks:
    1. Ensures the input is a list.
    2. Ensures the input is not empty.
    3. Ensures all elements are numeric (int or float).
    4. Filters out non-positive numbers (zero and negatives).

    Args:
        numbers: The list to validate and filter.

    Returns:
        A list containing only the positive numbers from the input.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, but received {type(numbers).__name__}")

    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    # Validate each element
    positive_numbers: List[Union[int, float]] = []

    for index, element in enumerate(numbers):
        # Check if element is numeric
        if not isinstance(element, (int, float)):
            raise TypeError(f"Element at index {index} ({type(element).__name__}: {element}) is not a valid number")

        # Check if element is positive
        if not is_positive_number(element):
            # We allow filtering out non-positive numbers as per the problem requirement
            # to find the three lowest *positive* numbers.
            continue

        positive_numbers.append(element)

    if len(positive_numbers) == 0:
        raise ValueError("No positive numbers found in the input list")

    return positive_numbers

def sort_positive_numbers(positive_numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Sort the list of positive numbers in ascending order.

    Args:
        positive_numbers: A list of positive numbers.

    Returns:
        A new list containing the same numbers sorted in ascending order.
    """
    # Create a copy to avoid mutating the original list, then sort it
    sorted_numbers = sorted(positive_numbers)
    return sorted_numbers

def get_three_smallest_sum(
    sorted_numbers: List[Union[int, float]], 
    count: int = 3
) -> Union[int, float]:
    """
    Calculate the sum of the first 'count' numbers from a sorted list.

    Args:
        sorted_numbers: A list of numbers sorted in ascending order.
        count: The number of elements to sum from the start of the list.

    Returns:
        The sum of the specified number of smallest elements.

    Raises:
        ValueError: If there are not enough elements in the list to fulfill the request.
    """
    # Determine how many elements we actually have
    available_count = len(sorted_numbers)

    # Check if we have enough elements
    if available_count < count:
        raise ValueError(
            f"Requesting {count} smallest numbers, but only {available_count} positive numbers are available"
        )

    # Calculate the sum using a loop for explicit step visibility
    total_sum: Union[int, float] = 0

    # Sum the first 'count' elements
    for i in range(count):
        total_sum += sorted_numbers[i]

    return total_sum

def sum_three_smallest_nums(numbers: List) -> Union[int, float]:
    """
    Find the sum of the three lowest positive numbers from a given list.

    This function:
    1. Validates the input list (must be non-empty).
    2. Extracts all positive numbers (greater than zero).
    3. Sorts the positive numbers in ascending order.
    4. Sums the first three numbers from the sorted list.

    Args:
        numbers: A list of numeric values (integers or floats).

    Returns:
        The sum of the three smallest positive numbers.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the list is empty, contains no positive numbers, 
                    or has fewer than three positive numbers.
    """
    # Step 1: Validate input and extract positive numbers
    filtered_numbers = validate_input_list(numbers)

    # Step 2: Sort the positive numbers
    sorted_numbers = sort_positive_numbers(filtered_numbers)

    # Step 3: Calculate the sum of the three smallest
    return get_three_smallest_sum(sorted_numbers, count=3)