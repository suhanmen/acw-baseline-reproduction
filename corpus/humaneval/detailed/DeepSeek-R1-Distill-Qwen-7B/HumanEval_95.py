def check_dict_case(dict):
    if not dict:  # Check if the dictionary is empty
        return False

    # Check if all keys are strings and determine their case
    key_cases = []
    for key in dict:
        if not isinstance(key, str):  # If key is not a string, return False
            return False
        if key.islower():
            key_cases.append('lower')
        elif key.isupper():
            key_cases.append('upper')
        else:
            # Keys are numbers or other types which are not strings
            return False

    # Check if all keys are either lower or upper
    if not key_cases:  # This can only happen if the dict has at least one key, which is checked earlier
        return False
    all_lower = all(kc == 'lower' for kc in key_cases)
    all_upper = all(kc == 'upper' for kc in key_cases)

    return all_lower or all_upper