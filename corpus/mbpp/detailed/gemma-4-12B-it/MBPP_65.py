from typing import List, Any, Union


def recursive_list_sum(data: List[Any]) -> int:
    """
    Calculates the sum of all integers within a nested list structure.

    The function handles:
    - Integers at the top level or nested levels.
    - Lists containing integers or other nested lists.
    - Deeply nested structures.

    Args:
        data (List[Any]): A list containing integers or other lists of integers.

    Returns:
        int: The total sum of all integers found in the structure.

    Raises:
        TypeError: If the input is not a list or if the list contains
                   non-integer/non-list elements.
    """
    # Validation: Ensure the input is actually a list
    if not isinstance(data, list):
        raise TypeError(f"Expected input to be a list, but got {type(data).__name__}")

    total_sum: int = 0

    # Iterate through each element in the provided list
    for item in data:
        # Handle the case where the item is an integer
        if isinstance(item, int):
            total_sum += item

        # Handle the case where the item is another list (recursive case)
        elif isinstance(item, list):
            # Recursively calculate the sum of the sub-list
            sub_list_sum = recursive_list_sum(item)
            total_sum += sub_list_sum

        # Handle unexpected types (e.g., strings, floats, None)
        else:
            raise TypeError(
                f"List contains an invalid type: {type(item).__name__}. "
                "Only integers and lists are supported."
            )

    return total_sum


# Test cases provided in the prompt
if __name__ == "__main__":
    # Test case 1
    # 1 + 2 + (3 + 4) + (5 + 6) = 3 + 7 + 11 = 21
    assert recursive_list_sum([1, 2, [3, 4], [5, 6]]) == 21

    # Test case 2
    # 7 + 10 + (15 + 14) + (19 + 41) = 17 + 29 + 60 = 106
    assert recursive_list_sum([7, 10, [15, 14], [19, 41]]) == 106

    # Test case 3
    # 10 + 20 + (30 + 40) + (50 + 60) = 30 + 70 + 110 = 210
    assert recursive_list_sum([10, 20, [30, 40], [50, 60]]) == 210