def decimal_to_Octal(n):
    # Input Validation
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # Handle zero case
    if n == 0:
        return "0"

    # Handle negative numbers
    if n < 0:
        octal_digits = []
        n = abs(n)
        while n > 0:
            remainder = n % 8
            octal_digits.append(remainder)
            n = n // 8
        # Prepend the negative sign
        octal_str = "-" + "".join(map(str, octal_digits))
        print(f"Negative number handled: {n} -> {octal_str}")
        return octal_str

    # Conversion Process
    octal_digits = []
    while n > 0:
        remainder = n % 8
        octal_digits.append(remainder)
        n = n // 8

    # Join the digits to form the octal string
    octal_str = "".join(map(str, octal_digits))
    print(f"Positive number handled: {n} -> {octal_str}")
    return octal_str

# Test Cases
print(decimal_to_Octal(10))    # Should output "12"
print(decimal_to_Octal(2))     # Should output "2"
print(decimal_to_Octal(33))    # Should output "41")