import re
from typing import Union

def _is_non_empty_string(value: Union[str, int, float]) -> bool:
    """Check if the input is a non-empty string after conversion attempts."""
    if isinstance(value, str) and len(value) > 0:
        return True
    return False

def _validate_string_representation(value: Union[str, int, float]) -> tuple[bool, str]:
    """
    Validate that the input can be represented as a non-empty string of digits.
    Returns (is_valid, error_message).
    """
    # If it's already a string, ensure it's not empty
    if isinstance(value, str):
        if len(value) == 0:
            return False, "Input string is empty."
        # Check for non-digit characters (except potentially a leading minus for negatives, but numbers aren't undulating)
        if value != value.strip():
            return False, "Input string contains leading or trailing whitespace."
        if not value.isdigit():
            return False, "Input string contains non-digit characters."
        # Handle negative numbers represented as strings: they are invalid for undulating checks
        if value.startswith('-'):
            return False, "Input string represents a negative number."
        return True, ""

    # If it's not a string, attempt to convert to string
    string_repr = str(value)

    # Check for empty string after conversion (e.g., empty string passed as arg isn't possible via str() unless input was empty string which is handled above)
    if len(string_repr) == 0:
        return False, "Converted input string is empty."

    # Check for non-digit characters
    if not string_repr.isdigit():
        return False, f"Input {value} contains non-digit characters or is negative."

    # Handle negative numbers converted from int/float
    if string_repr.startswith('-'):
        return False, f"Input {value} represents a negative number."

    return True, ""

def _check_single_digit(string_value: str) -> bool:
    """
    Check if the string consists of a single digit.
    A single digit is not undulating by definition (needs at least 2 distinct repeating patterns or at least 3 digits to form a pattern like aba or abc... wait, standard definition usually requires at least 3 digits for a pattern to be recognizable, or specifically length >= 2 with alternating digits).
    Let's refine based on standard definitions: 
    An undulating number has two alternating digits (e.g., 121, 12321 is oscillating? No, usually just two distinct digits).
    Actually, 121 is 1, 2, 1. 
    1212121 is 1, 2, 1, 2, 1, 2, 1.
    12321 is NOT undulating (3 distinct digits).
    11 is not undulating (only one distinct digit, no alternation).

    Therefore, length must be >= 3 to form a minimum pattern like "aba".
    If length < 3, return False.
    """
    return len(string_value) < 3

def _check_unique_digits(string_value: str) -> bool:
    """
    Ensure the number has exactly two unique digits.
    An undulating number must alternate between two specific digits.
    If there are more than 2 unique digits, it cannot be undulating.
    If there is only 1 unique digit (e.g., 111), it is not undulating.
    """
    unique_digits = set(string_value)

    if len(unique_digits) != 2:
        return False
    return True

def _verify_alternating_pattern(string_value: str) -> bool:
    """
    Verify that the digits strictly alternate between the two unique digits found.
    For example: "12121" -> d0='1', d1='2'. Next must be '1', then '2', etc.
    Or: "12321" -> d0='1', d1='2', d2='3' (fails unique check anyway, but this adds robustness).

    Logic:
    First digit is D1.
    Second digit is D2.
    Third digit must be D1.
    Fourth digit must be D2.
    And so on.
    """
    # We already checked length >= 3 and exactly 2 unique digits.

    digit_0 = string_value[0]
    digit_1 = string_value[1]

    # If the first two digits are the same (e.g., "112..."), it breaks the immediate alternation for undulating.
    # Undulating definition implies d[0] != d[1].
    if digit_0 == digit_1:
        return False

    # Iterate through the rest of the string starting from index 2
    for i in range(2, len(string_value)):
        if i % 2 == 0:
            # Even indices (0, 2, 4...) should match digit_0
            # Index 0 is base case, so check 2, 4...
            if string_value[i] != digit_0:
                return False
        else:
            # Odd indices (1, 3, 5...) should match digit_1
            # Index 1 is base case, so check 3, 5...
            if string_value[i] != digit_1:
                return False

    return True

