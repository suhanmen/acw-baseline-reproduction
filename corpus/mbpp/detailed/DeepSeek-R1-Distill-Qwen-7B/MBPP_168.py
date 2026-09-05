def frequency(arr, number):
    # Handle the case where the array is empty
    if not arr:
        return 0

    # Handle the case where the number is not in the array
    if number not in arr:
        return 0

    # Handle the case where all elements are the same
    if all(e == arr[0] for e in arr):
        return len(arr)

    # Count the frequency of the number in the array
    count = 0
    for num in arr:
        if num == number:
            count += 1

    return count

# Example usage:
print(frequency([1,2,3],4))          # Output: 0
print(frequency([1,2,2,3,3,3,4],3))  # Output: 3
print(frequency([0,1,2,3,1,2],1))    # Output: 2