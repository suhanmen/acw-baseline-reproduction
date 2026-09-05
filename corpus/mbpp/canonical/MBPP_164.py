import math 
def divSum(n): 
    sum = 1; 
    i = 2; 
    while(i * i <= n): 
        if (n % i == 0): 
            sum = (sum + i +math.floor(n / i)); 
        i += 1; 
    return sum; 
def areEquivalent(num1,num2): 
    return divSum(num1) == divSum(num2); 