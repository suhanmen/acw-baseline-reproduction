from typing import Any, List, Tuple, Union

LengthValueTuple = Tuple[int, Any]
"""Type alias for a tuple containing (length, list_element)."""

InvalidInputType = type(...)
"""Placeholder to represent an invalid input type for explicit error messages."""


def _validate_lists_input(input_data: Any) -> List[Any]:
    """
    Validate that the input is a non-null list containing only lists.

    This function performs strict type checking to ensure:
    1. The input is not None.
    2. The input is a list (or tuple, handled as a list).
    3. Every element inside is itself a list.

    Args:
        input_data: The input to validate.

    Returns:
        The validated input list if successful.

    Raises:
        TypeError: If the input structure is invalid.
    """
    if input_data is None:
        raise TypeError("Input data cannot be None.")

    if not isinstance(input_data, (list, tuple)):
        raise TypeError(f"Input must be a list or tuple of lists, got {type(input_data).__name__}.")

    if len(input_data) == 0:
        # An empty collection of lists is technically valid input for the algorithm
        # but returns an empty result, which is handled in the main logic.
        # We allow this to pass through to the logic layer.
        return list(input_data)

    for index, item in enumerate(input_data):
        if not isinstance(item, list):
            raise TypeError(
                f"All elements must be lists. Element at index {index} "
                f"is of type {type(item).__name__}."
            )

    return list(input_data)


def _compute_length_and_pair(value: Any) -> LengthValueTuple:
    """
    Compute the length of a list and pair it with the list itself.

    This helper function isolates the calculation of length and the creation
    of the comparison tuple to keep the main logic explicit and readable.

    Args:
        value: A list object to measure.

    Returns:
        A tuple containing (length_of_list, list_object).

    Raises:
        TypeError: If the input is not a list (should be caught earlier, but safe here).
    """
    if not isinstance(value, list):
        raise TypeError("Compute function received a non-list item.")

    length = len(value)
    result_pair = (length, value)
    return result_pair


def _extract_length(pair: LengthValueTuple) -> int:
    """
    Extract the integer length from the comparison tuple.

    Args:
        pair: A tuple of (length, list).

    Returns:
        The integer length component.
    """
    return pair[0]


def _extract_list(pair: LengthValueTuple) -> Any:
    """
    Extract the original list from the comparison tuple.

    Args:
        pair: A tuple of (length, list).

    Returns:
        The list component.
    """
    return pair[1]


def _find_max_by_length_lambda(
    pairs: List[LengthValueTuple]
) -> Tuple[int, Any]:
    """
    Find the pair with the maximum length using a lambda function.

    This function strictly uses a lambda expression for the comparison logic
    as required by the problem statement, while keeping the flow explicit.
    It handles the case where the list of pairs is empty by returning (0, None).

    Args:
        pairs: A list of (length, original_list) tuples.

    Returns:
        A tuple (max_length, corresponding_list).
    """
    if len(pairs) == 0:
        return (0, None)

    # Using max with a key that is a lambda function.
    # The lambda receives a pair (length, list) and returns its length for comparison.
    # key=lambda x: x[0]

    max_pair = max(
        pairs,
        key=lambda candidate_pair: candidate_pair[0]
    )

    return max_pair


def max_length_list(input_data: Any) -> LengthValueTuple:
    """
    Find the list with the maximum length from a given collection of lists.

    This function validates the input, transforms the data into comparable pairs,
    utilizes a lambda function to determine the maximum based on list length,
    and returns the result in a consistent format.

    Algorithm:
    1. Validate input types and structure.
    2. Transform each inner list into a (length, list) tuple.
    3. Use a lambda function with max() to identify the tuple with the highest length.
    4. Extract and return the length and the original list.

    Args:
        input_data: A list of lists to evaluate.

    Returns:
        A tuple containing:
        - The maximum length found (int).
        - The list object that has that length (list).
        If the input list is empty, returns (0, None).

    Raises:
        TypeError: If input is not a list of lists, or if non-list items are found inside.
    """

    # Step 1: Validate the input structure explicitly
    validated_data = _validate_lists_input(input_data)

    # Step 2: Transform the validated data into (length, list) pairs
    # We use a list comprehension with explicit logic for clarity and mutability safety
    transformed_pairs: List[LengthValueTuple] = []

    for inner_list in validated_data:
        # Compute length and create the pair using the dedicated helper
        pair = _compute_length_and_pair(inner_list)
        transformed_pairs.append(pair)

    # Step 3: Find the maximum pair using a lambda function
    # The lambda extracts the first element (length) for comparison
    if len(transformed_pairs) == 0:
        # Edge case: Empty input list (e.g., [])
        return (0, None)

    result_pair = _find_max_by_length_lambda(transformed_pairs)

    # Step 4: Extract the final components from the result pair
    max_length = _extract_length(result_pair)
    max_list = _extract_list(result_pair)

    return (max_length, max_list)