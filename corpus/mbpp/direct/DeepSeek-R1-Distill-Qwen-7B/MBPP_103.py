python
def eulerian_num(n, m):
    from math import comb

    if m < 0 or m >= n:
        return 0
    if m == 0 or m == 1:
        return 1 if m == 0 else comb(n, m)

    result = 0
    for k in range(m, n+1):
        result += (k - m) * comb(n, k)

    return result