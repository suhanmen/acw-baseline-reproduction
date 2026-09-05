def unique_digits(x):
    """Given a list of positive integers x. Return a sorted list of all 
    elements that haven't any even digit. The returned list should be sorted 
    in increasing order.

    Edge cases:
    - Empty input returns empty list
    - Any element with a zero or negative value returns empty list
    - Any element with all even digits is excluded

    Note: The input list should consist only of positive integers.
    """
    # Check if x is an empty list
    if not isinstance(x, list) or not x:
        return []

    # Validate that all elements are positive integers
    for num in x:
        if not isinstance(num, int) or num <= 0:
            return []

    result = []
    for num in x:
        # Convert the number to a string to easily check each digit
        num_str = str(num)
        # Flag to check if any even digit is present
        has_even = False
        for digit in num_str:
            # Convert digit to integer to check evenness
            d = int(digit)
            if d % 2 == 0:
                has_even = True
                break  # No need to check further digits

        if not has_even:
            result.append(num)

    # Sort the result in increasing order
    result.sort()

    return result