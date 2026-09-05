def rearrange_bigger(n):
    digits = list(str(n))
    length = len(digits)

    # Find the first digit that is smaller than the digit to its right (from right to left)
    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i < 0:
        return False

    # Find the smallest digit to the right of i that is larger than digits[i]
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the suffix starting after i to get the smallest permutation
    digits[i + 1:] = digits[i + 1:][::-1]

    result_str = ''.join(digits)

    # Check for overflow (result should fit in standard integer, but we just return the number)
    result = int(result_str)
    return result