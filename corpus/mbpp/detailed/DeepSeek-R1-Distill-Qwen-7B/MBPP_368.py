import itertools

def repeat_tuples(t, n):
    """
    Repeat the given tuple n times.

    Parameters:
        t (tuple): The tuple to be repeated.
        n (int): The number of times to repeat the tuple.

    Returns:
        tuple: A new tuple containing the original tuple repeated n times.

    Raises:
        TypeError: If t is not a tuple or n is not an integer.
        ValueError: If n is negative.
    """
    # Validate inputs
    if not isinstance(t, tuple):
        raise TypeError("The first argument must be a tuple.")
    if not isinstance(n, int):
        raise TypeError("The second argument must be an integer.")
    if n < 0:
        raise ValueError("The number of repetitions cannot be negative.")

    # Handle the case of an empty tuple
    if not t:
        return t

    # Generate the repeated tuple
    repeated = itertools.product(t, repeat=n)

    # Convert the iterator to a tuple and return
    return tuple(repeated)