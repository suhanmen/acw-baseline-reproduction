def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # We need to find if there exists a valid subsequence that has nesting.
    # A valid bracket sequence with nesting must contain at least one pair of brackets
    # where an opening bracket appears before a closing bracket, and between them
    # there is at least one more bracket pair (which could be empty if we consider direct nesting like [[]]).
    # Actually, direct nesting like "[]" inside "[]" as in "[[]]" means we have an open, then an open, then close, then close.
    # So we are looking for a pattern in the subsequence that looks like "[]".
    # But we can skip characters.
    # The key insight: To have a nested valid subsequence, we need to be able to form a pattern like "[]".
    # However, the example "[][]" returns False. This means simply having two pairs is not enough; they must be nested.
    # "[][]" -> valid subsequence could be "[][]" (not nested) or "[]" (not nested). We cannot form "[[]]" as a subsequence.
    # So we need to check if the original string contains a subsequence equivalent to "[[]]".
    # A subsequence equivalent to "[[]]" requires:
    # 1. An opening bracket '['
    # 2. Another opening bracket '[' that comes after the first one
    # 3. A closing bracket ']' that comes after the second '['
    # 4. A closing bracket ']' that comes after the third character (and before or after, but for validity it must close the second).
    # Actually, the simplest valid nested sequence is "[[]]".
    # So we just need to check if we can find indices i < j < k < l such that s[i] == '[', s[j] == '[', s[k] == ']', s[l] == ']'.
    # Note: The inner part "[]" is formed by j and k. The outer part is i and l.
    # Is it possible to have a nested subsequence without 4 characters?
    # No, the smallest nested valid sequence is "[[]]" which has 4 characters.
    # Therefore, the problem reduces to: Does the string contain the subsequence pattern "[[...]]" where the middle two form a pair?
    # Specifically, we need two '[' and two ']' in that order: [ ... [ ... ] ... ].

    count_open = 0
    count_close = 0

    # We need to find if we can pick two '[' and two ']' in the order [ [ ] ]
    # We can do this with a simple pass.
    # State machine approach:
    # 0: waiting for first '['
    # 1: found first '[', waiting for second '['
    # 2: found two '[', now we need a ']' (for the inner pair)
    # 3: found inner pair '[', now we need a closing ']' for the outer pair

    # Wait, the order is:
    # Index i: '['
    # Index j: '[' (must be > i)
    # Index k: ']' (must be > j) -> This forms the inner "[]"
    # Index l: ']' (must be > k) -> This forms the outer closing, closing i.
    # So we just need to find two '[' and then two ']' appearing after them?
    # No, the second ']' must come after the second '['. And the third ']' (outer) must come after the second ']'.
    # So the sequence of characters in the subsequence is at indices i, j, k, l with i < j < k < l and chars are [ [ ] ].

    # Algorithm:
    # Find the first '['.
    # Then find the next '[' after that.
    # Then find the next ']' after that second '['.
    # Then find the next ']' after that '].

    n = len(string)
    idx1 = -1 # index of first '['
    idx2 = -1 # index of second '['
    idx3 = -1 # index of first ']' (closing inner)
    idx4 = -1 # index of second ']' (closing outer)

    # Find first '['
    for i in range(n):
        if string[i] == '[':
            idx1 = i
            break

    if idx1 == -1:
        return False

    # Find second '[' after idx1
    for i in range(idx1 + 1, n):
        if string[i] == '[':
            idx2 = i
            break

    if idx2 == -1:
        return False

    # Find first ']' after idx2
    for i in range(idx2 + 1, n):
        if string[i] == ']':
            idx3 = i
            break

    if idx3 == -1:
        return False

    # Find second ']' after idx3
    for i in range(idx3 + 1, n):
        if string[i] == ']':
            idx4 = i
            break

    if idx4 == -1:
        return False

    return True