from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Defensive programming: Validate input types
    # Ensure 'numbers' is a list of integers
    if not isinstance(numbers, list):
        raise TypeError(f"Expected input 'numbers' to be of type list, got {type(numbers).__name__}")

    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in 'numbers' must be integers. Found: {type(item).__name__}")

    # Ensure 'delimeter' is an integer
    if not isinstance(delimeter, int):
        raise TypeError(f"Expected 'delimeter' to be of type int, got {type(delimeter).__name__}")

    # Handle edge cases: empty list or single-element list
    # These cases do not have any gaps between consecutive elements.
    list_length = len(numbers)
    if list_length <= 1:
        # Return a copy to ensure the original list is not modified 
        # and to maintain functional purity.
        return list(numbers)

    # Initialize the result list
    result_list: List[int] = []

    # Iterate through the input list to build the result
    # We use an explicit loop to clearly define the insertion logic
    for index in range(list_length):
        current_value = numbers[index]

        # Append the current element from the original list
        result_list.append(current_value)

        # Check if this is NOT the last element.
        # If it is not the last element, we need to insert the delimiter 
        # because there is a "consecutive" element following it.
        is_last_element = (index == list_length - 1)

        if not is_last_element:
            result_list.append(delimeter)

    return result_list