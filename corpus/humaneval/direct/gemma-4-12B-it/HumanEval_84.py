def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.

    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".

    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Calculate the sum of digits in binary representation
    # bin(N) returns a string like '0b1010', [2:] removes '0b'
    binary_repr = bin(N)[2:]
    digit_sum = sum(int(digit) for digit in binary_repr)

    # The problem examples show a pattern where the output is a binary string
    # representing the calculated digit sum.
    # Example 1: N=1000 -> bin(1000) is '1111101000' -> sum is 6. 
    # Wait, the prompt's examples are contradictory or follow a specific logic:
    # N=1000, sum=1 (Wait, bin(1000) has six 1s. If sum is 1, maybe it's not bit sum?)
    # Let's re-examine the prompt examples:
    # N = 1000, sum of digits = 1 (Wait, if 1000 is treated as 10^3, sum of digits is 1. Binary of 1 is "1")
    # N = 150, sum of digits = 6 (1+5+0=6. Binary of 6 is "110")
    # N = 147, sum of digits = 12 (1+4+7=12. Binary of 12 is "1100")
    # The logic is: Sum the decimal digits of N, then convert that sum to a binary string.

    decimal_digit_sum = sum(int(digit) for digit in str(N))
    return bin(decimal_digit_sum)[2:]