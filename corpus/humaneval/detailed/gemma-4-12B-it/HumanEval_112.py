def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # Defensive input validation: Ensure inputs are strings
    if not isinstance(s, str) or not isinstance(c, str):
        raise TypeError("Both 's' and 'c' must be strings.")

    def is_palindrome(text: str) -> bool:
        """
        Helper function to determine if a string is a palindrome.
        A palindrome reads the same forwards and backwards.
        """
        # An empty string or a single character string is technically a palindrome
        if len(text) <= 1:
            return True

        # Create the reversed version of the string
        reversed_text = text[::-1]

        # Compare original with reversed
        return text == reversed_text

    # Step 1: Identify the set of characters to be removed.
    # Using a set provides O(1) average time complexity for lookups.
    chars_to_remove = set(c)

    # Step 2: Construct the result string.
    # We iterate through 's' and keep characters not present in the removal set.
    filtered_chars = []
    for char in s:
        if char not in chars_to_remove:
            filtered_chars.append(char)

    # Join the list into a final resulting string.
    result_string = "".join(filtered_chars)

    # Step 3: Determine if the result string is a palindrome.
    is_palindrome_result = is_palindrome(result_string)

    # Step 4: Return the result as a tuple.
    return (result_string, is_palindrome_result)