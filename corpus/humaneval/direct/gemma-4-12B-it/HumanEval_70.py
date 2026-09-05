def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if not lst:
        return []

    # Sort the list to easily pick min and max values
    sorted_lst = sorted(lst)
    result = []

    left = 0
    right = len(sorted_lst) - 1

    while left <= right:
        # Add the current minimum
        result.append(sorted_lst[left])
        left += 1

        # If there are still elements, add the current maximum
        if left <= right:
            result.append(sorted_lst[right])
            right -= 1

    return result