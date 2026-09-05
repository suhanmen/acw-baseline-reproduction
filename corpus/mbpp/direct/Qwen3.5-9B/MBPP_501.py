def num_comm_div(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return gcd(a, b)