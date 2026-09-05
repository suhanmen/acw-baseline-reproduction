def zigzag(n, k):
    from math import comb
    result = 0
    for i in range(k + 1):
        sign = (-1) ** i
        combi = comb(n, i)
        term = (k + 1 - i) ** n
        result += sign * combi * term
    return result