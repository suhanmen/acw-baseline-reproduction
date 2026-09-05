from typing import Union

def closest_num(n: Union[int, float]) -> Union[int, float]:
    """
    Finds the closest smaller number than n.

    In the context of integers, this is typically n - 1.
    In the context of real numbers, 'closest' is subjective unless 
    a step size is defined; however, based on the provided assertions, 
    the intended behavior is to subtract 1 from the input.

    Args:
        n (Union[int, float]): The number to find the predecessor for.

    Returns:
        Union[int, float]: The number immediately smaller than n.

    Raises:
        TypeError: If the input is not an integer or a float.
        ValueError: If the input is not provided or is invalid.
    """
    # Step 1: Validate input type
    # We allow int and float as they are the standard numeric types.
    if not isinstance(n, (int, float)):
        raise TypeError(
            f"Input must be an integer or a float. Received: {type(n).__name__}"
        )

    # Step 2: Handle NaN (Not a Number) case
    # floats can be NaN, which doesn't have a "smaller" number in a useful way.
    if isinstance(n, float) and n != n:  # Standard check for NaN
        raise ValueError("Input cannot be NaN.")

    # Step 3: Define the logic for "closest smaller"
    # Based on the test cases:
    # 11 -> 10
    # 7  -> 6
    # 12 -> 11
    # The pattern is a decrement of 1.

    # We define the decrement value explicitly.
    decrement_value = 1

    # Step 4: Calculate the result
    # We explicitly perform the subtraction.
    result = n - decrement_value

    # Step 5: Final Return
    # We return the result, preserving the type (int stays int, float stays float).
    return result

# Explicit test assertions to verify behavior
if __name__ == "__main__":
    # These assertions ensure the code meets the requirements provided in the prompt.
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11