from typing import List, Any

def is_even(value: Any) -> bool:
    """
    Checks if the provided value is an integer and is even.

    Returns False for:
    - Non-integer types (e.g., floats, strings).
    - Integer values that are odd.
    Returns True for:
    - Integer values that are even.
    Returns False if the value is None or a float (even if the float represents an even integer),
    as this enforces strict type checking for "numbers" in the context of this problem.
    """
    if not isinstance(value, int):
        return False
    # Zero is even. Positive and negative even numbers are handled by the modulo operator correctly.
    return value % 2 == 0

def remove_odd(numbers: List[Any]) -> List[int]:
    """
    Removes all odd numbers from the input list, returning a new list containing
    only the even numbers.

    This function performs the following steps:
    1. Validates that the input is a list.
    2. Validates that the list does not contain None values (defensive programming).
    3. Iterates through each element in the list.
    4. Uses the is_even helper function to check if an element is an even integer.
    5. Collects elements that pass the check into a new result list.
    6. Returns the new list.

    Non-integer elements (like floats, strings) are excluded from the result.
    If the input list contains elements that are not integers, they are simply skipped
    rather than raising an error, ensuring the function always returns a valid list.
    """
    # Step 1: Validate input type. The problem implies a list of numbers.
    if not isinstance(numbers, list):
        # In a strict validation scenario, we might raise a TypeError here.
        # However, to match the specific assertions provided which use lists of ints,
        # and to provide a safe default behavior for non-list inputs in a defensive context,
        # we can either raise an error or return an empty list.
        # Given "remove odd numbers from a given list", providing a list is a requirement.
        # We will raise a TypeError to indicate invalid usage explicitly.
        raise TypeError("Input must be a list.")

    result: List[int] = []

    # Step 2 & 3: Iterate through the list
    for item in numbers:
        # Defensive check: While the assertion tests show integers, 
        # defensive code handles unexpected internal states or None types gracefully.
        # If an element is None, it cannot be an even number, so we skip it.
        if item is None:
            continue

        # Step 4: Check if the item is an even number
        if is_even(item):
            # Step 5: Append valid even integers to the result list
            result.append(item)

    # Step 6: Return the processed list
    return result

# The following lines are comments explaining the logic flow based on the assertions:
# 
# Assertion: assert remove_odd([1,2,3]) == [2]
# - Input: [1, 2, 3]
# - Item 1: is_even(1) -> 1 % 2 == 1 -> False. Not added.
# - Item 2: is_even(2) -> 2 % 2 == 0 -> True. Added to result.
# - Item 3: is_even(3) -> 3 % 2 == 1 -> False. Not added.
# - Result: [2]
#
# Assertion: assert remove_odd([2,4,6]) == [2,4,6]
# - All items are even integers. All are added.
#
# Assertion: assert remove_odd([10,20,3]) == [10,20]
# - 10 is even -> Added.
# - 20 is even -> Added.
# - 3 is odd -> Skipped.
# - Result: [10, 20]