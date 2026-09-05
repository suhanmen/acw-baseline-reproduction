def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """

    def validate_input(value):
        """
        Validates that the input is a positive integer.
        Raises a ValueError if the input is invalid.
        """
        if not isinstance(value, int):
            raise TypeError(f"Input must be an integer, got {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"Input must be a positive integer greater than 0, got {value}")
        # Although Python integers have arbitrary precision, strictly speaking
        # the problem implies standard positive integers. We accept large ints.
        return True

    def generate_collatz_sequence(current):
        """
        Generates the full Collatz sequence starting from the current number
        until it reaches 1. Returns the sequence as a list.
        """
        sequence = []

        while True:
            # Check if we have reached the end of the sequence (1)
            if current == 1:
                sequence.append(current)
                break

            # Append the current number to the sequence
            sequence.append(current)

            # Determine the next number based on Collatz rules
            if current % 2 == 0:
                # If even, next is n / 2
                next_val = current // 2
            else:
                # If odd, next is 3*n + 1
                next_val = (3 * current) + 1

            current = next_val

        return sequence

    def extract_odd_numbers(sequence):
        """
        Iterates through a sequence and collects only the odd numbers.
        Returns them in the order they appeared in the sequence.
        """
        odd_numbers = []

        for number in sequence:
            if number % 2 != 0:
                odd_numbers.append(number)

        return odd_numbers

    def sort_list(input_list):
        """
        Sorts a list of integers in ascending order.
        """
        return sorted(input_list)

    # --- Main Execution Logic ---

    # Step 1: Validate the input argument
    try:
        validate_input(n)
    except (TypeError, ValueError) as validation_error:
        # In a production environment, we might want to handle this differently 
        # (e.g., logging, specific exception handling), but raising is standard
        # for strict function contracts when input is invalid.
        raise validation_error

    # Step 2: Generate the full Collatz sequence for the validated input
    full_sequence = generate_collatz_sequence(n)

    # Step 3: Extract only the odd numbers from the generated sequence
    odd_elements = extract_odd_numbers(full_sequence)

    # Step 4: Sort the extracted odd numbers in increasing order
    sorted_odd_elements = sort_list(odd_elements)

    return sorted_odd_elements