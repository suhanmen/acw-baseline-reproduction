def gcd(a: int, b: int) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) of two positive integers
    using the Euclidean Algorithm.

    The GCD is the largest positive integer that divides each of the 
    integers without leaving a remainder.
    """

    # --- Input Validation ---

    # Check if the inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    # The problem specifies positive integers. 
    # GCD is typically defined for non-negative integers.
    # We check for <= 0 to strictly follow the "positive" requirement.
    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be positive integers (greater than zero).")

    # --- Logic ---

    # We use the Euclidean Algorithm.
    # The principle is that gcd(a, b) = gcd(b, a % b).
    # This continues until the remainder is zero.

    # We work with local copies to preserve the spirit of input immutability
    # although in Python integers are immutable anyway.
    current_a = a
    current_b = b

    while current_b != 0:
        # Calculate the remainder of current_a divided by current_b
        remainder = current_a % current_b

        # Update current_a to the old current_b
        current_a = current_b

        # Update current_b to the remainder
        current_b = remainder

    # When current_b becomes 0, current_a contains the GCD.
    return current_a

if __name__ == "__main__":
    # These assertions verify the requirements provided in the prompt.
    assert gcd(12, 17) == 1
    assert gcd(4, 6) == 2
    assert gcd(2, 9) == 1