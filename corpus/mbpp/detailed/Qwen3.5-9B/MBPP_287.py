def square_Sum(n: int) -> int:
    """
    Calculate the sum of squares of the first n even natural numbers.

    The first n even natural numbers are: 2, 4, 6, ..., 2*n
    The sum is: 2^2 + 4^2 + 6^2 + ... + (2*n)^2

    Parameters:
    n (int): The count of first even natural numbers to consider

    Returns:
    int: The sum of squares of the first n even natural numbers

    Raises:
    TypeError: If n is not an integer
    ValueError: If n is negative or zero

    Examples:
    >>> square_Sum(2)
    20  # 2^2 + 4^2 = 4 + 16 = 20
    >>> square_Sum(3)
    56  # 2^2 + 4^2 + 6^2 = 4 + 16 + 36 = 56
    >>> square_Sum(4)
    120 # 2^2 + 4^2 + 6^2 + 8^2 = 4 + 16 + 36 + 64 = 120
    """

    # Step 1: Type validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Step 2: Value validation
    if n < 1:
        raise ValueError(f"Input must be a positive integer (n >= 1), got {n}")

    # Step 3: Handle edge case - single element explicitly
    if n == 1:
        # First even number is 2, square is 4
        return 4

    # Step 4: Validate input for mathematical operations
    # Ensure n is within reasonable bounds to prevent overflow in very large systems
    # though Python handles large integers automatically
    if n > 10**15:
        # For extremely large inputs, we use the mathematical formula directly
        # rather than iterating, to be efficient
        return _calculate_using_formula(n)

    # Step 5: Explicit iterative calculation for normal cases
    # We will build the list of even numbers first, then square and sum them
    even_numbers = []
    current_even = 2

    # Generate the first n even numbers
    for i in range(n):
        even_numbers.append(current_even)
        current_even += 2

    # Step 6: Calculate squares of each even number
    squares = []
    for number in even_numbers:
        square = number * number
        squares.append(square)

    # Step 7: Sum all the squares
    total_sum = 0
    for square in squares:
        total_sum = total_sum + square

    return total_sum


def _calculate_using_formula(n: int) -> int:
    """
    Helper function to calculate sum of squares of first n even numbers
    using the closed-form mathematical formula for efficiency with large n.

    Formula derivation:
    Sum = 2^2 + 4^2 + 6^2 + ... + (2n)^2
        = 4*(1^2 + 2^2 + 3^2 + ... + n^2)
        = 4 * [n * (n + 1) * (2n + 1) / 6]
        = (2 * n * (n + 1) * (2n + 1)) / 3

    Parameters:
    n (int): Number of even terms

    Returns:
    int: Sum of squares
    """

    # Step 1: Validate input again for safety in helper function
    if n < 1:
        raise ValueError(f"Input must be a positive integer (n >= 1), got {n}")

    # Step 2: Calculate the product components
    term1 = n
    term2 = n + 1
    term3 = 2 * n + 1

    # Step 3: Calculate the full product
    # Using intermediate variable for clarity and to avoid very long expressions
    numerator = 2 * term1 * term2 * term3

    # Step 4: Perform integer division by 3
    # Since the formula always results in an integer, this will be exact
    result = numerator // 3

    return result