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
    count = 0
    for num in arr:
        if num == 0:
            continue

        s_num = str(num)
        digits_sum = 0

        # If the number is negative, the first character is '-'
        # The first digit after '-' should be treated as negative.
        if s_num.startswith('-'):
            # First digit is negative
            digits_sum += -int(s_num[1])
            # Remaining digits are positive
            for i in range(2, len(s_num)):
                digits_sum += int(s_num[i])
        else:
            # All digits are positive
            for char in s_num:
                digits_sum += int(char)

        if digits_sum > 0:
            count += 1

    return count