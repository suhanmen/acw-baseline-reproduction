def frequency_Of_Smallest(n,arr): 
    mn = arr[0] 
    freq = 1
    for i in range(1,n): 
        if (arr[i] < mn): 
            mn = arr[i] 
            freq = 1
        elif (arr[i] == mn): 
            freq += 1
    return freq 