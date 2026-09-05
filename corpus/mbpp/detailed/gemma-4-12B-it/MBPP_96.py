import math

def divisor(n: int) -> int:
    """
    Calculates the total number of divisors for a given integer n.

    A divisor of an integer n is an integer d such that n % d == 0.
    The function handles positive integers, zero, and negative integers.

    Args:
        n (int): The integer to check for divisors.

    Returns:
        int: The count of positive divisors.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is zero (as divisor count is undefined/infinite).
    """
    # Step 1: Input Validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    if n == 0:
        # Mathematically, every non-zero integer divides 0.
        # Usually, divisor counts are defined for non-zero integers.
        raise ValueError("The number of divisors for 0 is undefined (infinite).")

    # Step 2: Handle Negative Integers
    # The number of divisors for n is the same as the number of divisors for |n|.
    # We work with the absolute value to simplify the logic.
    target_number = abs(n)

    # Step 3: Handle the base case for 1
    if target_number == 1:
        return 1

    # Step 4: Iterate and count divisors
    # We only need to iterate up to the square root of the target_number.
    # If 'i' is a divisor, then 'target_number / i' is also a divisor.
    divisor_count = 0
    limit = int(math.isqrt(target_number))

    for i in range(1, limit + 1):
        # Check if i is a divisor
        if target_number % i == 0:
            # Case A: i is a divisor.
            # We check if i and (target_number / i) are the same (e.g., 3*3 = 9).
            complement = target_number // i

            if i == complement:
                # It's a perfect square root, count it once.
                divisor_count += 1
            else:
                # i and complement are distinct divisors, count both.
                divisor_count += 2

    return divisor_count

# Standard assertions as required by the problem statement
if __name__ == "__main__":
    assert divisor(15) == 4   # Divisors: 1, 3, 5, 15
    assert divisor(12) == 6   # Divisors: 1, 2, 3, 4, 6, 12
    assert divisor(9) == 3     # Divisors: 1, 3, 9