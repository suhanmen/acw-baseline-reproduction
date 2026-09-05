def find_even_Pair(A,N): 
    evenPair = 0
    for i in range(0,N): 
        for j in range(i+1,N): 
            if ((A[i] ^ A[j]) % 2 == 0): 
                evenPair+=1
    return evenPair; 