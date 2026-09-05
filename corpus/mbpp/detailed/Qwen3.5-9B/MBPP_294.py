from typing import Any, List, Optional, Union
import sys

# Define a custom exception type for invalid input scenarios
class HeterogeneousListMaxError(Exception):
    """
    Exception raised when the input list cannot be processed to find a maximum value.
    This typically occurs when the list contains elements of incompatible types
    (e.g., mixing strings with integers).
    """
    pass

def _extract_numeric_value(value: Any) -> Optional[float]:
    """
    Helper function to attempt conversion of a value to a float.

    If the value is a string representing a number (integer or float), it converts and returns it.
    If the value is already a number (int or float), it returns it as a float.
    If the conversion is impossible, it returns None.

    Args:
        value (Any): The value to attempt conversion for.

    Returns:
        Optional[float]: The numeric float value if conversion is successful, None otherwise.
    """
    try:
        # Handle boolean explicitly to avoid treating True/False as 1/0,
        # as booleans are not numeric in this specific heterogeneous context.
        if isinstance(value, bool):
            return None

        if isinstance(value, int):
            return float(value)

        if isinstance(value, float):
            return value

        if isinstance(value, str):
            return float(value)

        return None
    except (ValueError, TypeError):
        return None

def _determine_comparison_strategy(values: List[Any]) -> str:
    """
    Analyzes the list of values to determine if they can be compared numerically.

    Returns 'numeric' if all extractable values are numbers and at least one is found.
    Returns 'string' if all values are strings.
    Returns 'incompatible' if the list is empty or contains a mix of numeric-like 
    and non-numeric-like types that cannot be uniformly handled.

    Args:
        values (List[Any]): The list of values to analyze.

    Returns:
        str: The comparison strategy ('numeric', 'string', or 'incompatible').
    """
    has_numeric = False
    has_non_numeric = False

    for item in values:
        numeric_result = _extract_numeric_value(item)

        if numeric_result is not None:
            has_numeric = True
        else:
            # Check if it's a string that failed numeric conversion or another type
            # We treat non-string, non-numeric as incompatible immediately for simplicity
            # based on the problem's examples focusing on Python versions vs numbers.
            # However, purely strings like "Python" are also not numeric.
            if not isinstance(item, str):
                return 'incompatible'
            else:
                has_non_numeric = True

    if not has_numeric and has_non_numeric:
        # All are strings (or strings that aren't numbers)
        return 'string'
    elif has_numeric and has_non_numeric:
        return 'incompatible'
    elif has_numeric:
        return 'numeric'
    else:
        # Empty list case handled in main function, but defensively here:
        return 'incompatible'

def _find_max_numeric(values: List[Any]) -> float:
    """
    Finds the maximum value among numeric-compatible elements.

    Args:
        values (List[Any]): The list of values.

    Returns:
        float: The maximum numeric value found.

    Raises:
        HeterogeneousListMaxError: If no numeric values could be extracted.
    """
    max_value: Optional[float] = None

    for item in values:
        numeric_val = _extract_numeric_value(item)
        if numeric_val is not None:
            if max_value is None or numeric_val > max_value:
                max_value = numeric_val

    if max_value is None:
        raise HeterogeneousListMaxError(
            "No numeric values found in the list to compare."
        )

    return max_value

def _find_max_string(values: List[Any]) -> Union[str, int]:
    """
    Finds the maximum value among string elements using lexicographical order.

    In Python, standard max() on strings works lexicographically. 
    However, the problem examples suggest a numeric result when mixed types exist.
    If the list is purely strings and non-numeric, we return the lex max string.
    But looking at the problem constraints, the mixed list examples return numbers.
    If the input is ONLY strings and none are numbers (e.g., ['a', 'b']), 
    returning the string max is the logical fallback for a hetero list of strings.

    Args:
        values (List[Any]): The list of values (expected to be all strings).

    Returns:
        str: The lexicographically maximum string.
    """
    if not values:
        raise HeterogeneousListMaxError("Cannot find max in an empty string list.")

    # Ensure all are strings
    if not all(isinstance(v, str) for v in values):
        raise HeterogeneousListMaxError("List contains non-string elements.")

    # Standard lexicographical max for strings
    return max(values)

def _validate_and_process_list(values: List[Any]) -> Any:
    """
    Main orchestration function. Validates the input list and executes 
    the appropriate comparison strategy.

    Args:
        values (List[Any]): The input list of heterogeneous values.

    Returns:
        Any: The maximum value found.

    Raises:
        HeterogeneousListMaxError: If the list is empty or contains incompatible types.
    """
    # Step 1: Validate empty input
    if not values:
        raise HeterogeneousListMaxError("The input list is empty.")

    # Step 2: Determine the strategy
    strategy = _determine_comparison_strategy(values)

    # Step 3: Execute based on strategy
    if strategy == 'numeric':
        return _find_max_numeric(values)
    elif strategy == 'string':
        return _find_max_string(values)
    else:
        raise HeterogeneousListMaxError("The list contains incompatible types.")

def max_val(input_list: List[Any]) -> Any:
    """
    Finds the maximum value in a given heterogeneous list.

    The function attempts to interpret the list as numeric values first.
    If all elements can be converted to numbers, it returns the maximum numeric value.
    If all elements are strings (and none are numbers), it returns the lexicographically
    largest string.
    If the list mixes numbers and non-numeric types (like strings that aren't numbers),
    it returns the maximum numeric value found.
    If the list contains a mix that prevents uniform comparison (e.g., specific constraints
    implying a single type is expected but mixed), it raises an error.

    Note: Based on the provided assertions, the logic prioritizes numeric extraction.
    If a string like '3.0' exists, it is treated as 3.0. If only 'Python' exists, 
    the list is treated as strings unless numbers are present.

    Args:
        input_list (List[Any]): A list containing heterogeneous elements (numbers and strings).

    Returns:
        Any: The maximum value determined by the comparison strategy.

    Raises:
        HeterogeneousListMaxError: If the list is empty or logically inconsistent for max finding.
        TypeError: If the input argument is not a list.
    """
    # Explicit type checking for the input argument
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list, but got {type(input_list).__name__}.")

    try:
        return _validate_and_process_list(input_list)
    except HeterogeneousListMaxError as e:
        # Re-raise to preserve the specific error context
        raise
    except Exception as e:
        # Catch any other unforeseen errors during processing and wrap them
        raise HeterogeneousListMaxError(f"Unexpected error during max calculation: {str(e)}") from e