# noinspection PyUnusedLocal
def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25

    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    """

    # Step 1: Validate input type
    if not isinstance(txt, str):
        raise TypeError("Input must be a string")

    # Step 2: Handle empty string edge case
    if len(txt) == 0:
        return []

    # Step 3: Check for whitespace presence
    # We use str.isspace() or check if whitespace exists in the string
    # Since we need to check if ANY whitespace exists
    has_whitespace = False
    for char_code in range(ord(' '), ord('~') + 1):
        # This range covers printable ASCII, but let's be more robust
        pass

    # More robust whitespace check using Python's built-in split behavior logic
    # We check if the string can be split into more than 1 part by whitespace
    # Actually, simply checking if any character is whitespace is better

    # Re-approach: Check for whitespace explicitly
    whitespace_found = False
    for char in txt:
        if char.isspace():
            whitespace_found = True
            break

    if whitespace_found:
        # Case 1: Split on whitespace
        words = txt.split()
        return words

    # Case 2: No whitespace, check for commas
    # Check if comma exists in the string
    has_comma = False
    for char in txt:
        if char == ',':
            has_comma = True
            break

    if has_comma:
        # Case 2: Split on commas
        # Note: We keep the delimiters or remove them? 
        # Example: split_words("Hello,world!") ➞ ["Hello", "world!"]
        # This suggests we remove the comma and keep surrounding text
        words = txt.split(',')
        # Strip any potential empty strings that might result from adjacent commas
        # though the example doesn't show this case, defensive programming suggests handling it
        cleaned_words = []
        for word in words:
            if word != "":
                cleaned_words.append(word)
        return cleaned_words

    # Case 3: No whitespace and no commas - count odd order letters
    # Count lower-case letters with odd order in the alphabet (a=0, b=1, c=2...)
    # "odd order" means the index is odd: b(1), d(3), f(5), etc.

    odd_count = 0
    for char in txt:
        # Check if character is a lowercase letter
        if char.islower() and 'a' <= char <= 'z':
            # Calculate the order in the alphabet (a=0, b=1, ... z=25)
            # ord('a') = 97, so we subtract 97
            order = ord(char) - ord('a')

            # Check if the order is odd
            if order % 2 == 1:
                odd_count += 1

    return odd_count