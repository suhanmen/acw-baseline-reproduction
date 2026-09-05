from typing import Tuple, Any

def add_pairwise(tuples: Tuple[Any, ...]) -> Tuple[int, ...]:
    """
    Takes a tuple of integers and returns a new tuple containing the pairwise
    addition of adjacent elements.

    Examples:
    add_pairwise((1, 5, 7, 8, 10)) -> (6, 12, 15, 18)
    add_pairwise((2, 6, 8, 9, 11)) -> (8, 14, 17, 20)
    add_pairwise((3, 7, 9, 10, 12)) -> (10, 16, 19, 22)
    """
    result = []
    for i in range(len(tuples) - 1):
        result.append(tuples[i] + tuples[i + 1])
    return tuple(result)