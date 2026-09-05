def float_sort(t):
    # Extracting the second element of each tuple and converting to float
    # Then sorting the original tuples based on these extracted values in descending order
    return sorted(t, key=lambda x: float(x[1]), reverse=True)