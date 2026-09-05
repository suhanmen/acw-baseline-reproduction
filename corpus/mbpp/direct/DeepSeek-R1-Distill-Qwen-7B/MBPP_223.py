def is_majority(arr, x, majority):
    # Find the first occurrence of x
    first = arr.index(x)
    # Find the last occurrence of x
    last = arr[::-1].index(x)
    # Count the occurrences of x
    count = last - first + 1
    # Check if the majority condition is met
    return count >= majority