def is_integer(x: float) -> bool:
    """
    Check if a floating-point number is mathematically an integer.
    This handles edge cases like 5.0 being True and 5.5 being False.
    It also handles negative numbers correctly.
    """
    return float(x).is_integer()


def calculate_first_term(target: int, factor: int) -> int:
    """
    Given a target number and a factor, calculates the 'a' term
    in the equation: target = (a - b) * (a + b) = a^2 - b^2.

    Let product = target.
    We are looking for two factors, f1 and f2, such that:
    f1 * f2 = target
    And f2 - f1 = 2 * b (where b is an integer).
    This implies f2 and f1 must have the same parity (both even or both odd)
    so their difference is even.

    We iterate through factors.
    Let factor be f1 (the smaller factor).
    Then f2 = target / factor.

    We need to check if (f2 - f1) is divisible by 2 and non-negative.
    Actually, since target can be negative, we need to be careful.
    However, if target is positive, f2 >= f1 naturally if we iterate from 1 up to sqrt(target).
    If target is negative, let's say target = -15.
    We need a^2 - b^2 = -15 => b^2 - a^2 = 15.
    This is symmetric to the positive case, just swapping a and b roles effectively.
    Mathematically, x = y^2 - z^2 is possible iff x is odd or x is a multiple of 4.
    So -15 (odd) is possible. -16 (mult of 4) is possible. -14 (even not mult of 4) is not.

    The logic simplifies to checking parity properties of the number itself.
    However, to follow the "difference of two squares" derivation explicitly as requested by the problem style:
    We look for factors.

    For a general integer N:
    N = (u - v) * (u + v)
    Let A = u + v and B = u - v.
    Then A * B = N.
    Also, A + B = 2u and A - B = 2v.
    For u and v to be integers, (A + B) must be even and (A - B) must be even.
    This implies A and B must have the same parity.
    Since A * B = N, if N is odd, both A and B must be odd (same parity).
    If N is even, for A and B to have the same parity, both must be even (because if one is odd, the other is even, different parity).

    So:
    1. If N is odd, we just need to find at least one pair of factors (A, B). Since 1 and N are always factors, and both are odd, they work.
       Exception: We need N > 0 for 1 and N to be positive factors? 
       Wait, factors can be negative too.
       (-1) * (-15) = 15. Both odd.
       (-1) * 15 = -15. Different parity? No, -1 is odd, 15 is odd. Sum = 14 (even), Diff = 16 (even). Works.

    2. If N is even, N must be divisible by 4 to have two even factors.
       If N % 2 == 0 and N % 4 != 0 (i.e., N is 2 * odd), then any factorization will result in one even and one odd factor.
       Example: N = 6. Factors: 1*6 (odd, even), 2*3 (even, odd). No pair with same parity.
       Example: N = 4. Factors: 1*4 (odd, even), 2*2 (even, even). Pair (2,2) works.
       Example: N = 8. Factors: 1*8, 2*4. Pair (2,4) works (both even).

    Therefore, the condition is strictly:
    - If N is odd, it can be represented (unless N=0? 0 = 1^2 - 1^2. Yes. Unless we restrict positive squares? Problem doesn't say positive integers only for bases).
    - If N is even, it can be represented IF AND ONLY IF N is divisible by 4.

    Special case: N = 0.
    0 = 0^2 - 0^2. Also 1^2 - 1^2. True.

    Let's re-verify the logic with the explicit factorization method to ensure no edge cases are missed by the shortcut, although the shortcut is mathematically sound.
    We will implement the explicit factor search to adhere to the "spell out steps" requirement, but optimize it to stop early.

    However, for very large numbers, iterating to sqrt(N) might be slow if we aren't careful, but for this problem context, it's standard.
    Actually, the mathematical derivation is O(1). The factor search is O(sqrt(N)).
    Given the requirement for "thorough, defensive" code and "explicit steps", we can implement the check based on the derived property, but we should probably justify it or implement the search if "how" is implied.
    But the problem asks to "check whether...". The most efficient and correct way is the property check.
    Property: A number x can be written as a difference of two squares iff x is not of the form 2 * (odd number).
    i.e., x % 2 != 0 OR x % 4 == 0.

    Let's double check negative numbers.
    x = -5. -5 = 2^2 - 3^2 = 4 - 9 = -5. (2 is even, 3 is odd -> ok).
    Using formula: -5 is odd. Condition holds.
    x = -10. -10 = 2 * (-5). Even but not div by 4.
    Can -10 be written as a^2 - b^2?
    a^2 - b^2 = -10 => b^2 - a^2 = 10.
    10 = 2 * 5. No two factors of 10 have same parity.
    So -10 is False.
    Formula check: -10 % 4 is 2. Condition fails. Correct.

    So the algorithm is:
    1. Handle input validation.
    2. Check if number is 0 -> True.
    3. Check parity.
       If odd -> True.
       If even -> Check if divisible by 4.
         If yes -> True.
         If no -> False.

    This covers all cases efficiently and explicitly.
"""

