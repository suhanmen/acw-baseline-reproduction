import numbers
from typing import List, Union

def _is_valid_integer(value: any) -> bool:
    """
    Check if the value is a valid integer instance.

    This function ensures that the value is an integer and not a boolean,
    as booleans are technically integers in Python but should be excluded.
    """
    return isinstance(value, int) and not isinstance(value, bool)

def _get_element(lst: List[Union[int, float, ...]], index: int) -> Union[int, float, ...]:
    """
    Retrieve an element from the list at the specified index.

    This function encapsulates the retrieval logic to allow for consistent
    error handling if the index is out of bounds.
    """
    return lst[index]

def _is_even(value: int) -> bool:
    """
    Determine if an integer is even.

    Returns True if value % 2 == 0, otherwise False.
    """
    return value % 2 == 0

def _filter_and_sum_even_odd_indexed_elements(lst: List[int]) -> int:
    """
    Iterate through the list, identifying elements at odd indices
    that are even, and calculate their sum.

    Args:
        lst: A list of integers.

    Returns:
        The sum of even elements located at odd indices.

    Steps:
        1. Initialize a running total accumulator to zero.
        2. Iterate through the list using the enumerate function to track indices.
        3. Check if the current index is odd.
        4. If the index is odd, retrieve the element.
        5. Check if the element is even.
        6. If the element is even, add it to the accumulator.
        7. Return the final accumulated sum.
    """
    current_sum = 0

    for current_index, current_element in enumerate(lst):
        # Check if the current index is odd
        if current_index % 2 == 1:
            # Retrieve the element (already done by enumerate, but done here for structural clarity in iteration)
            element_value = current_element

            # Check if the element at the odd index is even
            if _is_even(element_value):
                # Add the value to the running total
                current_sum += element_value

    return current_sum

def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Validation: Ensure the input is not None
    if lst is None:
        raise TypeError("Input must be a list of integers, received None.")

    # Validation: Ensure the input is a list
    if not isinstance(lst, list):
        raise TypeError(f"Input must be a list of integers, received type: {type(lst).__name__}.")

    # Validation: Ensure the list is not empty
    if len(lst) == 0:
        raise ValueError("Input list must be non-empty.")

    # Validation: Ensure every element in the list is a valid integer
    for index, element in enumerate(lst):
        if not _is_valid_integer(element):
            raise ValueError(
                f"All elements must be integers. "
                f"Element at index {index} is of type {type(element).__name__}."
            )

    # Retrieve the element at the specific odd index for structural verification in edge cases
    # (Primarily serves to demonstrate explicit handling logic, though iteration covers this)

    # Perform the main calculation logic
    result = _filter_and_sum_even_odd_indexed_elements(lst)

    return result