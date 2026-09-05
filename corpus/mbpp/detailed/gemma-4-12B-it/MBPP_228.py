from typing import Any

def _validate_inputs(number: int, start_bit: int, end_bit: int) -> None:
    """
    Validates that the input types are integers and the bit range is logical.

    Args:
        number: The integer to check.
        start_bit: The starting bit position (0-indexed).
        end_bit: The ending bit position (0-indexed).

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If bit indices are negative or start is greater than end.
    """
    if not isinstance(number, int):
        raise TypeError(f"Input 'number' must be an integer, got {type(number).__name__}")
    if not isinstance(start_bit, int):
        raise TypeError(f"Input 'start_bit' must be an integer, got {type(start_bit).__name__}")
    if not isinstance(end_bit, int):
        raise TypeError(f"Input 'end_bit' must be an integer, got {type(end_bit).__name__}")

    if start_bit < 0:
        raise ValueError("Bit index 'start_bit' cannot be negative.")
    if end_bit < 0:
        raise ValueError("Bit index 'end_bit' cannot be negative.")
    if start_bit > end_bit:
        raise ValueError("The 'start_bit' must be less than or equal to 'end_bit'.")

def all_Bits_Set_In_The_Given_Range(number: int, start_bit: int, end_bit: int) -> bool:
    """
    Checks whether all the bits in the specified range [start_bit, end_bit] 
    are SET (equal to 1) in the given number.

    The range is inclusive. For example, if start_bit is 2 and end_bit is 4,
    it checks bits 2, 3, and 4.

    Args:
        number (int): The integer whose bits are to be checked.
        start_bit (int): The starting bit position (0-indexed).
        end_bit (int): The ending bit position (0-indexed).

    Returns:
        bool: True if all bits in the range are set, False otherwise.
    """
    # Validate inputs to ensure they are integers and the range is valid.
    _validate_inputs(number, start_bit, end_bit)

    # If the range is null or invalid (though handled by validation),
    # logic suggests checking if a condition exists. 
    # However, standard range behavior implies we check bits from start to end.

    # Step 1: Calculate the number of bits in the range.
    # Since the range is inclusive, the count is (end_bit - start_bit + 1).
    num_bits_in_range = end_bit - start_bit + 1

    # Step 2: Create a mask that has 1s in the specified range and 0s elsewhere.
    # We start with 1s for the length of the range.
    # Example: if num_bits_in_range is 3, range_mask_base will be 0b111 (7).
    range_mask_base = (1 << num_bits_in_range) - 1

    # Step 3: Shift the mask to the correct starting position.
    # Example: if start_bit is 2 and num_bits_in_range is 3, 
    # the mask becomes 0b11100 (28).
    final_mask = range_mask_base << start_bit

    # Step 4: Isolate the bits in the given range from the input number using bitwise AND.
    # This keeps only the bits present in the range.
    bits_in_range = number & final_mask

    # Step 5: Verify if all bits in that range are set.
    # If all bits in the range are set, the result of 'bits_in_range' 
    # must be exactly equal to 'final_mask'.
    # If any bit in that range was 0, 'bits_in_range' will be less than 'final_mask'.
    all_set = (bits_in_range == final_mask)

    return all_set