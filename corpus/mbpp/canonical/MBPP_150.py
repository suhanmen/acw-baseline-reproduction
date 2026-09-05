def does_Contain_B(a,b,c): 
    if (a == b): 
        return True
    if ((b - a) * c > 0 and (b - a) % c == 0): 
        return True
    return False