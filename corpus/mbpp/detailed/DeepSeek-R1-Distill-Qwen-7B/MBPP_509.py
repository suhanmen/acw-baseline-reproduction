def average_Odd(n):
    # Step 1: Validate the input
    if not isinstance(n, int) or n < 1 or n % 2 == 0:
        return "Invalid input"

    # Step 2: Generate list of odd numbers up to n
    odds = [i for i in range(1, n + 1, 2)]

    # Step 3: Calculate the number of odd numbers
    count = len(odds)

    # Edge case: if there are no odd numbers (shouldn't happen since n >=1 and odd)
    if count == 0:
        return "No odd numbers"

    # Step 4: Calculate the sum of odd numbers
    total = sum(odds)

    # Step 5: Calculate the average
    average = total / count

    # Step 6: Return the average
    return average

# Example usage:
print(average_Odd(9))  # Output: 5.0
print(average_Odd(5))  # Output: 3.0
print(average_Odd(11)) # Output: 6.0