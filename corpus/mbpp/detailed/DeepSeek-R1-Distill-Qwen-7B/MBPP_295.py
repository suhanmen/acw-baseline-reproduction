def sum_div(number):
    # Step 1: Input Validation
    if not isinstance(number, int) or number <= 0:
        return 0

    # Step 2: Initialize variables
    divisors = set()  # Using a set to avoid duplicates
    sqrt_number = int(number ** 0.5)

    # Loop through possible divisors up to the square root of the number
    for i in range(1, sqrt_number + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)

    # Step 3: Sum all divisors
    divisor_sum = sum(divisors)

    # Step 4: Return the result
    return divisor_sum

# Test the function with the provided assertions
assert sum_div(8) == 15, "Test case 8 failed"
assert sum_div(12) == 28, "Test case 12 failed"
assert sum_div(7) == 8, "Test case 7 failed"
print("All test cases passed")