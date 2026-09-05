from typing import List, Tuple, Union

Number = Union[int, float]
TuplePair = Tuple[Number, Number]

def _calculate_product(pair: TuplePair) -> Number:
    """
    Calculate the product of two numbers.

    Args:
        pair: A tuple containing exactly two numbers.

    Returns:
        The product of the two numbers.
    """
    first_value, second_value = pair[0], pair[1]
    result = first_value * second_value
    return result

def _validate_pair(pair: TuplePair) -> None:
    """
    Validate that the input pair is valid.

    A pair is valid if:
    1. It is a tuple.
    2. It contains exactly two elements.
    3. Both elements are numbers (int or float).

    Raises:
        ValueError: If the pair is not a valid tuple of two numbers.
        TypeError: If the pair elements are not of a numeric type.
    """
    # Check type of the pair itself
    if not isinstance(pair, tuple):
        raise TypeError(
            f"Expected a tuple for the pair, but got type {type(pair).__name__}."
        )

    # Check length of the pair
    if len(pair) != 2:
        raise ValueError(
            f"Expected a pair with exactly 2 elements, but got {len(pair)} elements."
        )

    # Check types of individual elements
    first_element, second_element = pair[0], pair[1]

    if not isinstance(first_element, (int, float)) or isinstance(first_element, bool):
        raise TypeError(
            f"First element of pair must be a number (int or float), got {type(first_element).__name__}."
        )

    if not isinstance(second_element, (int, float)) or isinstance(second_element, bool):
        raise TypeError(
            f"Second element of pair must be a number (int or float), got {type(second_element).__name__}."
        )

def _validate_input_list(input_list: List[TuplePair]) -> None:
    """
    Validate that the input list is valid.

    Requirements:
    1. It must be a list.
    2. It must not be None.
    3. It must contain at least one element.
    4. All elements must be valid pairs (checked by _validate_pair).

    Raises:
        TypeError: If the input is not a list or contains invalid types.
        ValueError: If the list is empty or contains invalid pairs.
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError(
            f"Expected a list of tuples, but got type {type(input_list).__name__}."
        )

    # Check for empty list
    if len(input_list) == 0:
        raise ValueError("The input list must contain at least one pair.")

    # Validate each pair in the list
    for index, item in enumerate(input_list):
        _validate_pair(item)

def max_product_tuple(input_list: List[TuplePair]) -> Number:
    """
    Find the maximum product from the pairs of tuples within a given list.

    This function calculates the product for each pair in the list and returns
    the maximum product found.

    Args:
        input_list: A list of tuples, where each tuple contains exactly two numbers.

    Returns:
        The maximum product calculated from the pairs.

    Raises:
        TypeError: If the input is not a list or contains invalid pair types.
        ValueError: If the list is empty or contains invalid pair values.
    """
    # Step 1: Validate the input list structure and contents
    _validate_input_list(input_list)

    # Step 2: Calculate the product for each pair in the list
    products = []
    for pair in input_list:
        product_value = _calculate_product(pair)
        products.append(product_value)

    # Step 3: Find the maximum value among the calculated products
    maximum_product = max(products)

    return maximum_product