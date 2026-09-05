from typing import List

def sub_list(list1: List[int], list2: List[int]) -> List[int]:
    """
    Subtracts elements of two lists index by index using map and lambda.

    Args:
        list1: The first list of integers.
        list2: The second list of integers.

    Returns:
        A list of integers where each element is the result of list1[i] - list2[i].

    Raises:
        ValueError: If the lists are of unequal length.
        TypeError: If inputs are not lists or contain non-numeric types.
    """
    # --- Input Validation ---

    # Check if inputs are actually lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be of type 'list'.")

    # Check if lists are of equal length
    len1 = len(list1)
    len2 = len(list2)
    if len1 != len2:
        raise ValueError(f"Lists must be of equal length. Received lengths {len1} and {len2}.")

    # Handle edge case: both lists are empty
    if len1 == 0:
        return []

    # Verify that all elements in both lists are integers or floats
    for item in list1:
        if not isinstance(item, (int, float)):
            raise TypeError(f"List 1 contains non-numeric element: {item}")
    for item in list2:
        if not isinstance(item, (int, float)):
            raise TypeError(f"List 2 contains non-numeric element: {item}")

    # --- Core Logic ---

    # Define a lambda function that takes two arguments and returns their difference.
    # This follows the requirement to use a lambda function.
    subtraction_logic = lambda x, y: x - y

    # Use the map function to apply the subtraction_logic to elements from both lists.
    # map(function, iterable1, iterable2) processes elements by position.
    result_iterator = map(subtraction_logic, list1, list2)

    # Convert the map object (iterator) back into a list.
    # We use list() because map returns a generator-like object in Python 3.
    result_list = list(result_iterator)

    return result_list

# Verification of assertions provided in the prompt
if __name__ == "__main__":
    # These assertions confirm the requirements are met.
    assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert sub_list([1, 2], [3, 4]) == [-2, -2]
    assert sub_list([90, 120], [50, 70]) == [40, 50]