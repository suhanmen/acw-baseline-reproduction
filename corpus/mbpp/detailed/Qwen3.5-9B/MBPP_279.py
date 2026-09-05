def is_valid_input(n):
    """
    Validates the input n for the nth decagonal number function.

    The input n must be:
    - An integer (or a type that can be exactly represented as a Python int).
    - A positive integer (n >= 1), as decagonal numbers are defined for positive indices.

    Returns:
        bool: True if the input is valid, False otherwise.

    Raises:
        TypeError: If the input is not an integer or a convertible type.
        ValueError: If the integer value is not positive (n < 1).
    """
    # Step 1: Check if n is an integer.
    # We use isinstance to check for int, but explicitly exclude bool because
    # bool is a subclass of int in Python and True/False are technically 1/0.
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Step 2: Explicitly handle the boolean case to prevent True/False being accepted as 1/0.
    if isinstance(n, bool):
        raise TypeError(f"Input must be an integer, got bool")

    # Step 3: Check if the value is a positive integer.
    # Decagonal numbers are defined for n >= 1.
    if n < 1:
        raise ValueError(f"Input must be a positive integer (n >= 1), got {n}")

    return True


def calculate_decagonal_number(n):
    """
    Calculates the nth decagonal number using the explicit formula.

    The formula for the nth decagonal number is:
        D(n) = 4n^2 - 3n

    Parameters:
        n (int): A positive integer representing the position in the sequence.

    Returns:
        int: The nth decagonal number.
    """
    # Step 1: Calculate n squared.
    n_squared = n * n

    # Step 2: Multiply n squared by 4.
    term_one = 4 * n_squared

    # Step 3: Multiply n by 3.
    term_two = 3 * n

    # Step 4: Subtract term_two from term_one to get the result.
    decagonal_value = term_one - term_two

    return decagonal_value


def is_num_decagonal(n):
    """
    Finds the nth decagonal number with full input validation and explicit logic.

    This function serves as the main entry point. It validates the input strictly
    and then computes the result using a dedicated helper function.

    Parameters:
        n (int): The position (1-indexed) of the decagonal number to find.

    Returns:
        int: The nth decagonal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not a positive integer.
    """
    # Step 1: Validate the input explicitly.
    is_valid_input(n)

    # Step 2: Compute and return the decagonal number.
    return calculate_decagonal_number(n)