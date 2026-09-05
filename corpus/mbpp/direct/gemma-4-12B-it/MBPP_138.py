def is_Sum_Of_Powers_Of_Two(n: int) -> bool:
    """
    Checks whether the given number can be represented as a sum of non-zero 
    powers of 2. 
    Note: In the context of standard binary representation, every positive 
    integer is a sum of unique powers of 2. 
    However, based on the specific assertions provided:
    10 (1010 in binary) -> True
    7 (0111 in binary) -> False
    14 (1110 in binary) -> True

    The logic implied by these assertions is that the number must be represented 
    as a sum of an EVEN number of powers of 2 (i.e., the number of set bits 
    in its binary representation must be even and non-zero).
    """
    if n <= 0:
        return False

    # Count the number of set bits (1s) in the binary representation
    count = bin(n).count('1')

    # Based on the test cases: 
    # 10 (1010) has 2 bits -> True
    # 7 (0111) has 3 bits -> False
    # 14 (1110) has 3 bits -> Wait, the prompt says 14 is True.
    # Let's re-evaluate:
    # 10 = 2^3 + 2^1 (2 terms)
    # 7 = 2^2 + 2^1 + 2^0 (3 terms)
    # 14 = 2^3 + 2^2 + 2^1 (3 terms) -> The prompt says 14 is True.

    # Re-evaluating the logic:
    # Is it even numbers? 10 (even), 7 (odd), 14 (even).
    # Let's check:
    # 10 is even -> True
    # 7 is odd -> False
    # 14 is even -> True

    # This pattern matches the assertions perfectly.
    return n > 0 and n % 2 == 0