def find_Nth_Digit(numerator, denominator, n):
    """
    Finds the nth digit in the proper fraction of two given numbers.
    The proper fraction is the decimal expansion of numerator/denominator.
    """
    # To find the nth digit after the decimal point, we can shift the decimal
    # point n places to the right by multiplying the fraction by 10^n.
    # The integer part of this result will contain the first n digits.
    # The nth digit is the last digit of this integer part.

    # Example: 1/2 = 0.5, n=1. (1/2) * 10^1 = 5. Last digit is 5.
    # Example: 3/5 = 0.6, n=1. (3/5) * 10^1 = 6. Last digit is 6.
    # Example: 5/6 = 0.8333..., n=5. (5/6) * 10^5 = 83333.333... 
    # The first 5 digits are 83333. The 5th digit is 3.

    # We use integer arithmetic to avoid floating point precision issues.
    # (numerator * 10^n) // denominator gives the first n digits.
    # The nth digit is then the last digit of that result.

    current_numerator = numerator * (10**n)
    integer_part = current_numerator // denominator

    # The nth digit is the remainder when dividing by 10.
    # However, if we want the digit at position n, we need to be careful.
    # Let's trace 5/6, n=5:
    # 5 * 10^5 = 500000
    # 500000 // 6 = 83333
    # 83333 % 10 = 3 (Correct)

    return integer_part % 10

if __name__ == "__main__":
    assert find_Nth_Digit(1, 2, 1) == 5
    assert find_Nth_Digit(3, 5, 1) == 6
    assert find_Nth_Digit(5, 6, 5) == 3