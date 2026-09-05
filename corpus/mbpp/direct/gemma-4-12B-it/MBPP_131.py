def reverse_vowels(s: str) -> str:
    """
    Reverses only the vowels in a given string.
    """
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        if chars[left] not in vowels:
            left += 1
        elif chars[right] not in vowels:
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)

if __name__ == "__main__":
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"