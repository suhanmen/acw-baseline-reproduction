def check_last(arr, p, n):
    # Perform the operation p times on the nth element (0-based index)
    for _ in range(p):
        # Toggle the element's parity (even/odd) each time
        arr[arr.index(n % 2)] ^= 1

    # Check the parity of the last element
    last = arr[-1]
    if last % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Example usage:
# check_last([5,7,10],3,1) should return "ODD"
# check_last([2,3],2,3) should return "EVEN"
# check_last([1,2,3],3,1) should return "ODD"