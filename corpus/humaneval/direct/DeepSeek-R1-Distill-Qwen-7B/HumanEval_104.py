def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.

    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    valid_numbers = []
    for num in x:
        str_num = str(num)
        has_even = False
        for digit in str_num:
            if int(digit) % 2 == 0:
                has_even = True
                break
        if not has_even:
            valid_numbers.append(num)
    valid_numbers.sort()
    return valid_numbers