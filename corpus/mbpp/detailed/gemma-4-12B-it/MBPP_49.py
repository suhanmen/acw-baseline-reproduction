from typing import List, Any, Union

def specified_element(matrix: List[List[Any]], index: int) -> List[Any]:
    """
    Extracts every element at a specific index from a given two-dimensional list.

    Args:
        matrix: A list of lists containing elements of any type.
        index: The zero-based index of the element to extract from each inner list.

    Returns:
        A list of elements found at the specified index in each inner list.

    Raises:
        TypeError: If the matrix is not a list or if the elements inside are not lists.
        ValueError: If the matrix is empty or the index is out of bounds for any row.
        IndexError: If the index provided is negative or otherwise invalid for the context.
    """

    # Validate that the primary input is a list.
    if not isinstance(matrix, list):
        raise TypeError(f"Input 'matrix' must be a list, received {type(matrix).__name__}.")

    # Handle the degenerate case of an empty outer list.
    if len(matrix) == 0:
        return []

    # Validate that every item in the outer list is actually a list.
    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError(f"Element at index {i} in the matrix must be a list, received {type(row).__name__}.")

    # Define a container for the extracted values.
    extracted_values: List[Any] = []

    # Iterate through every row in the 2D list.
    for row_index, row in enumerate(matrix):
        # Check if the row is empty.
        if not row:
            raise ValueError(f"Row at index {row_index} is empty; cannot extract element at index {index}.")

        # Check if the provided index is valid for the current row.
        # We check bounds explicitly to provide descriptive error messages.
        row_length = len(row)

        # Note: Python supports negative indexing (e.g., -1 for the last element).
        # However, to ensure production-grade safety and predictability, 
        # we check if the absolute value is within the valid range.
        if index >= row_length or index < -row_length:
            raise IndexError(
                f"Index {index} is out of bounds for row at index {row_index} "
                f"(row length is {row_length})."
            )

        # Extract the element at the target position.
        target_element = row[index]

        # Append the found element to our result list.
        extracted_values.append(target_element)

    return extracted_values

# Verification against provided assertions
if __name__ == "__main__":
    # Test case 1: Index 0 (First elements)
    # Expected: [1, 4, 7]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0) == [1, 4, 7]

    # Test case 2: Index 2 (Third elements)
    # Expected: [3, 6, 9]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 2) == [3, 6, 9]

    # Test case 3: Index 1 (Second elements)
    # Expected: [2, 5, 1]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 1) == [2, 5, 1]