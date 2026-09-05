def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the string into parts while preserving spaces.
    # Since we need to keep spaces as they are, we can split by spaces but 
    # join them back carefully. However, a simple .split(' ') preserves 
    # multiple spaces as empty strings in the list.

    words = s.split(' ')
    result = []

    for word in words:
        if word == '':
            # This handles multiple consecutive spaces
            result.append('')
        else:
            # Sort characters of the word based on ASCII value
            sorted_word = "".join(sorted(word))
            result.append(sorted_word)

    return " ".join(result)