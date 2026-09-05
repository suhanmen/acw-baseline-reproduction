def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0  # Handle empty list case

    total = 0
    for index, value in enumerate(lst):
        # Check if the position (index + 1) is even
        if (index + 1) % 2 == 0:
            # Check if the value is odd
            if value % 2 != 0:
                total += value
    return total