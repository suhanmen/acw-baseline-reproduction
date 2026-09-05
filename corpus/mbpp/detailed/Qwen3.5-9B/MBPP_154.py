from typing import Any, List, Union

def validate_row_structure(row: Any, row_index: int) -> None:
    """
    Validates that the row at the given index is actually a list (or array-like).
    If not, raises a ValueError.

    :param row: The element from the main list to check.
    :param row_index: The index of the row for error messages.
    """
    if not isinstance(row, list):
        raise ValueError(
            f"Row at index {row_index} is not a list. "
            f"Expected a list, but got {type(row).__name__}."
        )

def validate_extract_index(extract_index: Union[int, float]) -> int:
    """
    Validates and normalizes the column index to be a valid integer.

    :param extract_index: The user-provided column index.
    :return: The normalized integer index.
    :raises: TypeError or ValueError if the input is invalid.
    """
    if not isinstance(extract_index, (int, float)):
        raise TypeError(
            f"Extract index must be a number (int or float), "
            f"got {type(extract_index).__name__}."
        )

    # Convert float to int if it represents a whole number
    normalized_index = int(extract_index)

    if normalized_index != extract_index:
        raise ValueError(
            f"Extract index must be a whole number. "
            f"Provided value {extract_index} resulted in {normalized_index}."
        )

    return normalized_index

def extract_column_from_row(row: List[Any], col_index: int) -> Any:
    """
    Safely extracts a single element from a row at the specified column index.

    :param row: The source list (row).
    :param col_index: The column index to retrieve.
    :return: The element found at the specified index.
    :raises: IndexError if the index is out of bounds.
    """
    if col_index < 0 or col_index >= len(row):
        raise IndexError(
            f"Column index {col_index} is out of bounds for row of length {len(row)}."
        )
    return row[col_index]

def extract_column_from_matrix(matrix: List[List[Any]], col_index: int) -> List[Any]:
    """
    Extracts a specific column from a two-dimensional list (matrix).

    This function iterates through each row of the matrix, validates its structure,
    and collects the element at the specified column index into a new list.

    :param matrix: The 2D list to process.
    :param col_index: The column index to extract.
    :return: A new list containing the elements from the specified column.
    :raises: ValueError if the matrix is empty, rows are not lists, or column index is invalid.
    :raises: IndexError if any row is shorter than the requested column index + 1.
    """
    # Handle empty matrix case explicitly
    if not matrix:
        raise ValueError("The input matrix is empty (contains no rows).")

    result_column: List[Any] = []

    for row_index, row in enumerate(matrix):
        # Validate that the current item is actually a list
        validate_row_structure(row, row_index)

        # Validate that the column index is within the bounds of the current row
        # This handles cases where rows might have different lengths (jagged arrays)
        if col_index >= len(row):
            raise IndexError(
                f"Row at index {row_index} has length {len(row)}, "
                f"which is insufficient for column index {col_index}."
            )

        # Extract and append the element
        element = extract_column_from_row(row, col_index)
        result_column.append(element)

    return result_column

def specified_element(matrix: List[List[Any]], col_index: Union[int, float]) -> List[Any]:
    """
    Extracts every specified element (column) from a given two dimensional list.

    This is the main entry point. It performs validation on the inputs,
    handles edge cases such as empty inputs or malformed structures,
    and returns the extracted column as a new list.

    :param matrix: A two-dimensional list (list of lists) of arbitrary elements.
    :param col_index: The index of the column to extract. Can be an int or float.
    :return: A list containing the elements of the specified column.
    :raises: TypeError, ValueError, or IndexError if inputs are invalid.
    """
    # 1. Validate the column index first
    validated_col_index = validate_extract_index(col_index)

    # 2. Extract the column, handling all row validations internally
    result = extract_column_from_matrix(matrix, validated_col_index)

    return result