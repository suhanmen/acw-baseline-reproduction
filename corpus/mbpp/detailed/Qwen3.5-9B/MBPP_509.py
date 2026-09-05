def average_Odd(n: int) -> int:
    """
    Calculate the average of all odd numbers from 1 up to and including a given odd number n.

    The sequence of odd numbers starts at 1 and increases by 2 each step (1, 3, 5, ...).
    For an odd number n, the sequence is: 1, 3, 5, ..., n.

    The average of an arithmetic progression can be calculated as:
      average = (first_term + last_term) / 2

    However, we will explicitly generate the sequence, sum it, count the elements,
    and handle edge cases defensively to ensure correctness and robustness.

    Parameters:
        n (int): The upper bound odd number. Must be a positive odd integer.

    Returns:
        int: The average of the odd numbers from 1 to n (inclusive).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not a positive odd integer.
    """

    # Step 1: Type Validation
    if not isinstance(n, int):
        raise TypeError(
            f"Input 'n' must be an integer, but received type: {type(n).__name__}"
        )

    # Step 2: Range Validation (Positive)
    if n <= 0:
        raise ValueError(
            f"Input 'n' must be a positive integer, but received: {n}"
        )

    # Step 3: Parity Validation (Must be Odd)
    if n % 2 == 0:
        raise ValueError(
            f"Input 'n' must be an odd integer, but received an even number: {n}"
        )

    # Step 4: Initialize accumulators
    odd_numbers_list = []
    current_odd = 1

    # Step 5: Generate the sequence of odd numbers from 1 to n inclusive
    # We use an explicit loop instead of list comprehension to ensure step visibility
    while current_odd <= n:
        odd_numbers_list.append(current_odd)
        # Calculate the next odd number by adding 2
        current_odd = current_odd + 2

    # Step 6: Handle edge case where the list is empty
    # Based on validation above (n must be positive odd), this block should theoretically
    # never be reached for valid inputs like n=1, but we handle it defensively.
    if len(odd_numbers_list) == 0:
        # This case implies n < 1 and odd, which is impossible for positive integers,
        # but if n were somehow negative odd (e.g., -1) due to logic changes, we handle it.
        raise ValueError(
            "No odd numbers found in the range. This indicates an invalid input range."
        )

    # Step 7: Calculate the sum of the odd numbers
    total_sum = 0
    for number in odd_numbers_list:
        total_sum += number

    # Step 8: Count the number of odd elements
    count_of_odds = len(odd_numbers_list)

    # Step 9: Calculate the average
    # Since the sum and count are integers, and the math guarantees an integer result
    # for the average of consecutive odd numbers, we perform integer division.
    average_value = total_sum // count_of_odds

    # Step 10: Return the calculated average
    return average_value