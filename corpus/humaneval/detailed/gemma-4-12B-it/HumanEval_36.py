import math

def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Handle numbers where no positive integers less than n exist
    # The problem implies we are looking at positive integers or standard natural numbers.
    # Integers less than n are 0, 1, ..., n-1. 
    # Since "divisible by 11 or 13" usually refers to positive multiples in these types of puzzles,
    # but mathematically 0 is divisible by everything. However, 0 contains no '7'.
    # We will iterate through all integers from 1 to n-1 to be safe and clear.
    if n <= 1:
        return 0

    def is_divisible_by_11_or_13(number: int) -> bool:
        """Check if a number is divisible by 11 or 13."""
        is_divisible_by_11 = (number % 11 == 0)
        is_divisible_by_13 = (number % 13 == 0)
        return is_divisible_by_11 or is_divisible_by_13

    def count_sevens_in_number(number: int) -> int:
        """Count occurrences of the digit '7' in the decimal representation of a number."""
        # Convert to string to easily iterate over digits
        # We use absolute value to handle negative numbers if they were to occur
        string_representation = str(abs(number))
        count = 0
        for char in string_representation:
            if char == '7':
                count += 1
        return count

    total_seven_count = 0

    # Iterate through every integer strictly less than n.
    # Based on the doctest:
    # fizz_buzz(78) -> integers < 78. 
    # Multiples of 11: 11, 22, 33, 44, 55, 66, 77 (one 7)
    # Multiples of 13: 13, 26, 39, 52, 65, 78 (78 is not < 78)
    # Wait, let's re-check the doctest logic:
    # fizz_buzz(78): numbers < 78 divisible by 11 or 13.
    # Multiples of 11 < 78: 11, 22, 33, 44, 55, 66, 77. (77 has one '7')
    # Multiples of 13 < 78: 13, 26, 39, 52, 65. (No '7's)
    # Total '7's = 1. 
    # Hmm, the doctest says fizz_buzz(78) is 2. 
    # Let's re-evaluate. 
    # If fizz_buzz(78) is 2, and fizz_buzz(79) is 3...
    # The difference between 78 and 79 is the inclusion of 78 itself.
    # 78 / 13 = 6. 78 contains one '7' at the start? No, 78 is 7 and 8.
    # 78 contains one '7'. 
    # If fizz_buzz(78) = 2, maybe it includes 0? No, 0 doesn't have 7.
    # Maybe it includes 77? 77 / 11 = 7. 77 has two '7's.
    # Let's re-calculate:
    # Multiples of 11 < 78: 11, 22, 33, 44, 55, 66, 77.
    # 77 contains two 7s. 
    # Multiples of 13 < 78: 13, 26, 39, 52, 65. 
    # Total 7s = 2. (This matches fizz_buzz(78) == 2).
    # For fizz_buzz(79): numbers < 79 include 78.
    # 78 is divisible by 13. 78 contains one '7'.
    # Total 7s = 2 (from 77) + 1 (from 78) = 3. (This matches fizz_buzz(79) == 3).

    # Conclusion: The logic is correct. Iterate i from 1 to n-1.
    # We start at 1 because 0 doesn't have the digit 7 and is technically divisible by 11/13.
    # Starting at 0 or 1 doesn't change the result for '7' counts.
    for current_number in range(1, n):
        if is_divisible_by_11_or_13(current_number):
            sevens_in_this_num = count_sevens_in_number(current_number)
            total_seven_count += sevens_in_this_num

    return total_seven_count