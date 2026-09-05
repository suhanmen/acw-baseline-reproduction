def is_num_keith(n: int) -> bool:
    """
    A Keith number is an integer n with k digits such that when you start
    a sequence with the digits of n and continuously add the sum of the 
    previous k terms, n eventually appears in the sequence.
    """
    # Keith numbers must have at least 2 digits
    if n < 10:
        return False

    # Get digits of the number
    digits = [int(d) for d in str(n)]
    k = len(digits)

    # Initialize sequence with digits
    sequence = list(digits)

    # Generate sequence until the last term is >= n
    while True:
        next_term = sum(sequence[-k:])
        if next_term == n:
            return True
        if next_term > n:
            return False
        sequence.append(next_term)