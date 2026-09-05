from typing import List, Tuple, Union

Number = Union[int, float]

def calculate_pair_product(a: Number, b: Number) -> Number:
    """
    Calculates the product of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b

def validate_tuple(t: Tuple) -> None:
    """
    Validates that the input is a tuple with exactly two numeric elements.

    Args:
        t: The tuple to validate.

    Raises:
        TypeError: If the input is not a tuple.
        ValueError: If the tuple does not have exactly two elements.
        TypeError: If any element is not a number (int or float).
    """
    if not isinstance(t, tuple):
        raise TypeError(f"Input must be a tuple, but got {type(t).__name__}")

    if len(t) != 2:
        raise ValueError(f"Each tuple must contain exactly two elements, but got {len(t)}")

    for index, element in enumerate(t):
        if not isinstance(element, (int, float)):
            raise TypeError(f"All elements must be numbers. Invalid element at index {index}: {element} (type: {type(element).__name__})")

def validate_input_list(input_list: List[Tuple]) -> None:
    """
    Validates that the input is a list of tuples.

    Args:
        input_list: The list to validate.

    Raises:
        TypeError: If the input is not a list or if elements are not tuples.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but got {type(input_list).__name__}")

    for i, item in enumerate(input_list):
        validate_tuple(item)

def find_minimum_product(tuple_list: List[Tuple]) -> Number:
    """
    Finds the minimum product from all pairs within the provided list of tuples.

    This function iterates through each tuple in the list, calculates the product
    of the two numbers within that tuple, and keeps track of the smallest product found so far.

    Args:
        tuple_list: A list of tuples, where each tuple contains exactly two numbers.

    Returns:
        The minimum product found among all tuples in the list.

    Raises:
        TypeError: If the input list is empty or contains invalid elements.
        ValueError: If the list is empty.
    """
    if len(tuple_list) == 0:
        raise ValueError("The input list of tuples cannot be empty.")

    # Initialize the minimum product with the product of the first tuple
    # We validate the first tuple explicitly before using it.
    first_tuple = tuple_list[0]
    validate_tuple(first_tuple)

    initial_product = calculate_pair_product(first_tuple[0], first_tuple[1])
    current_minimum_product = initial_product

    # Iterate through the rest of the list starting from the second element
    for current_tuple in tuple_list[1:]:
        validate_tuple(current_tuple)

        current_product = calculate_pair_product(current_tuple[0], current_tuple[1])

        if current_product < current_minimum_product:
            current_minimum_product = current_product

    return current_minimum_product

def min_product_tuple(input_list: List[Tuple]) -> Number:
    """
    Wrapper function to find the minimum product from the pairs of tuples.
    Performs input validation and calls the core logic function.

    Args:
        input_list: A list of tuples containing two numeric elements each.

    Returns:
        The minimum product calculated from the valid tuples.

    Raises:
        TypeError: If the input is not a list of tuples or if tuples have invalid content.
        ValueError: If the input list is empty.
    """
    validate_input_list(input_list)
    return find_minimum_product(input_list)