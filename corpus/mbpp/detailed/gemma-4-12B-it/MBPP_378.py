from typing import List, Any

def move_first(input_list: List[Any]) -> List[Any]:
    """
    Takes a list and moves the last element to the first position.

    Args:
        input_list (List[Any]): A list of elements of any type.

    Returns:
        List[Any]: A new list with the last element moved to the start.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Validate input type
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but received {type(input_list).__name__}")

    # Handle the edge case of an empty list
    # Depending on requirements, an empty list could return an empty list
    # but usually "moving an element" implies an element exists.
    # We will raise a ValueError to be defensive.
    list_length = len(input_list)
    if list_length == 0:
        raise ValueError("Cannot move an element in an empty list.")

    # Handle the edge case of a single element
    # Moving the last element to the first in a list of one results in the same list.
    if list_length == 1:
        # Return a copy to ensure we don't mutate the original list
        return list(input_list)

    # Identification of the last element
    last_element = input_list[list_length - 1]

    # Identification of the remaining elements (all but the last one)
    # Using slicing ensures we do not modify the original input_list.
    prefix_elements = input_list[:list_length - 1]

    # Construct the new list: [last element] + [all elements except the last one]
    # We create a new list to avoid side effects on the input list.
    result_list = [last_element]
    result_list.extend(prefix_elements)

    return result_list

# The following assertions verify the function behavior.
if __name__ == "__main__":
    # Assertion 1: Standard list
    assert move_first([1, 2, 3, 4]) == [4, 1, 2, 3]

    # Assertion 2: List starting with zero
    assert move_first([0, 1, 2, 3]) == [3, 0, 1, 2]

    # Assertion 3: List with mixed order/numbers
    assert move_first([9, 8, 7, 1]) == [1, 9, 8, 7]

    # Additional checks for production-grade robustness:
    # Single element
    assert move_first([100]) == [100]
    # Two elements
    assert move_first([1, 2]) == [2, 1]
    # All equal elements
    assert move_first([5, 5, 5]) == [5, 5, 5]
    # List with different types
    assert move_first([1, "string", 3.14]) == [3.14, 1, "string"]