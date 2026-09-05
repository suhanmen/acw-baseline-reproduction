from collections import Counter

def find_Divisor(start, end):
    """
    Finds the maximum occurring divisor in the interval [start, end].
    A divisor is an integer that divides at least one number in the range.
    The goal is to find the integer x such that the count of numbers in 
    [start, end] divisible by x is maximized.

    If multiple integers have the same maximum frequency, the smallest 
    such integer is typically returned by logic, but given the assertions,
    we need to identify which divisor appears most often.
    """
    # The range is inclusive [start, end]
    # Any divisor x must be in the range [1, end]
    # However, any x > end occurs 0 times.
    # Any x > (end - start) can occur at most once (unless it is exactly 1).
    # The number of multiples of x in [start, end] is:
    # count = floor(end/x) - floor((start-1)/x)

    max_count = -1
    best_divisor = 1

    # We only need to check divisors up to 'end'.
    # To optimize, we can note that for large ranges, 
    # smaller divisors occur more frequently.
    # Specifically, 1 is a divisor of every number.
    # However, the assertions suggest a specific behavior.
    # find_Divisor(2,2) -> multiples of 1: {2} (count 1), multiples of 2: {2} (count 1).
    # find_Divisor(2,5) -> multiples of 1: {2,3,4,5} (4), multiples of 2: {2,4} (2).
    # wait, if 1 is allowed, it would always be the max.
    # Looking at assertions:
    # (2,2) -> 2. This implies 1 is not considered or we pick the largest divisor 
    # among those with max frequency.
    # (2,5) -> 2. Multiples of 1: {2,3,4,5} (4). Multiples of 2: {2,4} (2). 
    # If 1 was the answer, (2,5) would be 1. 
    # Since (2,5) is 2, it implies we are looking for the maximum divisor 
    # that appears MORE than once, or there is a constraint that divisor > 1.

    # Re-evaluating assertions:
    # find_Divisor(2,2) == 2
    # find_Divisor(2,5) == 2
    # find_Divisor(5,10) == 2

    # Let's check frequency of divisors > 1:
    # (2,2): Divisor 2 appears 1 time. Max is 2.
    # (2,5): Divisor 2 appears 2 times ({2,4}). Divisor 3 appears 1 time ({3}). 
    #        Divisor 4 appears 1 time ({4}). Divisor 5 appears 1 time ({5}).
    #        Max frequency is 2, achieved by divisor 2.
    # (5,10): Divisor 2 appears 3 times ({6,8,10}). Divisor 3 appears 2 times ({6,9}).
    #         Divisor 4 appears 1 time ({8}). Divisor 5 appears 2 times ({5,10}).
    #         Max frequency is 3, achieved by divisor 2.

    # Logic: Find x > 1 that maximizes count of multiples in [start, end].
    # If multiple x have same max count, the smallest x is usually the one 
    # with the highest frequency, but the question asks for "maximum occurring divisor".
    # This could mean the divisor that has the highest count.

    for x in range(2, end + 1):
        count = (end // x) - ((start - 1) // x)
        if count > max_count:
            max_count = count
            best_divisor = x
        elif count == max_count:
            # If frequencies are equal, the problem doesn't specify, 
            # but usually, we'd keep the smaller one or the larger one.
            # Given the results, the smallest x for max frequency seems to work.
            pass

    return best_divisor