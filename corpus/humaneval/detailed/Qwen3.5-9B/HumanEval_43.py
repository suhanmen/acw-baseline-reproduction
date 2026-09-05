from typing import List, Union

def _validate_integer_input(value: object) -> bool:
    """
    Helper function to check if a value is an integer.
    Floats (even whole numbers) are explicitly rejected as they are not integers.
    """
    if not isinstance(value, int):
        return False
    # Python 2 compatibility note: In Python 3, bool is a subclass of int.
    # We must explicitly reject booleans if we want strict integer validation.
    if isinstance(value, bool):
        return False
    return True

def _validate_input_list(input_list: object) -> tuple[bool, Union[List[int], None]]:
    """
    Helper function to validate that the input is a list containing only integers.
    Returns a tuple of (is_valid, validated_list).
    If invalid, the list part is None.
    """
    if not isinstance(input_list, list):
        return False, None

    for index, item in enumerate(input_list):
        if not _validate_integer_input(item):
            return False, None

    return True, input_list

def _find_pair_summing_to_zero(numbers: List[int]) -> bool:
    """
    Helper function that iterates through a list of integers to find if
    any two distinct elements sum to zero.

    Logic:
    1. Iterate through each number with its index.
    2. For each number, iterate through all subsequent numbers (to avoid duplicates
       and self-pairing).
    3. Check if the sum of the current pair is zero.
    4. If found, return True immediately.
    5. If the loop completes without finding a pair, return False.
    """
    # Guard against empty lists or lists with fewer than 2 elements here
    # (though the main function handles size, this adds defensive depth)
    if len(numbers) < 2:
        return False

    n = len(numbers)

    # Iterate through the list up to the second-to-last element
    for i in range(n - 1):
        current_num = numbers[i]

        # Iterate through the list starting from the element after current_num
        for j in range(i + 1, n):
            partner_num = numbers[j]

            # Check if the sum is exactly zero
            total = current_num + partner_num
            if total == 0:
                return True

    return False

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Edge Cases Handled:
    - Empty list: Returns False.
    - Single element list: Returns False.
    - Lists containing non-integers: Raises TypeError.
    - Lists with zero and its negative: Returns True (e.g., [0, 0] -> True).
    - Lists with all positives or all negatives: Returns False.
    - Large lists: Efficient O(N^2) search with early exit.
    """
    # Step 1: Validate the input list structure and content
    is_valid, validated_list = _validate_input_list(l)

    if not is_valid:
        raise TypeError("Input must be a list of integers.")

    # Step 2: Check basic size constraints early for clarity
    list_size = len(validated_list)
    if list_size == 0:
        return False

    if list_size == 1:
        return False

    # Step 3: Delegate the core logic to the specialized helper
    # This ensures the complex loop logic is isolated and tested independently
    has_pair = _find_pair_summing_to_zero(validated_list)

    return has_pair