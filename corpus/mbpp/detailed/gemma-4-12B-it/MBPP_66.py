from typing import List, Union

def pos_count(numbers: List[Union[int, float]]) -> int:
    """
    Counts the number of positive numbers in a given list.

    A positive number is defined as any number strictly greater than zero.

    Args:
        numbers (List[Union[int, float]]): A list of integers or floats.

    Returns:
        int: The count of positive numbers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric types.
        ValueError: If the input list is None.
    """
    # Validate that the input is not None
    if numbers is None:
        raise ValueError("The input list cannot be None.")

    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}.")

    # Handle the edge case of an empty list explicitly
    if len(numbers) == 0:
        return 0

    positive_count: int = 0

    # Iterate through every element in the provided list
    for index, item in enumerate(numbers):
        # Validate that the element is a numeric type (int or float)
        # We exclude bool because in Python, True is treated as 1 and False as 0
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(
                f"Element at index {index} is not a valid number. "
                f"Found: {type(item).__name__} with value {item}."
            )

        # Check if the number is strictly greater than zero
        is_positive: bool = item > 0

        if is_positive:
            # Increment the counter if the condition is met
            positive_count += 1

    return positive_count

if __name__ == "__main__":
    # Verification of provided assertions
    assert pos_count([1, -2, 3, -4]) == 2
    assert pos_count([3, 4, 5, -1]) == 3
    assert pos_count([1, 2, 3, 4]) == 4