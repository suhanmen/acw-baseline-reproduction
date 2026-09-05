import math

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
    # Validation: Check if N is an integer
    if not isinstance(N, int):
        raise ValueError(f"Input N must be an integer, received: {type(N)}")

    # Validation: Check bounds as per constraints (0 <= N <= 10000)
    if N < 0:
        raise ValueError(f"Input N must be non-negative, received: {N}")
    if N > 10000:
        raise ValueError(f"Input N exceeds maximum constraint of 10000, received: {N}")

    # Edge case: Handle 0 explicitly
    # While the problem says "positive integer", the constraint includes 0.
    # The sum of digits in binary for 0 is 0.
    if N == 0:
        # In many contexts, 0 is represented as "0" in binary.
        # However, the example logic suggests a specific mapping.
        # Looking at the examples:
        # 1000 -> sum of binary digits is 6 -> output "1" ?? 
        # Let's re-evaluate the examples provided in the prompt.
        pass

    # RE-EVALUATING THE PROBLEM DESCRIPTION:
    # The prompt description is slightly confusing: 
    # "For N = 1000, the sum of digits will be 1 the output should be '1'."
    # This implies a specific operation. Let's look at all examples:
    # 1. N=1000: Sum of binary digits of 1000 (1111101000) is 6. The prompt says "sum ... will be 1".
    #    Wait, 1000 is 1111101000 in binary. The sum of digits is 6.
    #    If the output is "1", and the prompt says "sum will be 1", 
    #    it seems we are calculating something else.
    #    Let's look at N=150. 150 in binary is 10010110. Sum is 4.
    #    The prompt says "sum ... will be 6" and output "110".
    #    Wait, let's look at the numbers again.
    #    N=1000 -> 1000 / 2 = 500... 
    #    Let's try: Binary of 1000 is 1111101000.
    #    Let's try Sum of digits of N (decimal): 1+0+0+0 = 1. Binary of 1 is "1".
    #    Let's try N=150: Sum of digits is 1+5+0 = 6. Binary of 6 is "110".
    #    Let's try N=147: Sum of digits is 1+4+7 = 12. Binary of 12 is "1100".

    # Conclusion: The task is:
    # 1. Calculate the sum of the decimal digits of N.
    # 2. Convert that sum into its binary representation as a string.

    # Step 1: Calculate the sum of decimal digits of N.
    def calculate_decimal_digit_sum(number: int) -> int:
        absolute_number = abs(number)
        digit_sum = 0
        temp_number = absolute_number

        while temp_number > 0:
            digit = temp_number % 10
            digit_sum += digit
            temp_number //= 10

        return digit_sum

    # Execute Step 1
    total_decimal_sum = calculate_decimal_digit_sum(N)

    # Step 2: Convert the resulting sum to a binary string.
    # The bin() function returns a string starting with '0b', so we slice it.
    if total_decimal_sum == 0:
        binary_string = "0"
    else:
        # bin(6) -> '0b110'
        raw_binary = bin(total_decimal_sum)
        binary_string = raw_binary[2:]

    return binary_string