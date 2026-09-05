def max_Product(arr):
    # Step 1: Input Validation
    if len(arr) < 2:
        return None

    # Step 2: Generate all possible pairs and calculate their products
    pairs = [(arr[i], arr[j], i, j) for i in range(len(arr)) for j in range(i+1, len(arr))]

    # Step 3: Filter out invalid pairs (if any)
    valid_pairs = [pair for pair in pairs if pair[0] != 0 or pair[1] != 0]

    # Step 4: If there are only zeros, return the two largest zeros
    if len(valid_pairs) == 0 and all(x == 0 for x in arr):
        return (max(arr), max(arr))

    # Step 5: Find the pair with the maximum product
    max_pair = None
    max_product = float('-inf')
    for pair in valid_pairs:
        product = pair[0] * pair[1]
        if product > max_product or (product == max_product and (pair[2], pair[3]) > max_pair):
            max_product = product
            max_pair = (pair[2], pair[3])

    # Step 6: If there are multiple pairs with the same maximum product, return the one with the highest indices
    if max_pair is None:
        return None

    # Step 7: Return the values of the pair instead of their indices
    return (arr[max_pair[2]], arr[max_pair[3]])