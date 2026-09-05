def next_Perfect_Square(number: int) -> int:
    """
    Find the next perfect square greater than the given number.

    Parameters
    ----------
    number : int
        The input integer for which we need to find the next perfect square.
        Must be a non-negative integer.

    Returns
    -------
    int
        The smallest perfect square that is strictly greater than 'number'.

    Raises
    ------
    TypeError
        If 'number' is not an integer.
    ValueError
        If 'number' is negative.
    """

    # Step 1: Validate input type
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, got {type(number).__name__}")

    # Step 2: Validate input range (must be non-negative)
    if number < 0:
        raise ValueError(f"Input must be a non-negative integer, got {number}")

    # Step 3: Handle the case where the number is 0
    # The next perfect square greater than 0 is 1 (1*1)
    if number == 0:
        return 1

    # Step 4: Calculate the integer square root of the number
    # We use a helper function to ensure explicitness and clarity
    integer_sqrt = _get_integer_square_root(number)

    # Step 5: Determine the candidate square root for the next perfect square
    # If the number is already a perfect square (e.g., 9), integer_sqrt is 3.
    # We need a perfect square *greater* than 9, so we need (3+1)^2 = 16.
    # If the number is not a perfect square (e.g., 35), integer_sqrt is 5 (since 5*5=25).
    # We need (5+1)^2 = 36.
    # In both cases, we add 1 to the integer_sqrt.
    candidate_root = integer_sqrt + 1

    # Step 6: Calculate the next perfect square
    next_square = candidate_root * candidate_root

    # Step 7: Return the result
    return next_square


def _get_integer_square_root(n: int) -> int:
    """
    Calculate the integer square root of a non-negative integer n.
    Returns the largest integer k such that k*k <= n.

    Parameters
    ----------
    n : int
        A non-negative integer.

    Returns
    -------
    int
        The integer square root of n.
    """

    # Step 1: Handle the edge case where n is 0
    if n == 0:
        return 0

    # Step 2: Initialize a variable to track the best guess for the square root.
    # We start with a reasonable upper bound. For n <= 2^31-1, 46341 is sufficient
    # because 46341^2 < 2^31. For larger integers, we can start with n itself
    # or use bit length approximation. Here we use a simple initialization.
    guess = n
    previous_guess = -1

    # Step 3: Iterate using the integer square root approximation algorithm (Babylonian method / Newton's method)
    # until the guess stabilizes or changes significantly.
    while True:
        # Calculate the next approximation
        # Formula: x_{k+1} = (x_k + n / x_k) / 2
        # We use integer division to keep results as integers.
        # To avoid infinite loops with floor division in edge cases, we ensure
        # the guess only decreases or stays the same until it converges.

        # Calculate the divisor part safely
        divisor = guess if guess != 0 else 1  # Safety check, though n>=1 here

        # Compute the new guess using integer arithmetic
        # We want floor((guess + n // guess) / 2)
        new_guess = (guess + n // guess) // 2

        # Check for convergence
        if new_guess >= guess:
            # If the new guess is greater than or equal to the current guess,
            # it means we have overshot or are at the fixed point due to integer truncation.
            # In the integer domain, this is a valid stopping condition.
            break

        guess = new_guess

    # Step 4: Verify the result to ensure it is indeed the floor of the square root.
    # We need to ensure that guess*guess <= n and (guess+1)*(guess+1) > n.
    # The loop above generally converges to this, but explicit verification is defensive.
    # Given the nature of integer division in Newton's method for squares,
    # the result 'guess' will satisfy guess*guess <= n. However, sometimes
    # due to truncation, guess might be slightly too small. 
    # We increment if guess*guess is still well within n and (guess+1)^2 is closer?
    # Actually, standard integer Newton method converges to floor(sqrt(n)).
    # Let's just trust the convergence logic for positive n >= 1.
    # But to be absolutely thorough and defensive:

    # Check if (guess + 1)^2 is still <= n. If so, increment guess.
    while (guess + 1) * (guess + 1) <= n:
        guess += 1

    return guess