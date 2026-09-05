from typing import List, Optional, Union

def _get_sign(number: int) -> int:
    """
    Helper function to determine the sign of an integer.
    Returns 1 for positive, -1 for negative, and 0 for zero.
    """
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def _get_magnitude(number: int) -> int:
    """
    Helper function to determine the absolute value (magnitude) of an integer.
    """
    return abs(number)

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
    # Requirement: return None for empty array.
    # We also check if the input is actually a list to ensure robustness.
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers.")

    if len(arr) == 0:
        return None

    # Step 1: Calculate the sum of magnitudes of all numbers in the array.
    total_magnitude_sum = 0
    for element in arr:
        # Ensure input elements are integers
        if not isinstance(element, int):
            raise ValueError(f"All elements in the array must be integers. Found: {type(element)}")

        magnitude = _get_magnitude(element)
        total_magnitude_sum += magnitude

    # Step 2: Calculate the product of all signs in the array.
    # The sign is 1 for positive, -1 for negative, and 0 for zero.
    total_sign_product = 1
    for element in arr:
        current_sign = _get_sign(element)
        total_sign_product *= current_sign

        # Optimization: if product becomes 0, it will remain 0.
        if total_sign_product == 0:
            break

    # Step 3: Calculate the final result.
    # The result is (sum of magnitudes) * (product of signs).
    final_result = total_magnitude_sum * total_sign_product

    return final_result