from typing import List, Union, Tuple

# Define a type alias for clarity on what the function returns.
# The return type is either an empty list or a list containing two integers:
# [value, index].
ResultList = List[Union[int, None]]

def pluck(arr: List[Union[int, None]]) -> ResultList:
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

    # Step 1: Validate the input to ensure it is a list.
    # Although the constraints imply valid input, robust code should check.
    if not isinstance(arr, list):
        return []

    # Step 2: Check if the array is empty.
    # If there are no elements, there can be no even value.
    if len(arr) == 0:
        return []

    # Step 3: Initialize variables to track the best candidate found so far.
    # 'smallest_even_value' will hold the minimum even integer encountered.
    # Initialize it to a value larger than any possible input constraint (arbitrary high number).
    # Since constraints say node.value >= 0, we can start with -1 to indicate 'none found yet'.
    smallest_even_value: int = -1
    smallest_even_index: int = -1

    # We need a flag to know if we have found at least one even number.
    has_even_found: bool = False

    # Step 4: Iterate through the array using index enumeration.
    for index in range(len(arr)):
        current_value = arr[index]

        # Step 5: Validate that the current element is actually an integer.
        # This handles potential edge cases where the list might contain non-integer data.
        if not isinstance(current_value, int):
            # If a non-integer is encountered, we cannot process it as a node value.
            # Based on defensive coding principles, we might choose to skip it or return [].
            # Given the problem context (tree nodes), skipping invalid nodes is a reasonable choice
            # to avoid crashing, though strictly speaking the input should be valid per constraints.
            continue

        # Step 6: Check if the current value is even.
        # An even number is divisible by 2 with no remainder.
        is_current_even = (current_value % 2 == 0)

        if is_current_even:
            # We have found an even number. Now determine if it's the new smallest.

            # If we haven't found any even number yet, this becomes our initial candidate.
            if not has_even_found:
                smallest_even_value = current_value
                smallest_even_index = index
                has_even_found = True
            else:
                # We already have a candidate. Compare the new even value with the current smallest.
                # We want the smallest value.
                if current_value < smallest_even_value:
                    smallest_even_value = current_value
                    smallest_even_index = index
                # If current_value == smallest_even_value, we do nothing because the problem
                # states: "return the node that has smallest index".
                # Since we are iterating from index 0 upwards, the first occurrence (smallest index)
                # is already stored in our variables. We do not need to update.

    # Step 7: Prepare the final result.
    # If no even numbers were found during the iteration, return an empty list.
    if not has_even_found:
        return []

    # Otherwise, construct the result list with the value and its index.
    return [smallest_even_value, smallest_even_index]