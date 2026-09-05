from typing import List, Any


def replace_list(original_list: List[Any], replacement_list: List[Any]) -> List[Any]:
    """
    Replaces the last element of the original_list with the entire replacement_list.

    If the original_list is empty, it returns a copy of the replacement_list.
    If the original_list contains only one element, it replaces that element 
    with the replacement_list.

    Args:
        original_list: The list where the last element is to be replaced.
        replacement_list: The list to be inserted in place of the last element.

    Returns:
        A new list with the replacement applied.

    Raises:
        TypeError: If either input is not a list.
    """
    # Input Validation: Ensure the inputs are actually lists
    if not isinstance(original_list, list):
        raise TypeError(f"Expected 'original_list' to be of type list, got {type(original_list).__name__}")

    if not isinstance(replacement_list, list):
        raise TypeError(f"Expected 'replacement_list' to be of type list, got {type(replacement_list).__name__}")

    # Edge Case: original_list is empty
    # If there is no last element to replace, the most logical behavior 
    # based on the substitution principle is to return the replacement_list itself.
    if len(original_list) == 0:
        return list(replacement_list)

    # Create a shallow copy of the original list to ensure the function 
    # does not mutate the input list (Functional Programming best practice).
    result_list = list(original_list)

    # Identify the index of the last element.
    # Using -1 is standard, but we calculate it explicitly for clarity.
    last_index = len(result_list) - 1

    # Define the part of the list before the last element.
    # If the list has only one element, prefix_part will be an empty list.
    prefix_part = result_list[:last_index]

    # We want to join the prefix_part with the replacement_list.
    # This effectively "drops" the last element of result_list and 
    # appends all elements of replacement_list.

    # We initialize the result with the prefix.
    final_output = []

    # Extend the final output with elements from the prefix.
    for item in prefix_part:
        final_output.append(item)

    # Extend the final output with elements from the replacement list.
    for replacement_item in replacement_list:
        final_output.append(replacement_item)

    return final_output


if __name__ == "__main__":
    # Test cases provided in the prompt
    assert replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert replace_list([1, 2, 3, 4, 5], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert replace_list(["red", "blue", "green"], ["yellow"]) == ["red", "blue", "yellow"]