from typing import Tuple

def division_elements(tuples_a: Tuple[int, ...], tuples_b: Tuple[int, ...]) -> Tuple[int, ...]:
    if len(tuples_a) != len(tuples_b):
        raise ValueError("Input tuples must have the same length")
    return tuple(a // b for a, b in zip(tuples_a, tuples_b))