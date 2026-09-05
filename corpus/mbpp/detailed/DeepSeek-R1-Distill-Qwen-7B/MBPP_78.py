def count_With_Odd_SetBits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n < 0:
        return 0

    count = 0
    for num in range(n + 1):
        binary_str = bin(num)
        ones = binary_str.count('1')
        if ones % 2 == 1:
            count += 1
    return count

# Test cases
assert count_With_Odd_SetBits(5) == 3
assert count_With_Odd_SetBits(10) == 5
assert count_With_Odd_SetBits(15) == 8