from typing import List

def get_odd_collatz(n: int) -> List[int]:
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
    # Input validation: ensure n is an integer
    if not isinstance(n, int):
        raise ValueError(f"Input n must be an integer, received {type(n).__name__}")

    # Input validation: ensure n is a positive integer as per requirements
    if n <= 0:
        raise ValueError(f"Input n must be a positive integer greater than 0, received {n}")

    def get_next_collatz_term(current_value: int) -> int:
        """
        Helper function to calculate the next number in the Collatz sequence.
        """
        if current_value % 2 == 0:
            # If even, divide by 2
            return current_value // 2
        else:
            # If odd, 3n + 1
            return (3 * current_value) + 1

    # A set to store unique odd numbers encountered in the sequence.
    # A set ensures we don't count the same odd number twice (though in 
    # standard Collatz, repeating a number implies entering a cycle).
    odd_numbers_found = set()

    # The sequence starts with the input n
    current_term = n

    # We continue until the sequence reaches 1
    while True:
        # Check if current_term is odd
        if current_term % 2 != 0:
            odd_numbers_found.add(current_term)

        # Termination condition: Collatz sequence reaches 1
        if current_term == 1:
            break

        # Calculate the next step
        current_term = get_next_collatz_term(current_term)

    # Convert the set to a list to allow sorting
    result_list = list(odd_numbers_found)

    # Sort the list in increasing order as required
    result_list.sort()

    return result_list