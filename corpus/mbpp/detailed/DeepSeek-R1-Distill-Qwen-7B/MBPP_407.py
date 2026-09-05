def rearrange_bigger(number):
    """
    Finds the next bigger number by rearranging the digits of the given number.
    Returns False if it's not possible.
    """
    # Handle negative numbers by returning False
    if number < 0:
        return False

    # Convert the number into a list of its digits
    digits = list(str(abs(number)))
    length = len(digits)

    # Iterate to find the first digit that can be swapped
    pivot = -1
    for i in range(length - 1):
        if digits[i] < digits[i + 1]:
            pivot = i
            break

    # If no pivot is found, the number is in descending order
    if pivot == -1:
        return False

    # Find the smallest digit greater than the pivot digit in the suffix
    for j in range(length - 1, pivot, -1):
        if digits[j] > digits[pivot]:
            break

    # Swap the pivot with the found digit
    digits[pivot], digits[j] = digits[j], digits[pivot]

    # Reverse the suffix to get the smallest possible number
    digits[pivot + 1:] = digits[pivot + 1:][::-1]

    # Convert back to number
    next_num = int(''.join(digits))

    # Check for leading zeros
    if next_num < number or digits[0] == '0':
        return False

    return next_num