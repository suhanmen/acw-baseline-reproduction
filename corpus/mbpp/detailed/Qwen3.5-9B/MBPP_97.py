from typing import List, Any, Dict

def frequency_lists(input_lists: List[List[Any]]) -> Dict[Any, int]:
    """
    Calculates the frequency count of all elements across a list of lists.

    The function traverses every sublist within the input list and counts
    the occurrences of each element found. The result is a dictionary where
    keys are the unique elements from all sublists and values are their total
    counts.

    This implementation is defensive:
    - It validates that the input is a list.
    - It validates that every item in the list is a list.
    - It handles edge cases like empty outer list, empty inner lists, etc.
    - It avoids integer overflow issues (Python handles large integers automatically).

    Args:
        input_lists (List[List[Any]]): A list containing zero or more sublists.

    Returns:
        Dict[Any, int]: A dictionary mapping each unique element to its total frequency count.

    Raises:
        TypeError: If the outer list is not a list, or if any inner item is not a list.
    """

    # Step 1: Validate the outer container type explicitly
    if not isinstance(input_lists, list):
        raise TypeError(
            f"Expected input to be a list of lists, but received a {type(input_lists).__name__}."
        )

    # Step 2: Initialize the frequency counter dictionary
    frequency_map: Dict[Any, int] = {}

    # Step 3: Iterate through each item in the outer list
    for outer_index, current_item in enumerate(input_lists):

        # Step 3.1: Validate that the current item is indeed a list
        if not isinstance(current_item, list):
            raise TypeError(
                f"Expected all items in the outer list to be lists. "
                f"Found item at index {outer_index} with type {type(current_item).__name__}."
            )

        # Step 4: Iterate through each element within the current sublist
        for element in current_item:

            # Step 4.1: Check if the element already exists in our frequency map
            if element in frequency_map:
                # Step 4.2: If it exists, increment its count
                frequency_map[element] += 1

            # Step 4.3: If it does not exist, initialize its count to 1
            else:
                frequency_map[element] = 1

    # Step 5: Return the populated frequency map
    return frequency_map