import sys 
def solve(a,n):   
    mx = -sys.maxsize - 1
    for j in range(1,n):  
        if (mx > a[j]):  
            return False  
        mx = max(mx,a[j - 1])    
    return True