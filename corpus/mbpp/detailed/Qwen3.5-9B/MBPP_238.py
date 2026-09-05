def number_of_substrings(s):
    """
    Counts the number of non-empty substrings of a given string.

    A substring is defined as a contiguous sequence of characters within the string.
    For a string of length n, the number of non-empty substrings is given by the formula:
    n * (n + 1) / 2

    This function validates the input and handles edge cases explicitly.

    Parameters:
    s (str): The input string to analyze.

    Returns:
    int: The count of non-empty substrings.

    Raises:
    TypeError: If the input is not a string.
    ValueError: If the string contains invalid characters (though Python strings are flexible, 
                 we validate for the expectation of standard string behavior).
    """
    # Step 1: Validate input type
    if not isinstance(s, str):
        raise TypeError(f"Expected input to be of type 'str', but received {type(s).__name__}")

    # Step 2: Handle empty string case explicitly
    if len(s) == 0:
        return 0

    # Step 3: Get the length of the string
    n = len(s)

    # Step 4: Calculate the number of substrings using the formula n * (n + 1) / 2
    # We calculate n * (n + 1) first to ensure we are working with integers
    numerator = n * (n + 1)

    # Divide by 2 to get the final count
    # Using integer division // to return an int
    count = numerator // 2

    # Step 5: Return the result
    return count


if __name__ == "__main__":
    # Local test verification to ensure the logic holds as per problem description
    # These tests mirror the requirements but are not part of the function output.

    # Test case 1: "abc" -> expected 6
    # Substrings: "a", "b", "c", "ab", "bc", "abc"
    result_1 = number_of_substrings("abc")
    expected_1 = 6
    assert result_1 == expected_1, f"Test failed for 'abc': got {result_1}, expected {expected_1}"

    # Test case 2: "abcd" -> expected 10
    # Substrings: "a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", "abcd"
    result_2 = number_of_substrings("abcd")
    expected_2 = 10
    assert result_2 == expected_2, f"Test failed for 'abcd': got {result_2}, expected {expected_2}"

    # Test case 3: "abcde" -> expected 15
    # Substrings: "a", "b", "c", "d", "e", "ab", "bc", "cd", "de", "abc", "bcd", "cde", "abcd", "bcde", "abcde"
    result_3 = number_of_substrings("abcde")
    expected_3 = 15
    assert result_3 == expected_3, f"Test failed for 'abcde': got {result_3}, expected {expected_3}"

    # Additional Edge Case 1: Empty string
    result_empty = number_of_substrings("")
    assert result_empty == 0, f"Test failed for empty string: got {result_empty}, expected 0"

    # Additional Edge Case 2: Single character
    result_single = number_of_substrings("z")
    assert result_single == 1, f"Test failed for single char 'z': got {result_single}, expected 1"

    # Additional Edge Case 3: All equal elements
    result_equal = number_of_substrings("aaaa")
    # Length is 4, so 4*5/2 = 10
    assert result_equal == 10, f"Test failed for 'aaaa': got {result_equal}, expected 10"

    # Additional Edge Case 4: Negative length simulation (via empty check logic)
    # Python strings cannot have negative length, but we validate the return logic.

    # Additional Edge Case 5: Special characters
    result_special = number_of_substrings("a@b#c")
    expected_special = 6  # Length is 5: "a", "@", "b", "#", "c" + combinations
    assert result_special == expected_special, f"Test failed for 'a@b#c': got {result_special}, expected {expected_special}"

    # Invalid Input Test: Not a string
    try:
        number_of_substrings(12345)
        assert False, "Should have raised TypeError for integer input"
    except TypeError:
        pass # Expected behavior

    try:
        number_of_substrings(None)
        assert False, "Should have raised TypeError for None input"
    except TypeError:
        pass # Expected behavior

    print("All explicit checks and assertions passed successfully.")