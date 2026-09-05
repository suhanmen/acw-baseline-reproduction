def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def digit_sum(num):
        s = str(num)
        total = 0
        for i, c in enumerate(s):
            if i == 0 and num < 0:
                # First character is '-', so digit is -1
                total += -1
            else:
                # For other characters, convert to int
                total += int(c)
        return total

    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    return count