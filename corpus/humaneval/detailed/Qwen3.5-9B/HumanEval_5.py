from typing import List


def _validate_input(numbers: List[int], delimiter: int) -> None:
    """
    Validates the input types for the intersperse function.

    Raises:
        TypeError: If 'numbers' is not a list or if it contains non-integer elements.
        TypeError: If 'delimiter' is not an integer.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected 'numbers' to be a list, but got {type(numbers).__name__}")

    for index, value in enumerate(numbers):
        if not isinstance(value, int):
            raise TypeError(
                f"Expected all elements in 'numbers' to be integers, "
                f"but found {type(value).__name__} at index {index}"
            )

    if not isinstance(delimiter, int):
        raise TypeError(f"Expected 'delimiter' to be an integer, but got {type(delimiter).__name__}")


def _build_result_with_intersperser(
    numbers: List[int], 
    delimiter: int, 
    is_empty: bool
) -> List[int]:
    """
    Helper function to construct the final list with the delimiter inserted.

    Logic:
    1. If the input list is empty, return an empty list immediately.
    2. If the input list has exactly one element, return that element (no delimiter needed).
    3. If the input list has multiple elements, iterate and insert the delimiter.

    Args:
        numbers: The validated list of integers.
        delimiter: The integer to insert between elements.
        is_empty: A flag indicating if the numbers list was empty (for early return).

    Returns:
        A new list with the delimiter interspersed.
    """
    # Handle the empty case explicitly
    if is_empty:
        return []

    # Handle the single element case explicitly
    if len(numbers) == 1:
        return numbers.copy()

    # Handle the case with multiple elements
    result: List[int] = []

    # Add the first element
    result.append(numbers[0])

    # Iterate through the rest of the list starting from the second element
    for i in range(1, len(numbers)):
        # Append the delimiter before the current element
        result.append(delimiter)
        # Append the current element
        result.append(numbers[i])

    return result


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    This function performs strict type validation on inputs to ensure correctness.
    It handles edge cases such as empty lists, single-element lists, and lists with 
    duplicate values explicitly.

    Args:
        numbers: A list of integers.
        delimiter: An integer to be placed between consecutive elements.

    Returns:
        A new list where 'delimiter' is inserted between every pair of adjacent 
        integers from the input list.

    Raises:
        TypeError: If input types are invalid.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
        >>> intersperse([5], 9)
        [5]
        >>> intersperse([7, 7, 7], 0)
        [7, 0, 7, 0, 7]
    """
    # Step 1: Validate all inputs explicitly
    _validate_input(numbers, delimiter)

    # Step 2: Check if the list is empty to set a flag for the builder
    is_empty: bool = len(numbers) == 0

    # Step 3: Call the helper function to build the result
    final_result: List[int] = _build_result_with_intersperser(numbers, delimiter, is_empty)

    # Step 4: Return the computed result
    return final_result