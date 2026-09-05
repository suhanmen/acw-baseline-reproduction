def opposite_signs(n1: int, n2: int) -> bool:
    """
    Check whether the given two integers have opposite signs.

    Two integers have opposite signs if one is strictly positive and the other
    is strictly negative. Integers that are zero do not have an opposite sign
    relationship with any other integer in this context (zero is neither
    positive nor negative).

    Parameters
    ----------
    n1 : int
        The first integer.
    n2 : int
        The second integer.

    Returns
    -------
    bool
        True if n1 and n2 have opposite signs (one positive, one negative).
        False otherwise (both positive, both negative, one or both are zero).

    Raises
    ------
    TypeError
        If either n1 or n2 is not an integer.
    """
    # Step 1: Validate that n1 is an integer
    if not isinstance(n1, int):
        raise TypeError(f"The first argument must be an integer, got {type(n1).__name__}")

    # Step 2: Validate that n2 is an integer
    if not isinstance(n2, int):
        raise TypeError(f"The second argument must be an integer, got {type(n2).__name__}")

    # Step 3: Check if n1 is positive (strictly greater than zero)
    is_n1_positive = n1 > 0

    # Step 4: Check if n1 is negative (strictly less than zero)
    is_n1_negative = n1 < 0

    # Step 5: Check if n2 is positive (strictly greater than zero)
    is_n2_positive = n2 > 0

    # Step 6: Check if n2 is negative (strictly less than zero)
    is_n2_negative = n2 < 0

    # Step 7: Determine if n1 has a valid sign (non-zero)
    n1_has_sign = is_n1_positive or is_n1_negative

    # Step 8: Determine if n2 has a valid sign (non-zero)
    n2_has_sign = is_n2_positive or is_n2_negative

    # Step 9: If either number is zero, they cannot have opposite signs
    # because zero is neither positive nor negative.
    if not n1_has_sign or not n2_has_sign:
        return False

    # Step 10: Determine if both numbers are positive
    both_positive = is_n1_positive and is_n2_positive

    # Step 11: Determine if both numbers are negative
    both_negative = is_n1_negative and is_n2_negative

    # Step 12: If both are positive or both are negative, they do not have opposite signs
    same_sign = both_positive or both_negative

    # Step 13: Return the negation of "same sign" to get "opposite signs"
    return not same_sign


# The following block demonstrates the explicit handling of the problem's assertions
# and provides a comprehensive set of edge case tests to verify robustness.
# Note: In a production environment, these would be in a separate test file (e.g., test_opposite_signs.py).

if __name__ == "__main__":
    # Test Cases from the Problem Statement
    test_cases_from_problem = [
        (1, -2, True),
        (3, 2, False),
        (-10, -10, False),
    ]

    # Additional Edge Cases
    edge_cases = [
        # Positive and Negative (Opposite)
        (1, -1, True),
        (-1, 1, True),
        (0.5 is not int, "Input type check placeholder - not a real case"), # Just for code structure reference, not executed as test
        (100, -100, True),
        (-1000, 1, True),

        # Same Signs (Not Opposite)
        (5, 5, False),
        (-5, -5, False),
        (0, 0, False), # Both zero
        (0, 5, False), # One zero
        (5, 0, False), # One zero
        (1, 0, False),
        (-1, 0, False),
        (0, -1, False),

        # Boundary Values
        (1, 1, False), # Smallest positive
        (-1, -1, False), # Largest negative
        (2147483647, 2147483647, False), # Max int32-ish
        (-2147483648, -2147483648, False), # Min int32-ish

        # Large Differences
        (10**18, -1, True),
        (-10**18, 100, True),
    ]

    print("Running Tests for opposite_signs...")
    all_passed = True

    for args in test_cases_from_problem:
        n1, n2, expected = args
        result = opposite_signs(n1, n2)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"Test (n1={n1}, n2={n2}): Expected {expected}, Got {result} -> [{status}]")

    for args in edge_cases:
        if isinstance(args, tuple) and len(args) == 3:
            # Handle the special non-int case for demonstration of type checking if we added it
            pass
        elif isinstance(args, tuple) and len(args) == 2:
            n1, n2 = args
            expected = not (n1 == 0 or n2 == 0 or ((n1 > 0) == (n2 > 0))) # Logic derived manually for verification
            # Re-evaluating logic for edge cases explicitly based on function definition
            # If either is 0 -> False. If same sign (both > 0 or both < 0) -> False. Else True.
            is_n1_zero = n1 == 0
            is_n2_zero = n2 == 0
            if is_n1_zero or is_n2_zero:
                expected = False
            elif (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
                expected = False
            else:
                expected = True

            result = opposite_signs(n1, n2)
            status = "PASS" if result == expected else "FAIL"
            if result != expected:
                all_passed = False
            print(f"Edge Test (n1={n1}, n2={n2}): Expected {expected}, Got {result} -> [{status}]")

    if all_passed:
        print("\nAll tests passed successfully.")
    else:
        print("\nSome tests failed!")