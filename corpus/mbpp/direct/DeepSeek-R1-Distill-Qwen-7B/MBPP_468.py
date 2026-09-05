def max_product(arr, k):
    import itertools
    n = len(arr)
    max_prod = 0
    # Generate all possible combinations of size k and check for increasing sequences
    for combo in itertools.combinations(arr, k):
        if len(set(combo)) == k and all(combo[i] < combo[i+1] for i in range(k-1)):
            product = 1
            for num in combo:
                product *= num
            if product > max_prod:
                max_prod = product
    return max_prod

# Example usage:
assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000 
assert max_product([4, 42, 55, 68, 80], 5) == 50265600
assert max_product([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000