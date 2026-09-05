def pos_nos(lst):
    """
    Returns a tuple of positive numbers from a given list.
    Note: To satisfy the specific assertions provided in the prompt,
    the function returns a tuple of numbers greater than zero.
    """
    result = tuple(x for x in lst if x > 0)
    return result

# The assertions provided in the prompt use a syntax (e.g., == 1,2) 
# that Python interprets as comparing the result to a tuple (1, 2).