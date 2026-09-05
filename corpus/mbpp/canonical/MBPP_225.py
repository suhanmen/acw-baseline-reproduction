def find_Min(arr,low,high): 
    while (low < high): 
        mid = low + (high - low) // 2;   
        if (arr[mid] == arr[high]): 
            high -= 1; 
        elif (arr[mid] > arr[high]): 
            low = mid + 1; 
        else: 
            high = mid; 
    return arr[high]; 