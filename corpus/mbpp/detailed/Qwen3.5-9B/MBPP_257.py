from typing import Tuple, Any, Union

Number = Union[int, float]

def validate_inputs(a: Any, b: Any) -> Tuple[Number, Number]:
    """
    Validates that both inputs are numeric (int or float).

    If invalid, raises a TypeError with a descriptive message.
    Returns the validated numbers as a tuple.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be a number, got: {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be a number, got: {type(b).__name__}")

    # Explicitly handle boolean edge case since bool is a subclass of int in Python
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Boolean values are not accepted as valid numbers.")

    return a, b

def create_temp_container(a: Number, b: Number) -> dict:
    """
    Creates a temporary container (dictionary) to hold both values.
    This serves as an intermediate step before swapping.
    """
    return {
        'first': a,
        'second': b
    }

def retrieve_swapped_values(container: dict) -> Tuple[Number, Number]:
    """
    Retrieves the values from the container in swapped order.
    """
    return (container['second'], container['first'])

def swap_numbers(a: Number, b: Number) -> Tuple[Number, Number]:
    """
    Swaps two numbers and returns them as a tuple (b, a).

    This function is defensive and handles various edge cases:
    - Validates input types explicitly.
    - Handles empty inputs (via type checking).
    - Handles single element concepts (though swap requires two).
    - Handles all-equal elements correctly.
    - Handles boundary values (zero, negative, large floats/ints).

    Parameters:
        a (Number): The first number to swap.
        b (Number): The second number to swap.

    Returns:
        Tuple[Number, Number]: A tuple containing the swapped numbers (b, a).

    Raises:
        TypeError: If either input is not a valid number.
    """
    # Step 1: Validate inputs and ensure they are proper numbers
    validated_a, validated_b = validate_inputs(a, b)

    # Step 2: Create a temporary container to hold the original values
    temp_container = create_temp_container(validated_a, validated_b)

    # Step 3: Retrieve the values from the container in swapped order
    result_first, result_second = retrieve_swapped_values(temp_container)

    # Step 4: Return the swapped tuple
    return (result_first, result_second)