# Standard library imports
from typing import List, Tuple, Optional

# Re-define the function signature exactly as provided in the prompt
def is_nested(string: str) -> bool:
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.
    '''
    # Helper function to validate that the input string contains ONLY square brackets
    def _validate_characters(input_str: str) -> bool:
        """
        Ensures the input string consists solely of '[' and ']' characters.
        Returns True if valid, raises ValueError otherwise.
        """
        if not isinstance(input_str, str):
            raise TypeError("Input must be a string.")

        for char in input_str:
            if char not in ('[', ']'):
                raise ValueError(f"Invalid character found: '{char}'. Input must contain only '[' and ']'.")

        return True

    # Helper function to check if a sequence of brackets is "balanced" (valid parenthesis)
    def _is_balanced(sequence: str) -> bool:
        """
        Checks if a string of brackets is balanced.
        A balanced string has matching open and close brackets in correct order.
        """
        balance_counter = 0
        for char in sequence:
            if char == '[':
                balance_counter += 1
            elif char == ']':
                balance_counter -= 1

            # If counter goes negative, closing bracket has no matching open bracket
            if balance_counter < 0:
                return False

        # Must be exactly zero at the end to be fully balanced
        return balance_counter == 0

    # Helper function to check if two balanced sequences are actually nested
    def _are_nested(seq1: str, seq2: str) -> bool:
        """
        Given two balanced bracket sequences, checks if one is strictly inside the other
        when concatenated. Specifically, we look for a pattern like [A]B[C] where A or C
        could be empty, or generally if a valid substring exists that is nested within the bounds
        of a larger valid substring.

        However, the problem asks if there is a VALID SUBSEQUENCE where nesting exists.
        This implies finding two indices i and j such that:
        substring(i, j) is balanced
        and substring(k, l) is balanced
        and substring(k, l) is strictly contained within the span of substring(i, j) 
        (or they overlap in a way that creates a nested structure in the original string).

        Actually, let's re-read carefully: "valid subsequence of brackets where at least one 
        bracket in the subsequence is nested".

        This means we can pick a subsequence of indices from the original string to form a 
        new string. That new string must be balanced AND must have the property that 
        character at index 'a' in the subsequence opens a pair that encloses character 'b'.

        Example: '[[]]' -> subsequence is the whole string. Nested.
        Example: '[][]' -> subsequences are '[]' (balanced, not nested) or '[[]' (invalid) etc.
        No balanced subsequence of '[][]' has nesting.

        Approach:
        We need to find if there exists ANY subsequence that is balanced AND has nesting.
        A balanced sequence has nesting if it contains a pattern '[ ... ]' where the inside is non-empty
        and valid.

        So, we iterate through all possible start and end indices of the original string.
        If we take the substring between start and end (inclusive), we can try to extract a balanced 
        subsequence from it. But we specifically need one that is nested.

        A simpler interpretation for "valid subsequence ... where at least one bracket ... is nested":
        Does the original string contain a pattern that allows us to construct a nested pair?

        Actually, the most robust way to solve "Is there a valid subsequence with nesting?" is:
        1. Check if the entire string (or any substring) allows forming a balanced sequence with depth >= 2.

        Let's look at the examples again.
        '[[]]' -> True. We can pick all chars. Balanced. Nested.
        '[][]' -> False. Best we can do is '[]' (depth 1).
        '[[]][[' -> True. First part '[[]]' works.
        '[]]]]]]][[[[[]' -> False. 
           Let's analyze '[]]]]]]][[[[[]'.
           Can we pick a subsequence?
           We need an open bracket followed eventually by a close bracket.
           To have nesting, we need [ [ ... ] ].
           This requires finding an open bracket at index i, then finding another open bracket at index j (j>i),
           then a close bracket at k (k>j), then a close bracket at l (l>k).
           AND, these indices must form a VALID subsequence.
           Wait, if we pick indices i, j, k, l, the subsequence is S[i]S[j]S[k]S[l].
           If S[i]='[', S[j]='[', S[k]=']', S[l]=']', the subsequence is '[[]]' which is balanced and nested.
           So the problem reduces to:
           Can we find 4 indices i < j < k < l such that:
           string[i] == '['
           string[j] == '['
           string[k] == ']'
           string[l] == ']'
           AND the subsequence formed is valid? 
           Actually, if we just pick four brackets like '[ [ ] ]', it is ALWAYS valid and nested.
           So the question is simply: Does the string contain at least two '[' and at least two ']' 
           that appear in the correct relative order to form '[[]]'?

           Let's test this hypothesis.
           Case: '[[]]' -> Has '[', '[', ']', ']'. Order: [ [ ] ]. Forms '[[]]'. Valid. Returns True. Correct.
           Case: '[][]' -> Brackets: [ ] [ ]. 
                    We can pick index 0 ('['), index 2 ('['), index 3 (']'), but we need index 4? No index 4.
                    Indices available: 0:[, 1:], 2:[, 3:].
                    To form '[[]]', we need i < j < k < l with [ [ ] ].
                    We have [ at 0, [ at 2. We need ] after 2. We have ] at 3. 
                    So we have [ (0), [ (2), ] (3). We need one more ] after 3. None exists.
                    Can we reorder? No, subsequence must preserve order.
                    So '[][]' fails this check. Returns False. Correct.

           Case: '[[]][[' -> Indices: 0:[, 1:[, 2:], 3:], 4:[, 5:[.
                    We have 0:[, 1:[, 2:], 3:]. Subsequence 0,1,2,3 gives '[[]]'. True. Correct.

           Case: '[]]]]]]][[[[[]' 
                    Let's trace indices.
                    0:[, 1:], 2:], 3:], 4:], 5:], 6:], 7:], 8:[, 9:[, 10:[, 11:[, 12:], 13:], 14:], 15:], 16:], 17:], 18:], 19:], 20:], 21:]
                    Wait, count manually.
                    '[]' (0,1), ']'*8 (2-9), '[['*3? No.
                    String: []]]]]]][[[[[]
                    0: [
                    1: ]
                    2: ]
                    3: ]
                    4: ]
                    5: ]
                    6: ]
                    7: ]
                    8: [
                    9: [
                    10: [
                    11: [
                    12: ]
                    13: [
                    14: ]
                    15: [
                    16: ]
                    17: [
                    18: [
                    19: [
                    20: ]
                    21: ]
                    22: ]
                    23: ]
                    24: ]
                    25: ]

                    We need i < j < k < l with [ [ ] ].
                    We need two open brackets before two close brackets.
                    Open brackets are at: 0, 8, 9, 10, 11, 13, 15, 17, 18, 19.
                    Close brackets are at: 1, 2, 3, 4, 5, 6, 7, 12, 14, 16, 20, 21, 22, 23, 24, 25.

                    Candidate for j (second open): Let's try 8.
                    We need an open before 8. We have 0. So i=0, j=8.
                    Now we need two closes after 8.
                    Closes after 8: 12, 14, 16, 20...
                    We can pick k=12, l=14.
                    Sequence: S[0]='[', S[8]='[', S[12]=']', S[14]=']'.
                    This forms '[[]]'.
                    Why does the example say False?

                    Let me re-read the example string carefully.
                    '[]]]]]]][[[[[]'
                    Let's count again.
                    [] (2 chars)
                    ]]]]]] (6 chars? let's count groups)
                    ] (1) ] (1) ] (1) ] (1) ] (1) ] (1) -> 6 ]s?
                    Let's copy paste and count indices carefully.
                    s = '[]]]]]]][[[[[]'
                    len(s) = 18?
                    0: [
                    1: ]
                    2: ]
                    3: ]
                    4: ]
                    5: ]
                    6: ]
                    7: ]
                    8: [
                    9: [
                    10: [
                    11: [
                    12: ]
                    13: [
                    14: ]
                    15: [
                    16: ]

                    Wait, my manual count was messy. Let's write a tiny script logic in head.
                    s = '[]]]]]]][[[[[]'
                    Chars:
                    0: [
                    1: ]
                    2: ]
                    3: ]
                    4: ]
                    5: ]
                    6: ]
                    7: ]
                    8: [
                    9: [
                    10: [
                    11: [
                    12: ]
                    13: [
                    14: ]

                    Wait, looking at the string '[]]]]]]][[[[[]':
                    Group 1: []
                    Group 2: ]]]]]] (6 closing brackets)
                    Group 3: [[[[] ? No.
                    Let's count the closing brackets after the first open.
                    [] (0,1)
                    ] (2) ] (3) ] (4) ] (5) ] (6) ] (7) ] (8) -> That's 7 closing brackets?
                    Then [ (9) [ (10) [ (11) [ (12) [ (13) ?
                    Then ] (14) ?

                    Actually, let's look at the example output again.
                    is_nested('[]]]]]]][[[[[]') ➞ False

                    If my logic "find [ [ ] ]" returns True for this, then my logic is wrong or my counting is wrong.
                    Let's assume the string is:
                    [ ] ] ] ] ] ] ] [ [ [ [ ]
                    Indices:
                    0: [
                    1: ]
                    2: ]
                    3: ]
                    4: ]
                    5: ]
                    6: ]
                    7: ]
                    8: [
                    9: [
                    10: [
                    11: [
                    12: ]

                    Ours:
                    Opens: 0, 8, 9, 10, 11
                    Closes: 1, 2, 3, 4, 5, 6, 7, 12

                    If we pick i=0, j=8.
                    We need k > 8, l > k such that s[k]=']', s[l]=']'.
                    Available closes > 8: 12.
                    Only one close bracket after index 8!
                    We need TWO close brackets to form the end of '[[]]'.
                    We have only one: at index 12.
                    Therefore, we cannot form '[[]]' using i=0 and j=8.

                    What about i=8, j=9?
                    Need closes > 9. Only one at 12. Fails.

                    So indeed, we cannot find the