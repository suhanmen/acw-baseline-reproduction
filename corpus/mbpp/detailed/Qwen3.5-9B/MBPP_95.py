from typing import List, Any, Union

# The problem asks for a function named Find_Min_Length (based on the assertion calls)
# that takes a list of sublists and returns the minimum length of those sublists.
# 
# Requirements analysis:
# 1. Input: A list of lists (or iterables) containing elements.
# 2. Output: An integer representing the minimum length.
# 3. Edge cases to handle:
#    - Empty outer list (no sublists).
#    - Empty inner lists (length 0).
#    - Sublists with zero elements.
#    - Negative numbers or other non-list iterables inside the outer list (input validation).
#    - Mixed types inside sublists (should still work for length calculation, but input validity matters).
# 4. Logic:
#    - Iterate through each sublist.
#    - Calculate the length of each sublist.
#    - Find the minimum of these lengths.
#    - If the outer list is empty, handle gracefully (likely raise an error or return specific value, 
#      but based on "defensive coding", raising a ValueError is standard for empty collections when a min is requested).

def _validate_outer_list(input_list: Any) -> List[Any]:
    """
    Validates that the input is a list.
    Raises a TypeError if it is not.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list, but received {type(input_list).__name__}.")
    return input_list

def _validate_sublist(sublist: Any) -> List[Any]:
    """
    Validates that each element in the outer list is a list.
    Raises a TypeError if any element is not a list.
    """
    if not isinstance(sublist, list):
        raise TypeError(f"All elements must be lists. Found {type(sublist).__name__} instead.")
    return sublist

def _calculate_lengths(sublists: List[List[Any]]) -> List[int]:
    """
    Calculates the length of each valid sublist.
    Returns a list of integers.
    """
    lengths = []
    for sublist in sublists:
        # Calculate length explicitly
        length_val = len(sublist)
        lengths.append(length_val)
    return lengths

def Find_Min_Length(input_data: Any) -> Union[int, None]:
    """
    Finds the minimum length of the sublists contained within the provided list.

    Parameters:
    - input_data: Expected to be a list of lists.

    Returns:
    - An integer representing the minimum length.
    - Returns None if the input list is empty (or raise ValueError depending on strictness, 
      here we return None for an empty set of lengths to avoid crashing, 
      though strictly mathematically min of empty set is undefined).
      However, to be production-grade and explicit, we will raise an error for empty input 
      because finding a minimum of nothing is logically undefined for this context.

    Let's refine the empty input handling:
    If the input list is empty, we cannot find a minimum length. 
    We will raise a ValueError to be explicit about the invalid state of having no data.
    """

    # Step 1: Validate the outer container
    validated_list = _validate_outer_list(input_data)

    # Step 2: Handle the empty outer list case explicitly
    if len(validated_list) == 0:
        # Raising an error is more explicit and defensive than returning None for a "find min" operation
        raise ValueError("Input list is empty. Cannot determine minimum length of sublists.")

    # Step 3: Validate all inner elements are lists
    # This ensures we don't try to call len() on invalid objects later, 
    # though len() exists for almost everything in Python, type safety is key for "defensive" code.
    for item in validated_list:
        _validate_sublist(item)

    # Step 4: Calculate lengths of all sublists
    lengths = _calculate_lengths(validated_list)

    # At this point, we know validated_list is not empty, so lengths is not empty.
    # We can safely call min().
    minimum_length = min(lengths)

    return minimum_length