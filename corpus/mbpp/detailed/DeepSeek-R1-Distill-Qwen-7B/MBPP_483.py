def first_Factorial_Divisible_Number(x):
    # Input validation for x <= 0
    if x <= 0:
        return "Invalid input: x must be a positive integer"

    # Special case when x is 1
    if x == 1:
        return 1

    # Initialize variables for the iterative approach
    n = 1
    current_factorial = 1

    while True:
        # Check if current_factorial is divisible by x
        if current_factorial % x == 0:
            return n

        # Increment n and compute the next factorial
        n += 1
        current_factorial *= n

        # Handle potential overflow (though in practice, Python handles big integers well)
        # However, theoretically, this loop could run indefinitely if x is 0 or negative, but we've already handled that