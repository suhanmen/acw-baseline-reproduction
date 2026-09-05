from typing import List, Any

def _validate_input(elements: List[Any], size: int) -> None:
    """
    Validates that the input list and the provided size are consistent.
    Raises ValueError or TypeError if inputs are invalid.
    """
    if not isinstance(elements, list):
        raise TypeError("The input 'elements' must be a list.")

    if not isinstance(size, int):
        raise TypeError("The input 'size' must be an integer.")

    actual_length = len(elements)
    if actual_length != size:
        raise ValueError(
            f"The provided size {size} does not match the actual list length {actual_length}."
        )

def get_Odd_Occurrence(elements: List[Any], size: int) -> Any:
    """
    Finds the element in a list that occurs an odd number of times.

    The problem constraints imply that there is exactly one such element.
    This implementation uses a frequency map (dictionary) to count 
    occurrences, ensuring O(n) time complexity and O(k) space complexity 
    where k is the number of unique elements.

    Args:
        elements (List[Any]): A list of items.
        size (int): The expected length of the list.

    Returns:
        Any: The element that occurs an odd number of times.

    Raises:
        ValueError: If no element occurs an odd number of times.
        TypeError: If inputs are of incorrect types.
    """
    # 1. Validate inputs
    _validate_input(elements, size)

    # 2. Handle edge case: empty list
    if size == 0:
        # Based on the problem description, this shouldn't happen with valid inputs,
        # but we handle it defensively.
        raise ValueError("The input list is empty; no element exists to return.")

    # 3. Count the frequency of each element
    # We use a dictionary to store counts. 
    # This handles any hashable type (int, str, etc.)
    occurrence_counts = {}

    for item in elements:
        if item in occurrence_counts:
            occurrence_counts[item] += 1
        else:
            occurrence_counts[item] = 1

    # 4. Identify the element with an odd count
    # We iterate through the dictionary to find the key with an odd value.
    result_element = None
    found_odd = False

    for element, count in occurrence_counts.items():
        if count % 2 != 0:
            result_element = element
            found_odd = True
            # We can break early because the problem implies exactly one odd occurrence.
            break

    # 5. Final verification
    if not found_odd:
        # This case occurs if all elements appear an even number of times.
        raise ValueError("No element in the provided list occurs an odd number of times.")

    return result_element

if __name__ == "__main__":
    # Test cases provided in the problem description
    assert get_Odd_Occurrence([1, 2, 3, 1, 2, 3, 1], 7) == 1
    assert get_Odd_Occurrence([1, 2, 3, 2, 3, 1, 3], 7) == 3
    assert get_Odd_Occurrence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5