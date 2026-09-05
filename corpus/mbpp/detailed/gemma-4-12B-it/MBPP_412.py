from typing import List, Any


def remove_odd_numbers(input_list: List[int]) -> List[int]:
    """
    Removes all odd numbers from a given list of integers.

    Args:
        input_list (List[int]): A list of integers to filter.

    Returns:
        List[int]: A new list containing only the even integers from the input.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Step 1: Validate input type
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but received {type(input_list).__name__}")

    # Step 2: Handle empty list edge case
    if len(input_list) == 0:
        return []

    # Step 3: Initialize result container
    # We use a new list to avoid modifying the input list in-place (defensive programming)
    even_numbers_result: List[int] = []

    # Step 4: Iterate and filter
    for item in input_list:
        # Validate that the element is an integer
        # Note: bool is a subclass of int, so we explicitly check type
        if not isinstance(item, int) or isinstance(item, bool):
            raise ValueError(f"All elements in the list must be integers. Found: {item} (type: {type(item).__name__})")

        # Determine if the number is even
        # An even number is divisible by 2 with a remainder of 0
        remainder = item % 2
        is_even = (remainder == 0)

        if is_even:
            even_numbers_result.append(item)

    return even_numbers_result


def remove_odd(input_list: List[int]) -> List[int]:
    """
    Wrapper function to match the required signature.
    """
    # Defensive check for None input
    if input_list is None:
        return []

    return remove_odd_numbers(input_list)


if __name__ == "__main__":
    # Test cases provided in the problem description
    assert remove_odd([1, 2, 3]) == [2]
    assert remove_odd([2, 4, 6]) == [2, 4, 6]
    assert remove_odd([10, 20, 3]) == [10, 20]

    # Additional edge cases
    assert remove_odd([]) == []                # Empty list
    assert remove_odd([1, 3, 5]) == []        # All odd
    assert remove_odd([2, 4, 8]) == [2, 4, 8] # All even
    assert remove_odd([0]) == [0]             # Zero (even)
    assert remove_odd([-2, -1, 0, 1, 2]) == [-2, 0, 2] # Negative numbers
    assert remove_odd([11]) == []             # Single odd
    assert remove_odd([42]) == [42]           # Single even