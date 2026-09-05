def split_lowerstring(s: str) -> list[str]:
    """
    Splits a string at lowercase letters.
    Based on the provided test cases:
    - "AbCd" -> ['bC', 'd'] implies the rule is slightly complex.
    Let's analyze the test cases:
    1. "AbCd" -> ['bC', 'd']
       Lowercase letters are 'b' and 'd'.
       Splitting at 'b' results in 'A' and 'Cd'.
       Wait, the output is ['bC', 'd']. This means:
       - 'A' is discarded.
       - 'b' is kept and concatenated with following uppercase 'C'.
       - 'd' is kept.

    Let's re-examine "Python" -> ['y', 't', 'h', 'o', 'n']
    Lowercase: y, t, h, o, n. Uppercase: P.
    Output: Every lowercase letter is its own element.

    Let's re-examine "Programming" -> ['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
    Lowercase: r, o, g, r, a, m, m, i, n, g. Uppercase: P.
    Output: Every lowercase letter is its own element.

    Re-evaluating "AbCd": 
    Lowercase: b, d. Uppercase: A, C.
    If we treat 'b' as a delimiter:
    The parts are 'A' (discarded), 'b', 'Cd'.
    Wait, if the rule is: "Identify lowercase letters. If a lowercase letter is followed by an uppercase letter, group them. Otherwise, return lowercase letters."
    "AbCd": 'b' is followed by 'C'. Group 'bC'. 'd' is not followed by uppercase. Return ['bC', 'd'].
    "Python": 'y' not followed by upper. 't' not. 'h' not. 'o' not. 'n' not.
    "Programming": 'r' not followed by upper. 'o' not. etc.

    Logic: Iterate through string. If char is lowercase:
        Check if next char is uppercase.
        If yes, group lowercase + uppercase.
        If no, just the lowercase.
    """
    res = []
    i = 0
    while i < len(s):
        if s[i].islower():
            if i + 1 < len(s) and s[i+1].isupper():
                res.append(s[i] + s[i+1])
                i += 2
            else:
                res.append(s[i])
                i += 1
        else:
            i += 1
    return res