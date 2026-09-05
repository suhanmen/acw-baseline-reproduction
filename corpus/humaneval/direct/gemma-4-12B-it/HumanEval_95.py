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

    # Check if all keys are strings
    for key in keys:
        if not isinstance(key, str):
            return False

    # Check if all keys are lowercase
    all_lower = True
    for key in keys:
        if not key.islower():
            all_lower = False
            break

    # Check if all keys are uppercase
    all_upper = True
    for key in keys:
        if not key.isupper():
            all_upper = False
            break

    # Special case for single character keys like "a" or "A"
    # islower() and isupper() return False for non-alphabetic strings like "1"
    # But the logic should hold that they are either all lowercase or all uppercase.
    # The prompt implies alphabetic behavior for "lower case" vs "upper case".

    # Re-evaluating the prompt examples:
    # "Name" -> False. "a" -> True. "STATE" -> True.
    # If all keys are strings and are all lowercase (islower) OR all uppercase (isupper).

    # Let's refine: a key must be purely lowercase or purely uppercase.
    # If a key is "1", it is neither lower nor upper.

    # Check if every key is strictly lowercase
    is_all_lower = all(isinstance(k, str) and k.islower() for k in keys)
    # Check if every key is strictly uppercase
    is_all_upper = all(isinstance(k, str) and k.isupper() for k in keys)

    # However, some keys might be strings but not have case (e.g. "123").
    # The example {"a":"apple", "b":"banana"} -> True.
    # "a".islower() is True. "b".islower() is True.

    # If there's a mix of cases or non-alphabetic strings that don't satisfy one of the two:
    # Let's use the logic: Every key must satisfy k == k.lower() (all lower)
    # OR every key must satisfy k == k.upper() (all upper).

    all_lower_strict = all(isinstance(k, str) and k == k.lower() and k.islower() for k in keys)
    all_upper_strict = all(isinstance(k, str) and k == k.upper() and k.isupper() for k in keys)

    # The example {"a":"apple", "b":"banana"} works with .islower()
    # The example {"Name":"John"...} returns False because "Name" is neither all lower nor all upper.

    # Let's try the most direct interpretation of the rules:
    # 1. All keys must be strings.
    # 2. All keys must be lower case OR all keys must be upper case.

    all_strings = all(isinstance(k, str) for k in keys)
    if not all_strings:
        return False

    is_lower = all(k.islower() for k in keys)
    is_upper = all(k.isupper() for k in keys)

    return is_lower or is_upper