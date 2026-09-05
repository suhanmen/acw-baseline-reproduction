from typing import List, Union

def exchange(lst1: List[Union[int, float]], lst2: List[Union[int, float]]) -> str:
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    # Helper function to validate that the input consists of numbers
    def validate_input_types(input_list: List[Union[int, float]]) -> bool:
        for item in input_list:
            if not isinstance(item, (int, float)):
                return False
        return True

    # Explicitly check for non-empty input as per problem description
    if not lst1 or not lst2:
        # Although the problem assumes non-empty, we handle this defensively
        return "NO"

    # Validate that both lists contain valid numbers
    if not validate_input_types(lst1) or not validate_input_types(lst2):
        raise ValueError("Both input lists must contain only numbers (int or float).")

    # To make lst1 contain only even numbers, we must identify all odd numbers 
    # currently in lst1. These are the "problems" that need to be swapped out.
    odd_elements_in_lst1 = []
    for item in lst1:
        # An even number is one where the remainder of division by 2 is 0.
        # Note: We use item % 2 != 0 to identify odd numbers.
        # This works for both positive and negative integers.
        if item % 2 != 0:
            odd_elements_in_lst1.append(item)

    # To resolve the "problems", we need to find even numbers in lst2
    # that can be swapped into the positions of the odd numbers in lst1.
    even_elements_in_lst2 = []
    for item in lst2:
        if item % 2 == 0:
            even_elements_in_lst2.append(item)

    # The core logic:
    # We can fix every odd number in lst1 if and only if there are at least 
    # as many even numbers in lst2 as there are odd numbers in lst1.
    # This is because each odd number in lst1 requires one unique even 
    # number from lst2 to replace it.

    count_of_odds_to_fix = len(odd_elements_in_lst1)
    count_of_evens_available = len(even_elements_in_lst2)

    if count_of_odds_to_fix <= count_of_evens_available:
        # We have enough even numbers in the second list to replace all 
        # odd numbers in the first list.
        return "YES"
    else:
        # There are more odd numbers in lst1 than there are even numbers 
        # available in lst2 to swap with.
        return "NO"