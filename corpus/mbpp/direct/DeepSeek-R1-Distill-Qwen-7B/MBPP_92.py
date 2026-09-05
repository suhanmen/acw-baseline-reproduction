def is_undulating(number):
    s = str(number)
    if len(s) == 0:
        return False
    first = s[0]
    second = s[1]
    if first == second:
        return False
    for i in range(2, len(s)):
        if s[i] == first and s[i-1] == second:
            continue
        elif s[i] == second and s[i-1] == first:
            continue
        else:
            return False
    return True

# Test cases
assert is_undulating(1212121) == True
assert is_undulating(1991) == False
assert is_undulating(121) == True