def remove_even(s: str) -> str:
    """
    Removes even-indexed characters (0-indexed) from a string.
    Actually, based on the assertions provided:
    "python" -> "pto" (Indices 0, 2, 4 are p, t, o)
    "program" -> "porm" (Indices 0, 2, 4, 6 are p, o, r, m)
    "language" -> "lnug" (Indices 0, 2, 4, 6 are l, n, u, g)
    The problem asks to remove "even characters", but the assertions show 
    it keeps characters at even indices and removes characters at odd indices.
    Wait, let's re-evaluate:
    "python"
    0: p
    1: y
    2: t
    3: h
    4: o
    5: n
    The result is "pto", which are indices 0, 2, 4. 
    The indices being removed are 1, 3, 5 (odd indices).
    In programming contexts, "even characters" usually refers to the position 
    index. If we remove characters at odd indices (1, 3, 5...), we are 
    keeping the even indices.
    """
    return "".join([s[i] for i in range(len(s)) if i % 2 == 0])

if __name__ == "__main__":
    assert remove_even("python") == "pto"
    assert remove_even("program") == "porm"
    assert remove_even("language") == "lnug"