from typing import List

def is_balanced(s: str) -> bool:
    """
    Helper function to check if a string of parentheses is balanced.
    A string is balanced if:
    1. The total number of '(' equals the total number of ')'.
    2. At any point while reading from left to right, the number of 
       '(' is greater than or equal to the number of ')'.
    """
    balance_count = 0
    for char in s:
        if char == '(':
            balance_count += 1
        elif char == ')':
            balance_count -= 1
        else:
            # This case handles characters that are not parentheses, 
            # though the prompt suggests only '(' and ')' will be provided.
            return False

        # If balance ever drops below zero, there's a closing paren 
        # without a preceding opening paren.
        if balance_count < 0:
            return False

    # The string is balanced only if the final count is exactly zero.
    return balance_count == 0

def match_parens(lst: List[str]) -> str:
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    # --- Input Validation ---
    # Ensure the input is a list.
    if not isinstance(lst, list):
        return "No"

    # The problem specifies a list of two strings.
    if len(lst) != 2:
        # While the prompt implies two strings will be given, 
        # we handle cases where the list is empty or has wrong size.
        return "No"

    string_a = lst[0]
    string_b = lst[1]

    # Ensure both elements are strings.
    if not isinstance(string_a, str) or not isinstance(string_b, str):
        return "No"

    # --- Logic ---
    # There are only two possible concatenations:
    # 1. string_a followed by string_b
    # 2. string_b followed by string_a

    # Candidate 1: a + b
    combination_one = string_a + string_b
    is_first_valid = is_balanced(combination_one)

    # Candidate 2: b + a
    combination_two = string_b + string_a
    is_second_valid = is_balanced(combination_two)

    # If either concatenation results in a balanced string, return 'Yes'.
    if is_first_valid or is_second_valid:
        return "Yes"
    else:
        return "No"