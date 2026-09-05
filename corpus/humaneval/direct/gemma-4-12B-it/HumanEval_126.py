def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # Check if list is sorted in ascending order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False

    # Check for more than 1 duplicate (i.e., count > 2)
    # The requirement says "more than 1 duplicate of the same number" 
    # which translates to "more than 2 occurrences of the same number".
    # Based on the example: [1, 2, 2, 3, 3, 4] -> True (2 occurrences is okay)
    # [1, 2, 2, 2, 3, 4] -> False (3 occurrences is not okay)
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > 2:
            return False

    return True