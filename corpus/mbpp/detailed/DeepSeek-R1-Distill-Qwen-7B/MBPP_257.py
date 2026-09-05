def swap_numbers(a, b):
    """
    Swaps the values of two numbers and returns them as a tuple.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        tuple: A tuple containing the swapped values (b, a).
    """
    temp = a
    a = b
    b = temp
    return (a, b)