def sum_of_digits(numbers):
    """
    Compute the sum of digits of each number in the given list.
    - Negative numbers are treated by ignoring the sign.
    - Non-integer items (like strings) are skipped.
    """
    total = 0
    for n in numbers:
        if isinstance(n, int) and not isinstance(n, bool):
            # Use absolute value to handle negative numbers
            total += sum(int(digit) for digit in str(abs(n)))
        elif isinstance(n, str):
            # For string digits, ignore non-digit characters and sum digits
            total += sum(int(digit) for digit in n if digit.isdigit())
    return total

# Assertions (for verification, not required to be executed as part of the solution):
# assert sum_of_digits([10,2,56])==14
# assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
# assert sum_of_digits([10,20,-4,5,-70])==19