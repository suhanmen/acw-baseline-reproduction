def find_Parity(number: int) -> str:
    """
    Determines and returns the parity string for a given integer.

    The function checks whether the input number is even or odd and returns
    a corresponding string: "Even Parity" or "Odd Parity".

    Args:
        number (int): The integer to check for parity.

    Returns:
        str: Either "Even Parity" if the number is even, or "Odd Parity" if the number is odd.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is an integer but is not within expected numeric bounds
                    (though mathematically parity applies to all integers, this guards
                    against unexpected non-numeric types masquerading or very large values
                    if desired, but primarily handles type safety).
    """

    # Step 1: Validate the input type explicitly.
    # We ensure the input is strictly an integer.
    # In Python, booleans are a subclass of int, so we must explicitly exclude them
    # if we want strict integer behavior, or accept them. 
    # Given the problem context of "numbers", we will accept standard integers.
    # We will reject booleans to be defensive against common Python gotchas.
    if isinstance(number, bool):
        raise TypeError("Input must be an integer, not a boolean.")

    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, received type: {type(number).__name__}")

    # Step 2: Define the threshold check (optional but good for defensive coding context).
    # While parity is defined for all integers, we proceed assuming the input passes type check.
    # No range validation is strictly necessary for mathematical parity, 
    # but we acknowledge the input is now confirmed as a valid int.

    # Step 3: Determine the remainder when divided by 2.
    remainder = number % 2

    # Step 4: Compare the remainder to determine parity.
    if remainder == 0:
        # Case: The number is perfectly divisible by 2.
        parity_status = "Even Parity"
    else:
        # Case: The remainder is 1 (since modulo 2 on an int yields 0 or 1).
        # This covers negative odd numbers as well (e.g., -3 % 2 == 1 in Python).
        parity_status = "Odd Parity"

    # Step 5: Return the calculated status string.
    return parity_status