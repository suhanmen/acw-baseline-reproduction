from typing import List, Any, Tuple, Optional

def _find_common_elements_preserving_order(list_a: List[Any], list_b: List[Any]) -> List[Any]:
    """
    Returns the common elements between list_a and list_b in the order they appear in list_a.

    This function:
    1. Iterates through list_a.
    2. For each element in list_a, checks if it exists in list_b.
    3. If it does, it adds it to the result list.
    4. Does not modify the original lists.
    5. Preserves duplicates if they appear in both lists in the same relative order in list_a.

    Example:
    list_a = ["red", "green", "black"]
    list_b = ["red", "pink", "green"]
    Result: ["red", "green"]
    """
    common_elements = []

    # Iterate through each element in the first list
    for current_element in list_a:
        # Check if the current element exists in the second list
        if current_element in list_b:
            common_elements.append(current_element)

    return common_elements

def _are_lists_equal(list_a: List[Any], list_b: List[Any]) -> bool:
    """
    Checks if two lists contain the exact same elements in the same order.

    This is a strict equality check for ordered sequences.
    """
    if len(list_a) != len(list_b):
        return False

    for index in range(len(list_a)):
        if list_a[index] != list_b[index]:
            return False

    return True

def same_order(list_a: List[Any], list_b: List[Any]) -> bool:
    """
    Checks if the common elements between two given lists are in the same order.

    Logic:
    1. Validates inputs to ensure they are lists.
    2. Extracts the common elements from both lists, preserving the order from list_a.
    3. Checks if the original lists (or a filtered view) maintain the same relative order 
       for these common elements.

    Actually, based on the problem statement and assertions:
    - Assertion 1: ["red","green","black","orange"] vs ["red","pink","green","white","black"] -> True
      Common in order of first: red, green, black. 
      In second list: red is at 0, green is at 2, black is at 4. Order is preserved.

    - Assertion 2: ["red","pink","green","white","black"] vs ["white","orange","pink","black"] -> False
      Common in order of first: red (not in second? wait, let's re-examine).
      Wait, let's re-read the second assertion carefully.
      List A: ["red","pink","green","white","black"]
      List B: ["white","orange","pink","black"]
      Common elements in A's order: pink, white, black.
      In B: white (index 0), pink (index 2), black (index 3).
      So the sequence in B is [white, pink, black].
      The sequence from A is [pink, white, black].
      These are different orders. Hence False.

    - Assertion 3: Same as Assertion 1 -> True.

    Therefore, the logic is:
    1. Find the subsequence of common elements as they appear in list_a.
    2. Find the subsequence of common elements as they appear in list_b.
    3. Compare these two subsequences for equality.

    Steps implemented in helper functions above.
    """

    # Input Validation
    if not isinstance(list_a, list):
        raise TypeError(f"Expected list for the first argument, got {type(list_a).__name__}")
    if not isinstance(list_b, list):
        raise TypeError(f"Expected list for the second argument, got {type(list_b).__name__}")

    # Edge Case Handling: Empty inputs
    # If both are empty, common elements are [], which are equal.
    # If one is empty, common elements are [], which are equal.
    # So empty lists should return True.

    # Step 1: Extract common elements preserving order from list_a
    common_from_a = _find_common_elements_preserving_order(list_a, list_b)

    # Step 2: Extract common elements preserving order from list_b
    # We need to iterate through list_b and pick elements that are in list_a
    common_from_b = []
    for element in list_b:
        if element in list_a:
            common_from_b.append(element)

    # Step 3: Compare the two extracted sequences
    # If they are identical, the order is preserved.
    return _are_lists_equal(common_from_a, common_from_b)