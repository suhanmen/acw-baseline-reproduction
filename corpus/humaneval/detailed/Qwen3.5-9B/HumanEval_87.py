from typing import Any, List, Tuple, Union

def get_row(lst: Any, x: Any) -> List[Tuple[int, int]]:
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

    # Validate the input list 'lst'
    if not isinstance(lst, list):
        raise TypeError("The input 'lst' must be a list.")

    # Validate the target value 'x'
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("The target value 'x' must be an integer (not boolean).")

    # Initialize a list to store all found coordinates
    # Each element will be a tuple (row_index, column_index)
    found_coordinates: List[Tuple[int, int]] = []

    # Iterate through each row in the provided list
    for row_index, row in enumerate(lst):
        # Validate that the current row is a list
        if not isinstance(row, list):
            raise TypeError(f"Row at index {row_index} is not a list.")

        # Iterate through each element in the current row
        # Enumerate provides both the column index and the element value
        for column_index, element in enumerate(row):
            # Check if the current element is exactly equal to the target x
            # Using 'isinstance(x, int)' ensures we don't match boolean subtypes of int if needed,
            # though the outer check on x already prevents x from being a bool.
            if element == x:
                # Create a coordinate tuple for this match
                # Format: (row, column)
                coordinate: Tuple[int, int] = (row_index, column_index)

                # Append the coordinate to our results list
                found_coordinates.append(coordinate)

    # The problem requires two sorting steps:
    # 1. Sort coordinates initially by rows in ascending order.
    # 2. Within the same row, sort coordinates by columns in descending order.

    # We can achieve this in a single sort operation using the `key` argument.
    # The key function returns a tuple: (row_index, -column_index)
    # - Python sorts tuples element by element.
    # - The first element (row_index) is sorted in ascending order (default).
    # - The second element (-column_index) effectively sorts the original column_index in descending order.
    #   (e.g., -5 < -4 < -3 means 5 > 4 > 3)

    found_coordinates.sort(key=lambda coord: (coord[0], -coord[1]))

    # Return the final sorted list of coordinates
    return found_coordinates