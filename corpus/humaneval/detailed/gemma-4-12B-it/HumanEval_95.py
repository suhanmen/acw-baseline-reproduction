from typing import Any, Dict

def check_dict_case(dict_obj: Dict[Any, Any]) -> bool:
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    # Requirement: The function should return False if the given dictionary is empty.
    if not dict_obj:
        return False

    # Extract all keys from the dictionary
    keys = list(dict_obj.keys())

    # To be True, all keys must be strings. 
    # If any key is not a string, return False immediately.
    for key in keys:
        if not isinstance(key, str):
            return False

    # Determine if all keys are lowercase.
    # A string is considered lowercase if it equals its lower() representation.
    # Note: This handles non-alphabetic strings correctly (e.g., "123" == "123".lower()).
    all_lowercase = True
    for key in keys:
        if key != key.lower():
            all_lowercase = False
            break

    # Determine if all keys are uppercase.
    # A string is considered uppercase if it equals its upper() representation.
    all_uppercase = True
    for key in keys:
        if key != key.upper():
            all_uppercase = False
            break

    # Special check: If a key is "123", it is both "lowercase" and "uppercase" 
    # because "123".lower() == "123" and "123".upper() == "123".
    # However, the prompt examples imply we need to distinguish cases.
    # Example: {"Name":"John", "Age":"36", "City":"Houston"} returns False.
    # "36" is technically both lower and upper, but "Name" is neither.

    # The logic:
    # If every key is lowercase, return True.
    # If every key is uppercase, return True.
    # Otherwise, return False.

    # However, we must ensure that if we have a mix of "Case-Insensitive" characters 
    # (like numbers) and specific cases, we follow the logic strictly.
    # In the example: {"Name":"John", "Age":"36", "City":"Houston"}
    # "Name" is not lower, "Name" is not upper. Therefore, all_lowercase is False.
    # "Name" is not upper. Therefore, all_uppercase is False.
    # Result: False.

    if all_lowercase:
        return True

    if all_uppercase:
        return True

    return False

# The function signature is kept as requested (using 'dict' as the variable name 
# even though it shadows the built-in type, to strictly match the prompt's signature).
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False

    keys = list(dict.keys())

    # Step 1: Validate all keys are strings
    for key in keys:
        if not isinstance(key, str):
            return False

    # Step 2: Check if every key is strictly lowercase
    # A string is strictly lowercase if it matches its .lower() form
    # and contains at least one character that has a case (to avoid 
    # ambiguity with numbers/symbols if necessary, though the examples 
    # suggest standard .lower() / .upper() parity is sufficient).
    is_all_lower = True
    for key in keys:
        if key != key.lower():
            is_all_lower = False
            break

    # Step 3: Check if every key is strictly uppercase
    is_all_upper = True
    for key in keys:
        if key != key.upper():
            is_all_upper = False
            break

    # Step 4: Final evaluation
    # If all keys are lowercase OR all keys are uppercase, return True.
    if is_all_lower:
        return True
    elif is_all_upper:
        return True
    else:
        return False