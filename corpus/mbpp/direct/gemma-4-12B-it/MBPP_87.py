def merge_dictionaries_three(dict1, dict2, dict3):
    """
    Merges three dictionaries into a single dictionary.
    If a key exists in multiple dictionaries, the value from the earliest 
    dictionary takes precedence, except in the specific test case behavior 
    where 'B' in dict1 overrides 'B' in dict2 and dict3.

    Looking closely at the provided assertions:
    1. {R:Red, B:Black, P:Pink}, {G:Green, W:White}, {O:Orange, W:White, B:Black}
       Result: {B:Black, R:Red, P:Pink, G:Green, W:White, O:Orange}
       -> 'B' is Black (from dict1). 'W' is White (from dict2).
    2. {R:Red, B:Black, P:Pink}, {L:lavender, B:Blue}, {G:Green, W:White}
       Result: {W:White, P:Pink, B:Black, R:Red, G:Green, L:lavender}
       -> 'B' is Black (from dict1). 'L' is lavender (from dict2). 'W' is White (from dict3).

    In all cases, the result contains keys from all three. 
    The value for a duplicate key is taken from the dictionary that appeared first 
    in the arguments list.
    """
    # Create a new dictionary to store the merged result.
    # By iterating in order and only adding if key is not present,
    # we preserve the first occurrence of any key.
    merged = {}

    for d in [dict1, dict2, dict3]:
        for key, value in d.items():
            if key not in merged:
                merged[key] = value

    return merged