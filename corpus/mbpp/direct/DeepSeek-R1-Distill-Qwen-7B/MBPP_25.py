def find_Product(arr, n):
    from collections import Counter
    count = Counter(arr)
    non_repeated = [key for key, value in count.items() if value == 1]
    product = 1
    for num in non_repeated:
        product *= num
    return product

# Example usage:
print(find_Product([1,1,2,3],4))  # Output: 6
print(find_Product([1,2,3,1,1],5))  # Output: 6
print(find_Product([1,1,4,5,6],5))  # Output: 120