def remove_Occ(s: str, ch: str) -> str:
    if ch not in s:
        return s
    first = s.index(ch)
    last = s.rindex(ch)
    if first == last:
        return s[:first] + s[first + 1:]
    return s[:first] + s[first + 1:last] + s[last + 1:]

assert remove_Occ("hello", "l") == "heo"
assert remove_Occ("abcda", "a") == "bcd"
assert remove_Occ("PHP", "P") == "H"