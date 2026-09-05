def find_remainder(arr, lens, n): 
    mul = 1
    for i in range(lens):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 