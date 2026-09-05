from typing import List, Union

Number = Union[int, float]

def _validate_list(lst: List[Number]) -> None:
    """
    Validates that the input is a non-empty list of integers.

    Args:
        lst: The list to validate.

    Raises:
        TypeError: If lst is not a list or contains non-integer elements.
        ValueError: If lst is empty.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Expected a list, but got {type(lst).__name__}.")

    if len(lst) == 0:
        raise ValueError("Expected a non-empty list, but got an empty list.")

    for index, element in enumerate(lst):
        if not isinstance(element, int):
            raise TypeError(
                f"Element at index {index} ({element!r}) is not an integer. "
                f"Expected int, got {type(element).__name__}."
            )

def _is_odd(number: Number) -> bool:
    """
    Checks if a number is odd.

    An odd number is an integer that is not divisible by two.
    This function handles negative numbers correctly.

    Args:
        number: The number to check.

    Returns:
        True if the number is odd, False otherwise.
    """
    return number % 2 != 0

def _is_even_position(index: int) -> bool:
    """
    Checks if a given position (0-based index) is even.

    Args:
        index: The position to check.

    Returns:
        True if the position is even (0, 2, 4, ...), False otherwise.
    """
    return index % 2 == 0

def _sum_odd_at_even_positions(lst: List[Number]) -> Number:
    """
    Calculates the sum of all odd elements that are located at even positions.

    Args:
        lst: A validated list of integers.

    Returns:
        The calculated sum.
    """
    total_sum = 0
    element_count = 0

    for index in range(0, len(lst), 2):
        element = lst[index]
        position_type = "odd" if _is_odd(element) else "even"
        if _is_odd(element):
            total_sum += element
            element_count += 1

    return total_sum

def solution(lst: List[Number]) -> Number:
    """
    Given a non-empty list of integers, return the sum of all of the odd elements
    that are in even positions (indices 0, 2, 4, etc.).

    Args:
        lst: A non-empty list of integers.

    Returns:
        The sum of odd integers found at even indices.

    Examples:
        solution([5, 8, 7, 1]) ==> 12
        (Index 0: 5 is odd -> add 5. Index 2: 7 is odd -> add 7. Total: 12)

        solution([3, 3, 3, 3, 3]) ==> 9
        (Index 0: 3 is odd -> add 3. Index 2: 3 is odd -> add 3. Index 4: 3 is odd -> add 3. Total: 9)

        solution([30, 13, 24, 321]) ==> 0
        (Index 0: 30 is even (skip). Index 2: 24 is even (skip). Total: 0)
    """
    _validate_list(lst)
    return _sum_odd_at_even_positions(lst)