from typing import List, Dict

def search(lst: List[int]) -> int:
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Requirement validation: Ensure input is a list.
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of integers.")

    # The problem states a non-empty list of positive integers.
    # We handle empty list as a degenerate case.
    if not lst:
        return -1

    # Step 1: Count the frequency of each integer in the list.
    # We use a dictionary for O(n) time complexity for the counting phase.
    frequency_map: Dict[int, int] = {}
    for item in lst:
        # Validation: ensure the items are actually integers.
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item)}")

        # The problem specifies positive integers (greater than zero).
        # While the behavior for non-positive integers isn't strictly defined,
        # we filter for values > 0 as per the prompt's wording.
        if item > 0:
            frequency_map[item] = frequency_map.get(item, 0) + 1

    # Step 2: Identify all candidates.
    # A candidate is an integer x such that frequency(x) >= x.
    candidates: List[int] = []
    for value, count in frequency_map.items():
        if count >= value:
            candidates.append(value)

    # Step 3: Find the greatest candidate.
    # If candidates is empty, the problem specifies returning -1.
    if not candidates:
        return -1

    # Find the maximum value in the candidates list.
    max_candidate = candidates[0]
    for i in range(1, len(candidates)):
        if candidates[i] > max_candidate:
            max_candidate = candidates[i]

    return max_candidate