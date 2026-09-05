def find_even_Pair(arr, n):
    """
    Counts the number of pairs (i, j) where i < j and (arr[i] ^ arr[j]) is even.
    A XOR operation results in an even number if and only if both numbers 
    have the same parity (both even or both odd).
    """
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Number of pairs from even numbers is C(even_count, 2)
    # Number of pairs from odd numbers is C(odd_count, 2)
    # Combination formula: n * (n - 1) / 2
    pairs = (even_count * (even_count - 1) // 2) + (odd_count * (odd_count - 1) // 2)
    return pairs