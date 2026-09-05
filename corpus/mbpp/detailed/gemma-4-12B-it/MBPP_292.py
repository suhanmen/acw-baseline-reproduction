from typing import Union

def find(dividend: Union[int, float], divisor: Union[int, float]) -> Union[int, float]:
    """
    Calculates the quotient of two numbers.

    The function performs integer division if the result is a whole number 
    or if the inputs are integers and the quotient is expected to be an integer 
    based on standard division behavior in the provided test cases.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        The quotient of dividend / divisor.

    Raises:
        ValueError: If the divisor is zero.
        TypeError: If inputs are not numeric types.
    """

    # Step 1: Validate input types
    # We ensure that both arguments are either integers or floats.
    is_dividend_numeric = isinstance(dividend, (int, float))
    is_divisor_numeric = isinstance(divisor, (int, float))

    if not is_dividend_numeric or not is_divisor_numeric:
        raise TypeError(
            f"Inputs must be numeric. Received: dividend={type(dividend)}, "
            f"divisor={type(divisor)}"
        )

    # Step 2: Handle the division by zero edge case
    # Division by zero is mathematically undefined and must be caught explicitly.
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")

    # Step 3: Perform the division
    # We use standard float division first to determine the precise quotient.
    raw_quotient = dividend / divisor

    # Step 4: Determine the return type and value
    # The provided assertions (10,3) == 3 imply floor division (integer division).
    # However, standard production-grade math might require floats. 
    # Based on the specific test cases:
    # 10/3 = 3.333... -> 3
    # 4/2 = 2.0 -> 2
    # 20/5 = 4.0 -> 4
    # This suggests we should return the floor of the quotient.

    # We use int() to truncate towards zero, or math.floor for downward rounding.
    # Given the examples, integer truncation/floor is the intended behavior.
    final_result = int(raw_quotient)

    return final_result

# The following assertions verify the requirements are met.
if __name__ == "__main__":
    # Test cases provided in the problem description
    assert find(10, 3) == 3
    assert find(4, 2) == 2
    assert find(20, 5) == 4