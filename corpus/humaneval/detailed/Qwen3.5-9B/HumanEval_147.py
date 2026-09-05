from typing import List, Tuple

def _generate_sequence(n: int) -> List[int]:
    """
    Generates the sequence a where a[i] = i * i - i + 1 for 1-based index i.

    Args:
        n (int): The length of the sequence to generate (1 ≤ n).

    Returns:
        List[int]: The generated sequence of integers.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if n < 1:
        raise ValueError(f"Input n must be a positive integer (≥ 1), got {n}")

    sequence = []
    for i in range(1, n + 1):
        value = i * i - i + 1
        sequence.append(value)

    return sequence

def _get_remainder_mod_3(number: int) -> int:
    """
    Computes the remainder of a number when divided by 3.
    Handles negative numbers correctly to always return 0, 1, or 2.

    Args:
        number (int): The integer to compute the remainder for.

    Returns:
        int: The remainder in the range [0, 2].
    """
    return number % 3

def _count_valid_triples(
    sequence: List[int],
    n: int
) -> int:
    """
    Counts the number of triples (i, j, k) such that 0 ≤ i < j < k < n
    and (sequence[i] + sequence[j] + sequence[k]) is divisible by 3.

    Args:
        sequence (List[int]): The list of integers to examine.
        n (int): The length of the sequence (must match len(sequence)).

    Returns:
        int: The count of valid triples.
    """
    if n < 3:
        return 0

    count = 0
    remainder_sum_mod_3 = 0

    # Iterate through all possible triples with explicit indices
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum_abc = sequence[i] + sequence[j] + sequence[k]
                remainder_sum_mod_3 = _get_remainder_mod_3(sum_abc)

                if remainder_sum_mod_3 == 0:
                    count += 1

    return count

def get_max_triples(n: int) -> int:
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected type int for argument 'n', got {type(n).__name__}")

    if n < 1:
        raise ValueError(f"Input n must be a positive integer (≥ 1), got {n}")

    # Validate that n is not excessively large to prevent timeout in O(n^3) approach
    # For production systems, one might switch algorithms for n > 5000.
    if n > 5000:
        raise ValueError("Input n is too large for the current O(n^3) algorithm. Please use n <= 5000.")

    sequence = _generate_sequence(n)

    # Validate sequence generation (sanity check for length)
    if len(sequence) != n:
        raise RuntimeError(f"Internal error: Generated sequence length {len(sequence)} does not match n={n}.")

    result = _count_valid_triples(sequence, n)

    return result