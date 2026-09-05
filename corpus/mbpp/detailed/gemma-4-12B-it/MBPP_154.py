from typing import List, Any, Union

def specified_element(matrix: List[List[Any]], index: int) -> List[Any]:
    """
    Extracts the element at a specific index from every row of a 2D list.

    Args:
        matrix: A two-dimensional list (list of lists).
        index: The zero-based index of the element to extract from each row.

    Returns:
        A list containing the elements found at the specified index in each row.

    Raises:
        TypeError: If the input matrix is not a list or if the index is not an integer.
        ValueError: If the matrix is empty or if the index is out of bounds for any row.
    """
    # --- Input Validation ---

    # Validate that matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(f"Input 'matrix' must be a list, received {type(matrix).__name__}")

    # Validate that index is an integer
    if not isinstance(index, int):
        raise TypeError(f"Input 'index' must be an integer, received {type(index).__name__}")

    # Handle the degenerate case of an empty outer list
    if len(matrix) == 0:
        # Depending on requirements, this could return [] or raise an error.
        # Given the assertions, it's safer to return an empty list for an empty matrix.
        return []

    # --- Processing ---

    extracted_elements: List[Any] = []

    # Iterate through each row in the 2D list
    for row_index, row in enumerate(matrix):
        # Validate that each element in the matrix is indeed a list
        if not isinstance(row, list):
            raise ValueError(f"Element at matrix index {row_index} is not a list: {row}")

        # Check if the current row is empty
        if len(row) == 0:
            raise ValueError(f"Row at matrix index {row_index} is empty, cannot access index {index}")

        # Check if the requested index is within the bounds of the current row
        # This handles both negative indices (which Python normally allows) 
        # and indices larger than the row length.
        # To be production-grade, we ensure the index is strictly valid for the row.
        if index < 0 or index >= len(row):
            raise IndexError(
                f"Index {index} is out of bounds for row at position {row_index} "
                f"(row length: {len(row)})"
            )

        # Extract the element and add it to our result list
        target_value = row[index]
        extracted_elements.append(target_value)

    return extracted_elements