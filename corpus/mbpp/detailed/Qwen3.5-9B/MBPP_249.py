from typing import List, Any, Optional

def _validate_single_list(input_list: Any) -> None:
    """
    Validates that the input is a list and that all elements are hashable.

    This function raises a TypeError if the input is not a list.
    It also attempts to validate that elements are hashable (required for set operations),
    raising a TypeError if any element is unhashable (e.g., another list or dict).
    """
    if not isinstance(input_list, list):
        raise TypeError(
            f"Expected a list as input, but received {type(input_list).__name__}."
        )

    for index, element in enumerate(input_list):
        try:
            hash(element)
        except TypeError as e:
            raise TypeError(
                f"Element at index {index} ({element!r}) is not hashable and cannot be used in set operations."
            ) from e


def _lambda_based_intersection(
    list_a: List[Any], 
    list_b: List[Any]
) -> List[Any]:
    """
    Computes the intersection of two lists using a lambda function.

    Logic:
    1. Create a set from the first list for O(1) average time complexity lookups.
    2. Iterate through the second list.
    3. Use a lambda function to check if each element of the second list exists in the set.
    4. Collect all matching elements into a result list.
    5. Return the result list, preserving the order of appearance from the second list.

    Note: This implementation preserves duplicates from the second list if they exist
    and match elements in the first list, as per standard intersection behavior on sequences.
    """
    # Step 1: Convert the first list into a set for efficient lookup
    # This handles the 'validation' of existence implicitly by relying on Python's set hashing.
    set_a = set(list_a)

    # Step 2: Define the lambda function that checks membership
    # The lambda takes an element and the set, returning True if the element is in the set.
    is_in_set = lambda element: element in set_a

    # Step 3: Initialize an empty list to hold the intersection results
    intersection_results: List[Any] = []

    # Step 4: Iterate over the second list
    for current_element in list_b:
        # Step 5: Apply the lambda function to the current element
        if is_in_set(current_element):
            # Step 6: Append the element to the results if it satisfies the condition
            intersection_results.append(current_element)

    # Step 7: Return the final list of intersecting elements
    return intersection_results


def intersection_array(list_a: List[Any], list_b: List[Any]) -> List[Any]:
    """
    Finds the intersection of two arrays using a lambda function.

    This function is the main entry point. It performs validation on both inputs
    to ensure they are valid lists containing only hashable elements.
    If validation passes, it delegates the actual intersection logic to the
    helper function `_lambda_based_intersection`.

    Args:
        list_a: The first list of elements.
        list_b: The second list of elements.

    Returns:
        A list containing elements common to both input lists.
        The order of elements in the result follows their order of appearance in list_b.

    Raises:
        TypeError: If either input is not a list or contains unhashable elements.
    """
    # Explicitly validate the first input list
    _validate_single_list(list_a)

    # Explicitly validate the second input list
    _validate_single_list(list_b)

    # Execute the core logic
    return _lambda_based_intersection(list_a, list_b)