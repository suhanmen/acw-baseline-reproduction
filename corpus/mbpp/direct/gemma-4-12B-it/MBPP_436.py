def neg_nos(lst):
    """
    Returns a tuple of negative numbers from the list.
    Note: The assertions in the prompt imply a tuple return 
    since the syntax (-1, -6) represents a tuple.
    """
    return tuple(x for x in lst if x < 0)

# Standard practice to ensure the logic matches the assertion style provided.
# Since the prompt says "print negative numbers" but provides "== -1, -6" 
# assertions, the function must return them to satisfy the equality check.