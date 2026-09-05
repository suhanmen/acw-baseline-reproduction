def common_in_nested_lists(nested_lists):
    count = {}
    for lst in nested_lists:
        for num in lst:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    return sorted([num for num, c in count.items() if c >= 2])