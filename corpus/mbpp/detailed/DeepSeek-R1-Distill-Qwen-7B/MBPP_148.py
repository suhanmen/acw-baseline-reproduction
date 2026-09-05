def sum_digits_twoparts(n):
    if n == 0:
        return 0

    digits = list(str(n))
    max_sum = 0

    # Try all possible splits
    for i in range(len(digits)):
        # Create the first number by reducing the i-th digit and setting the rest to 9
        new_digits = []
        for j in range(len(digits)):
            if j == i:
                # Reduce the current digit by 1
                new_digit = str(int(digits[j]) - 1)
                new_digits.append(new_digit)
            else:
                # Set all digits after to 9
                new_digits.append('9')

        # Check if the new_digits start with '0's
        if new_digits[0] == '0' and i == 0:
            continue

        a = int(''.join(new_digits))
        b = n - a

        # Calculate the sum of digits of a and b
        sum_digits = sum(int(d) for d in str(a)) + sum(int(d) for d in str(b))
        if sum_digits > max_sum:
            max_sum = sum_digits

    return max_sum

# Test cases
print(sum_digits_twoparts(35))  # Expected output: 17
print(sum_digits_twoparts(7))   # Expected output: 7
print(sum_digits_twoparts(100))  # Expected output: 19