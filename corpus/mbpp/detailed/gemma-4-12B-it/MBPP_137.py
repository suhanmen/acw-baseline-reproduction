from typing import List, Union


def zero_count(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the ratio of zero elements to the total number of elements 
    in a list of numbers.

    Args:
        numbers (List[Union[int, float]]): A list of integers or floats.

    Returns:
        float: The ratio of zeros in the list. Returns 0.0 if the list is empty.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
    """
    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected input type 'list', but received '{type(numbers).__name__}'.")

    # Handle the edge case of an empty list immediately
    total_elements = len(numbers)
    if total_elements == 0:
        return 0.0

    zero_count_accumulator = 0

    # Iterate through the list to count zeros
    for index, item in enumerate(numbers):
        # Validate that each element is a numeric type (int or float)
        # Note: bool is a subclass of int in Python, so we explicitly exclude it
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(
                f"Element at index {index} is of type '{type(item).__name__}'. "
                "All elements must be integers or floats."
            )

        # Check if the element is strictly zero
        # Using '== 0' is standard here as we want to catch both 0 and 0.0
        if item == 0:
            zero_count_accumulator += 1

    # Calculate the final ratio
    # Since we handled the empty list case above, total_elements is guaranteed > 0
    ratio = zero_count_accumulator / total_elements

    # We round to handle floating point precision issues if necessary, 
    # though standard division is expected to match the assertions.
    # Based on the assertions (e.g., 0.15), standard float division is used.
    return float(ratio)


if __name__ == "__main__":
    # The assertions provided in the problem description
    assert zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.15
    assert zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]) == 0.00
    assert zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 0.00