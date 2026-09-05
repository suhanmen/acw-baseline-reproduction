from typing import Union

def highest_Power_of_2(n: Union[int, float]) -> int:
    """
    Finds the highest power of 2 that is less than or equal to a given number.

    Args:
        n (Union[int, float]): The input number to evaluate.

    Returns:
        int: The highest power of 2 less than or equal to n.

    Raises:
        ValueError: If the input is less than 1.
        TypeError: If the input is not a numeric type.
    """
    # 1. Input Validation: Type Checking
    # We ensure the input is either an integer or a float.
    if not isinstance(n, (int, float)):
        raise TypeError(f"Input must be a number, but received {type(n).__name__}")

    # 2. Input Validation: Value Range
    # The smallest power of 2 is 2^0 = 1. 
    # If n is less than 1, there is no positive integer power of 2 <= n.
    # We handle this as an error case for clarity.
    if n < 1:
        raise ValueError(f"Input must be at least 1. Received: {n}")

    # 3. Handle edge case: n is exactly 1
    # 2^0 is the highest power of 2 <= 1.
    if n == 1:
        return 1

    # 4. Algorithm: Iterative approach
    # We start at 1 (which is 2^0) and keep doubling until 
    # the next power of 2 exceeds n.

    current_power_of_2: int = 1
    next_power_of_2: int = 2

    # We use a loop to find the threshold.
    # Since powers of 2 grow exponentially, this is very efficient (O(log n)).
    while next_power_of_2 <= n:
        # Update current_power_of_2 to be the largest power found so far
        current_power_of_2 = next_power_of_2

        # Calculate the next power of 2
        next_power_of_2 = current_power_of_2 * 2

    return current_power_of_2

# Standard Assertions to verify correctness
if __name__ == "__main__":
    # Test case 1: General case (10 -> 8)
    assert highest_Power_of_2(10) == 8

    # Test case 2: General case (19 -> 16)
    assert highest_Power_of_2(19) == 16

    # Test case 3: Exact power of 2 (32 -> 32)
    assert highest_Power_of_2(32) == 32

    # Additional test cases
    assert highest_Power_of_2(1) == 1
    assert highest_Power_of_2(2) == 2
    assert highest_Power_of_2(3) == 2
    assert highest_Power_of_2(63) == 32
    assert highest_Power_of_2(64) == 64
    assert highest_Power_of_2(1024.5) == 1024