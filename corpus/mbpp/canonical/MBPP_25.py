def find_Product(arr,n): 
    arr.sort() 
    prod = 1
    for i in range(0,n,1): 
        if (arr[i - 1] != arr[i]): 
            prod = prod * arr[i] 
    return prod; 