import math
from typing import List, Union

Number = Union[int, float]

def _is_valid_number(element: object) -> bool:
    """
    Helper function to check if an element is a valid number (int or float).
    This ensures type safety before attempting any mathematical operations.
    """
    return isinstance(element, (int, float))

def _is_valid_gcd_input(elements: List[Number]) -> bool:
    """
    Helper function to validate the entire list for GCD calculation.
    Constraints:
    - The list must not be empty.
    - Every element must be a number.
    - Every element must be non-zero (GCD is typically defined for non-zero integers).
    - All elements should ideally be integers. If a float is passed, we check if it's effectively an integer.
    For this problem, we will enforce that inputs are integers to avoid ambiguity with float division results.
    """
    if not elements:
        return False

    for element in elements:
        if not _is_valid_number(element):
            return False
        if not isinstance(element, int) or isinstance(element, bool):
            # Exclude booleans as they are a subclass of int in Python but semantically different here.
            # Also, standard GCD is for integers. If floats were allowed, we would need to convert them,
            # but the problem context implies integer arrays.
            return False
        if element == 0:
            return False

    return True

def _calculate_pairwise_gcd(a: int, b: int) -> int:
    """
    Helper function to calculate the Greatest Common Divisor (GCD) of two numbers.
    Uses the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def get_gcd(elements: List[Number]) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) of all elements in the given list.

    Logic:
    1. Validate the input list to ensure it's not empty and contains only valid non-zero integers.
    2. Initialize the running GCD with the first element of the list.
    3. Iterate through the remaining elements.
    4. Update the running GCD by calculating the GCD of the current running GCD and the next element.
    5. Return the final result.

    Properties:
    gcd(a, b, c) = gcd(gcd(a, b), c)
    gcd(a, 0) is not handled here as 0 is an invalid input per the validation step.
    If the list contains a single element, that element is returned.
    """
    # Step 1: Validate input
    if not _is_valid_gcd_input(elements):
        raise ValueError(
            "Input list must be non-empty and contain only non-zero integers. "
            "Found empty list, zero value, non-integer, or invalid type."
        )

    # Step 2: Initialize result with the first element
    current_gcd = elements[0]

    # Step 3 & 4: Iterate through the rest of the elements
    for index in range(1, len(elements)):
        next_element = elements[index]

        # Calculate GCD of current accumulated GCD and the new element
        current_gcd = _calculate_pairwise_gcd(current_gcd, next_element)

        # Optimization: If GCD becomes 1, it cannot get any smaller (for positive integers)
        if current_gcd == 1:
            break

    # Step 5: Return the final result
    return current_gcd