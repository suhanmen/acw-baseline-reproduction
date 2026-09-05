def find_Sum(arr,n): 
    return sum([x for x in arr if arr.count(x) > 1])