def validate_input(n):
    """
    Validates the input argument n.

    Requirements for a valid input:
    1. n must be an integer.
    2. n must be non-negative (>= 0).

    Returns:
    bool: True if the input is valid.

    Raises:
    TypeError: If n is not an integer.
    ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Input must be non-negative, got {n}")

    return True


def generate_first_n_odds(n):
    """
    Generates the first n odd natural numbers as a list.

    Odd natural numbers start from 1, 3, 5, 7, ...
    The k-th odd number (1-indexed) can be calculated as (2 * k) - 1.

    Args:
        n (int): The count of odd numbers to generate. Must be >= 0.

    Returns:
        list[int]: A list containing the first n odd natural numbers.
    """
    odd_numbers = []

    if n == 0:
        return odd_numbers

    for count_index in range(1, n + 1):
        current_odd_number = (2 * count_index) - 1
        odd_numbers.append(current_odd_number)

    return odd_numbers


def compute_square(value):
    """
    Computes the square of a given number.

    Args:
        value (int): The number to be squared.

    Returns:
        int: The square of the input value.
    """
    return value * value


def sum_list_items(items):
    """
    Computes the sum of a list of numbers using an explicit loop.

    Args:
        items (list[int]): The list of numbers to sum.

    Returns:
        int: The sum of the items in the list.
    """
    total_sum = 0
    count = len(items)

    if count == 0:
        return total_sum

    for index in range(count):
        item_value = items[index]
        total_sum = total_sum + item_value

    return total_sum


def square_Sum(n):
    """
    Finds the sum of squares of the first n odd natural numbers.

    Mathematical definition:
    Sum = 1^2 + 3^2 + 5^2 + ... + (2n-1)^2

    Steps performed:
    1. Validate the input n.
    2. Generate the sequence of the first n odd natural numbers.
    3. Calculate the square for each number in the sequence.
    4. Sum all the squared values.

    Args:
        n (int): The number of odd natural numbers to consider.

    Returns:
        int: The sum of the squares of the first n odd natural numbers.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Examples:
        square_Sum(2) -> 1^2 + 3^2 = 1 + 9 = 10
        square_Sum(3) -> 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
        square_Sum(4) -> 1^2 + 3^2 + 5^2 + 7^2 = 1 + 9 + 25 + 49 = 84
    """
    # Step 1: Validate the input explicitly
    validate_input(n)

    # Step 2: Generate the list of the first n odd natural numbers
    odd_numbers_sequence = generate_first_n_odds(n)

    # Step 3: Initialize the accumulator for the sum of squares
    running_total = 0

    # Step 4: Iterate through the generated sequence
    count = len(odd_numbers_sequence)
    index = 0

    while index < count:
        current_odd = odd_numbers_sequence[index]

        # Compute the square of the current odd number
        current_square = compute_square(current_odd)

        # Add the square to the running total
        running_total = running_total + current_square

        # Move to the next element
        index = index + 1

    # Step 5: Return the final result
    return running_total