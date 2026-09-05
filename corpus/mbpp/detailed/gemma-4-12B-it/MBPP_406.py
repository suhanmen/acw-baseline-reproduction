from typing import Union

def find_Parity(number: Union[int, float]) -> str:
    """
    Determines the parity of a given number.

    Parity is typically defined for integers. Even numbers are divisible by 2
    with no remainder. Odd numbers leave a remainder of 1 when divided by 2.

    Args:
        number (Union[int, float]): The input number to check.

    Returns:
        str: "Even Parity" if the number is even, "Odd Parity" if odd.

    Raises:
        TypeError: If the input is not a numeric type.
        ValueError: If the input is a float with a non-zero fractional part,
                    as parity is not defined for non-integers.
    """
    # Step 1: Validate Input Type
    # We ensure the input is either an int or a float to prevent attribute errors.
    if not isinstance(number, (int, float)):
        raise TypeError(f"Input must be a number, received {type(number).__name__}.")

    # Step 2: Handle Float Edge Cases
    # Parity is a concept for integers. 
    # If a float is passed (e.g., 7.0), it can be treated as an integer.
    # If a float has decimals (e.g., 7.5), parity is undefined.
    if isinstance(number, float):
        # Check if the number is equivalent to an integer
        if not number.is_integer():
            raise ValueError(f"Parity is not defined for non-integer numbers: {number}")
        # Convert to integer for the parity logic
        number_to_check = int(number)
    else:
        number_to_check = number

    # Step 3: Handle Negatives
    # The mathematical definition of parity applies to integers. 
    # -2 is even, -3 is odd. The modulo operator in Python handles 
    # negative numbers correctly for this purpose (e.g., -3 % 2 == 1).

    # Step 4: Calculation logic
    # Use the modulo operator to find the remainder when divided by 2.
    remainder = number_to_check % 2

    # Step 5: Determine Result String
    if remainder == 0:
        result = "Even Parity"
    else:
        result = "Odd Parity"

    return result

# The following assertions are required by the problem statement.
if __name__ == "__main__":
    # Test cases provided in the prompt
    assert find_Parity(12) == "Even Parity"
    assert find_Parity(7) == "Odd Parity"
    assert find_Parity(10) == "Even Parity"