def count_pairs(arr, n, k):
    """
    Counts the number of distinct pairs (a, b) in an array such that 
    the absolute difference between a and b is exactly k.

    Note: The problem interpretation for 'distinct' based on the 
    provided test cases implies pairs of indices (i, j) such that i < j
    and |arr[i] - arr[j]| == k.
    """
    count = 0
    # Using a frequency map to handle potential duplicate values 
    # in the array while maintaining the count of valid pairs.
    # However, the assertions suggest we are counting pairs of indices.
    # Let's re-examine:
    # [1, 5, 3, 4, 2], k=3: (1,4), (5,2) -> count 2. 
    # (Actually, it looks like it checks every element x to see if x+k exists)

    # Based on assertion 3: [2, 4, 1, 3, 4], k=2 
    # Pairs: (2,4), (4,2), (1,3), (3,1), (4,2) -- wait.
    # Let's look at [2, 4, 1, 3, 4], k=2 again.
    # Pairs with diff 2: (2,4) at indices (0,1), (2,4) at indices (0,4), 
    # (1,3) at indices (2,3). Total 3.

    # This means we count pairs of indices (i, j) where i < j and |arr[i] - arr[j]| == k.

    # Implementation:
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) == k:
                count += 1
    return count