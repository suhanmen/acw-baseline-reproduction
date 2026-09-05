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
    # A valid subsequence of brackets is nested if there is a structure like [[]]
    # contained within the string. This means we are looking for at least one 
    # opening bracket that has another valid bracket pair inside it.
    # Essentially, we need to find if there's a pair of brackets [ ] 
    # that contains at least one other complete pair [ ] inside it.

    stack = []
    # We look for any instance of nested pairs. 
    # A pair is nested if we see an opening bracket, then a complete pair, 
    # and then the closing bracket for the first one.

    # To solve this efficiently, we can check for the pattern [ [ ] ]
    # However, the subsequence can be non-contiguous.
    # The core requirement "valid subsequence of brackets where at least one is nested"
    # mathematically means we need to find indices i < j < k < l 
    # such that string[i] == '[' and string[l] == ']' and 
    # string[j] == '[' and string[k] == ']' where i < j < k < l.

    # Let's track the indices of opening brackets.
    open_indices = []
    for i, char in enumerate(string):
        if char == '[':
            open_indices.append(i)
        elif char == ']':
            if open_indices:
                # We found a complete pair at (open_indices.pop(), i)
                # If there was at least one '[' still in the stack before this 
                # pair was completed, it means this pair is nested inside a 
                # larger bracket structure.
                # Actually, the rule is: if we close a pair and there is 
                # still an open bracket "waiting", it's nested.
                # Wait, the logic: "at least one bracket is nested" 
                # means there exists a pair [ ] inside another pair [ ].

                # Let's re-evaluate: is there i < j < k < l such that
                # s[i]='[', s[j]='[', s[k]=']', s[l]=']'
                # This is equivalent to finding if we have 2 open brackets 
                # before we see 2 closing brackets.
                pass

    # Correct logic for "valid subsequence with at least one nested":
    # This means we need to find a subsequence [ [ ] ] 
    # which is the definition of nesting.

    # Let's count how many '[' we have seen.
    # If we see a '[' and we already have a '[' that hasn't been closed yet,
    # and then we see a ']' and then another ']', we have found a nested structure.

    # Simplified: We need to find if there's a pair of brackets [ ] 
    # that contains another pair [ ] inside it.

    # Let's track the nesting depth.
    # If at any point the depth reaches 2, and we later see a closing bracket
    # that closes the outer one, it's nested.

    # Or even simpler: is there a subsequence [ [ ] ]?
    # We can check this by iterating through the string.

    # Let's try a different approach:
    # A string contains a nested subsequence [ [ ] ] if there exist
    # indices i < j < k < l such that s[i]='[', s[j]='[', s[k]=']', s[l]=']'.

    # This is true if:
    # There exists an index i such that string[i] == '['
    # There exists an index j > i such that string[j] == '['
    # There exists an index k > j such that string[k] == ']'
    # There exists an index l > k such that string[l] == ']'

    # Let's find the first '[' at i.
    # Then find the first '[' at j > i.
    # Then find the first ']' at k > j.
    # Then find the first ']' at l > k.

    first_open = -1
    for i in range(len(string)):
        if string[i] == '[':
            first_open = i
            break

    if first_open == -1: return False

    second_open = -1
    for i in range(first_open + 1, len(string)):
        if string[i] == '[':
            second_open = i
            break

    if second_open == -1: return False

    first_close = -1
    for i in range(second_open + 1, len(string)):
        if string[i] == ']':
            first_close = i
            break

    if first_close == -1: return False

    second_close = -1
    for i in range(first_close + 1, len(string)):
        if string[i] == ']':
            second_close = i
            break

    return second_close != -1