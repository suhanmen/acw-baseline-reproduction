def count_Digits(number):
    # Input validation: check if the input is an integer
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")

    # Handle the case of zero explicitly
    if number == 0:
        return 1

    # Convert the number to its absolute value to handle negatives
    num = abs(number)

    # Initialize the count of digits
    digit_count = 0

    # Loop until all digits are processed
    while num > 0:
        num = num // 10
        digit_count += 1

    return digit_count

# Test the function with the given examples
assert count_Digits(12345) == 5, "Test case 1 failed"
assert count_Digits(11223305) == 8, "Test case 2 failed"
assert count_Digits(4123459) == 7, "Test case 3 failed"

print("All test cases passed successfully!")