def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    def unique_count(word):
        return len(set(word))

    # Sort by (-unique_count, word) to get max unique first, then lexicographical order
    words.sort(key=lambda w: (-unique_count(w), w))
    return words[0]