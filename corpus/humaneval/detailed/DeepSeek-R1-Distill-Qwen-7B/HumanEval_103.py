def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    # Check if inputs are valid
    if n <= 0 or m <= 0:
        return -1
    if n > m:
        return -1

    # Calculate the sum of integers from n to m
    number_of_terms = m - n + 1
    sum_numbers = (number_of_terms // 2) * (n + m)

    # Compute the average
    average = sum_numbers / number_of_terms

    # Round to the nearest integer and convert to binary
    rounded = round(average)
    binary = bin(rounded)

    # Return the binary string without the '0b' prefix
    return binary[2:]