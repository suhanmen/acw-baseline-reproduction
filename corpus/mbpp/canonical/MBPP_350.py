def minimum_Length(s) : 
    maxOcc = 0
    n = len(s) 
    arr = [0]*26
    for i in range(n) : 
        arr[ord(s[i]) -ord('a')] += 1
    for i in range(26) : 
        if arr[i] > maxOcc : 
            maxOcc = arr[i] 
    return n - maxOcc 