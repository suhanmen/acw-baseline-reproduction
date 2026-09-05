from typing import List, Optional

def _compute_magnitude_sum(values: List[int]) -> int:
    """
    Compute the sum of the absolute values (magnitudes) of the provided integers.

    :param values: A list of integers.
    :return: The sum of absolute values.
    """
    total_magnitude = 0
    for number in values:
        magnitude = abs(number)
        total_magnitude += magnitude
    return total_magnitude

def _compute_sign_product(values: List[int]) -> Optional[int]:
    """
    Compute the product of the signs of the provided integers.

    The sign of a number is:
    - 1 if the number is positive.
    - -1 if the number is negative.
    - 0 if the number is zero.

    If any number is zero, the product of signs is immediately 0.
    If the list is empty, return None (though the caller handles empty lists).

    :param values: A list of integers.
    :return: The product of signs (1, -1, or 0), or None if the list was empty.
    """
    if not values:
        return None

    sign_product = 1
    has_zero = False

    for number in values:
        if number == 0:
            has_zero = True
            break
        if number > 0:
            # Sign is 1, multiplying by 1 changes nothing, so we can skip multiplication
            # but logically we acknowledge the sign is 1.
            pass
        elif number < 0:
            # Sign is -1, multiply current product by -1
            sign_product *= -1

    if has_zero:
        return 0

    return sign_product

def _validate_input(values: List) -> bool:
    """
    Validate that the input is a list containing only integers.

    :param values: The input to validate.
    :return: True if valid, raises ValueError otherwise.
    """
    if not isinstance(values, list):
        raise TypeError("Input must be a list of integers.")

    for idx, item in enumerate(values):
        if not isinstance(item, int) or isinstance(item, bool):
            raise ValueError(f"All elements must be integers. Found type {type(item).__name__} at index {idx}.")

    return True

def prod_signs(arr: List[int]) -> Optional[int]:
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    # Step 1: Validate the input type and contents
    _validate_input(arr)

    # Step 2: Handle the empty array case explicitly as per requirements
    if len(arr) == 0:
        return None

    # Step 3: Calculate the sum of magnitudes
    magnitude_sum = _compute_magnitude_sum(arr)

    # Step 4: Calculate the product of signs
    signs_product = _compute_sign_product(arr)

    # Step 5: Compute the final result
    # Note: If signs_product is 0 (due to a zero in input), the result is 0.
    final_result = magnitude_sum * signs_product

    return final_result