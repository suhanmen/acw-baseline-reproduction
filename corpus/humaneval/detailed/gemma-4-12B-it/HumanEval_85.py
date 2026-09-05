from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Input Validation: Check if the input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of integers.")

    # Input Validation: Check if the list is empty
    if len(lst) == 0:
        # Although the prompt says "non-empty", production code should handle it.
        # Returning 0 as the sum of an empty selection.
        return 0

    # Input Validation: Ensure all elements are integers
    for item in lst:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item)}")

    total_sum = 0

    # We iterate through the list by index to identify positions.
    # Indices in Python are 0-based. Odd indices are 1, 3, 5, etc.
    for index in range(len(lst)):
        # Check if the current index is odd
        is_odd_index = (index % 2 != 0)

        if is_odd_index:
            # Retrieve the value at the odd index
            current_value = lst[index]

            # Check if the value itself is even
            is_even_value = (current_value % 2 == 0)

            if is_even_value:
                # Add the value to the running total
                total_sum = total_sum + current_value

    return total_sum