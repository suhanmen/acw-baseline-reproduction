from typing import List, Any, Tuple, Union

def sequential_search(arr: List[Any], target: Any) -> Tuple[bool, int]:
    """
    Searches for a target element within a list using the sequential search algorithm.

    The sequential search (or linear search) checks each element of the list 
    one by one from the beginning until the target is found or the end of 
    the list is reached.

    Args:
        arr (List[Any]): The list of elements to search through.
        target (Any): The value to search for in the list.

    Returns:
        Tuple[bool, int]: A tuple containing:
            - A boolean indicating if the element was found (True) or not (False).
            - The index of the first occurrence of the target (if found), 
              otherwise -1.

    Raises:
        TypeError: If the input arr is not a list or target is of an incompatible type.
    """

    # Validate input types
    if not isinstance(arr, list):
        raise TypeError(f"Expected input 'arr' to be of type list, but got {type(arr).__name__}")

    # Note: target can be any type as long as it's comparable with elements in the list
    # The search will naturally handle cases where types are incomparable by raising a TypeError.

    # Handle edge case: empty list
    if len(arr) == 0:
        # Element cannot be found in an empty list
        return (False, -1)

    # Initialize variables to track the search state
    found_status: bool = False
    result_index: int = -1

    # Iterate through the list using indices to keep track of the position
    # We use a range based on the length of the list to ensure we visit every element.
    list_length: int = len(arr)

    for current_index in range(list_length):
        current_element: Any = arr[current_index]

        # Check if the current element matches the target
        # Using equality operator for comparison
        if current_element == target:
            # Target found, update result variables
            found_status = True
            result_index = current_index

            # Since sequential search typically returns the first occurrence,
            # we break out of the loop immediately.
            break

    # Return the final status and the index
    # If the loop completes without finding the target, 
    # found_status remains False and result_index remains -1.
    return (found_status, result_index)

# The following assertions validate the logic against the problem requirements
if __name__ == "__main__":
    # These are the provided test cases
    assert sequential_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31) == (True, 3)
    assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61], 61) == (True, 7)
    assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56], 48) == (True, 6)