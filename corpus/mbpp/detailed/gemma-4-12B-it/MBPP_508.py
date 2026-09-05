from typing import List, Any

def same_order(list_a: List[Any], list_b: List[Any]) -> bool:
    """
    Determines if the common elements between two lists appear in the same 
    relative order in both lists.

    Example:
    list_a = ["red", "green", "black", "orange"]
    list_b = ["red", "pink", "green", "white", "black"]
    Common elements: ["red", "green", "black"]
    Order in list_a: ["red", "green", "black"]
    Order in list_b: ["red", "green", "black"]
    Result: True
    """

    # Input Validation: Ensure inputs are lists
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be of type list.")

    # Handle degenerate cases: If either list is empty, 
    # there are no common elements, which trivially maintains order.
    if not list_a or not list_b:
        return True

    # Step 1: Identify common elements.
    # We use a set to find unique common elements to optimize lookup.
    # Note: If the problem implies handling duplicates specifically,
    # we'd use a different approach, but standard "common elements" 
    # usually refers to the intersection of the sets of items.
    set_a = set(list_a)
    set_b = set(list_b)
    common_elements_set = set_a.intersection(set_b)

    # If there are no common elements, the order is vacuously true.
    if not common_elements_set:
        return True

    # Step 2: Extract common elements from list_a in their original order.
    # We preserve duplicates if they exist in the original list, 
    # but only if they are part of the common set.
    ordered_common_a = []
    for item in list_a:
        if item in common_elements_set:
            ordered_common_a.append(item)

    # Step 3: Extract common elements from list_b in their original order.
    ordered_common_b = []
    for item in list_b:
        if item in common_elements_set:
            ordered_common_b.append(item)

    # Step 4: Compare the relative order of these common elements.
    # Because we might have duplicates in the input lists (e.g., 
    # ["a", "a"] and ["a"]), we need to ensure that the sequence 
    # of common elements is identical.
    # However, the problem asks for "common elements" order. 
    # Standard interpretation for "same order" in this context 
    # compares the filtered sequences.

    # Let's refine: The "common elements" are the items that appear 
    # in both. If an item appears multiple times in both, we check 
    # if that sequence is preserved.

    # Comparison logic:
    # We check if the list of common items found in list_a 
    # matches the list of common items found in list_b.

    # Note: If a list has duplicates like ["red", "red"] and 
    # the other has ["red"], the "common elements" sequence logic 
    # can be ambiguous. Given the test cases, the elements are unique.

    # To be robust against duplicates while maintaining order:
    # We ensure the sequence of items found in list_a that exist 
    # in list_b is exactly the same sequence as those in list_b 
    # that exist in list_a.

    # We must handle the case where common elements might appear 
    # multiple times in one list but only once in another.
    # Standard set intersection logic suggests we look at unique common items.

    unique_common_ordered_a = []
    seen_a = set()
    for item in ordered_common_a:
        if item not in seen_a:
            unique_common_ordered_a.append(item)
            seen_a.add(item)

    unique_common_ordered_b = []
    seen_b = set()
    for item in ordered_common_b:
        if item not in seen_b:
            unique_common_ordered_b.append(item)
            seen_b.add(item)

    # Final Equality Check
    is_same_order = (unique_common_ordered_a == unique_common_ordered_b)

    return is_same_order