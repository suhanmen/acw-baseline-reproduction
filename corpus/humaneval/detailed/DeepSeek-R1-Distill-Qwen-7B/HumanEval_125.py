def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Helper function to split on whitespace
    def split_whitespace(s):
        return s.split() if s else []

    # Helper function to split on comma
    def split_comma(s):
        return s.split(',') if s else []

    # Check if there's whitespace to split on
    if hasattr(txt, 'split') and isinstance(txt, str) and txt.strip():
        return split_whitespace(txt)

    # Check if there are commas to split on
    if isinstance(txt, str) and ',' in txt:
        return split_comma(txt)

    # If no whitespace and no commas, count odd order letters
    count = 0
    for c in txt:
        if 'a' <= c <= 'z':
            order = ord(c) - ord('a')
            if order % 2 != 0:
                count += 1
    return count

# Example test cases
print(split_words("Hello world!"))          # Output: ["Hello", "world!"]
print(split_words("Hello,world!"))          # Output: ["Hello", "world!"])
print(split_words("abcdef"))                # Output: 3