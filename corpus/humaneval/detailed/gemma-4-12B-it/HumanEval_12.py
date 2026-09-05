from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    # Validate the input type. Although the type hint suggests List[str], 
    # production-grade code should handle unexpected types gracefully.
    if not isinstance(strings, list):
        raise TypeError(f"Input must be a list, but received {type(strings).__name__}")

    # Handle the empty list edge case explicitly.
    if len(strings) == 0:
        return None

    # Track the current longest string found during the iteration.
    # We initialize it with the first element since we already checked 
    # that the list is not empty.
    current_longest_string: str = strings[0]
    current_max_length: int = len(current_longest_string)

    # Iterate through the list starting from the second element (index 1).
    # If the list only has one element, this loop will not execute.
    for index in range(1, len(strings)):
        current_item: str = strings[index]

        # Defensive check: ensure every element in the list is actually a string.
        if not isinstance(current_item, str):
            raise TypeError(f"All elements in the list must be strings. "
                            f"Found {type(current_item).__name__} at index {index}.")

        # Calculate the length of the current element.
        current_item_length: int = len(current_item)

        # We only update current_longest_string if the current_item_length 
        # is strictly GREATER than current_max_length. 
        # This ensures we preserve the first occurrence in case of a tie.
        if current_item_length > current_max_length:
            current_longest_string = current_item
            current_max_length = current_item_length

    return current_longest_string