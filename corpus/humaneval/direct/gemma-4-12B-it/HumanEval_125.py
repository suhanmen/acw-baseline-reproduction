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
    if ' ' in txt or '\t' in txt or '\n' in txt or '\r' in txt:
        return txt.split()
    elif ',' in txt:
        return [w for w in txt.split(',') if w]
    else:
        count = 0
        for char in txt:
            if 'a' <= char <= 'z':
                # ord('a') is 97. The problem defines ord('a') = 0.
                # So the index is ord(char) - ord('a').
                index = ord(char) - ord('a')
                if index % 2 != 0:
                    count += 1
        return count