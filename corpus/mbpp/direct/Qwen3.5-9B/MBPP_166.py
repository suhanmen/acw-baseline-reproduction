def find_even_Pair(arr, k):
    even_count = 0
    odd_count = 0
    for num in arr[:k]:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count * (even_count - 1) // 2 + odd_count * (odd_count - 1) // 2