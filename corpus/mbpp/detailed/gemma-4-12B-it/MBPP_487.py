from typing import List, Tuple, Any

def sort_tuple(input_list: List[Tuple[Any, ...]]) -> List[Tuple[Any, ...]]:
    """
    Sorts a list of tuples in increasing order based on the last element 
    of each tuple.

    Args:
        input_list: A list of tuples.

    Returns:
        A new list of tuples sorted by the last element.

    Raises:
        TypeError: If the input is not a list or contains non-tuple elements.
        ValueError: If any tuple in the list is empty.
        TypeError: If the last elements of the tuples are not comparable.
    """
    # 1. Validate that the input is actually a list.
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but received {type(input_list).__name__}.")

    # 2. Handle the edge case of an empty list immediately.
    if len(input_list) == 0:
        return []

    # 3. Validate the contents of the list to ensure they are tuples and not empty.
    # We do this upfront to provide clear error messages.
    for index, item in enumerate(input_list):
        if not isinstance(item, tuple):
            raise TypeError(f"Element at index {index} is not a tuple: {item}")
        if len(item) == 0:
            raise ValueError(f"Element at index {index} is an empty tuple; cannot access last element.")

    # 4. Create a copy of the list to avoid mutating the original input (defensive programming).
    # Even though Python's sort() can be used, returning a new list is safer for functional purity.
    working_list = list(input_list)

    def get_last_element(tup: Tuple[Any, ...]) -> Any:
        """Helper function to extract the last element of a tuple."""
        return tup[-1]

    # 5. Use Python's built-in Timsort algorithm (via sorted()) which is stable.
    # We explicitly provide a key function to target the last element.
    try:
        sorted_result = sorted(
            working_list, 
            key=get_last_element
        )
    except TypeError as e:
        # This occurs if the last elements are of incomparable types (e.g., int and str).
        raise TypeError("The last elements of the tuples are not comparable.") from e

    return sorted_result

if __name__ == "__main__":
    # Verification of the assertions provided in the prompt.
    assert sort_tuple([(1, 3), (3, 2), (2, 1)]) == [(2, 1), (3, 2), (1, 3)]
    assert sort_tuple([(2, 4), (3, 3), (1, 1)]) == [(1, 1), (3, 3), (2, 4)]
    assert sort_tuple([(3, 9), (6, 7), (4, 3)]) == [(4, 3), (6, 7), (3, 9)]