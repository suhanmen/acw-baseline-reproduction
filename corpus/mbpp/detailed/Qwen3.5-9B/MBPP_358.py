from typing import List, Tuple, Union

def _validate_input_lists(list_a: List, list_b: List) -> None:
    """
    Validates that both input lists are valid for modulo division.

    Checks performed:
    1. Both inputs must be lists.
    2. Both lists must be of the same length.
    3. Both lists must not be empty (handled by the loop range implicitly, but good to explicit check).
    4. Every element in list_b (the divisor) must be non-zero.
    """
    # Check type: both must be lists
    if not isinstance(list_a, list):
        raise TypeError(f"First argument must be a list, got {type(list_a).__name__}")

    if not isinstance(list_b, list):
        raise TypeError(f"Second argument must be a list, got {type(list_b).__name__}")

    # Check for empty lists
    if len(list_a) == 0:
        raise ValueError("First list cannot be empty.")
    if len(list_b) == 0:
        raise ValueError("Second list cannot be empty.")

    # Check for equal lengths
    if len(list_a) != len(list_b):
        raise ValueError(f"Lists must have the same length. "
                         f"List A has {len(list_a)} elements, List B has {len(list_b)} elements.")

    # Check for zero divisors in list_b
    for index, divisor in enumerate(list_b):
        if divisor == 0:
            raise ValueError(f"Division by zero is not allowed at index {index} in the divisor list.")

def _perform_modulo_division(
    dividend_list: List[Union[int, float]],
    divisor_list: List[Union[int, float]]
) -> List[Union[int, float]]:
    """
    Performs the element-wise modulo division using map and lambda.

    Logic:
    Result[i] = dividend_list[i] % divisor_list[i]
    """
    return list(
        map(
            lambda dividend, divisor: dividend % divisor,
            dividend_list,
            divisor_list
        )
    )

def moddiv_list(list_a: List, list_b: List) -> List[Union[int, float]]:
    """
    Finds the modulo division of two lists using map and lambda function.

    This function takes two lists of numbers, validates them, and returns a new list
    where each element is the result of (list_a[i] % list_b[i]).

    Examples:
        moddiv_list([4,5,6],[1, 2, 3]) -> [0, 1, 0]
        moddiv_list([3,2],[1,4]) -> [0, 2]
        moddiv_list([90,120],[50,70]) -> [40, 50]
    """
    # Step 1: Validate inputs to handle edge cases and invalid data explicitly
    _validate_input_lists(list_a, list_b)

    # Step 2: Perform the calculation using map and lambda
    result = _perform_modulo_division(list_a, list_b)

    return result