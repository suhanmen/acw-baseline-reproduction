import math

def is_woodall(n: int) -> bool:
    """
    Checks if a given number is a Woodall number.
    A Woodall number is a number of the form n = p * 2^p - 1, 
    where p is a non-negative integer.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a Woodall number, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
    """
    # Input Validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n)}")

    # Woodall numbers are defined for p >= 0.
    # p=0: 0 * 2^0 - 1 = -1
    # p=1: 1 * 2^1 - 1 = 1
    # p=2: 2 * 2^2 - 1 = 7
    # p=3: 3 * 2^3 - 1 = 23
    # p=4: 4 * 2^4 - 1 = 63
    # p=5: 5 * 2^5 - 1 = 159
    # p=6: 6 * 2^6 - 1 = 383

    # Handle the degenerate case of -1 (p=0)
    if n == -1:
        return True

    # Woodall numbers for p >= 1 are all positive.
    # If n is less than 1 and not -1, it cannot be a Woodall number.
    if n < 1:
        return False

    # We need to find if there exists a p such that p * 2^p - 1 = n
    # This is equivalent to p * 2^p = n + 1
    target = n + 1

    # Since we need to check if n is Woodall, we can iterate through 
    # possible values of p. 
    # Because p * 2^p grows exponentially, we will reach n quickly.
    # p=1, 2^1=2, p*2^p=2
    # p=10, 2^10=1024, p*2^p=10240
    # p=20, 2^20=1,048,576, p*2^p=20,971,520

    # We can use a safe upper bound for p.
    # For a 64-bit integer, p would not exceed 60.
    # For very large integers, we iterate until p * 2^p exceeds target.

    p = 1
    while True:
        # Calculate current Woodall component: p * 2^p
        # Using bit shifting for 2^p as it is more efficient and precise for large ints
        power_of_two = 1 << p
        current_product = p * power_of_two

        # If the current value exceeds the target, the number is not a Woodall number
        if current_product > target:
            break

        # If the current value matches the target, n is a Woodall number
        if current_product == target:
            return True

        # Increment p to check the next potential Woodall number
        p += 1

        # Safety break for extremely large inputs to prevent infinite loops 
        # if target logic were somehow flawed, though mathematically this is bounded.
        if p > 1000000: 
            break

    return False