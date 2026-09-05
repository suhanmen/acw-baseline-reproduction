from typing import Optional

def _validate_input(s: str) -> None:
    """
    Validates that the input is a string and contains only balanced bracket characters.

    This function:
    1. Checks if the input is a string.
    2. Checks if the string contains any character other than '[' or ']'.
    3. Checks if the total count of '[' and ']' is equal (necessary for full balancing).
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    if len(s) == 0:
        # An empty string is trivially balanced and requires 0 swaps, but the problem
        # implies finding swaps to balance. We allow it as a valid balanced state.
        pass

    open_count = 0
    close_count = 0

    for char in s:
        if char != '[' and char != ']':
            raise ValueError(f"Invalid character '{char}' found in input. Only '[' and ']' are allowed.")

        if char == '[':
            open_count += 1
        elif char == ']':
            close_count += 1

    if open_count != close_count:
        raise ValueError(
            f"Cannot balance the string with the minimum number of swaps because the "
            f"number of opening brackets ({open_count}) does not match the number of closing "
            f"brackets ({close_count}). For a solution to exist, counts must be equal."
        )


def _find_mismatch_indices(s: str) -> tuple[list[int], list[int]]:
    """
    Identifies indices of misplaced brackets.

    A bracket at index 'i' is considered misplaced if:
    - It is an opening bracket '[' but we currently have an excess of closing brackets needed to balance.
      In the standard algorithm for this problem, we track a balance counter.
      If we encounter a ']' when the balance is negative (or zero in a strict sequence check where we need an open first),
      it is a candidate for swapping.

    However, the specific logic for "minimum swaps" between two types of characters (only '[' and ']') 
    where we can swap any two characters relies on finding the first closing bracket that appears before its matching open bracket.

    Strategy:
    1. Traverse the string maintaining a balance counter (starts at 0, +1 for '[', -1 for ']').
    2. Whenever the balance drops below zero, it means we have encountered a ']' without a preceding unmatched '['.
    3. This specific ']' is a "mismatched closing bracket" that must be swapped with an ']' that comes later in the string.
    4. We collect the index of every such "bad" closing bracket.
    5. Since the total number of open and close brackets is equal, for every "bad" closing bracket encountered early,
       there must be a corresponding "surplus" closing bracket that appears later in the string that should be an opening bracket 
       (conceptually, we need an '[' here, but we found a ']' later that shouldn't be there, or rather, we need to swap the current ']'
       with a future ']' that is causing a balance issue, but the most efficient swap is between the earliest bad ']' and the earliest ']'
       that appears when we have a surplus of closing brackets?

    Let's refine the specific algorithm for "Minimum Swaps to Balance Brackets" (swapping any two characters):

    Algorithm:
    1. Identify the set of indices where the prefix sum (balance) becomes negative. Let's call these `bad_closing_indices`.
       - These are positions `i` where `s[i] == ']'` and the balance *before* processing `s[i]` is 0 or less? 
       Actually, standard logic: 
       Balance starts at 0.
       Iterate i from 0 to n-1:
         If s[i] == '[': balance += 1
         Else: balance -= 1
         If balance < 0: This means we have a closing bracket that doesn't match a previous open bracket.
                    This `s[i]` is definitely a `bad_closing` bracket.
                    We record `i`.
    2. For every `bad_closing` bracket identified, we need to swap it with a `surplus_closing` bracket.
       A `surplus_closing` bracket is a `']'` that appears after all `bad_closing` brackets have been handled? 
       Actually, it's simpler:
       We have `k` occurrences where the balance drops below zero. These are the `k` closing brackets that are in the wrong place.
       To fix this, we must swap each of these `k` closing brackets with a closing bracket that appears later in the string 
       and causes no prefix balance drop (or simply, we need `k` opening brackets in those early spots, so we grab `k` closing brackets
       from the later part of the string and swap them in).

       How many closing brackets are there that are NOT part of the `bad_closing` set?
       Actually, we just need to know how many times the balance went negative. Let this be `m`.
       We need to perform `m` swaps. Why?
       Each swap can fix exactly one instance of the balance dropping below zero if we swap a misplaced `]` (that caused the drop)
       with a `]` that is currently sitting in a valid spot (or a spot that will later cause a drop if not moved).

       Specifically, if the balance drops below zero `m` times, it means there are `m` closing brackets that appear before their matching opening brackets.
       We need to bring `m` opening brackets to these `m` positions. We do this by swapping these `m` misplaced `]`'s with `m` `]`'s that appear later in the string.
       Since the total count of `[` and `]` is equal, if we have `m` misplaced `]`s early, there must be `m` `]`s later that are effectively "extra" closing brackets relative to the ideal prefix structure.

       Therefore, the minimum number of swaps is exactly equal to the number of times the running balance drops below zero.

    Returns:
    A tuple containing:
      - List of indices where a closing bracket caused the balance to drop below zero.
      - None (we don't need the surplus indices explicitly for the count, but the logic relies on the count of bad ones).
    """
    mismatch_indices: list[int] = []
    balance: int = 0

    for i, char in enumerate(s):
        if char == '[':
            balance += 1
        elif char == ']':
            balance -= 1

        # If balance drops below zero, we have encountered a closing bracket 
        # that does not have a matching opening bracket before it.
        if balance < 0:
            mismatch_indices.append(i)

    return mismatch_indices, balance


def _calculate_min_swaps(s: str) -> int:
    """
    Calculates the minimum number of swaps required to balance the bracket string.

    Logic:
    1. Iterate through the string tracking the balance (opening - closing).
    2. Count how many times the balance becomes negative.
    3. Each negative balance event indicates a closing bracket that appears before its matching opening bracket.
    4. To fix this with minimum swaps, we swap each such misplaced closing bracket with a closing bracket 
       that appears later in the string (which acts as a placeholder for an opening bracket).
    5. The number of swaps required is exactly equal to the number of times the balance goes negative.
    """
    mismatch_indices, final_balance = _find_mismatch_indices(s)

    # The number of swaps is the count of mismatches found.
    min_swaps = len(mismatch_indices)

    return min_swaps


def swap_count(input_str: str) -> int:
    """
    Calculates the minimum number of swaps required to balance the brackets in the given string.

    This function attempts to balance the string by swapping any two characters.
    It returns the minimum number of swaps needed.

    Args:
        input_str: The string containing brackets ('[' and ']') and potentially other characters (though validation will fail).

    Returns:
        An integer representing the minimum number of swaps required.

    Raises:
        ValueError: If the input is not a string, contains invalid characters, 
                    or if the number of opening and closing brackets is unequal.

    Examples:
        swap_count("[]][][") -> 2
        swap_count("[[][]]") -> 0
        swap_count("[[][]]][") -> 1
    """
    _validate_input(input_str)

    return _calculate_min_swaps(input_str)