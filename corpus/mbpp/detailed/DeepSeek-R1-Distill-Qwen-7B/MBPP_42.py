def find_Sum(arr):
    # Handle empty array case
    if not arr:
        return 0

    # Create a dictionary to count occurrences of each element
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    # Calculate the sum of repeated elements
    total = 0
    for num, count in counts.items():
        if count > 1:
            total += num * count

    return total

# Test cases
print(find_Sum([1,2,3,1,1,4,5,6]))  # Expected output: 3
print(find_Sum([1,2,3,1,1]))         # Expected output: 3
print(find_Sum([1,1,2]))              # Expected output: 2
print(find_Sum([]))                    # Expected output: 0
print(find_Sum([5,5]))                # Expected output: 10
print(find_Sum([0,0]))                # Expected output: 0
print(find_Sum([-1, -1, 2]))         # Expected output: -2