from typing import List

def modular_inverse(elements: List[int], count: int, p: int) -> int:
    """
    Counts array elements whose modular inverse under a given prime p 
    is equal to the element itself.

    The mathematical condition for an element 'x' to satisfy its own 
    modular inverse under modulo 'p' is:
    x * x ≡ 1 (mod p)

    Additionally, for a modular inverse to exist, 'x' must be coprime to 'p'.
    Since 'p' is specified as a prime number, this means x must not be a 
    multiple of p (i.e., x % p != 0).

    Args:
        elements: A list of integers to check.
        count: An integer (unused in logic but required by signature).
        p: The prime number for the modulo operation.

    Returns:
        The count of elements satisfying the condition.

    Raises:
        ValueError: If p is less than 2 (not a prime or not valid for modulo).
    """
    # Input Validation
    if not isinstance(elements, list):
        raise ValueError("The 'elements' argument must be a list of integers.")

    if not isinstance(p, int) or p < 2:
        raise ValueError("The prime 'p' must be an integer greater than or equal to 2.")

    if not isinstance(count, int):
        raise ValueError("The 'count' argument must be an integer.")

    # We want to count elements where (x * x) % p == 1
    # This automatically implies that the modular inverse of x is x.
    # Note: If x % p == 0, (0 * 0) % p is 0, which is not 1, 
    # so we don't need an explicit coprimality check if we use the formula.

    valid_count = 0

    for item in elements:
        # Ensure the item is an integer
        if not isinstance(item, int):
            # Skip non-integers or handle as error; given requirements, 
            # we assume integer list but check for safety.
            continue

        # Step 1: Calculate the value of x modulo p
        # This handles negative numbers and numbers larger than p.
        normalized_x = item % p

        # Step 2: Calculate the square of the normalized value
        square_value = normalized_x * normalized_x

        # Step 3: Check if the square is congruent to 1 modulo p
        remainder_after_square = square_value % p

        if remainder_after_square == 1:
            valid_count += 1

    return valid_count

# The problem description asks for the counts to match specific assertions.
# Assertion 1: [1, 6, 4, 5], p=7. 
# 1^2=1 (True), 6^2=36=1 (True), 4^2=16=2 (False), 5^2=25=4 (False).
# Wait, the assertion says modular_inverse([1, 6, 4, 5], 4, 7) == 2.
# My manual check: 1 and 6 satisfy. Count is 2. Correct.

# Assertion 2: [1, 3, 8, 12, 12], p=13.
# 1^2=1 (True), 3^2=9, 8^2=64=12, 12^2=144. 144/13: 13*11=143. 144%13=1 (True).
# 1 and 12 satisfy. (There are two 12s). Total 3?
# Let's re-check: 1, 3, 8, 12, 12.
# 1^2 % 13 = 1.
# 3^2 % 13 = 9.
# 8^2 % 13 = 64 % 13 = 12.
# 12^2 % 13 = 144 % 13 = 1.
# 12^2 % 13 = 144 % 13 = 1.
# Total count = 3. Correct.

# Assertion 3: [2, 3, 4, 5], p=6. (Note: 6 is not prime, but the logic x^2 % p == 1 still holds).
# 2^2=4, 3^2=9%6=3, 4^2=16%6=4, 5^2=25%6=1.
# Only 5 satisfies. Count = 1. Correct.