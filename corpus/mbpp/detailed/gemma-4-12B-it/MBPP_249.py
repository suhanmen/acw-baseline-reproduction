from typing import List, Any

def intersection_array(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Finds the intersection of two arrays using a lambda function.
    The intersection contains elements that are present in both lists.
    The order of elements in the result follows the order of appearance 
    in the first list.
    """

    # --- Input Validation ---
    # Check if both inputs are lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be of type list.")

    # Handle cases where inputs are None (though type hint suggests List)
    if list1 is None or list2 is None:
        raise ValueError("Input lists cannot be None.")

    # --- Edge Case Handling ---
    # If either list is empty, the intersection is always an empty list.
    if len(list1) == 0 or len(list2) == 0:
        return []

    # --- Logic Implementation ---

    # To optimize lookup time from O(N) to O(1) per element,
    # we convert the second list into a set.
    # This ensures that checking "is x in list2" is efficient.
    lookup_set = set(list2)

    # The problem specifically requires the use of a lambda function.
    # We define a lambda that checks if an element from list1 exists in the lookup set.
    # We use this lambda inside a filter operation.
    is_in_both = lambda element: element in lookup_set

    # We iterate through list1 and keep only elements that satisfy the lambda.
    # Note: To handle potential duplicates in list1 while maintaining 
    # a mathematical intersection (unique elements), we can track seen items,
    # but the provided assertions suggest we should preserve elements of list1 
    # that are found in list2.

    # Filter the first list based on the lambda predicate.
    filtered_iterator = filter(is_in_both, list1)

    # Convert the filter object back into a list.
    result_list = list(filtered_iterator)

    # --- Final Cleanup ---
    # If there are duplicate values in list1 that are also in list2, 
    # and the goal is a unique set of shared items, we would use a set.
    # However, looking at the assertions:
    # [1, 2, 3, 5, 7, 8, 9, 10] and [1, 2, 4, 8, 9] -> [1, 2, 8, 9]
    # The logic above perfectly satisfies these requirements.

    return result_list

# The provided assertions are satisfied by this implementation.
if __name__ == "__main__":
    # Assertions for verification
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [3, 5, 7, 9]) == [3, 5, 7, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [10, 20, 30, 40]) == [10]