def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    def validate_input_list(sequence, name):
        """
        Validates that the provided sequence is a list containing only integers.
        Raises a ValueError if validation fails.

        Args:
            sequence: The list to validate.
            name: A string identifier for the list (used in error messages).

        Returns:
            The validated list.

        Raises:
            TypeError: If the input is not a list.
            ValueError: If the list contains non-integer elements.
        """
        if not isinstance(sequence, list):
            raise TypeError(f"{name} must be a list, but got {type(sequence).__name__}.")

        for index, value in enumerate(sequence):
            if not isinstance(value, int):
                raise ValueError(f"{name}[{index}] is not an integer: {value!r} (type: {type(value).__name__}).")

        return sequence

    def find_odds_in_list(sequence):
        """
        Identifies all odd numbers within the given sequence.

        Args:
            sequence: The list of integers to scan.

        Returns:
            A list of odd integers found in the sequence.
        """
        odds = []
        for number in sequence:
            if number % 2 != 0:
                odds.append(number)
        return odds

    def count_even_numbers(sequence):
        """
        Counts the total number of even integers in the given sequence.

        Args:
            sequence: The list of integers to count.

        Returns:
            An integer representing the count of even numbers.
        """
        count = 0
        for number in sequence:
            if number % 2 == 0:
                count += 1
        return count

    # Step 1: Validate Inputs
    # We explicitly check for types and content constraints as per defensive programming practices.
    try:
        valid_lst1 = validate_input_list(lst1, "lst1")
        valid_lst2 = validate_input_list(lst2, "lst2")
    except (TypeError, ValueError) as validation_error:
        raise validation_error

    # Step 2: Analyze the initial state of lst1
    # We need to determine how many odd numbers currently exist in lst1.
    # These are the elements that MUST be replaced.
    current_odd_count = len(find_odds_in_list(valid_lst1))

    # Step 3: Analyze the potential resources available in lst2
    # We need to count how many even numbers exist in lst2.
    # These are the elements that can be swapped IN to replace the odds in lst1.
    available_even_count = count_even_numbers(valid_lst2)

    # Step 4: Determine feasibility
    # Logic:
    # - To make lst1 all evens, every odd number currently in lst1 must be swapped out.
    # - This requires at least `current_odd_count` new even numbers from lst2.
    # - If lst2 has enough even numbers (available_even_count >= current_odd_count), 
    #   we can perform the swaps.
    # - If lst2 does not have enough even numbers, we cannot eliminate all odds from lst1.

    if available_even_count >= current_odd_count:
        return "YES"
    else:
        return "NO"