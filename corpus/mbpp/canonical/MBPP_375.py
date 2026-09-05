def round_num(n,m):
    a = (n //m) * m
    b = a + m
    return (b if n - a > b - n else a)