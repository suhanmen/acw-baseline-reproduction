def find_Max_Num(digits, num_digits):
    # Handle edge cases for num_digits
    if num_digits < 0:
        raise ValueError("num_digits must be a non-negative integer")
    if num_digits == 0:
        return 0
    if not digits:
        return 0
    if len(digits) != num_digits:
        raise ValueError("The length of digits must equal num_digits")

    # Handle cases where all elements are the same
    if len(set(digits)) == 1:
        return int(''.join(str(d) for d in digits))

    # Sort digits in descending order
    sorted_digits = sorted(digits, reverse=True)

    # Check for all zeros after sorting
    if all(d == 0 for d in sorted_digits):
        return 0

    # Construct the largest number
    largest_number = ''.join(str(d) for d in sorted_digits[:num_digits])

    # Handle case where all digits are zero
    return int(largest_number) if largest_number else 0