def recursive_list_sum(lst):
    """
    Calculate the sum of all numbers in a possibly nested list.

    :param lst: A list containing numbers and/or other lists.
    :return: The sum of all numbers in the nested structure.
    """
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        elif isinstance(element, (int, float)):
            total += element
        # For other types, we can choose to raise an error or ignore them.
        # Since the problem assumes valid inputs, we'll proceed by ignoring other types.
    return total

# Example usage and assertions
assert recursive_list_sum([]) == 0, "Empty list should return 0"
assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21, "Sum of [1,2,[3,4],[5,6]] should be 21"
assert recursive_list_sum([7, 10, [15,14],[19,41]]) == 106, "Sum of [7,10,[15,14],[19,41]] should be 106"
assert recursive_list_sum([10, 20, [30,40],[50,60]]) == 210, "Sum of [10,20,[30,40],[50,60]] should be 210"