def no_of_subsequences(arr, k):
    """
    Find the number of non-empty subsequences such that the product 
    of their elements is strictly less than k.
    """
    n = len(arr)
    # We use dynamic programming.
    # dp[i][p] could represent number of subsequences using first i elements
    # with product p. However, since k can be large, we use a dictionary
    # or a list of products to store counts of products.

    # count[product] = number of subsequences that result in this product
    counts = {}

    for x in arr:
        new_counts = {}
        # Option 1: Start a new subsequence with just the element x
        if x < k:
            new_counts[x] = new_counts.get(x, 0) + 1

        # Option 2: Append x to all existing subsequences
        for prod, count in counts.items():
            new_prod = prod * x
            if new_prod < k:
                new_counts[new_prod] = new_counts.get(new_prod, 0) + count

        # Merge new_counts into counts
        for prod, count in new_counts.items():
            counts[prod] = counts.get(prod, 0) + count

    return sum(counts.values())

if __name__ == "__main__":
    assert no_of_subsequences([1,2,3,4], 10) == 11
    assert no_of_subsequences([4,8,7,2], 50) == 9
    assert no_of_subsequences([5,6,7,8], 15) == 4