def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    '''
    if not lst:
        return 0

    total = 0
    for number in lst:
        if type(number) is int and number >= 0:
            if number % 2 != 0:
                total += number ** 2
    return total

# Test cases to ensure correctness
assert double_the_difference([1, 3, 2, 0]) == 10, "Test case 1 failed"
assert double_the_difference([-1, -2, 0]) == 0, "Test case 2 failed"
assert double_the_difference([9, -2]) == 81, "Test case 3 failed"
assert double_the_difference([0]) == 0, "Test case 4 failed"
assert double_the_difference([]) == 0, "Test case 5 failed"
assert double_the_difference([True, False, 5, 3.5]) == 25, "Test case 6 failed"