def does_Contain_B(a, b, c):
    def is_present(n):
        if n == 0:
            return True
        k = round((n)**(1/3))
        if k**3 + k == n:
            return True
        if (k-1)**3 + (k-1) == n:
            return True
        if (k+1)**3 + (k+1) == n:
            return True
        return False

    for k in range(-abs(c), abs(c) + 1):
        if is_present(k**3 + k):
            return True
    return False

assert does_Contain_B(1,7,3) == True
assert does_Contain_B(1,-3,5) == False
assert does_Contain_B(3,2,5) == False