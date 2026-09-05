def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''

    s1, s2 = lst[0], lst[1]

    def is_balanced(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0

    def check_concat(s1, s2):
        # Check s1 + s2
        if is_balanced(s1 + s2):
            return True
        # Check s2 + s1
        if is_balanced(s2 + s1):
            return True
        return False

    # Handle edge cases
    if len(lst) != 2 or not (all(c in '()\' for c in s1) and all(c in '()\' for c in s2)):
        return 'No'

    # Check if either string alone is balanced
    if is_balanced(s1) or is_balanced(s2):
        return 'Yes'

    # Check the possible concatenations
    if check_concat(s1, s2):
        return 'Yes'
    else:
        return 'No'

    # If none of the above conditions apply, check for some other possibilities
    # For example, s1 has more '(' than s2, etc.
    # But the above checks should cover all possibilities