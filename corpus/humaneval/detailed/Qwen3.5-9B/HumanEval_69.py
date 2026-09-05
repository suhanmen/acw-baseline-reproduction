from collections import Counter

def _validate_list_element(lst):
    """
    Validates that a single element within the list is a positive integer.
    Returns True if valid, raises ValueError otherwise.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")

    for i, element in enumerate(lst):
        if not isinstance(element, int):
            raise ValueError(f"Element at index {i} is not an integer: {type(element).__name__}")
        if element <= 0:
            raise ValueError(f"Element at index {i} must be positive, got: {element}")
    return True

def _count_frequencies(lst):
    """
    Counts the frequency of each valid integer in the list.
    Returns a dictionary mapping each integer to its count.
    """
    frequency_map = {}

    for value in lst:
        if value in frequency_map:
            frequency_map[value] += 1
        else:
            frequency_map[value] = 1

    return frequency_map

def _check_criteria(candidate_value, frequency):
    """
    Checks if a specific integer meets the criteria:
    frequency >= candidate_value.
    """
    return frequency >= candidate_value

def search(lst):
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

    # Step 1: Validate the input structure and contents
    _validate_list_element(lst)

    # Step 2: Calculate frequencies of all numbers in the list
    frequency_map = _count_frequencies(lst)

    # Step 3: Initialize variables to track the best candidate found so far
    # We start with -1 because that is the required return value if no candidate exists.
    greatest_valid_candidate = -1

    # Step 4: Iterate through each unique number found in the list
    for number in frequency_map.keys():
        frequency = frequency_map[number]

        # Step 5: Check if the current number meets the criteria (frequency >= number)
        if _check_criteria(number, frequency):
            # Step 6: Update the greatest_valid_candidate if this number is larger than current
            if number > greatest_valid_candidate:
                greatest_valid_candidate = number

    # Step 7: Return the result
    return greatest_valid_candidate