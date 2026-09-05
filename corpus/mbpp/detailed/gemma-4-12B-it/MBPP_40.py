from collections import Counter
from typing import List, Dict, Any

def freq_element(nested_list: List[List[Any]]) -> Dict[Any, int]:
    """
    Finds the frequency of all elements within a nested list (list of lists).

    Args:
        nested_list (List[List[Any]]): A list containing lists of elements.

    Returns:
        Dict[Any, int]: A dictionary where keys are the unique elements found 
                         in all sub-lists and values are their respective counts.

    Raises:
        TypeError: If the input is not a list or if elements inside are not 
                   hashable (as they must be keys in a dictionary).
        ValueError: If the input contains nested elements that are not lists.
    """
    # Input Validation: Ensure the primary input is a list.
    if not isinstance(nested_list, list):
        raise TypeError(f"Expected input to be a list, but got {type(nested_list).__name__}")

    # Handle the edge case of an empty outer list.
    if not nested_list:
        return {}

    # Initialize a Counter object to store frequencies efficiently.
    # Counter is a subclass of dict designed for counting hashable objects.
    frequency_counter = Counter()

    # Iterate through the outer list to process each sub-list.
    for index, sub_list in enumerate(nested_list):
        # Validation: Check if the nested item is actually a list.
        if not isinstance(sub_list, list):
            raise ValueError(f"Element at index {index} is not a list: {sub_list}")

        # Process each item within the inner list.
        for element in sub_list:
            # Defensive check: Elements must be hashable to be used as dictionary keys.
            # This includes integers, strings, tuples, etc.
            try:
                # Update the counter with the current element.
                # Counter.update() adds 1 for each occurrence of the item.
                frequency_counter.update([element])
            except TypeError as exc:
                raise TypeError(
                    f"Element '{element}' at sub-list index {index} is unhashable "
                    f"and cannot be counted. Error: {exc}"
                ) from exc

    # Convert the Counter object to a standard dictionary to match requested return type.
    # The order of elements in the dictionary depends on the insertion order (Python 3.7+).
    result_dictionary = dict(frequency_counter)

    return result_dictionary

if __name__ == "__main__":
    # These assertions verify the production-grade logic.
    assert freq_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]) == \
           ({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})

    assert freq_element([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == \
           ({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1})

    assert freq_element([[15, 20, 30, 40], [80, 90, 100, 110], [30, 30, 80, 90]]) == \
           ({30: 3, 80: 2, 90: 2, 15: 1, 20: 1, 40: 1, 100: 1, 110: 1})