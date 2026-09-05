from typing import List, Any, Dict

def freq_count(input_list: List[Any]) -> Dict[Any, int]:
    """
    Calculates the frequency of each element in a given list.

    Args:
        input_list (List[Any]): A list containing elements to be counted.

    Returns:
        Dict[Any, int]: A dictionary where keys are unique elements 
                         from the input list and values are their respective counts.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains unhashable types (like lists or dicts).
    """
    # Validation: Check if the input is indeed a list
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be of type list, but received {type(input_list).__name__}")

    # Edge Case: Handle empty list
    if not input_list:
        return {}

    # Initialize the dictionary to store the frequencies
    # Using a dictionary to map elements (keys) to their occurrence counts (values)
    frequency_map: Dict[Any, int] = {}

    # Iterate through every element in the provided list
    for item in input_list:
        # Defensive Check: Dictionary keys must be hashable.
        # Types like list, set, or dict are not hashable and will raise a TypeError.
        try:
            _check_hashable(item)
        except TypeError as exc:
            raise ValueError(f"List contains an unhashable element: {item}. "
                             "All elements must be hashable (e.g., int, str, tuple).") from exc

        # Logic: If the item is already in our map, increment its count.
        # Otherwise, initialize its count to 1.
        if item in frequency_map:
            current_count = frequency_map[item]
            new_count = current_count + 1
            frequency_map[item] = new_count
        else:
            # First time encountering this element
            frequency_map[item] = 1

    return frequency_map

def _check_hashable(obj: Any) -> None:
    """
    Helper function to verify if an object can be used as a dictionary key.
    This is part of the defensive programming approach to ensure the function 
    doesn't crash with a standard TypeError midway through processing.
    """
    try:
        hash(obj)
    except TypeError:
        # Re-raise to be caught by the main loop's error handling
        raise TypeError("Object is not hashable")

if __name__ == "__main__":
    # These assertions verify the behavior against the provided requirements.
    # Note: Dictionary order does not affect equality in Python.

    # Case 1: Multiple counts, specific sequence
    assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

    # Case 2: Mixed sequence
    assert freq_count([1,2,3,4,3,2,4,1,3,1,4]) == {1: 3, 2: 2, 3: 3, 4: 3}

    # Case 3: Diverse numbers
    assert freq_count([5,6,7,4,9,10,4,5,6,7,9,5]) == {10: 1, 5: 3, 6: 2, 7: 2, 4: 2, 9: 2}

    # Additional Edge Cases
    # Empty list
    assert freq_count([]) == {}

    # Single element
    assert freq_count([100]) == {100: 1}

    # All equal elements
    assert freq_count([1, 1, 1, 1]) == {1: 4}

    # Negative numbers and zero
    assert freq_count([-1, 0, -1, 5, 0]) == {-1: 2, 0: 2, 5: 1}