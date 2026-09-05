from typing import Any, Tuple


def check_type(input_tuple: Tuple[Any, ...]) -> bool:
    """
    Checks if all elements within a given tuple have the same data type.

    Args:
        input_tuple (Tuple[Any, ...]): A tuple of elements of any type.

    Returns:
        bool: True if all elements share the same type, False otherwise.

    Raises:
        TypeError: If the input provided is not a tuple.
    """
    # Validate input type explicitly
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Expected input of type 'tuple', but received '{type(input_tuple).__name__}'.")

    # Handle the edge case of an empty tuple
    # Technically, an empty set of elements vacuously satisfies the condition 
    # that all elements are of the same type.
    if len(input_tuple) == 0:
        return True

    # Handle the case of a single element tuple
    # A single element always matches its own type.
    if len(input_tuple) == 1:
        return True

    # Use the first element to establish the reference type
    first_element = input_tuple[0]
    reference_type = type(first_element)

    # Iterate through the tuple and compare every element's type 
    # against the reference type.
    for index, element in enumerate(input_tuple):
        # Skip the first element since it is our reference
        if index == 0:
            continue

        current_element_type = type(element)

        # If any element's type differs from the reference, return False immediately
        if current_element_type is not reference_type:
            return False

    # If the loop completes without returning False, all types are identical
    return True


if __name__ == "__main__":
    # Test cases provided in the problem description
    assert check_type((5, 6, 7, 3, 5, 6)) == True
    assert check_type((1, 2, "4")) == False
    assert check_type((3, 2, 1, 4, 5)) == True

    # Additional edge cases
    # Empty tuple
    assert check_type(()) == True
    # Single element
    assert check_type((10,)) == True
    # All same strings
    assert check_type(("a", "b", "c")) == True
    # All same booleans
    assert check_type((True, False, True)) == True
    # Mixed floats and ints (different types)
    assert check_type((1.0, 1)) == False