from typing import List, Optional, Tuple

def is_valid_number(value: object) -> bool:
    """
    Check if the given value is a valid number (int or float).

    Args:
        value: The value to check

    Returns:
        True if value is a number, False otherwise
    """
    return isinstance(value, (int, float)) and not isinstance(value, bool)

def is_positive_or_zero(x: number) -> bool:
    """
    Check if a number is positive or zero.

    Args:
        x: The number to check

    Returns:
        True if x > 0 or x == 0, False otherwise
    """
    return x > 0 or x == 0

def is_negative(x: number) -> bool:
    """
    Check if a number is negative.

    Args:
        x: The number to check

    Returns:
        True if x < 0, False otherwise
    """
    return x < 0

def separate_by_sign(array: List[number]) -> Tuple[List[number], List[number]]:
    """
    Separate the array into two lists: one with non-negative numbers and one with negative numbers.

    Args:
        array: The input list of numbers

    Returns:
        A tuple containing two lists: (non_negative_list, negative_list)
    """
    non_negative: List[number] = []
    negative: List[number] = []

    for item in array:
        if is_positive_or_zero(item):
            non_negative.append(item)
        else:
            negative.append(item)

    return (non_negative, negative)

def re_arrange(array: List[object], length: int) -> Optional[List[number]]:
    """
    Re-arrange the given array in alternating positive and negative items.
    The pattern starts with a negative number if possible, then alternates:
    negative, positive, negative, positive, ...

    Args:
        array: The input list containing numbers
        length: The expected length of the array (should match len(array))

    Returns:
        The re-arranged list with alternating signs, or None if input is invalid

    Raises:
        TypeError: If input types are invalid
        ValueError: If length mismatch or other structural issues
    """
    # Validate input types
    if not isinstance(array, list):
        raise TypeError("Input array must be a list")

    if not isinstance(length, int):
        raise TypeError("Length must be an integer")

    if len(array) != length:
        raise ValueError(f"Array length ({len(array)}) does not match specified length ({length})")

    # Validate all elements are valid numbers
    for i, item in enumerate(array):
        if not is_valid_number(item):
            raise TypeError(f"Invalid element at index {i}: {item} is not a number")
        if isinstance(item, bool):
            raise TypeError(f"Boolean values are not allowed at index {i}: {item}")

    # Handle empty array case
    if length == 0:
        return []

    # Separate the array into non-negative and negative lists
    non_negative, negative = separate_by_sign(array)

    # Initialize result array
    result: List[number] = []

    # Get iterators for both lists
    non_negative_iter = iter(non_negative)
    negative_iter = iter(negative)

    # Build the result with alternating pattern: negative, positive, negative, positive...
    # We'll use a flag to track which type we need next
    should_be_negative = True

    current_index = 0
    total_elements = length

    while current_index < total_elements:
        if should_be_negative:
            # Try to get a negative number
            try:
                value = next(negative_iter)
                result.append(value)
            except StopIteration:
                # No more negative numbers, add what we can from non-negative
                try:
                    value = next(non_negative_iter)
                    result.append(value)
                except StopIteration:
                    # We're done
                    break
            should_be_negative = False
        else:
            # Try to get a non-negative number
            try:
                value = next(non_negative_iter)
                result.append(value)
            except StopIteration:
                # No more non-negative numbers, add what we can from negative
                try:
                    value = next(negative_iter)
                    result.append(value)
                except StopIteration:
                    # We're done
                    break
            should_be_negative = True

        current_index += 1

    # Verify we have exactly the right number of elements
    if len(result) != length:
        raise ValueError(f"Could not create a valid arrangement with {length} elements")

    return result