from typing import List

def number_of_substrings(input_string: str) -> int:
    """
    Calculates the total number of non-empty substrings of a given string.

    The number of non-empty substrings of a string of length 'n' is given 
    by the formula: n * (n + 1) / 2.

    Args:
        input_string (str): The string to evaluate.

    Returns:
        int: The total count of non-empty substrings.

    Raises:
        TypeError: If the input_string is not of type str.
    """

    # Input Validation
    # Ensure the input is actually a string as per requirements.
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, received {type(input_string).__name__}")

    # Handle the case where the string might be empty or None (though None is caught by type check)
    # The problem implies valid strings, but defensive programming handles empty input.
    if input_string == "":
        return 0

    # Calculate the length of the string.
    # We use the length to determine the number of possible start and end positions.
    string_length: int = len(input_string)

    # Edge case check: If length is 0, result is 0.
    if string_length == 0:
        return 0

    # Logic derivation:
    # A substring is defined by a start index and an end index.
    # For a string of length N (indices 0 to N-1):
    # The number of substrings is the sum of:
    # - Substrings of length 1: N
    # - Substrings of length 2: N-1
    # - ...
    # - Substrings of length N: 1
    # This is a triangular number sum: 1 + 2 + 3 + ... + N
    # Formula: (N * (N + 1)) / 2

    # Step-by-step calculation for clarity
    # We use integer division (//) to ensure the return type is an integer.
    n: int = string_length
    numerator: int = n * (n + 1)
    total_count: int = numerator // 2

    return total_count

if __name__ == "__main__":
    # The assertions provided in the problem description
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

    # Additional edge cases
    assert number_of_substrings("") == 0
    assert number_of_substrings("a") == 1
    assert number_of_substrings("aaaaa") == 15