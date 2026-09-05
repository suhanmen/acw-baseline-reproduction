def rearrange_bigger(n):
    s = list(str(n))
    i = len(s) - 1
    while i > 0:
        if s[i] > s[i-1]:
            break
        i -= 1
    if i == 0:
        return False
    j = len(s) - 1
    while s[j] <= s[i-1]:
        j -= 1
    s[i-1], s[j] = s[j], s[i-1]
    s = ''.join(s)
    if s[0] == '0':
        return False
    return int(s)