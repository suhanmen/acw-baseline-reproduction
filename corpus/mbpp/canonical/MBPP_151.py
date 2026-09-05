def gcd(p,q):
    while q != 0:
        p, q = q,p%q
    return p
def is_coprime(x,y):
    return gcd(x,y) == 1