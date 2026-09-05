import re

def is_even_character(char):
    """
    Determines if a character represents an even number when interpreted as a digit.

    Logic:
    1. Check if the character is a digit (0-9).
    2. If it is a digit, convert it to an integer.
    3. Check if the integer value is divisible by 2.

    If the character is not a digit, or if it is a digit but odd, this returns False.
    If the character is a digit and even, this returns True.

    This function is used to identify characters to be REMOVED based on the problem
    statement's implied logic from the examples, although the problem description
    says "remove even characters" and the examples suggest removing characters at
    even indices OR characters that are even numbers.

    Let's re-evaluate based on the provided examples:
    "python" -> "pto"
      Indices: p(0), y(1), t(2), h(3), o(4), n(5)
      Kept: p(0), t(2), o(4) -> These are at EVEN indices.
      Removed: y(1), h(3), n(5) -> These are at ODD indices.

    "program" -> "porm"
      Indices: p(0), r(1), o(2), g(3), r(4), a(5), m(6)
      Kept: p(0), o(2), r(4), m(6) -> These are at EVEN indices.

    "language" -> "lnug"
      Indices: l(0), a(1), n(2), g(3), u(4), a(5), g(6), e(7)
      Wait, "language" -> "lnug"
      l(0), n(2), u(4), e(7)? No, e is at 7.
      Let's look at the result "lnug":
      l (index 0)
      n (index 2)
      u (index 4)
      g (index 6) - wait, the example says "lnug".
      Original: l a n g u a g e
      Indices:  0 1 2 3 4 5 6 7
      Result:   l n u g ? No, "lnug" has 4 chars.
      l (0), n (2), u (4), g (6). Yes, these are indices 0, 2, 4, 6.
      So the pattern is: KEEP characters at EVEN INDICES. REMOVE characters at ODD INDICES.

    The problem statement says "remove even characters".
    This is ambiguous. Does "even characters" mean:
    1. Characters that represent even numbers (2, 4, 6, 8, 0)?
    2. Characters located at even positions (indices 0, 2, 4...)?
    3. Characters located at odd positions (indices 1, 3, 5...)?

    Based on the examples:
    "python" -> "pto" (kept indices 0, 2, 4). Removed indices 1, 3, 5.
    "program" -> "porm" (kept indices 0, 2, 4, 6). Removed indices 1, 3, 5.
    "language" -> "lnug" (kept indices 0, 2, 4, 6). Removed indices 1, 3, 5, 7.

    Conclusion: The task is to KEEP characters at even indices and REMOVE characters at odd indices.
    The phrasing "remove even characters" in the prompt text is likely a misphrasing of
    "remove characters at odd positions" or the user considers the count of previous items 
    making the current item "even" (1st item is index 0, 2nd is index 1... this doesn't fit).
    Actually, if we count 1-based: 
    p(1), y(2), t(3), h(4), o(5), n(6). Even positions: y, h, n. Remove them.
    Keep: p, t, o. Matches "pto".

    So the rule is: Remove characters that are at ODD 1-based positions (which correspond to EVEN indices 0-based).
    Wait, let's re-read carefully.
    1-based:
    python: 1:p, 2:y, 3:t, 4:h, 5:o, 6:n.
    Remove even positions (2, 4, 6) -> y, h, n.
    Result: p, t, o. -> "pto". Matches.

    program: 1:p, 2:r, 3:o, 4:g, 5:r, 6:a, 7:m.
    Remove even positions (2, 4, 6) -> r, g, a.
    Result: p, o, r, m. -> "porm". Matches.

    language: 1:l, 2:a, 3:n, 4:g, 5:u, 6:a, 7:g, 8:e.
    Remove even positions (2, 4, 6, 8) -> a, g, a, e.
    Result: l, n, u, g. -> "lnug". Matches.

    Therefore, the logic is: Filter the string to keep only characters where (index + 1) is odd.
    Equivalently, keep characters where the 0-based index is even (0, 2, 4...).

    However, the prompt says "remove even characters".
    If I interpret "even characters" as "characters at even positions (1-based)", then I remove them.
    This aligns with the examples.

    I will proceed with the logic: Keep characters at 0-based even indices (1, 3, 5... 1-based).
    Remove characters at 0-based odd indices (2, 4, 6... 1-based).

    Re-verification:
    Input: "python"
    Index 0 ('p'): Keep.
    Index 1 ('y'): Remove.
    Index 2 ('t'): Keep.
    Index 3 ('h'): Remove.
    Index 4 ('o'): Keep.
    Index 5 ('n'): Remove.
    Output: "pto". Correct.

    Input: "program"
    0(p) -> Keep
    1(r) -> Remove
    2(o) -> Keep
    3(g) -> Remove
    4(r) -> Keep
    5(a) -> Remove
    6(m) -> Keep
    Output: "porm". Correct.

    Input: "language"
    0(l) -> Keep
    1(a) -> Remove
    2(n) -> Keep
    3(g) -> Remove
    4(u) -> Keep
    5(a) -> Remove
    6(g) -> Keep
    7(e) -> Remove
    Output: "lnug". Correct.

    So the function must filter the string to include only characters at indices 0, 2, 4, etc.
    """
    try:
        char_code = ord(char)
        # Check if it's a digit to see if the problem meant numeric evenness?
        # No, the examples clearly show positional filtering.
        # But wait, does "even characters" mean alphabetic characters? No.
        # The examples are definitive.
        # We need to determine if the character itself is considered "even".
        # But the examples don't rely on the character values being even numbers.
        # 'y' is not a number, but it is removed in "python" (index 1).
        # 't' is not a number, but it is kept in "python" (index 2).
        # So it's purely positional.
        # Why does the problem say "remove even characters"?
        # Maybe it implies "remove the character if its 1-based position is even".
        # I will implement the positional logic derived from examples.
        pass
    except TypeError:
        raise TypeError(f"Input must be a string, got {type(char)}")

