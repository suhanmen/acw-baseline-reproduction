def find_even_Pair(lst, n):
    even = 0
    odd = 0
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even * (even - 1) // 2) + (odd * (odd - 1) // 2)