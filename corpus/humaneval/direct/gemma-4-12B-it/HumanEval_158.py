def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return ""

    # We want to maximize unique character count,
    # then minimize lexicographical order.
    # By using a tuple (-unique_count, word), we can use min()
    # to find the best result.

    best_word = words[0]
    max_unique = -1

    # Sorting strategy: 
    # Primary key: number of unique characters (Descending)
    # Secondary key: lexicographical order (Ascending)

    best_word = min(words, key=lambda w: (-len(set(w)), w))

    return best_word