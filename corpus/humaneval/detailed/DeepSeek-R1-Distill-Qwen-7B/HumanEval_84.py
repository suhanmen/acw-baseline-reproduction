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
    # Input validation
    if not isinstance(N, int) or N < 0 or N > 10000:
        return "Invalid input"

    # Handle the case when N is zero
    if N == 0:
        return "0"

    # Convert N to its binary representation
    binary_str = bin(N)[2:]  # [2:] to remove the '0b' prefix

    # Calculate the sum of binary digits
    sum_binary = 0
    for digit in binary_str:
        sum_binary += int(digit)

    return str(sum_binary)