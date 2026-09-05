from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.

    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    # Defensive check for input types
    if not isinstance(lst, list):
        raise ValueError("Input 'lst' must be a list of lists.")

    # Initialize the container for coordinates
    coordinates: List[Tuple[int, int]] = []

    # Handle empty list case
    if not lst:
        return coordinates

    # Iterate through each row with its index
    for row_index, row in enumerate(lst):
        # Defensive check: ensure each row is actually a list
        if not isinstance(row, list):
            raise ValueError(f"Element at index {row_index} is not a list.")

        # Iterate through each element in the row with its column index
        for col_index, element in enumerate(row):
            # Check if the current element matches the target x
            if element == x:
                # Store the result as a tuple (row_index, col_index)
                coordinates.append((row_index, col_index))

    # Sort logic:
    # 1. Primary sort key: row index (ascending)
    # 2. Secondary sort key: column index (descending)
    # Python's sort is stable, so we can perform this in two steps 
    # or use a custom key. A custom key is cleaner for multiple directions.

    def sort_key_func(coord: Tuple[int, int]) -> Tuple[int, int]:
        row_idx, col_idx = coord
        # We return row_idx as positive (ascending) 
        # and col_idx as negative (to achieve descending order during sorting)
        return (row_idx, -col_idx)

    # Apply the sorting logic
    coordinates.sort(key=sort_key_func)

    return coordinates