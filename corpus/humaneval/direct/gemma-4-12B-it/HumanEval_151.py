def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  

    If the input list is empty, return 0.
    '''
    total = 0
    for x in lst:
        # Check if the element is an integer and not negative
        if isinstance(x, int) and x >= 0:
            # Check if the integer is odd
            if x % 2 != 0:
                total += x**2
    return total