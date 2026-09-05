from typing import Any

def is_Sum_Of_Powers_Of_Two(n: Any) -> bool:
    """
    Checks whether a given number can be represented as a sum of 
    distinct non-zero powers of 2.

    Wait, looking at the requirements and assertions provided:
    assert is_Sum_Of_Powers_Of_Two(10) == True  -> 10 = 2^3 + 2^1 (8 + 2)
    assert is_Sum_Of_Powers_Of_Two(7) == False   -> 7 = 2^2 + 2^1 + 2^0 (4 + 2 + 1)
    assert is_Sum_Of_Powers_Of_Two(14) == True   -> 14 = 2^3 + 2^2 + 2^1 (8 + 4 + 2)

    Analysis of the assertions:
    - 10 (binary 1010): Sum of 2 powers of 2 (2^3, 2^1). True.
    - 7 (binary 0111): Sum of 3 powers of 2 (2^2, 2^1, 2^0). False.
    - 14 (binary 1110): Sum of 3 powers of 2 (2^3, 2^2, 2^1). True.

    Wait, the prompt asks: "sum of non-zero powers of 2".
    In mathematics, "non-zero powers of 2" usually refers to 2^k where k >= 0 (1, 2, 4, 8...).
    However, the logic in the assertions suggests a specific constraint:
    10 is True (2 powers), 7 is False (3 powers), 14 is True (3 powers).

    Wait, let's re-examine the assertions:
    10 in binary is 1010. It has two 1s.
    7 in binary is 0111. It has three 1s.
    14 in binary is 1110. It has three 1s.

    If 14 is True and 7 is False, the difference is the presence of 2^0 (1).
    A number can be represented as a sum of non-zero powers of 2 if it is even.
    Because 2^k where k >= 1 are all even. 2^0 is 1 (odd).
    If a number is even, it is a sum of powers of 2 where all exponents are >= 1.
    If a number is odd, it MUST include 2^0.

    Let's check:
    10 is even -> True.
    7 is odd -> False.
    14 is even -> True.

    The logic appears to be: Is the number even and greater than 0?
    Or more specifically, can it be formed using ONLY powers of 2 that are > 1?
    Powers of 2 are: 1, 2, 4, 8, 16...
    "Non-zero powers of 2" usually means 2^x where x is a non-zero integer?
    If x > 0, then the powers are 2^1=2, 2^2=4, 2^3=8...
    If a number can be represented as a sum of these, it must be even.

    Let's verify:
    10 = 8 + 2 (Both are 2^x where x > 0) -> True.
    7 = 4 + 2 + 1 (Includes 2^0, where 0 is not a non-zero power) -> False.
    14 = 8 + 4 + 2 (All are 2^x where x > 0) -> True.

    Conclusion: The function checks if the number is even and positive.
    However, there is one more nuance: 0 is not typically representable as a sum of 
    positive powers unless the sum is empty.

    Let's implement the logic:
    A number is a sum of powers of 2 (2^k for k >= 1) if and only if it is even and > 0.
    """

    # Step 1: Validate input type
    if not isinstance(n, int):
        raise ValueError(f"Input must be an integer, received: {type(n).__name__}")

    # Step 2: Handle non-positive numbers
    # Sums of powers of 2 (2^k for k >= 1) are always positive.
    # 0 cannot be represented as a sum of non-zero powers of 2.
    if n <= 0:
        return False

    # Step 3: Check if the number is even
    # A number is a sum of powers 2^1, 2^2, 2^3... if and only if it is even.
    # Because all such powers are divisible by 2.
    is_even = (n % 2 == 0)

    if is_even:
        return True
    else:
        return False

def is_Sum_Of_Powers_Of_Two(n: Any) -> bool:
    """
    Determines if a number can be represented as a sum of non-zero powers of 2.
    Based on the provided test cases:
    - 10 (even) -> True
    - 7 (odd) -> False
    - 14 (even) -> True

    Logic: The number must be even and positive.
    """
    # Explicit input validation
    if not isinstance(n, int):
        # If the input is a float that is equivalent to an integer (e.g., 10.0),
        # we should decide if we allow it. Standard practice is to be strict.
        return False

    # Handle degenerate case: 0 or negative numbers
    # A sum of powers of 2 (2^k where k >= 1) must be at least 2.
    if n <= 0:
        return False

    # A number is a sum of powers of 2 (2^1, 2^2, 2^3...) 
    # if and only if it is even.
    # This is because any sum of even numbers is even.
    # Conversely, any even number has a binary representation where the 
    # least significant bit is 0, meaning it only uses powers 2^1, 2^2, ...
    is_even = (n % 2 == 0)

    if is_even:
        return True
    else:
        return False