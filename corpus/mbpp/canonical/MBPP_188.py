def prod_Square(n):
    for i in range(2,(n) + 1):
        if (i*i < (n+1)):
            for j in range(2,n + 1):
                if ((i*i*j*j) == n):
                    return True;
    return False;