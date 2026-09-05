from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Defensive check: Ensure the input is actually a string
    if not isinstance(txt, str):
        raise TypeError("Input 'txt' must be a string.")

    # Handle empty string case explicitly
    if txt == "":
        # Based on the logic: 
        # 1. No whitespace -> 
        # 2. No commas -> 
        # 3. Count lowercase letters with odd indices.
        # Empty string contains 0 such letters.
        return 0

    # Step 1: Check for whitespaces
    has_whitespace = False
    for char in txt:
        if char.isspace():
            has_whitespace = True
            break

    if has_whitespace:
        # Behavior: split on whitespace
        # Using split() without arguments handles multiple spaces and leading/trailing whitespace
        result = txt.split()
        return result

    # Step 2: If no whitespaces, check for commas
    has_comma = False
    for char in txt:
        if char == ',':
            has_comma = True
            break

    if has_comma:
        # Behavior: split on commas
        # We split by comma and filter out empty strings caused by leading/trailing/consecutive commas
        raw_split = txt.split(',')
        result = []
        for part in raw_split:
            if part != "":
                result.append(part)
        return result

    # Step 3: If no whitespaces and no commas, count lower-case letters with odd order.
    # ord('a') = 0 (even), ord('b') = 1 (odd), ord('c') = 2 (even), ord('d') = 3 (odd)...
    # This is equivalent to checking if (ord(char) - ord('a')) % 2 != 0
    # Which is also equivalent to checking if ord(char) is odd, provided it is a lowercase letter.

    odd_order_count = 0
    base_ord = ord('a')

    for char in txt:
        # Check if character is a lowercase letter
        if 'a' <= char <= 'z':
            # Calculate the order in the alphabet (0-indexed)
            alphabet_order = ord(char) - base_ord

            # Check if the order is odd
            if alphabet_order % 2 != 0:
                odd_order_count += 1

    return odd_order_count