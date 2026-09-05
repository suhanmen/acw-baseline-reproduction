import typing

def _validate_integer_input(value: typing.Any) -> int:
    """
    Validates that the provided input is an integer.

    Args:
        value: The input to check.

    Returns:
        The integer value if valid.

    Raises:
        TypeError: If the input is not an instance of int.
    """
    if not isinstance(value, int):
        # We explicitly check for bool because bool is a subclass of int in Python,
        # but usually, we don't want True/False treated as 1/0 in strict math functions.
        if isinstance(value, bool):
            raise TypeError(f"Input must be an integer, but received {type(value).__name__}.")
        raise TypeError(f"Input must be an integer, but received {type(value).__name__}.")

    return value

def add(x: int, y: int) -> int:
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    # Step 1: Validate inputs strictly to ensure production-grade robustness.
    # This prevents unexpected behavior from floats or strings.
    validated_x = _validate_integer_input(x)
    validated_y = _validate_integer_input(y)

    # Step 2: Perform the addition.
    # Python handles arbitrarily large integers (bignums), 
    # so we don't need to worry about standard 32-bit or 64-bit overflow.
    result = validated_x + validated_y

    # Step 3: Return the final calculated value.
    return result