def num_comm_div(a, b):
    # Handle edge cases where either number is zero
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    if a == b:
        return abs(a)

    # Ensure a is the larger number to simplify the algorithm
    a, b = max(a, b), min(a, b)

    # Apply the Euclidean algorithm
    while b != 0:
        a, b = b, a % b

    # The GCD is now in a
    return a