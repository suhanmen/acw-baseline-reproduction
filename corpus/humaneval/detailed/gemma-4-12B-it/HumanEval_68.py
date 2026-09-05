from typing import List, Union, Optional

def pluck(arr: List[int]) -> List[Union[int, None]]:
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    # Defensive check: Ensure the input is a list
    if not isinstance(arr, list):
        return []

    # Handle empty list case explicitly
    if not arr:
        return []

    # Tracking variables for the best candidate found so far
    # We use None to indicate that no even number has been encountered yet
    smallest_even_value: Optional[int] = None
    best_index: Optional[int] = None

    # Iterate through the list once to find the smallest even value
    # Complexity: O(n) time, O(1) space
    for current_index, current_value in enumerate(arr):
        # Validate that the value is an integer
        if not isinstance(current_value, int):
            # In production, we might raise a ValueError, but based on requirements, 
            # we skip or handle gracefully. Here we treat non-integers as invalid.
            continue

        # Check if the value is even (non-negative integers inclusive of 0)
        is_even: bool = (current_value % 2 == 0)

        if is_even:
            # If this is the first even number we've seen, it is currently the best
            if smallest_even_value is None:
                smallest_even_value = current_value
                best_index = current_index
            else:
                # If the current even number is strictly smaller than our record,
                # update the record.
                if current_value < smallest_even_value:
                    smallest_even_value = current_value
                    best_index = current_index
                # Note: If current_value == smallest_even_value, we do nothing,
                # because the problem requires the smallest index, and we are 
                # iterating from left to right (index 0 to n).

    # Final result construction
    if smallest_even_value is None:
        # No even values were found in the array
        return []

    # Return the result in the format [value, index]
    result = [smallest_even_value, best_index]
    return result