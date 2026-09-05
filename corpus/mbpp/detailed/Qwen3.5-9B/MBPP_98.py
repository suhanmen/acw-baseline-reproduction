from typing import Union, Sequence, List
import math

def _validate_input(input_sequence: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    """
    Validates that the input is a sequence containing only numbers (int or float).
    Returns a new list with the valid numbers to ensure the main function remains pure.

    Parameters:
    input_sequence (Sequence): The input to be validated.

    Returns:
    List[Union[int, float]]: A list of validated numbers.

    Raises:
    ValueError: If the input is not a sequence or contains non-numeric elements.
    TypeError: If the input is not a sequence type.
    """
    if input_sequence is None:
        raise ValueError("Input sequence cannot be None.")

    # Ensure the input is a sequence but not a string (strings are sequences of chars)
    if not isinstance(input_sequence, (list, tuple)) or isinstance(input_sequence, str):
        if isinstance(input_sequence, str):
            raise TypeError("Input sequence cannot be a string.")
        raise TypeError(f"Input must be a list or tuple of numbers, got {type(input_sequence).__name__}.")

    validated_list = []
    for index, item in enumerate(input_sequence):
        if isinstance(item, bool):
            raise TypeError(f"Boolean values are not allowed at index {index}.")
        if not isinstance(item, (int, float)):
            raise TypeError(f"Element at index {index} ({item!r}) is not a number.")
        validated_list.append(item)

    return validated_list

def _compute_product(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Computes the product of all numbers in the list.
    Uses an explicit loop for clarity and control.

    Parameters:
    numbers (List[Union[int, float]]): List of numbers to multiply.

    Returns:
    Union[int, float]: The product of all elements.
    """
    if len(numbers) == 0:
        raise ValueError("Cannot compute product of an empty list.")

    product_result = 1
    for current_number in numbers:
        product_result *= current_number

    return product_result

def _compute_mean(numbers: List[Union[int, float]]) -> float:
    """
    Computes the arithmetic mean (average) of the numbers.
    This is equivalent to (product / length) ONLY IF the problem specifically asked for mean.
    HOWEVER, re-reading the prompt: "multiply all the numbers in a list and divide with the length of the list".
    The standard arithmetic mean is Sum / Length.
    The prompt explicitly says "multiply all the numbers" then "divide with the length".
    This is a specific operation: (Product / Length), not the standard Mean (Sum / Length).
    Let's stick strictly to the prompt's instruction: (Product / Length).

    Parameters:
    numbers (List[Union[int, float]]): List of numbers.

    Returns:
    float: The result of dividing the product of the numbers by their count.
    """
    if len(numbers) == 0:
        raise ValueError("Cannot divide by zero length list.")

    product_value = _compute_product(numbers)
    list_length = float(len(numbers))

    return product_value / list_length

def multiply_num(input_sequence: Union[List[Union[int, float]], tuple]) -> float:
    """
    Multiplies all the numbers in the input sequence and divides the result by the length of the sequence.

    Strictly follows the prompt: (Product of all numbers) / (Length of list).

    Examples based on prompt assertions:
    multiply_num((8, 2, 3, -1, 7)) 
       -> Product: 8*2*3*-1*7 = -336
       -> Length: 5
       -> Result: -336 / 5 = -67.2

    multiply_num((-10,-20,-30))
       -> Product: -10*-20*-30 = -6000
       -> Length: 3
       -> Result: -6000 / 3 = -2000.0

    multiply_num((19,15,18))
       -> Product: 19*15*18 = 5130
       -> Length: 3
       -> Result: 5130 / 3 = 1710.0

    Parameters:
    input_sequence: A list or tuple of integers or floats.

    Returns:
    float: The calculated value (Product / Length).

    Raises:
    ValueError: If the list is empty.
    TypeError: If elements are not numbers or input type is invalid.
    """
    # Step 1: Validate and normalize the input
    validated_numbers = _validate_input(input_sequence)

    # Step 2: Check for empty list after validation
    if len(validated_numbers) == 0:
        raise ValueError("The input list cannot be empty.")

    # Step 3: Compute the product of all numbers
    total_product = _compute_product(validated_numbers)

    # Step 4: Get the length of the list as a float to ensure division result is float
    sequence_length = float(len(validated_numbers))

    # Step 5: Perform the final division
    result_value = total_product / sequence_length

    return result_value