from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Defensive check: ensure the input is actually a list
    if not isinstance(values, list):
        raise TypeError(f"Expected input type 'list', but received '{type(values).__name__}'")

    # Handle empty list case explicitly
    if not values:
        return []

    result_list: List[int] = []

    for item in values:
        # We use isinstance(item, int) to check for the integer type.
        # Note: In Python, bools are subclasses of int (True == 1, False == 0).
        # The docstring examples suggest filtering for standard integers.
        # If bools should be excluded, an additional check is required.
        # Based on standard "filter integers" logic, we check type strictly
        # to avoid including booleans if the goal is specifically numeric integers.

        is_type_integer = isinstance(item, int)
        is_boolean = isinstance(item, bool)

        # Filter logic: must be an int, but not a boolean
        if is_type_integer and not is_boolean:
            result_list.append(item)
        else:
            # Item is either not an int (string, float, dict, etc.)
            # or it is a boolean which we skip.
            continue

    return result_list

# Note on Booleans: 
# If the requirement specifically allows Booleans (since they are technically 
# integers in Python), the 'not is_boolean' check should be removed.
# However, in production systems, 'filter_integers' usually intends 
# to extract whole numbers, not truth values.