from typing import List, Any
from numbers import Number

def _validate_single_element(value: Any) -> bool:
    """
    Helper function to validate that a single element is a numeric type 
    that supports exponentiation.

    Args:
        value: The element to validate.

    Returns:
        bool: True if the value is valid, False otherwise.
    """
    return isinstance(value, Number) and not isinstance(value, bool)

def _cube_number(value: Number) -> Number:
    """
    Helper function to compute the cube of a single numeric element.

    Args:
        value: A numeric value.

    Returns:
        Number: The cube of the value (value ** 3).
    """
    return value ** 3

def cube_nums(input_list: List[Any]) -> List[Number]:
    """
    Computes the cube of each individual element in the input list.

    This function iterates through the provided list, validates each element
    to ensure it is numeric, and calculates its cube using a lambda function
    as required by the problem statement. It handles edge cases such as empty
    lists, single elements, lists with all equal elements, zero, negative numbers,
    and explicitly rejects non-numeric inputs.

    Args:
        input_list: A list of numeric elements to be cubed.

    Returns:
        List[Number]: A new list containing the cubes of the input elements.

    Raises:
        TypeError: If the input is not a list or if any element is not a number.
    """

    # Step 1: Validate the outer container type.
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    # Step 2: Initialize an empty list to store the results.
    result_list: List[Number] = []

    # Step 3: Define the lambda function as required.
    # The lambda takes a single argument 'x' and returns x raised to the power of 3.
    cube_lambda = lambda x: x ** 3

    # Step 4: Iterate through each element in the input list explicitly.
    for current_element in input_list:

        # Step 5: Validate the current element type explicitly.
        # We check if it is an instance of Number.
        # Note: In Python, bool is a subclass of int, so we must exclude it explicitly
        # if we do not want booleans to be treated as numbers.
        if not _validate_single_element(current_element):
            raise TypeError(f"All elements must be numeric. Found invalid type: {type(current_element).__name__} with value: {current_element}")

        # Step 6: Apply the lambda function to the validated element.
        cubed_value = cube_lambda(current_element)

        # Step 7: Append the resulting cube to the result list.
        result_list.append(cubed_value)

    # Step 8: Return the final list of cubes.
    return result_list