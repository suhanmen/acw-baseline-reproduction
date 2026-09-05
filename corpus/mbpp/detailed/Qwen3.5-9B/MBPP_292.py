def find_divisor(a: float, b: float) -> int:
    """
    Find the integer quotient of two numbers using repeated subtraction.

    This function calculates 'a // b' using a defensive, explicit approach
    suitable for educational or constrained environments where the division 
    operator itself might be restricted or to demonstrate algorithmic logic.

    It adheres to the following logic:
    1. Validate inputs (ensure they are numbers).
    2. Handle the division by zero case explicitly.
    3. Handle negative numbers by converting to absolute values, performing 
       the operation, and adjusting the sign based on the original operands.
    4. Use repeated subtraction to calculate the integer quotient.

    Parameters:
    a (float): The dividend.
    b (float): The divisor.

    Returns:
    int: The integer quotient of a divided by b.

    Raises:
    TypeError: If inputs are not numeric.
    ValueError: If the divisor is zero.
    """

    # --- Step 1: Input Validation ---
    # Ensure both arguments are either int or float
    if not isinstance(a, (int, float)):
        raise TypeError(f"Dividend must be a number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Divisor must be a number, got {type(b).__name__}")

    # Check if they are actually numeric types (reject booleans explicitly)
    # Booleans are technically ints in Python, but logically distinct here
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Boolean values are not accepted as numeric inputs")

    # --- Step 2: Handle Division by Zero ---
    # Explicitly check if divisor is zero before proceeding
    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    # --- Step 3: Store Original Signs ---
    # We need to determine the sign of the result.
    # The result is negative if exactly one of the operands is negative.
    # The result is positive if both are positive or both are negative.
    is_negative_result = False

    if a < 0 and b > 0:
        is_negative_result = True
    elif a > 0 and b < 0:
        is_negative_result = True
    # If both are negative or both positive, is_negative_result remains False

    # --- Step 4: Work with Absolute Values ---
    # Convert operands to their absolute values for the subtraction loop.
    # This simplifies the logic of the subtraction process.
    dividend_abs = abs(a)
    divisor_abs = abs(b)

    # Ensure divisor_abs is strictly positive (it shouldn't be if input passed, but safety first)
    if divisor_abs == 0:
        raise ValueError("Divisor absolute value is zero.")

    # --- Step 5: Calculate Quotient via Repeated Subtraction ---
    # Initialize the quotient counter to zero.
    quotient = 0

    # Loop until the dividend is less than the divisor
    # In a production environment, floating point precision issues could 
    # cause infinite loops if not careful, but for integer-logic simulation
    # with floats treated as integers, this is standard.
    while dividend_abs >= divisor_abs:
        dividend_abs = dividend_abs - divisor_abs
        quotient = quotient + 1

    # --- Step 6: Adjust Sign ---
    # Apply the stored sign logic to the calculated positive quotient
    if is_negative_result:
        quotient = -quotient

    return quotient


# Additional internal utility to handle the specific problem constraints 
# if direct division operator usage were prohibited for the core logic, 
# though Python's // operator works directly. 
# This function demonstrates the 'defensive' and 'explicit' style requested.
def find(a, b):
    """
    Wrapper function matching the required signature and assertions.
    It utilizes find_divisor to implement the logic safely and explicitly.

    This wrapper exists to ensure the exact function name 'find' is used 
    as implied by the problem statement assertions: assert find(10,3) == 3.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numeric.")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return find_divisor(a, b)