def no_of_subsequences(arr, k):
    """
    Calculate the number of non-empty subsequences in a non-negative array where the product of elements is smaller than k.

    Args:
        arr (list of int): The input array.
        k (int): The target product value.

    Returns:
        int: The number of valid subsequences.
    """
    # Input validation
    if not arr or k <= 0:
        return 0 if k <= 0 else len(arr) if all(num == 0 for num in arr) else 0

    # Handle special cases
    n = len(arr)
    if n == 0:
        return 0

    if k == 1:
        return 0

    # Generate all possible non-empty subsequences and count those with product < k
    def count_subsequences(index, current_product):
        if index == n:
            return 0 if current_product >= k else 1
        # Exclude the current element
        exclude = count_subsequences(index + 1, current_product)
        # Include the current element if it doesn't make the product exceed k
        include = 0
        if current_product * arr[index] < k:
            include = count_subsequences(index + 1, current_product * arr[index])
        return exclude + include

    total = count_subsequences(0, 1)
    return total