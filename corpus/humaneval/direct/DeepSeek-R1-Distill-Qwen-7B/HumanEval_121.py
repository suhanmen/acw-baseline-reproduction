def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions."""
    total = 0
    for index, num in enumerate(lst):
        if num % 2 != 0 and index % 2 == 0:
            total += num
    return total