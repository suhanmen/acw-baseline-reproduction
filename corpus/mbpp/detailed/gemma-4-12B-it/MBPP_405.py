from typing import Any, Tuple, Union

def check_tuplex(input_tuple: Tuple[Any, ...], target_element: Any) -> bool:
    """
    Checks whether a specific element exists within a given tuple.

    Args:
        input_tuple (Tuple[Any, ...]): A tuple containing elements of any type.
        target_element (Any): The element to search for in the tuple.

    Returns:
        bool: True if the target_element is found in the input_tuple, False otherwise.

    Raises:
        TypeError: If the input_tuple is not a tuple or target_element is not provided.
    """
    # Validate that input_tuple is actually a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(
            f"Expected input_tuple to be of type 'tuple', "
            f"but received '{type(input_tuple).__name__}'."
        )

    # Handle the edge case of an empty tuple explicitly
    # If the tuple is empty, no element can exist within it.
    if len(input_tuple) == 0:
        return False

    # Initialize a flag to track if the element is found
    is_element_present: bool = False

    # Iterate through each item in the tuple using an explicit loop
    # This allows us to handle each element individually and clearly.
    for current_item in input_tuple:
        # Use equality check to compare the current item with the target
        # We use '==' to support equality for strings, integers, etc.
        if current_item == target_element:
            is_element_present = True
            # Once the element is found, we can break out of the loop early
            break

    return is_element_present

if __name__ == "__main__":
    # Internal testing to ensure logic remains robust
    # Test Case 1: Element exists (string)
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True

    # Test Case 2: Element does not exist (string representation of an int)
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), '5') == False

    # Test Case 3: Element exists (integer)
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3) == True

    # Edge Case: Empty Tuple
    assert check_tuplex((), "anything") == False

    # Edge Case: Single element match
    assert check_tuplex(("single",), "single") == True

    # Edge Case: Single element mismatch
    assert check_tuplex(("single",), "different") == False

    # Edge Case: All elements are equal
    assert check_tuplex((1, 1, 1), 1) == True

    # Edge Case: Negative numbers and zero
    assert check_tuplex((0, -1, -5), -5) == True