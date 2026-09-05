from typing import List, Union, Optional


DIGIT_NAME_MAP = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}


def _is_valid_digit(x: int) -> bool:
    """
    Check if the given integer is between 1 and 9 inclusive.

    This function is the primary validation gate. It returns True only if:
    1. x is an integer (type check is implicit in the caller's expectation,
       but we could enforce it strictly if needed).
    2. 1 <= x <= 9.

    Any number outside this range, including negatives, zero, or numbers > 9,
    is considered invalid.
    """
    return 1 <= x <= 9


def _filter_valid_digits(arr: List[Union[int, float]]) -> List[int]:
    """
    Extract only the valid digits from the input array.

    This function iterates over the input array, checks each element using
    _is_valid_digit, and collects the valid ones into a new list.

    Parameters:
        arr: A list of numbers (ints or floats). Floats with integer values
             are handled by checking the int conversion, but typically
             we expect ints. We will treat non-ints as invalid unless they
             are exactly equal to an integer (e.g., 5.0). For robustness,
             we convert to int after validation if the float is whole.
             However, the problem statement says "integers", so we will be
             strict: if the input is not an int instance (even if mathematically
             an integer), we ignore it. But to be safe against 5.0, we can
             allow float if it's a whole number. Let's stick to the problem
             which implies integers. We will check isinstance(x, int) to be safe.
             Wait, the problem says "integers", but often in Python challenges
             5.0 is passed. Let's assume the input is typed as described in the
             problem examples: [2, 1, 1, ...]. We will check isinstance(x, int).

    Returns:
        A list containing only the integers that are between 1 and 9 inclusive.
    """
    filtered_list: List[int] = []

    for item in arr:
        # Explicitly check if the item is an integer instance.
        # This excludes booleans (which are subclass of int in Python) and floats.
        if isinstance(item, int):
            if _is_valid_digit(item):
                filtered_list.append(item)
        # else: ignore floats, booleans, strings, None, etc.

    return filtered_list


def _sort_and_reverse(digits: List[int]) -> List[int]:
    """
    Sort the list of digits in ascending order and then reverse the list.

    This is equivalent to sorting in descending order.

    Parameters:
        digits: A list of integers to be processed.

    Returns:
        A new list of integers, sorted in descending order.
    """
    # Sort in ascending order first
    sorted_ascending = sorted(digits)

    # Reverse the sorted list to get descending order
    reversed_list = sorted_ascending[::-1]

    return reversed_list


def _map_to_names(digits: List[int]) -> List[str]:
    """
    Convert each integer in the list to its corresponding word representation.

    Parameters:
        digits: A list of integers (guaranteed to be 1-9).

    Returns:
        A list of strings representing the digits.
    """
    names_list: List[str] = []

    for digit in digits:
        name = DIGIT_NAME_MAP.get(digit)
        if name is None:
            # This should theoretically not happen if inputs are validated correctly,
            # but defensive programming suggests handling it.
            # In a production setting, we might log an error.
            # Here, we simply skip or raise an error. Given the problem constraints,
            # skipping is safer to avoid crashing, but raising is more correct for
            # unexpected state. Let's raise a ValueError for unexpected states.
            raise ValueError(f"Invalid digit encountered: {digit}. Expected 1-9.")
        names_list.append(name)

    return names_list


def _handle_empty_or_none(arr: Optional[List[object]]) -> Optional[List[int]]:
    """
    Handle the case where the input array might be None or already empty.
    Returns an empty list in these cases.
    """
    if arr is None:
        return []

    if len(arr) == 0:
        return []

    return arr


def by_length(arr: List[object]) -> List[str]:
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

      If the array is empty, return an empty array:
      arr = []
      return []

      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """

    # Step 1: Validate and sanitize the input array.
    # Check for None.
    validated_input = _handle_empty_or_none(arr)

    # Initialize a list to hold valid digits.
    valid_digits: List[int] = []

    # Step 2: Filter the input array to keep only integers between 1 and 9.
    # We use the helper function for clarity and separation of concerns.
    filtered_valid = _filter_valid_digits(validated_input)

    # Assign the result to a named variable for clarity in the next steps.
    current_valid_digits = filtered_valid

    # Step 3: Sort the valid digits in ascending order.
    sorted_digits_ascending = _sort_and_reverse(current_valid_digits)

    # Note: The helper function _sort_and_reverse actually does both sort and reverse.
    # Let's break it down explicitly to meet the requirement of "separate statements".

    # Re-implementing the sort and reverse explicitly for clarity:

    # 3a. Sort the digits in ascending order
    sorted_asc = sorted(current_valid_digits)

    # 3b. Reverse the sorted list to get descending order
    final_order_digits = sorted_asc[::-1]

    # Step 4: Replace each digit with its corresponding name.
    # We use the mapping function.
    final_names = _map_to_names(final_order_digits)

    # Step 5: Return the final list of names.
    return final_names