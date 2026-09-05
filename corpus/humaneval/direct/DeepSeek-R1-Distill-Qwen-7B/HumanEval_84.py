def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary."""
    if N == 0:
        return "0"
    binary = bin(N)[2:]  # Convert to binary and remove '0b'
    sum_digits = binary.count('1')
    return bin(sum_digits)[2:]  # Convert the sum to binary and return it as a string