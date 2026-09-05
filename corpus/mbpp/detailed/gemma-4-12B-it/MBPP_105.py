from typing import List, Any

def count(input_list: List[bool]) -> int:
    """
    Counts the number of True boolean values in a given list.

    Args:
        input_list (List[bool]): A list of boolean values.

    Returns:
        int: The count of True values.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that are not booleans 
                    (or types that cannot be evaluated as booleans in a strict context).
    """
    # Validate that the input is actually a list
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input type 'list', but received '{type(input_list).__name__}'.")

    # Handle edge case: Empty list
    if len(input_list) == 0:
        return 0

    true_count = 0

    # Iterate through each element to verify type and count Truthy values
    for index, element in enumerate(input_list):
        # Strict check: Ensure the element is specifically a boolean.
        # In Python, bool is a subclass of int, so 'isinstance(True, int)' is True.
        # We use 'type(element) is bool' to ensure we don't count integers like 1.
        if type(element) is not bool:
            raise ValueError(
                f"Element at index {index} is of type '{type(element).__name__}'. "
                "Only boolean values (True/False) are allowed."
            )

        # Check if the boolean value is True
        if element is True:
            true_count += 1
        else:
            # Explicitly handle False case (redundant for logic, but good for visibility)
            pass

    return true_count

# Test assertions provided in the problem description
if __name__ == "__main__":
    assert count([True, False, True]) == 2
    assert count([False, False]) == 0
    assert count([True, True, True]) == 3