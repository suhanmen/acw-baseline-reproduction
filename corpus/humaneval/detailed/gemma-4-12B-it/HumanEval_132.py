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

    # --- Input Validation ---
    # Ensure the input is a string.
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")

    # The problem states the string contains only square brackets.
    # We check for any characters that are not '[' or ']'.
    allowed_chars = {'[', ']'}
    for char in string:
        if char not in allowed_chars:
            raise ValueError(f"Invalid character '{char}' detected. Only '[' and ']' are allowed.")

    # Handle empty string edge case.
    if len(string) == 0:
        return False

    # --- Logic Breakdown ---
    # The problem asks for a "valid subsequence of brackets" where at least one 
    # bracket is "nested". 
    # In the context of bracket logic:
    # 1. A "valid subsequence" refers to a set of brackets that form a balanced pair [].
    # 2. "Nested" means a bracket pair is inside another bracket pair, e.g., [[...]].
    # 3. This is equivalent to saying there exists an occurrence of "[[" or "]]" 
    #    within a balanced part of the string, or more simply, that we can find 
    #    a pair of brackets that contains another pair of brackets inside it.
    # 4. From the examples:
    #    '[][]' -> False (Two adjacent pairs, no nesting)
    #    '[[]]' -> True (Inner pair is nested inside outer pair)
    #    '[[][]]' -> True (Inner pairs nested inside outer pair)
    #    '[]]]]]]][[[[[]' -> False (Though it has brackets, there's no valid 
    #    nested structure formed by a balanced subsequence).

    # To solve this, we need to find if there exists a balanced subsequence 
    # of the form [[...]] or similar. 
    # A simple way to detect nesting is to track the depth of open brackets.
    # If at any point we encounter an open bracket '[' while the current 
    # depth is already at least 1, and we eventually close those brackets 
    # validly, we have found nesting.

    # However, the prompt specifies a "valid subsequence". A subsequence 
    # is formed by deleting zero or more elements.
    # A nested subsequence exists if and only if there is a '[' followed 
    # by another '[' followed by a ']' followed by a ']'.
    # This is because [ [ ] ] is the simplest nested structure.
    # If we can find four indices i < j < k < l such that 
    # string[i] == '[', string[j] == '[', string[k] == ']', string[l] == ']'
    # then we have a nested valid subsequence.

    # Let's verify this logic against examples:
    # '[[]]' -> indices 0,1,2,3 are [ [ ] ]. Valid nested subsequence. True.
    # '[]]]]]]][[[[[]' -> contains '[' at 0, ']' at 1. Then ']'s. Then '['s.
    # There is no sequence of i < j < k < l forming [[]]. False.
    # '[][]' -> indices 0,1 are [], 2,3 are []. No i < j < k < l for [[]]. False.
    # '[]' -> No nested. False.
    # '[[][]]' -> indices 0, 1, 2, 3 form [[]]? No, but indices 0, 1, 4, 5 
    #              form [[]] (the outermost and the right inner one). True.
    # '[[]][[' -> indices 0, 1, 2, 3 form [[]]. True.

    def find_nested_subsequence(input_str):
        """
        Searches for four indices i < j < k < l such that 
        input_str[i] == '['
        input_str[j] == '['
        input_str[k] == ']'
        input_str[l] == ']'
        """
        # To find if such a subsequence exists efficiently:
        # We need to find the first '[' (index i)
        # Then the next '[' (index j)
        # Then the next ']' (index k)
        # Then the next ']' (index l)

        first_open = -1
        second_open = -1
        first_close = -1
        second_close = -1

        # This greedy approach is slightly wrong because we need i < j < k < l.
        # Correct logic:
        # Find the first occurrence of '['.
        # Find the next occurrence of '[' after that.
        # Find the next occurrence of ']' after the second '['.
        # Find the next occurrence of ']' after the first ']'.

        # Let's use a more robust approach:
        # A nested subsequence exists if there's a '[' before another '[' 
        # which is before a ']' which is before another ']'.

        # Step 1: Find the first '['
        i = -1
        for idx in range(len(input_str)):
            if input_str[idx] == '[':
                i = idx
                break

        if i == -1:
            return False

        # Step 2: Find the next '[' after i
        j = -1
        for idx in range(i + 1, len(input_str)):
            if input_str[idx] == '[':
                j = idx
                break

        if j == -1:
            return False

        # Step 3: Find the first ']' after j
        k = -1
        for idx in range(j + 1, len(input_str)):
            if input_str[idx] == ']':
                k = idx
                break

        if k == -1:
            return False

        # Step 4: Find the next ']' after k
        l = -1
        for idx in range(k + 1, len(input_str)):
            if input_str[idx] == ']':
                l = idx
                break

        if l == -1:
            return False

        # If we found all four in order, a nested subsequence exists.
        return True

    # Execute the logic
    result = find_nested_subsequence(string)
    return result