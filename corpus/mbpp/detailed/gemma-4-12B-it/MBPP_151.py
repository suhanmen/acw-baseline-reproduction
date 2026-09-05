import math

def is_coprime(num1: int, num2: int) -> bool:
    """
    Determines whether two integers are co-prime.
    Two numbers are co-prime (or relatively prime) if their greatest 
    common divisor (GCD) is exactly 1.

    Args:
        num1 (int): The first integer to check.
        num2 (int): The second integer to check.

    Returns:
        bool: True if the numbers are co-prime, False otherwise.

    Raises:
        TypeError: If either input is not an integer.
        ValueError: If inputs are non-positive, as co-primality is 
                    typically defined for positive integers in basic number theory,
                    though mathematically GCD(0, 1) = 1. We enforce positive 
                    integers for strict production safety.
    """
    # --- Input Validation ---

    # Ensure both inputs are integers
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Both inputs must be integers.")

    # Handle cases involving zero or negative numbers
    # While GCD(0, 1) is 1, usually 'coprime' refers to positive integers.
    # We check for non-positive values to ensure deterministic behavior.
    if num1 <= 0 or num2 <= 0:
        # Depending on requirements, one might allow 0 if the other is 1.
        # For standard production use, we restrict to positive integers.
        raise ValueError("Both numbers must be positive integers greater than zero.")

    # --- Core Logic ---

    def calculate_gcd(a: int, b: int) -> int:
        """
        Calculates the Greatest Common Divisor using the Euclidean Algorithm.
        This is a helper function to keep the main logic clean.
        """
        # Work with absolute values to be safe, though inputs are validated above
        temp_a = abs(a)
        temp_b = abs(b)

        while temp_b != 0:
            remainder = temp_a % temp_b
            temp_a = temp_b
            temp_b = remainder

        return temp_a

    # Step 1: Calculate the Greatest Common Divisor
    common_divisor = calculate_gcd(num1, num2)

    # Step 2: Check if the GCD is 1
    is_relatively_prime = (common_divisor == 1)

    return is_relatively_prime

# The following assertions verify the correctness of the implementation.
if __name__ == "__main__":
    # Requirement Assertions
    assert is_coprime(17, 13) == True
    assert is_coprime(15, 21) == False
    assert is_coprime(25, 45) == False