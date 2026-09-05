def intersection_nested_lists(a, b):
    """
    Find the intersection of elements in nested lists a and b.

    Args:
        a (list): A list of elements or nested lists.
        b (list): A list of lists, each containing elements or nested lists.

    Returns:
        list: A list of lists, where each sublist contains elements present in both a and b.

    Raises:
        ValueError: If inputs are not lists.

    Step-by-step explanation:
    1. Validate inputs to ensure a and b are lists.
    2. Convert elements in a and b to a single list of all elements using flatten helper.
    3. For each sublist in b, check if all its elements are present in the flattened a list.
    4. Collect sublist from b if the check passes, maintaining original structure.
    5. Return the list of collected sublists.
    """
    # Validate inputs
    if not isinstance(a, list) or not isinstance(b, list):
        raise ValueError("Both a and b must be lists.")

    # Helper function to flatten a nested list
    def flatten(nested_list):
        result = []
        for element in nested_list:
            if isinstance(element, list):
                result.extend(flatten(element))
            else:
                result.append(element)
        return result

    # Flatten both a and b
    flat_a = flatten(a)
    flat_b = flatten(b)

    # For each sublist in b, check if all elements are in flat_a
    result = []
    for sublist in b:
        all_in = all(elem in flat_a for elem in sublist)
        if all_in:
            result.append(sublist)

    return result

# Test cases
assert intersection_nested_lists( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]) == [[12], [7, 11], [1, 5, 8]]
assert intersection_nested_lists([[2, 3, 1], [4, 5], [6, 8]], [[4, 5], [6, 8]]) == [[], []]
assert intersection_nested_lists(['john','amal','joel','george'],[['john'],['jack','john','mary'],['howard','john'],['jude']]) == [['john'], ['john'], ['john'], []]