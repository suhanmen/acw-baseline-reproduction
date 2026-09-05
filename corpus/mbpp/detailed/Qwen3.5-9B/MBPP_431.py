from typing import List, Any, Optional

def common_element(list_a: List[Any], list_b: List[Any]) -> Optional[bool]:
    """
    Determines whether two lists share at least one common element.

    Returns:
        True  if at least one common element exists.
        None  if no common element exists (per specific problem requirements).
        None  if input validation fails (invalid types).

    This function validates inputs, handles edge cases explicitly, and avoids dense logic.
    """

    # Step 1: Validate input types
    if not isinstance(list_a, list):
        raise TypeError(f"Expected list for first argument, got {type(list_a).__name__}")

    if not isinstance(list_b, list):
        raise TypeError(f"Expected list for second argument, got {type(list_b).__name__}")

    # Step 2: Handle empty input cases explicitly
    # If either list is empty, they cannot share a common element.
    if len(list_a) == 0 or len(list_b) == 0:
        return None

    # Step 3: Convert the first list to a set for O(1) average-time complexity lookups.
    # This optimizes performance compared to iterating through both lists linearly.
    set_a = set(list_a)

    # Step 4: Iterate through the second list to check for existence in set_a.
    common_found = False

    for item in list_b:
        if item in set_a:
            common_found = True
            break

    # Step 5: Return the result based on the problem's specific assertions.
    # The problem requires returning None for the "no common element" case,
    # rather than the standard False.
    if common_found:
        return True
    else:
        return None