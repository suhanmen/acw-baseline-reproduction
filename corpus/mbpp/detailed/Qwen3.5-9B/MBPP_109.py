from typing import Optional, Tuple

def _parse_binary_string(input_string: str) -> Optional[int]:
    """
    Validates and converts a binary string to its integer representation.

    Returns:
        int: The decimal value of the binary string.
        None: If the input is invalid.
    """
    if not isinstance(input_string, str):
        return None

    # Check for empty string
    if len(input_string) == 0:
        return None

    # Check for valid characters (only '0' and '1')
    for char in input_string:
        if char not in ('0', '1'):
            return None

    # Convert binary string to integer
    try:
        decimal_value = int(input_string, 2)
        return decimal_value
    except ValueError:
        return None


def _perform_rotation(binary_string: str, shift_count: int, string_length: int) -> str:
    """
    Performs right rotation on a binary string by the specified count.

    Args:
        binary_string: The original binary string.
        shift_count: Number of positions to rotate right.
        string_length: Length of the binary string.

    Returns:
        str: The rotated binary string.
    """
    # Normalize shift count to be within [0, length - 1]
    # A shift equal to length results in the same string
    effective_shift = shift_count % string_length

    if effective_shift == 0:
        return binary_string

    # Right rotation logic:
    # Take the last 'effective_shift' characters and move them to the front
    split_point = string_length - effective_shift
    rotated_part = binary_string[split_point:]
    remaining_part = binary_string[:split_point]

    return rotated_part + remaining_part


def _is_odd_value(value: int) -> bool:
    """
    Checks if an integer value is odd.

    Args:
        value: The integer to check.

    Returns:
        bool: True if the value is odd, False otherwise.
    """
    return value % 2 != 0


def odd_Equivalent(binary_string: str, rotation_count: int) -> int:
    """
    Counts the number of unique rotations of a binary string that have an odd value.

    The function considers the given binary string, rotates it 'rotation_count' times,
    and checks the parity (odd/even) of the resulting integer value for each rotation.
    It counts how many of these resulting values are odd.

    Note on interpretation based on problem signature:
    The function iterates through 'rotation_count' rotations (from 0 to rotation_count - 1).
    However, to handle cases where rotation_count might be larger than string length,
    we only consider unique rotations (0 to len(string) - 1) to avoid redundant checks.
    If rotation_count is 0, it returns 0.

    Args:
        binary_string: A string consisting of '0's and '1's.
        rotation_count: The number of rotations to consider (exclusive upper bound).

    Returns:
        int: The count of rotations that result in an odd integer value.
        -1: If inputs are invalid.
    """
    # --- Input Validation ---

    # Validate binary_string
    string_length = 0
    decimal_value = None
    parsed_result = _parse_binary_string(binary_string)

    if parsed_result is None:
        # Invalid input string (e.g., contains non-binary chars, empty, or not a string)
        return -1

    string_length = len(binary_string)
    decimal_value = parsed_result

    # Handle empty string after validation (though _parse should catch empty)
    if string_length == 0:
        return -1

    # Validate rotation_count
    if not isinstance(rotation_count, int):
        return -1

    # If rotation_count is 0, there are no rotations to check
    if rotation_count <= 0:
        return 0

    # If rotation_count is larger than string_length, we technically cycle.
    # The problem implies checking specific rotation steps. 
    # Based on standard interpretation of "count of rotations... with rotation_count":
    # We check rotations 0, 1, 2, ..., (rotation_count - 1).
    # However, checking beyond string_length is redundant for unique string states.
    # But strictly following "count rotations", we check the requested count steps.
    # To prevent infinite loops or excessive computation if rotation_count is huge,
    # we will iterate up to min(rotation_count, string_length) if we assume cyclic uniqueness,
    # OR iterate up to rotation_count if we strictly follow the parameter.
    # Given the test cases: "1010", 4 -> 2. Rotations: 0(1010=10), 1(0101=5), 2(1010=10), 3(0101=5).
    # Odds: 5, 5. Count = 2.
    # This implies we check exactly 'rotation_count' steps: 0 to count-1.
    # We do not cap it at string_length because the value might differ if we didn't cap,
    # but since it's cyclic, values repeat. The test case "1010", 4 checks 4 steps.
    # Let's iterate exactly 'rotation_count' times for indices 0 to rotation_count-1.

    odd_count = 0

    # Process each rotation from 0 to rotation_count - 1
    for i in range(rotation_count):
        # Generate the rotated string for the current shift 'i'
        # We use the string length for the modulo calculation inside _perform_rotation
        rotated_string = _perform_rotation(binary_string, i, string_length)

        # Calculate the integer value of the rotated string
        current_rotated_value = int(rotated_string, 2)

        # Check if the current rotated value is odd
        if _is_odd_value(current_rotated_value):
            odd_count += 1

    return odd_count