def is_undulating(number_str: str) -> bool:
    """
    Determines if a given string of digits represents an undulating number.
    An undulating number is defined by the pattern where each digit is 
    different from its immediate neighbors, and the sequence of digits 
    oscillates (e.g., low-high-low-high or high-low-high-low).

    Specifically, for any three consecutive digits (a, b, c), 
    the middle digit 'b' must be either strictly greater than both 'a' 
    and 'c', or strictly less than both 'a' and 'c'.

    Args:
        number_str (str): A string of digits.

    Returns:
        bool: True if the string is undulating, False otherwise.

    Raises:
        ValueError: If the input is not a string or contains non-digit characters.
        TypeError: If the input is None.
    """
    # --- Input Validation ---
    if number_str is None:
        raise TypeError("Input must be a string, not None.")

    if not isinstance(number_str, str):
        raise ValueError("Input must be a string.")

    if not number_str.isdigit():
        # Handle empty string or non-numeric characters
        if number_str == "":
            return False
        raise ValueError("Input string must contain only digits.")

    # --- Edge Case Handling ---
    # An undulating sequence requires at least 3 digits to establish a pattern.
    # However, by common convention:
    # 1 digit: vacuously true as there are no neighbors to violate the rule.
    # 2 digits: true if the two digits are not equal.
    # 3+ digits: must strictly oscillate.

    length = len(number_str)

    if length == 0:
        return False

    if length == 1:
        return True

    if length == 2:
        digit_one = int(number_str[0])
        digit_two = int(number_str[1])
        # Must not be the same digit to be "undulating"
        return digit_one != digit_two

    # --- Main Logic ---
    # We iterate through the string and check every triplet of consecutive digits.
    # For a string of length N, there are N-2 triplets.

    for i in range(length - 2):
        # Extract current triplet
        val_a = int(number_str[i])
        val_b = int(number_str[i + 1])
        val_c = int(number_str[i + 2])

        # Rule 1: No two adjacent digits can be equal.
        # (This is covered by the oscillation check, but made explicit for clarity).
        if val_a == val_b or val_b == val_c:
            return False

        # Rule 2: The sequence must oscillate.
        # This means val_b must be a "peak" or a "valley".
        is_peak = (val_b > val_a) and (val_b > val_c)
        is_valley = (val_b < val_a) and (val_b < val_c)

        if not (is_peak or is_valley):
            # If it is neither a peak nor a valley, the sequence is not undulating.
            # For example, "123" (increasing) or "321" (decreasing) or "122" (plateau).
            return False

    return True