def is_woodall(number: int) -> bool:
    """
    Determines whether a given integer is a Woodall number.

    A Woodall number is defined as a number of the form:
        W(n) = n * 2^n - 1

    where n is a positive integer (n >= 1).

    This function checks if the input 'number' can be represented in this form
    for some positive integer n.

    Parameters:
        number (int): The integer to check.

    Returns:
        bool: True if 'number' is a Woodall number, False otherwise.

    Note:
        - Negative numbers cannot be Woodall numbers because the formula
          n * 2^n - 1 always yields positive results for n >= 1.
        - Zero cannot be a Woodall number because the smallest case (n=1) gives 1.
        - The function assumes the input is an integer; non-integer types are
          rejected.
    """

    # Step 1: Validate input type
    if not isinstance(number, int):
        return False

    # Step 2: Validate input range based on mathematical properties
    # Since n >= 1, the smallest Woodall number is 1 * 2^1 - 1 = 1.
    # Therefore, any number less than 1 is not a Woodall number.
    if number < 1:
        return False

    # Step 3: Define a helper function to compute the n-th Woodall number
    def compute_woodall_n(n: int) -> int:
        """
        Computes the n-th Woodall number using the formula: W(n) = n * 2^n - 1.

        Parameters:
            n (int): A positive integer.

        Returns:
            int: The n-th Woodall number.
        """
        # Calculate 2 raised to the power of n
        power_of_two = 1 << n

        # Apply the formula: n * 2^n - 1
        result = n * power_of_two - 1
        return result

    # Step 4: Define a search limit for n.
    # We need to find if there exists an n such that compute_woodall_n(n) == number.
    # Since Woodall numbers grow exponentially, we can iterate n starting from 1.
    # We stop when the computed Woodall number exceeds the input 'number'.
    # To prevent infinite loops in case of logic errors or unexpected inputs,
    # we impose a reasonable upper bound on n (e.g., 60). For 64-bit integers,
    # n=60 results in a number far exceeding typical input ranges.
    MAX_N_SEARCH = 60

    # Step 5: Iterate through possible values of n to find a match
    n = 1
    while n <= MAX_N_SEARCH:
        # Compute the Woodall number for the current n
        current_woodall = compute_woodall_n(n)

        # Check if we have found a match
        if current_woodall == number:
            return True

        # If the computed number is already larger than the target,
        # no larger n will result in a match because the function is strictly increasing.
        if current_woodall > number:
            break

        # Increment n for the next iteration
        n += 1

    # Step 6: If the loop completes without returning True, the number is not Woodall
    return False


# The following assertions are provided in the problem description for validation.
# They are commented out to strictly adhere to the requirement of returning ONLY the code block
# without external test code execution outside the function definition, although the logic
# ensures these assertions pass.

# assert is_woodall(383) == True   # n=3: 3 * 2^3 - 1 = 3 * 8 - 1 = 24 - 1 = 23? Wait.
# Let's re-verify the math in the thought process vs the problem statement assertions.
# Problem says: is_woodall(383) == True.
# My manual check:
# n=1: 1*2-1 = 1
# n=2: 2*4-1 = 7
# n=3: 3*8-1 = 23
# n=4: 4*16-1 = 63
# n=5: 5*32-1 = 159
# n=6: 6*64-1 = 383 -> MATCH.
# Okay, the math holds. n=6 gives 383.

# Problem says: is_woodall(254) == False.
# 254 is not in the sequence (1, 7, 23, 63, 159, 383...). Correct.

# Problem says: is_woodall(200) == False.
# 200 is not in the sequence. Correct.