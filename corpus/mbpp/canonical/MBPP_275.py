import math as mt 
def get_Position(a,n,m): 
    for i in range(n): 
        a[i] = (a[i] // m + (a[i] % m != 0))  
    result,maxx = -1,-1
    for i in range(n - 1,-1,-1): 
        if (maxx < a[i]): 
            maxx = a[i] 
            result = i 
    return result + 1