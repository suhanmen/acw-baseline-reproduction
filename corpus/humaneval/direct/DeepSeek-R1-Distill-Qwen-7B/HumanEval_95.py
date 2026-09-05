def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    if not dict:
        return False
    # Get all keys to check
    keys = dict.keys()
    # Check if all string keys are lowercase or all are uppercase
    # Find the case of the first string key
    first_str_key = None
    for key in keys:
        if isinstance(key, str):
            first_str_key = key
            break
    if not first_str_key:
        # No string keys found
        return True
    # Determine the case of the first string key
    if first_str_key.islower():
        # Check if all string keys are lowercase
        for key in keys:
            if isinstance(key, str) and not key.islower():
                return False
        return True
    elif first_str_key.isupper():
        # Check if all string keys are uppercase
        for key in keys:
            if isinstance(key, str) and not key.isupper():
                return False
        return True
    else:
        # The first string key is neither lower nor upper (unlikely as per problem constraints)
        return False