def remove_even_positions(string_input):
    """
    Removes characters at even 1-based positions from the input string.
    Based on the analysis of the provided examples:
    - "python" (indices 0-5) -> "pto" (kept 0, 2, 4).
    - This corresponds to removing characters at 1-based even indices (2, 4, 6...).
    - Which is equivalent to keeping characters at 0-based even indices (0, 2, 4...).

    This function constructs a new string containing only the characters 
    from the input string that appear at even 0-based indices.
    """
    # Validate input type
    if not isinstance(string_input, str):
        raise TypeError(f"Expected string input, but received {type(string_input).__name__}")

    # Initialize a list to hold the characters that will be kept
    kept_characters_list = []

    # Iterate through the string with an explicit index counter
    current_index = 0
    string_length = 0

    try:
        string_length = len(string_input)
    except TypeError:
        # This should be caught by the isinstance check above, but kept for safety
        raise TypeError(f"Cannot determine length of {type(string_input)}")

    # Loop through the string
    while current_index < string_length:
        current_character = string_input[current_index]

        # Check if the current index is even (0, 2, 4, ...)
        # 0 % 2 == 0 -> True (Keep)
        # 1 % 2 == 0 -> False (Skip)
        is_even_index = (current_index % 2) == 0

        if is_even_index:
            kept_characters_list.append(current_character)

        # Increment the index to move to the next character
        current_index += 1

    # Join the list of kept characters to form the final result string
    result_string = "".join(kept_characters_list)

    return result_string

def main():
    """
    Entry point to demonstrate the functionality and run the provided assertions.
    """
    print("Running assertions...")

    try:
        # Test Case 1
        test_input_1 = "python"
        expected_output_1 = "pto"
        actual_output_1 = remove_even_positions(test_input_1)
        assert actual_output_1 == expected_output_1, f"Test 1 failed: {actual_output_1} != {expected_output_1}"
        print(f"Test 1 Passed: {test_input_1} -> {actual_output_1}")

        # Test Case 2
        test_input_2 = "program"
        expected_output_2 = "porm"
        actual_output_2 = remove_even_positions(test_input_2)
        assert actual_output_2 == expected_output_2, f"Test 2 failed: {actual_output_2} != {expected_output_2}"
        print(f"Test 2 Passed: {test_input_2} -> {actual_output_2}")

        # Test Case 3
        test_input_3 = "language"
        expected_output_3 = "lnug"
        actual_output_3 = remove_even_positions(test_input_3)
        assert actual_output_3 == expected_output_3, f"Test 3 failed: {actual_output_3} != {expected_output_3}"
        print(f"Test 3 Passed: {test_input_3} -> {actual_output_3}")

        # Additional Edge Cases

        # Edge Case: Empty String
        empty_input = ""
        empty_result = remove_even_positions(empty_input)
        assert empty_result == "", f"Empty string test failed: {empty_result}"
        print("Edge Case Passed: Empty string -> ''")

        # Edge Case: Single Character
        single_input = "a"
        single_result = remove_even_positions(single_input)
        assert single_result == "a", f"Single char test failed: {single_result}"
        print("Edge Case Passed: Single char 'a' -> 'a'")

        # Edge Case: Two Characters
        two_char_input = "ab"
        two_char_result = remove_even_positions(two_char_input)
        # Keep index 0 ('a'), remove index 1 ('b')
        assert two_char_result == "a", f"Two char test failed: {two_char_result}"
        print("Edge Case Passed: Two chars 'ab' -> 'a'")

        # Edge Case: All Equal Elements
        equal_input = "aaaa"
        equal_result = remove_even_positions(equal_input)
        # Keep 0, 2 ('a', 'a'), remove 1, 3
        assert equal_result == "aa", f"Equal elements test failed: {equal_result}"
        print("Edge Case Passed: All equal 'aaaa' -> 'aa'")

        # Edge Case: Special Characters and Numbers
        special_input = "a1b2c3d4"
        special_result = remove_even_positions(special_input)
        # 0:a, 2:c, 4:e(no e, 5 is index 5? 0:a,1:1,2:b,3:2,4:c,5:3,6:d,7:4)
        # Keep: a (0), b (2),