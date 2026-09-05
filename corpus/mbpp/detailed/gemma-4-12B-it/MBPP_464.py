from typing import Any, Dict

def check_value(data: Dict[str, Any], target_value: Any) -> bool:
    """
    Checks if all values in the provided dictionary are equal to the target_value.

    Args:
        data (Dict[str, Any]): The dictionary to inspect.
        target_value (Any): The value to compare against every entry in the dictionary.

    Returns:
        bool: True if all values in the dictionary match target_value, False otherwise.
              Returns True for an empty dictionary as the condition "all values are equal 
              to target_value" is vacuously true.

    Raises:
        TypeError: If data is not a dictionary.
    """
    # Validate that the input data is actually a dictionary
    if not isinstance(data, dict):
        raise TypeError(f"Expected input 'data' to be a dict, but got {type(data).__name__}")

    # Handle the empty dictionary edge case.
    # In logic, a universal quantification over an empty set is True.
    if not data:
        return True

    # Extract the values from the dictionary into a list/iterator
    dictionary_values = list(data.values())

    # Check if there are any values at all (redundant due to empty check, but safe)
    if not dictionary_values:
        return True

    # Iterate through every value in the dictionary to check for equality
    for current_value in dictionary_values:
        # Perform an explicit equality check
        is_equal = (current_value == target_value)

        # If any single value does not match the target, the condition is failed
        if not is_equal:
            return False

    # If the loop completes without returning False, all values matched the target
    return True

if __name__ == "__main__":
    # Test cases provided in the problem description
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10) == False
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 12) == True
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 5) == False

    # Additional edge cases
    # Empty dictionary
    assert check_value({}, 10) == True

    # Single element matching
    assert check_value({'A': 1}, 1) == True

    # Single element not matching
    assert check_value({'A': 1}, 2) == False

    # All equal elements but different from target
    assert check_value({'A': 5, 'B': 5}, 5) == True
    assert check_value({'A': 5, 'B': 5}, 6) == False

    # Mixed types (False expected unless target matches perfectly)
    assert check_value({'A': 1, 'B': "1"}, 1) == False