from typing import Any, List, Tuple, Union


def _validate_tuple_list(data: Any, variable_name: str = "data") -> List[Tuple[Any, ...]]:
    """
    Validates that the input is a list containing only tuples.

    Raises:
        TypeError: If data is not a list.
        TypeError: If any element within data is not a tuple.
        ValueError: If the list is empty (as per problem context, we expect to check for k elements).
    """
    if not isinstance(data, list):
        raise TypeError(f"{variable_name} must be a list, but got {type(data).__name__}.")

    if len(data) == 0:
        raise ValueError(f"{variable_name} cannot be an empty list.")

    for index, item in enumerate(data):
        if not isinstance(item, tuple):
            raise TypeError(
                f"{variable_name}[{index}] must be a tuple, but got {type(item).__name__}."
            )

    return data


def _validate_k_value(k: Any) -> int:
    """
    Validates that k is a non-negative integer.

    Raises:
        TypeError: If k is not an integer (excluding booleans which are int subclasses).
        ValueError: If k is negative.
    """
    # Booleans are technically integers in Python, but usually not what we want for counts.
    if isinstance(k, bool):
        raise TypeError("k cannot be a boolean.")

    if not isinstance(k, int):
        raise TypeError(f"k must be an integer, but got {type(k).__name__}.")

    if k < 0:
        raise ValueError(f"k must be non-negative, but got {k}.")

    return k


def _check_length_requirement(element: Tuple[Any, ...], k: int) -> bool:
    """
    Checks if a specific tuple element has a length of exactly k.

    Args:
        element: The tuple to check.
        k: The required length.

    Returns:
        True if len(element) == k, False otherwise.
    """
    return len(element) == k


def check_k_elements(data: List[Tuple[Any, ...]], k: Any) -> bool:
    """
    Checks if all tuples in the given list have exactly k elements.

    This function performs:
    1. Input validation for the list structure.
    2. Input validation for the integer k.
    3. Iterative checking of each tuple's length.

    Returns:
        True if every tuple in the list has exactly k elements.
        False if any tuple does not have exactly k elements.

    Raises:
        TypeError: If data is not a list of tuples or k is not an integer.
        ValueError: If data is empty or k is negative.
    """
    # Step 1: Validate the data structure
    validated_data = _validate_tuple_list(data)

    # Step 2: Validate the k value
    validated_k = _validate_k_value(k)

    # Step 3: Iterate through each element and check its length
    all_match = True

    for current_tuple in validated_data:
        tuple_length = len(current_tuple)
        is_match = _check_length_requirement(current_tuple, validated_k)

        if not is_match:
            all_match = False
            # We can stop here since we only need to know if ALL match.
            break

    return all_match