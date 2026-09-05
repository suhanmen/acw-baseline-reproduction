from typing import List, Tuple, Any

def _validate_input(data: Any) -> List[Tuple[str, int]]:
    """
    Validates that the input is a list of tuples where:
    - Each tuple has exactly two elements.
    - The first element is a string (subject name).
    - The second element is an integer (marks).

    Raises:
        TypeError: If the input type is incorrect or element types are invalid.
        ValueError: If the input list contains empty tuples or invalid data.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")

    if len(data) == 0:
        return []

    for index, item in enumerate(data):
        if not isinstance(item, tuple):
            raise TypeError(f"Element at index {index} must be a tuple, found {type(item).__name__}.")

        if len(item) != 2:
            raise ValueError(f"Element at index {index} must contain exactly 2 elements, found {len(item)}.")

        subject, marks = item

        if not isinstance(subject, str):
            raise TypeError(f"Subject at index {index} must be a string, found {type(subject).__name__}.")

        if not isinstance(marks, int):
            raise TypeError(f"Marks at index {index} must be an integer, found {type(marks).__name__}.")

    return data

def subject_marks(data: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Sorts a list of (subject, marks) tuples based on the marks in ascending order.

    Args:
        data: A list of tuples containing a subject name (str) and marks (int).

    Returns:
        A new list of tuples sorted by marks in ascending order.

    Raises:
        TypeError: If input structure is invalid.
        ValueError: If tuple structure is invalid.
    """
    # Step 1: Validate the input data structure explicitly
    validated_data = _validate_input(data)

    # Step 2: Create a copy to avoid mutating the original list
    sorted_data = list(validated_data)

    # Step 3: Sort the list using a lambda function that extracts the second element (marks)
    # Key extraction: lambda x: x[1]
    # This ensures ascending order by default.
    sorted_data.sort(key=lambda subject_mark_tuple: subject_mark_tuple[1])

    return sorted_data