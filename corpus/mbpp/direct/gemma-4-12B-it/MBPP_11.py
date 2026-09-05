def remove_Occ(s: str, char: str) -> str:
    """
    Removes the first and last occurrence of a given character from a string.
    If the character occurs only once, it is removed.
    If it occurs multiple times, both the first and last are removed.
    """
    if char not in s:
        return s

    first_index = s.find(char)
    last_index = s.rfind(char)

    if first_index == last_index:
        # Only one occurrence exists
        return s[:first_index] + s[first_index+1:]
    else:
        # Multiple occurrences exist
        return s[:first_index] + s[first_index+1:last_index] + s[last_index+1:]

if __name__ == "__main__":
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"