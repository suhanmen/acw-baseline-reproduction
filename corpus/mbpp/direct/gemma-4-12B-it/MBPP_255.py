import itertools

def combinations_colors(colors, n):
    """
    Generates all combinations with repetitions of a specified number of 
    colors from a given list of three colors.
    """
    return list(itertools.combinations_with_replacement(colors, n))