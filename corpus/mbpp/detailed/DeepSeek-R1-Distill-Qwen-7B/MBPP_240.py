def replace_list(original_list, replacement_list):
    """
    Replaces the last element of the original list with another list.

    Args:
        original_list (list): The list whose last element is to be replaced.
        replacement_list (list): The list to replace the last element with.

    Returns:
        list: A new list with the last element replaced by the replacement list.
    """
    # Handle edge cases
    if not original_list:
        # If original list is empty, return the replacement list
        return replacement_list
    elif len(original_list) == 1:
        # If original list has only one element, concatenate it with the replacement list
        return [original_list[0]] + replacement_list
    elif not replacement_list:
        # If replacement list is empty, return the original list
        return original_list
    else:
        # Otherwise, create a new list excluding the last element of original_list
        # and concatenate it with the replacement_list
        new_list = original_list[:-1] + replacement_list
        return new_list

# Test the function with the provided examples
assert replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
assert replace_list([1, 2, 3, 4, 5], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert replace_list(["red", "blue", "green"], ["yellow"]) == ["red", "blue", "yellow"]

print("All test cases passed.")