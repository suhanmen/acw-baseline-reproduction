from typing import List

def find_Nth_Digit(numerator: int, denominator: int, n: int) -> int:
    """
    Finds the nth digit in the fractional part of the decimal representation 
    of a fraction (numerator / denominator).

    For example:
    1/2 = 0.5 -> 1st digit is 5
    3/5 = 0.6 -> 1st digit is 6
    5/6 = 0.8333... -> 5th digit is 3 (since the digits are 8, 3, 3, 3, 3, ...)

    Note: The problem implies n is 1-indexed.
    """
    # Input Validation
    if not isinstance(numerator, int) or not isinstance(denominator, int) or not isinstance(n, int):
        raise TypeError("All inputs must be integers.")

    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")

    if n <= 0:
        raise ValueError("n must be a positive integer (1-indexed).")

    # Handle sign and normalization
    # The "proper fraction" usually refers to the decimal part.
    # We treat the absolute values to find the digits.
    num = abs(numerator)
    den = abs(denominator)

    # A proper fraction is strictly less than 1.
    # If numerator >= denominator, we only care about the fractional part.
    # e.g., 7/3 = 2.333... -> proper fraction part is 0.333...
    num = num % den

    # Edge case: If num is 0, the fraction is 0.000...
    if num == 0:
        return 0

    # To find the n-th digit after the decimal point:
    # Multiplying by 10 shifts the decimal point one place to the right.
    # For 1/2 (0.5), 1st digit:
    # 1/2 * 10 = 5.0 -> integer part is 5.
    # For 5/6 (0.8333...), 5th digit:
    # We need to move the decimal 5 places.
    # (5/6) * 10^5 = 500000 / 6 = 83333.333...
    # The 5th digit is the last digit before the decimal point of this result.

    # Step 1: Calculate the multiplier 10^n
    # We use power of 10 to shift the nth digit to the units place.
    multiplier = 10 ** n

    # Step 2: Calculate the numerator after shifting
    # This represents (numerator / denominator) * 10^n
    shifted_numerator = num * multiplier

    # Step 3: Perform integer division to find the value up to the units place
    # Example: 5/6 * 10^5 = 83333.333... 
    # integer division gives 83333
    total_value_at_n = shifted_numerator // den

    # Step 4: Extract the units digit
    # 83333 % 10 = 3
    nth_digit = total_value_at_n % 10

    return int(nth_digit)

if __name__ == "__main__":
    # The following assertions are provided by the problem description
    assert find_Nth_Digit(1, 2, 1) == 5
    assert find_Nth_Digit(3, 5, 1) == 6
    assert find_Nth_Digit(5, 6, 5) == 3