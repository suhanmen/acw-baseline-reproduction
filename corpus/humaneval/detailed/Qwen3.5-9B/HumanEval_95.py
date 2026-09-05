from typing import Any, Dict

def _is_string_key(key: Any) -> bool:
    """
    Helper function to check if a given key is a string instance.
    Returns False if the key is not a string (e.g., int, float, None, etc.).
    """
    if key is None:
        return False
    if not isinstance(key, str):
        return False
    return True

def _is_all_lower_case(s: str) -> bool:
    """
    Helper function to check if a given string consists entirely of lowercase characters.
    Returns False if the string contains any uppercase or non-alphabetic characters that are not lowercase.
    However, the problem implies checking if all keys are strictly lower case letters.
    The examples suggest that keys like "a" are lower, "A" are upper.
    We interpret "lower case" as s.lower() == s and "upper case" as s.upper() == s.
    This handles mixed alphabets correctly (e.g., "hello" is lower, "HELLO" is upper).
    """
    return s.lower() == s

def _is_all_upper_case(s: str) -> bool:
    """
    Helper function to check if a given string consists entirely of uppercase characters.
    Similar logic to _is_all_lower_case but for uppercase.
    """
    return s.upper() == s

def _check_dict_case_inner(keys: list) -> bool:
    """
    Internal helper to determine the case consistency of a list of string keys.
    Returns a tuple: (is_all_lower, is_all_upper) or (False, False) if not all are strings.
    """
    all_lower = True
    all_upper = True

    for key in keys:
        if not _is_string_key(key):
            return (False, False)

        s = key

        # Check if the string is actually lower case
        # A string is considered "lower case" if it equals its lowercase version
        # And it shouldn't have any non-letter chars that break the expectation?
        # The problem statement examples imply simple casing checks.
        # "a" -> lower, "A" -> upper.
        # What about "a1"? "a1".lower() is "a1". "a1".upper() is "A1".
        # If the requirement is strict letters, we might need to filter.
        # But looking at "STATE" and "ZIP", they are all caps. "a", "b" are all low.
        # Let's assume the definition is simply: s == s.lower() and s == s.upper() is impossible for len>0 unless non-alpha exists?
        # No, "a" is lower. "A" is upper.
        # If we have "a1", is it lower? "a1" == "a1".lower() -> True.
        # Is it upper? "a1" == "a1".upper() -> False ("A1").
        # So "a1" is treated as lower case string in this context.

        is_current_lower = (s == s.lower())
        is_current_upper = (s == s.upper())

        if not is_current_lower:
            all_lower = False

        if not is_current_upper:
            all_upper = False

        # Optimization: If both are already false, we can stop early
        if not all_lower and not all_upper:
            return (False, False)

    return (all_lower, all_upper)

def check_dict_case(d: Dict[Any, Any]) -> bool:
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.

    Logic:
    1. If dictionary is empty, return False.
    2. Extract keys.
    3. Verify all keys are strings. If any key is not a string, return False.
    4. Check if all string keys are lowercase. If yes, return True.
    5. Check if all string keys are uppercase. If yes, return True.
    6. If neither condition is met, return False.
    """

    # Edge case: Empty dictionary
    if not d:
        return False

    # Extract keys into a list for iteration
    keys = list(d.keys())

    if len(keys) == 0:
        # This theoretically shouldn't happen after the 'if not d' check,
        # but explicit check for robustness.
        return False

    # Step 3: Validate that all keys are strings
    for key in keys:
        if not _is_string_key(key):
            return False

    # Step 4: Check if all keys are lowercase
    # We iterate once to determine the status of each key
    all_keys_lower = True
    for key in keys:
        s = key
        if s != s.lower():
            all_keys_lower = False
            break

    if all_keys_lower:
        return True

    # Step 5: Check if all keys are uppercase
    # We iterate once to determine the status of each key
    all_keys_upper = True
    for key in keys:
        s = key
        if s != s.upper():
            all_keys_upper = False
            break

    if all_keys_upper:
        return True

    # Step 6: Neither condition was met
    return False