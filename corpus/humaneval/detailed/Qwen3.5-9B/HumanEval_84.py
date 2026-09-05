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

    def is_valid_input(value):
        """
        Validates that the input is a non-negative integer within the 
        specified constraints (0 <= N <= 10000).

        Args:
            value: The input value to validate.

        Returns:
            True if valid, raises TypeError or ValueError otherwise.
        """
        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError(f"Expected an integer, got {type(value).__name__}")

        # Check if the value is non-negative (handle explicit negatives)
        if value < 0:
            raise ValueError(f"Negative number {value} is not allowed. Constraint: 0 <= N.")

        # Check upper bound constraint
        if value > 10000:
            raise ValueError(f"Number {value} exceeds maximum allowed value of 10000.")

        return True

    def calculate_digit_sum(n):
        """
        Calculates the sum of the decimal digits of a given integer n.

        Args:
            n: A non-negative integer.

        Returns:
            An integer representing the sum of the digits.
        """
        # Initialize the accumulator for the sum
        digit_sum = 0

        # Handle the case where n is 0 explicitly before the loop
        if n == 0:
            return 0

        # Process each digit by extracting the last digit and dividing the number
        temp_n = n
        while temp_n > 0:
            current_digit = temp_n % 10
            digit_sum += current_digit
            temp_n = temp_n // 10

        return digit_sum

    def decimal_to_binary_string(decimal_number):
        """
        Converts a non-negative decimal integer to its binary string representation
        without leading zeros (except for the number 0 itself).

        Args:
            decimal_number: A non-negative integer.

        Returns:
            A string representing the number in binary format.
        """
        # Handle the zero case explicitly
        if decimal_number == 0:
            return "0"

        binary_digits = []
        temp_val = decimal_number

        # Repeatedly divide by 2 and collect remainders
        while temp_val > 0:
            remainder = temp_val % 2
            binary_digits.append(str(remainder))
            temp_val = temp_val // 2

        # The digits were collected in reverse order (least significant first)
        # so we must reverse them to get the correct binary string
        binary_digits.reverse()

        return "".join(binary_digits)

    # --- Main Execution Flow ---

    # Step 1: Validate the input argument
    try:
        is_valid_input(N)
    except (TypeError, ValueError) as validation_error:
        # Re-raise to ensure the caller knows about the invalid input
        raise validation_error

    # Step 2: Calculate the sum of the decimal digits
    digit_sum_result = calculate_digit_sum(N)

    # Step 3: Convert the resulting sum to a binary string
    final_binary_output = decimal_to_binary_string(digit_sum_result)

    # Step 4: Return the final result
    return final_binary_output