def max_product(arr, n):
    # Input validation
    if not arr:
        return 0
    if n <= 0 or n > len(arr):
        return 0

    # Handle cases where all elements are negative
    if all(x < 0 for x in arr):
        if n % 2 == 1:
            return max(arr) ** n
        else:
            return (max(arr) ** n) if max(arr) > 0 else 0

    # Sort the array to facilitate finding increasing subsequences
    sorted_arr = sorted(arr)
    max_prod = float('-inf')

    # Iterate through the sorted array with a sliding window of size n
    for i in range(len(sorted_arr) - n + 1):
        window = sorted_arr[i:i+n]
        # Check if the window is increasing
        increasing = True
        for j in range(1, len(window)):
            if window[j] <= window[j-1]:
                increasing = False
                break
        if increasing:
            current_product = 1
            for num in window:
                current_product *= num
            if current_product > max_prod:
                max_prod = current_product

    # Return the maximum product found
    return max_prod if max_prod != float('-inf') else 0