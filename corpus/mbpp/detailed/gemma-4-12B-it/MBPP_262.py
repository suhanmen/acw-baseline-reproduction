from typing import List, Any, Tuple

def split_two_parts(input_list: List[Any], split_index: int) -> Tuple[List[Any], List[Any]]:
    """
    Splits a given list into two parts based on a specified index.

    The first part contains elements from the start of the list up to (but not including)
    the split_index. The second part contains the remaining elements.

    Args:
        input_list: The list of elements to be split.
        split_index: The integer index at which to split the list.

    Returns:
        A tuple containing two lists: (first_part, second_part).

    Raises:
        TypeError: If input_list is not a list or split_index is not an integer.
        ValueError: If split_index is negative or exceeds the length of the list.
    """

    # --- Input Validation ---

    # Ensure input_list is actually a list
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input_list to be of type list, but got {type(input_list).__name__}")

    # Ensure split_index is an integer
    if not isinstance(split_index, int):
        raise TypeError(f"Expected split_index to be of type int, but got {type(split_index).__name__}")

    list_length = len(input_list)

    # Validate that the split_index is within the bounds of the list
    # Note: split_index can be 0 (resulting in an empty first part)
    # and can be equal to list_length (resulting in an empty second part).
    if split_index < 0:
        raise ValueError(f"split_index must be non-negative, but got {split_index}")

    if split_index > list_length:
        raise ValueError(
            f"split_index {split_index} exceeds the list length {list_length}"
        )

    # --- Edge Case Handling ---

    # Case: Empty list
    if list_length == 0:
        # split_index must be 0 here due to the validation above
        return ([], [])

    # Case: Single element list
    if list_length == 1:
        if split_index == 0:
            return ([], [input_list[0]])
        elif split_index == 1:
            return ([input_list[0]], [])

    # --- Processing ---

    # Define the end of the first part.
    # The problem statement says the "length of the first part" is given by split_index.
    # Therefore, the first part contains elements from index 0 to split_index - 1.

    # Extract the first part using list slicing
    first_part = input_list[0:split_index]

    # Extract the second part using list slicing
    # Slicing from split_index to the end of the list.
    second_part = input_list[split_index:list_length]

    # Return the result as a tuple of two lists
    return (first_part, second_part)

if __name__ == "__main__":
    # Testing the logic against provided assertions
    assert split_two_parts([1,1,2,3,4,4,5,1], 3) == ([1, 1, 2], [3, 4, 4, 5, 1])
    assert split_two_parts(['a', 'b', 'c', 'd'], 2) == (['a', 'b'], ['c', 'd'])
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'], 4) == (['p', 'y', 't', 'h'], ['o', 'n'])