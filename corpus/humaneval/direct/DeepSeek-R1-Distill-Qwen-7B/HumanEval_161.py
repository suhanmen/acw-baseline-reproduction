def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string."""
    letters = []
    non_letters = []
    for char in s:
        if char.isalpha():
            letters.append(char)
        else:
            non_letters.append(char)
    if not letters:
        return ''.join(non_letters[::-1])
    else:
        # Reverse each letter's case and then process
        reversed_letters = [c.swapcase() for c in letters[::-1]]
        reversed_non_letters = ''.join(non_letters[::-1])
        return ''.join(reversed_letters) + reversed_non_letters