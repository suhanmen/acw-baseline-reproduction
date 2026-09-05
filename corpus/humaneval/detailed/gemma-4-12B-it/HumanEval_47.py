from typing import List, Union


def median(l: list) -> Union[int, float]:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Validate input type
    if not isinstance(l, list):
        raise TypeError(f"Expected input type 'list', but received '{type(l).__name__}'")

    # Handle empty list edge case
    if len(l) == 0:
        raise ValueError("Cannot calculate the median of an empty list.")

    # Validate that all elements are numbers
    for item in l:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numeric. Found: {type(item).__name__}")

    # Create a sorted copy of the list to avoid mutating the original input
    sorted_list = sorted(l)

    list_length = len(sorted_list)

    # Determine if the length is odd or even
    is_even = (list_length % 2 == 0)

    if is_even:
        # For even lengths, the median is the average of the two middle elements.
        # Indices are zero-based.
        upper_middle_index = list_length // 2
        lower_middle_index = upper_middle_index - 1

        value_one = sorted_list[lower_middle_index]
        value_two = sorted_list[upper_middle_index]

        # Use float division for even length averages
        median_value = (value_one + value_two) / 2.0
        return median_value
    else:
        # For odd lengths, the median is the middle element.
        middle_index = list_length // 2
        median_value = sorted_list[middle_index]
        return median_value