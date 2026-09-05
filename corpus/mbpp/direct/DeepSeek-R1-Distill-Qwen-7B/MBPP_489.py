def frequency_Of_Largest(n, arr):
    if not arr:
        return 0  # Assuming handling empty array case as per problem requirements

    max_val = max(arr)
    return arr.count(max_val)