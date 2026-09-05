def find(quotient, divisor):
    # Input validation: ensure both inputs are integers
    if not isinstance(quotient, int) or not isinstance(divisor, int):
        raise ValueError("Both inputs must be integers")

    # Handle division by zero
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Handle cases where the quotient is less than the divisor
    if quotient < divisor:
        return quotient

    # Calculate and return the remainder
    remainder = quotient % divisor
    return remainder