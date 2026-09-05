def kth_element(arr, k):
    # Step 1: Check if the array is empty
    if not arr:
        raise ValueError("Array is empty")

    # Step 2: Check if k is a positive integer within bounds
    if not isinstance(k, int) or k <= 0 or k > len(arr):
        raise ValueError("Invalid k value")

    # Step 3: Calculate the index
    index = k - 1

    # Step 4: Return the element at the calculated index
    return arr[index]