def can_be_difference_of_squares(number: int) -> bool:
    """
    Determines if a given integer can be represented as the difference of two squares of integers.

    Logic:
    x = a^2 - b^2 = (a-b)(a+b)
    Let u = a-b, v = a+b. Then x = u*v.
    Also v - u = (a+b) - (a-b) = 2b.
    For b to be an integer, (v - u) must be even.
    This means u and v must have the same parity (both even or both odd).

    Case 1: x is odd.
    Any factorization of an odd number consists of two odd numbers.
    Since 1 and x are always factors (for non-zero), and both are odd, we can always find a solution.
    For x = 1: 1 = 1^2 - 0^2.
    For x = -1: -1 = 0^2 - 1^2.
    So all odd integers return True.

    Case 2: x is even.
    For u and v to have the same parity when their product is even, they MUST both be even.
    (They cannot be both odd, because odd * odd = odd).
    So x must be divisible by 2 * 2 = 4.
    If x is even but not divisible by 4 (i.e., x = 2 * odd), no such u, v exist.

    Special Case: x = 0.
    0 = 0^2 - 0^2. True.
    Also 0 = 1^2 - 1^2.

    Summary Condition:
    True if (x is odd) OR (x is divisible by 4).
    False otherwise (which covers x = 2 * odd).

    Args:
        number: The integer to check. Can be negative, zero, or positive.

    Returns:
        True if the number can be represented as the difference of two squares, False otherwise.
    """
    # Input validation: Ensure the input is an integer type.
    # Although the type hint says int, defensive coding requires checking runtime types.
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, got {type(number).__name__}")

    # Explicitly handle the zero case, though the formula covers it (0 is divisible by 4).
    # 0 % 4 is 0, so the formula works for 0 too.
    # However, explicit handling makes the logic clearer for readers.
    if number == 0:
        return True

    # Check if the number is odd.
    # An odd number can always be expressed as difference of squares.
    # Example: 5 = 3^2 - 2^2 = 9 - 4 = 5.
    if number % 2 != 0:
        return True

    # If the number is even, it must be divisible by 4.
    # Example: 4 = 2^2 - 0^2 = 4.
    # Example: 8 = 3^2 - 1^2 = 9 - 1 = 8.
    # Example: 10 = 2 * 5 (not div by 4) -> False.
    if number % 4 == 0:
        return True

    # If we reach here, the number is even but not divisible by 4.
    # Example: 2, 6, 10, 14, -2, -6, etc.
    # These cannot be represented as a difference of two squares.
    return False


def main():
    """
    Main function to demonstrate the usage and validate against provided assertions.
    """
    # Test Case 1: 5 (Odd) -> Expected True
    result_5 = can_be_difference_of_squares(5)
    assert result_5 == True, f"Test failed for 5: expected True, got {result_5}"

    # Test Case 2: 10 (Even, not div by 4) -> Expected False
    result_10 = can_be_difference_of_squares(10)
    assert result_10 == False, f"Test failed for 10: expected False, got {result_10}"

    # Test Case 3: 15 (Odd) -> Expected True
    result_15 = can_be_difference_of_squares(15)
    assert result_15 == True, f"Test failed for 15: expected True, got {result_15}"

    # Additional Edge Cases for thoroughness
    # Zero
    assert can_be_difference_of_squares(0) == True

    # Negative Odd
    assert can_be_difference_of_squares(-5) == True

    # Negative Even (div by 4)
    assert can_be_difference_of_squares(-16) == True

    # Negative Even (not div by 4)
    assert can_be_difference_of_squares(-6) == False

    # Minimum integer (if sys limits apply, but logic holds)
    # Large number
    assert can_be_difference_of_squares(1000003) == True  # Odd

    # Large even not div by 4
    assert can_be_difference_of_squares(1000002) == False  # Ends in 2

    # Large even div by 4
    assert can_be_difference_of_squares(1000000) == True

    print("All assertions passed successfully.")


if __name__ == "__main__":
    main()