def count_Squares(m,n): 
    if (n < m): 
        temp = m 
        m = n 
        n = temp 
    return n * (n + 1) * (3 * m - n + 1) // 6