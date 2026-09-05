def get_Inv_Count(arr,n): 
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1,n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 