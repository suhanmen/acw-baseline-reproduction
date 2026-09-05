from typing import List, Tuple, Any, Dict

def max_occurrences(input_list: List[Any]) -> Tuple[Any, int]:
    """
    Finds the item with the maximum frequency in a given list.

    In the case of a tie (multiple items having the same maximum frequency),
    the item that first reached that maximum frequency count during the 
    sequential scan of the list is returned.

    Args:
        input_list: A list of elements of any hashable type.

    Returns:
        A tuple containing (the_item, its_frequency).

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input list contains unhashable elements.
    """

    # --- Input Validation ---

    # Check if the input is actually a list
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input of type list, but received {type(input_list).__name__}")

    # Handle empty list edge case
    if len(input_list) == 0:
        raise ValueError("The input list must not be empty.")

    # --- Frequency Counting ---

    # Use a dictionary to store counts of each unique element
    # A dictionary provides O(1) average time complexity for lookups and insertions
    frequency_map: Dict[Any, int] = {}

    # Keep track of the order of appearance to handle ties correctly
    # However, the requirements imply we just need the first one to hit the max.
    # We will iterate through the list to build the frequency map.
    for item in input_list:
        # Ensure the item is hashable (required for dict keys)
        try:
            # If item exists, increment; otherwise, initialize to 1
            if item in frequency_map:
                frequency_map[item] = frequency_map[item] + 1
            else:
                frequency_map[item] = 1
        except TypeError as exc:
            raise TypeError(f"List contains unhashable element: {item}") from exc

    # --- Finding the Maximum ---

    # We need to find the item with the highest count.
    # To ensure we handle ties correctly (returning the one that occurred 
    # first/was dominant), we can iterate through the original list 
    # and check the frequency map.

    max_frequency = -1
    result_item = None

    # We want to find which item has the highest count.
    # Based on the provided assertions, if there is a tie, the 
    # logic usually favors the first one encountered in the list 
    # that possesses that maximum frequency.

    # First, find the absolute maximum frequency value
    for count in frequency_map.values():
        if count > max_frequency:
            max_frequency = count

    # Second, find the first item in the original list that has this frequency
    # This ensures stable behavior for ties.
    for item in input_list:
        current_count = frequency_map.get(item)

        if current_count == max_frequency:
            result_item = item
            break

    return (result_item, max_frequency)

if __name__ == "__main__":
    # Verification against provided assertions
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == (2, 5)
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18]) == (8, 2)
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10]) == (20, 3)