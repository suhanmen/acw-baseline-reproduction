from typing import List, Tuple, Any, Union

def index_on_inner_list(data: List[Union[Tuple, List]], index: int) -> List[Union[Tuple, List]]:
    """
    Sorts a list of lists (or tuples) based on a specific index of the inner elements.

    The function performs the following steps:
    1. Validates that the input data is a list.
    2. Validates that the index is a non-negative integer.
    3. Validates that every inner element is a sequence (list or tuple) and contains the requested index.
    4. Sorts the data in ascending order based on the value at the specified index.
    5. Returns a new sorted list.

    Args:
        data: A list of sequences (e.g., lists or tuples).
        index: The zero-based index of the element in the inner sequence to sort by.

    Returns:
        A new list sorted by the value at the specified index.

    Raises:
        TypeError: If the input data is not a list or if elements are not sequences.
        ValueError: If the index is out of bounds for any of the inner sequences.
        IndexError: If the provided index is negative.
    """
    # Validate input type for the main container
    if not isinstance(data, list):
        raise TypeError(f"Expected a list for 'data', but got {type(data).__name__}.")

    # Validate index type and value
    if not isinstance(index, int):
        raise TypeError(f"Expected an integer for 'index', but got {type(index).__name__}.")

    if index < 0:
        raise IndexError(f"Index must be non-negative, but received {index}.")

    # Handle edge case: empty input list
    if len(data) == 0:
        return []

    # Check validity of inner elements before sorting
    # This ensures we fail fast with a descriptive error rather than crashing inside the sort
    for item in data:
        if not isinstance(item, (list, tuple)):
            raise TypeError(f"All elements in the list must be sequences (list or tuple). "
                            f"Found {type(item).__name__}: {item}")

        if index >= len(item):
            raise ValueError(f"Index {index} is out of bounds for the inner element: {item}")

    # Define a helper function for the sort key
    # This makes the logic explicit and readable
    def get_sort_key(inner_sequence: Union[Tuple, List]) -> Any:
        return inner_sequence[index]

    # Create a copy to avoid mutating the original input list (standard production practice)
    # We use sorted() which returns a new list.
    # The key parameter specifies we sort based on the value at the provided index.
    sorted_list = sorted(data, key=get_sort_key)

    return sorted_list

# The assertions provided in the problem description:
if __name__ == "__main__":
    # Test Case 1: Sort by index 0 (Name) - Note: The assertion expects alphabetical order 
    # except the provided assertion in the prompt seems to follow a specific order.
    # Let's re-verify the provided assertions.
    # Assertion 1: index 0 -> Beau (B), Brady (B), Greyson (G), Wyatt (W)
    # Wait, the prompt's assertion result for index 0 is:
    # [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
    # This is sorted alphabetically.

    test_data = [
        ('Greyson Fulton', 98, 99), 
        ('Brady Kent', 97, 96), 
        ('Wyatt Knott', 91, 94), 
        ('Beau Turnbull', 94, 98)
    ]

    # Verification of requirements:
    # index 0: Beau (B), Brady (B), Greyson (G), Wyatt (W) -> Correct alphabetical
    # index 1: 91 (Wyatt), 94 (Beau), 97 (Brady), 98 (Greyson) -> Correct numeric
    # index 2: 94 (Wyatt), 96 (Brady), 98 (Beau), 99 (Greyson) -> Correct numeric