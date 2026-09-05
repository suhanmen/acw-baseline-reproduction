import math
from typing import Union

def next_Perfect_Square(n: Union[int, float]) -> int:
    """
    Finds the smallest perfect square integer strictly greater than the given number n.

    Args:
        n (Union[int, float]): The input number to compare against.

    Returns:
        int: The next perfect square greater than n.

    Raises:
        TypeError: If the input is not an int or float.
        ValueError: If the input is a negative number (as perfect squares 
                    are non-negative and the logic depends on real square roots).
    """
    # 1. Input Validation: Check for correct types
    if not isinstance(n, (int, float)):
        raise TypeError(f"Input must be a number, received {type(n).__name__}")

    # 2. Input Validation: Handle negative numbers
    # While math.sqrt(negative) produces complex numbers, the concept of
    # "next perfect square" in this context implies searching in the domain of non-negative integers.
    if n < 0:
        # Smallest perfect square > any negative number is 0.
        # However, many definitions start at 1. Given the standard sequence 0, 1, 4, 9...
        # if n is -5, the next square is 0. If n is -1, it's 0.
        # If the requirement implies strictly positive squares, this would change to 1.
        # We will assume 0 is the first perfect square.
        return 0

    # 3. Calculate the floor of the square root
    # We use math.isqrt for integers to maintain precision, or math.sqrt for floats.
    # To be safe with large floats and ints, we convert n to float for sqrt.
    try:
        current_root_float = math.sqrt(float(n))
    except OverflowError:
        # Handle cases where n is larger than the maximum float
        # This is an edge case for extremely large integers.
        # We can use math.isqrt for integers specifically.
        current_root_float = math.isqrt(int(n))

    # 4. Determine the integer base for the next square
    # If n is 35, sqrt(35) is ~5.91. floor(5.91) = 5. The next root is 6.
    # If n is 9, sqrt(9) is 3.0. We need the next square STRICTLY greater than 9.
    # Therefore, even if n is a perfect square, we must increment the root.

    # Cast to int to get the floor
    base_root = int(current_root_float)

    # Check if n is exactly a perfect square of base_root
    # We use a small epsilon for float comparison or direct check for integers
    is_perfect_square = False
    if base_root * base_root == n:
        is_perfect_square = True
    elif (base_root + 1) * (base_root + 1) == n:
        # This case handles precision issues where float sqrt might be slightly off
        # but results in a perfect square.
        is_perfect_square = True

    if is_perfect_square:
        # If n is 9 (3^2), the next root is 3 + 1 = 4.
        next_root = base_root + 1
    else:
        # If n is 35 (root ~5.91), the next root is floor(5.91) + 1 = 6.
        # However, we must ensure that floor(sqrt(n)) + 1 is actually the next root.
        # Example: if n = 8, sqrt(8) = 2.82. floor is 2. Next root 3. 3^2 = 9. Correct.
        # We need to handle the case where n is between (base_root)^2 and (base_root+1)^2
        next_root = base_root + 1

        # Safety check: if n was 8.1, and base_root was 2, next_root is 3.
        # If n was 8.9, and base_root was 2, next_root is 3.
        # If n was 9.0, the is_perfect_square logic handles it.

        # One edge case: if n is 8.9, sqrt(8.9) is 2.98. 
        # If n is 9.1, sqrt(9.1) is 3.01. base_root is 3. next_root is 4.
        # Let's refine the logic:
        # The next root is the smallest integer r such that r^2 > n.

        # Re-calculating next_root more robustly:
        # Since we need strictly greater than n, we can take the floor of sqrt(n)
        # and add 1, unless n is a perfect square (which we handled).
        # Wait, if n = 8.5, sqrt(8.5) = 2.91, floor is 2, +1 is 3. 3^2 = 9. Correct.
        # If n = 9.0, sqrt(9.0) = 3.0, floor is 3, +1 is 4. 4^2 = 16. Correct.
        pass

    # Re-verifying the logic to ensure it's production-grade and handles floats correctly
    # Let's use a simpler, more robust approach:
    # 1. Find the floor of the square root.
    # 2. Check if (floor_root + 1)^2 is greater than n.
    # 3. If it is, that's our answer.
    # 4. If not (which happens if n is very close to a square but slightly larger),
    #    increment and check again.

    # Let's restart the logic inside the function for clarity:

    # Final logic implementation:
    actual_root_floor = int(math.isqrt(int(n))) if isinstance(n, int) else int(math.sqrt(n))

    # Candidate 1: (actual_root_floor + 1)^2
    candidate_root = actual_root_floor + 1
    candidate_square = candidate_root * candidate_root

    # If candidate_square is not greater than n (due to float precision or 
    # rounding), increment until it is.
    while candidate_square <= n:
        candidate_root += 1
        candidate_square = candidate_root * candidate_root

    return candidate_square

def next_Perfect_Square(n: Union[int, float]) -> int:
    # Re-writing to be extremely explicit and follow all requirements

    # 1. Type Check
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be an integer or a float.")

    # 2. Domain Check
    if n < 0:
        return 0

    # 3. Calculate the integer square root floor
    # We convert to float to handle inputs like 35.5
    # We use math.sqrt and then int() to get the floor
    try:
        root_float = math.sqrt(float(n))
    except OverflowError:
        # For extremely large numbers, use math.isqrt
        root_float = math.isqrt(int(n))

    root_floor = int(root_float)

    # 4. Determine the next integer root
    # We want the smallest integer 'r' such that r*r > n.
    # Start checking from root_floor + 1.
    next_root = root_floor + 1

    # 5. Validation Loop
    # While the square of our candidate root is not strictly greater than n,
    # increment the root. This handles cases where n is very close to a 
    # perfect square or precision issues.
    while True:
        square = next_root * next_root
        if square > n:
            return square
        next_root += 1