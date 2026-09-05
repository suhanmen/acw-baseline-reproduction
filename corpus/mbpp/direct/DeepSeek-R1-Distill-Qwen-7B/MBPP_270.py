def sum_even_and_even_index(lst):
    total = 0
    for index, number in enumerate(lst):
        if index % 2 == 0 and number % 2 == 0:
            total += number
    return total

# Example usage:
# print(sum_even_and_even_index([5, 6, 12, 1, 18, 8], 6))  # Output: 30
# print(sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18], 10))  # Output: 26
# print(sum_even_and_even_index([5, 6, 12, 1], 4))  # Output: 12