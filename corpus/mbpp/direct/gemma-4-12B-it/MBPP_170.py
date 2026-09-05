def sum_range_list(lst, start_index, end_index):
    """
    Finds the sum of numbers in a list between the specified indices (inclusive).
    """
    # The problem defines the range such that the start and end indices are inclusive.
    # Examples:
    # [2,1,5,6,8,3,4,9,10,11,8,12], 8, 10 -> indices 8, 9, 10 are 10, 11, 8. Sum = 29.
    # [2,1,5,6,8,3,4,9,10,11,8,12], 5, 7 -> indices 5, 6, 7 are 3, 4, 9. Sum = 16.
    # [2,1,5,6,8,3,4,9,10,11,8,12], 7, 10 -> indices 7, 8, 9, 10 are 9, 10, 11, 8. Sum = 38.

    return sum(lst[start_index : end_index + 1])

if __name__ == "__main__":
    assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],8,10)==29
    assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],5,7)==16
    assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],7,10)==38