def is_undulating(number: Union[str, int, float]) -> bool:
    """
    Checks whether the given number is undulating or not.

    An undulating number is a positive integer that has two alternating digits.
    Examples:
    - 121 (1, 2, 1) -> True
    - 1212121 (1, 2, 1, 2, 1...) -> True
    - 1991 (1, 9, 9, 1) -> False (9, 9 is not alternating)
    - 12321 -> False (three unique digits)
    - 11 -> False (only one unique digit, no alternation)

    Args:
        number: The input to check. Can be an integer, float, or string.

    Returns:
        True if the number is undulating, False otherwise.
    """

    # Step 1: Validate the input.
    # We accept strings directly or convert numbers to strings.
    # We must reject empty strings, strings with non-digits, and negative numbers.

    is_valid_input, error_msg = _validate_string_representation(number)
    if not is_valid_input:
        # Explicit handling of validation failure
        # Although the problem asks to check if it's undulating, 
        # production code should handle invalid inputs gracefully or explicitly.
        # Given the assertion style in the prompt, we assume valid inputs or explicit False for invalid.
        # However, "explicitly deal with invalid ones" suggests we should return False or handle it.
        # Since the problem implies a boolean check on the property of a number, 
        # and negative/empty inputs don't possess this property, returning False is appropriate.
        return False

    string_value = str(number)

    # Step 2: Check for trivial cases (length).
    # An undulating number must have at least 3 digits to show a pattern (aba).
    # e.g., length 1: '5' -> False
    # e.g., length 2: '12' -> True or False? 
    #   Standard definition: "An undulating number is a positive integer that has two alternating digits."
    #   Usually implies pattern like 121. 
    #   Let's check the provided examples:
    #   "121" -> True (length 3)
    #   "1212121" -> True (length 7)
    #   "1991" -> False
    #   There is no example for length 2. 
    #   MathWorld or general consensus: "Undulating" usually refers to numbers like 121, 12321 (though 12321 has 3 digits alternating 1,2,3? No, that's oscillating).
    #   Strictly, undulating has TWO alternating digits.
    #   If input is "12", does it alternate? Yes, 1 then 2. But is it a number?
    #   Let's stick to the strongest interpretation: Pattern must repeat or complete a cycle?
    #   Actually, most definitions say "at least 3 digits". 
    #   Let's assume length < 3 returns False to be safe against single digits and pairs which lack a "cycle".
    #   Wait, if I have "12", is it undulating? 
    #   If the definition is "digits alternate", then 12 alternates. 
    #   However, the pattern must be consistent. 
    #   Let's look at "12321". This is "oscillating" or "palindromic with peak", but not undulating with TWO digits.
    #   Let's rely on the "two unique digits" and "alternating" logic.
    #   If length is 2, e.g. "12": Unique={1,2}. d0=1, d1=2. Loop range(2, 2) is empty. Returns True.
    #   Is "12" undulating? 
    #   Common puzzles usually require odd length for 'aba' or just the alternating property.
    #   Given "121" is True, let's assume "12" might be False because it's not a full undulating pattern (often defined as n >= 3).
    #   Let's enforce length >= 3.
    if len(string_value) < 3:
        return False

    # Step 3: Check for the number of unique digits.
    # Must be exactly 2.
    # Example: "111" -> 1 unique -> False.
    # Example: "123" -> 3 unique -> False.
    if not _check_unique_digits(string_value):
        return False

    # Step 4: Verify the strict alternating pattern.
    # Example: "121" -> 1, 2, 1. Matches d0, d1, d0. -> True.
    # Example: "1991" -> 1, 9, 9. 
    #   d0=1, d1=9. 
    #   i=2: expects 1, gets 9. Fail. -> False.
    if not _verify_alternating_pattern(string_value):
        return False

    # If all checks pass, it is undulating.
    return True