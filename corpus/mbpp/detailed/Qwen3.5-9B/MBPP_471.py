from typing import List, Tuple, Union

Number = Union[int, float]
ModuloResult = Tuple[Number, Number]


def validate_array(arr: List[Number]) -> None:
    """
    Validates that the input array is not empty and contains only numeric values.

    :param arr: The input list to validate.
    :raises ValueError: If the array is empty or contains non-numeric elements.
    """
    if not arr:
        raise ValueError("Input array cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements in the array must be numeric (int or float).")


def validate_modulo(n: Number) -> None:
    """
    Validates the modulo divisor n.

    :param n: The divisor n.
    :raises ValueError: If n is not a number, zero, or negative.
    """
    if not isinstance(n, (int, float)):
        raise ValueError("Modulo n must be a number.")

    if n == 0:
        raise ValueError("Modulo n cannot be zero.")

    if n < 0:
        raise ValueError("Modulo n must be non-negative.")


def calculate_partial_product_index(index: int, array: List[Number]) -> Number:
    """
    Calculates the product of the array up to the given index (exclusive).
    This is a helper to demonstrate explicit step-by-step logic for the multiplication process.
    However, for efficiency in the main logic, we will use the standard iterative approach.

    :param index: The current index being processed.
    :param array: The list of numbers.
    :return: The product of elements from 0 to index-1.
    """
    product = 1.0
    current_index = 0

    while current_index < index:
        current_value = array[current_index]
        product = product * current_value
        current_index += 1

    return product


def compute_remainder(array: List[Number], array_size: int, modulo: Number) -> Number:
    """
    Computes the remainder of the product of all elements in the array divided by modulo.

    This function performs the multiplication step-by-step, applying the modulo operation
    at each step to prevent the intermediate product from growing too large (which could
    lead to inefficiency or overflow in languages with fixed-size integers, though Python
    handles large integers automatically). Applying modulo at each step is also a standard
    technique to keep numbers manageable.

    :param array: The list of numbers to multiply.
    :param array_size: The size of the array (included for validation consistency).
    :param modulo: The number to divide by at the end.
    :return: The remainder of the total product divided by modulo.
    """
    # Initialize the running product as 1.0 to handle both int and float inputs consistently.
    total_product = 1.0

    # Iterate through each element in the array explicitly.
    for current_index in range(array_size):
        current_element = array[current_index]

        # Multiply the running product by the current element.
        total_product = total_product * current_element

        # Apply modulo at each step to keep the number manageable.
        # This is valid because (a * b) % n == (((a % n) * (b % n)) % n).
        total_product = total_product % modulo

    return total_product


def find_remainder(input_array: List[Number], size: int, mod_val: Number) -> Number:
    """
    Main function to find the remainder of array multiplication divided by n.

    This function serves as the primary entry point. It handles input validation,
    checks for consistency between the provided size and the actual array length,
    and then delegates the calculation to the helper function.

    :param input_array: The list of numbers to be multiplied.
    :param size: The expected size of the array.
    :param mod_val: The divisor n.
    :return: The remainder of the product divided by n.
    :raises ValueError: If inputs are invalid or inconsistent.
    """
    # Step 1: Validate the input array content.
    validate_array(input_array)

    # Step 2: Validate the modulo divisor.
    validate_modulo(mod_val)

    # Step 3: Check for consistency between the provided size and the actual array length.
    actual_length = len(input_array)
    if actual_length != size:
        raise ValueError(f"Array length ({actual_length}) does not match provided size ({size}).")

    # Step 4: Handle edge case where modulo is 1.
    # Any integer modulo 1 is 0.
    if mod_val == 1:
        return 0

    # Step 5: Perform the calculation using the helper function.
    result = compute_remainder(input_array, actual_length, mod_val)

    return result