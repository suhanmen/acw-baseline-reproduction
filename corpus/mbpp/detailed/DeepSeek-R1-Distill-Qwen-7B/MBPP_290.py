def max_length(input_list):
    """
    Find the list of lists with the maximum length and return it along with its length.

    Input:
        input_list: a list of lists

    Output:
        tuple containing (max_length, corresponding_sublist)
    """
    if not input_list:
        return (0, [])

    max_len = -1
    max_index = -1
    for index, sublist in enumerate(input_list):
        current_len = len(sublist)
        if current_len > max_len:
            max_len = current_len
            max_index = index
        elif current_len == max_len:
            if index < max_index:
                max_index = index

    # Retrieve the sublist with maximum length
    corresponding_sublist = input_list[max_index] if max_index != -1 else []
    return (max_len, corresponding_sublist)

# Test Cases
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
assert max_length([[1], [5, 7], [10, 12, 14, 15]]) == (4, [10, 12, 14, 15])
assert max_length([[5], [15, 20, 25]]) == (3, [15, 20, 25])