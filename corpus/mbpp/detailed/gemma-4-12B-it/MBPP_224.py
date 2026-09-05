import typing

def count_Set_Bits(n: int) -> int:
    """
    Counts the number of set bits (1s) in the binary representation 
    of a given integer.

    Args:
        n (int): The integer to analyze.

    Returns:
        int: The total count of set bits.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative integer (as bitwise 
                    representations of negative numbers vary by system).
    """
    # Validate that the input is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received: {type(n).__name__}")

    # Handle negative numbers. 
    # Since the problem involves standard bit counting (usually for unsigned/positive),
    # we raise a ValueError for negative numbers to ensure deterministic behavior.
    if n < 0:
        raise ValueError("This function is designed for non-negative integers.")

    # Handle the edge case of zero
    if n == 0:
        return 0

    # Use the Brian Kernighan's Algorithm to count set bits.
    # This algorithm is more efficient than iterating through every bit 
    # because it only loops as many times as there are set bits.

    count: int = 0

    # We create a temporary variable to avoid mutating the input directly 
    # (though integers are immutable in Python, it's good practice for clarity).
    current_number: int = n

    while current_number > 0:
        # This operation clears the least significant set bit.
        # Example: 6 (110) & 5 (101) = 4 (100)
        # The expression (n & (n - 1)) flips the rightmost set bit to 0.
        clear_last_set_bit = current_number & (current_number - 1)

        # Update the current_number to the value after clearing the bit.
        current_number = clear_last_set_bit

        # Increment the counter for every bit we cleared.
        count += 1

    return count

# The problem requires these specific assertions to pass:
if __name__ == "__main__":
    # These are provided in the prompt requirements.
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2