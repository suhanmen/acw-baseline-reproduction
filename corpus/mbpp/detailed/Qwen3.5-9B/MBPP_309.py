def maximum(a, b):
    """
    Determine the maximum of two numeric values.

    This function validates that both inputs are numeric (int or float),
    handles edge cases (equality, negatives, etc.), and returns the larger value.
    It avoids using built-in 'max()' to demonstrate explicit control flow.

    Parameters:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The greater of the two input numbers.

    Raises:
        TypeError: If either 'a' or 'b' is not a number (int or float).
    """
    # Step 1: Validate input 'a'
    if not isinstance(a, (int, float)):
        raise TypeError(f"Invalid input 'a': expected a number (int or float), got {type(a).__name__}")

    # Step 2: Validate input 'b'
    if not isinstance(b, (int, float)):
        raise TypeError(f"Invalid input 'b': expected a number (int or float), got {type(b).__name__}")

    # Step 3: Compare the two values using explicit logic
    # We check if 'a' is greater than 'b'.
    if a > b:
        result = a
    # We check if 'b' is greater than 'a'.
    elif b > a:
        result = b
    # If neither is greater, they are equal. We return either value.
    else:
        result = a

    # Step 4: Return the determined maximum value
    return result