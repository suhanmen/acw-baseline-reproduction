from typing import List


def multiples_of_num(m: int, n: int) -> List[int]:
    """
    Finds m number of multiples of n.

    Based on the provided test cases:
    multiples_of_num(4, 3) -> [3, 6, 9, 12]
    multiples_of_num(2, 5) -> [5, 10]
    multiples_of_num(9, 2) -> [2, 4, 6, 8, 10, 12, 14, 16, 18]

    The pattern indicates:
    - 'm' is the count of multiples to return.
    - 'n' is the base number whose multiples are being generated.
    - The result is [n*1, n*2, ..., n*m].
    """

    # --- Input Validation ---

    # Check if m (the count) is a non-negative integer.
    # The count must be at least 0 to return an empty list or more.
    if not isinstance(m, int):
        raise TypeError(f"The count 'm' must be an integer, received: {type(m).__name__}")
    if m < 0:
        raise ValueError(f"The count 'm' cannot be negative, received: {m}")

    # Check if n (the base) is an integer.
    # Based on the assertions, n is a positive integer.
    if not isinstance(n, int):
        raise TypeError(f"The base 'n' must be an integer, received: {type(n).__name__}")

    # --- Edge Case Handling ---

    # If m is 0, the user wants zero multiples.
    if m == 0:
        return []

    # --- Logic Implementation ---

    multiples_list: List[int] = []

    # We need to generate multiples from 1 up to m (inclusive).
    # We use a range starting at 1 and ending at m + 1.
    for current_multiplier in range(1, m + 1):
        # Calculate the current multiple.
        current_multiple = n * current_multiplier

        # Append the result to our collection.
        multiples_list.append(current_multiple)

    return multiples_list


if __name__ == "__main__":
    # Testing the provided assertions to ensure correctness.

    # Test Case 1: multiples_of_num(4, 3) == [3, 6, 9, 12]
    result1 = multiples_of_num(4, 3)
    assert result1 == [3, 6, 9, 12], f"Expected [3, 6, 9, 12], but got {result1}"

    # Test Case 2: multiples_of_num(2, 5) == [5, 10]
    result2 = multiples_of_num(2, 5)
    assert result2 == [5, 10], f"Expected [5, 10], but got {result2}"

    # Test Case 3: multiples_of_num(9, 2) == [2, 4, 6, 8, 10, 12, 14, 16, 18]
    result3 = multiples_of_num(9, 2)
    assert result3 == [2, 4, 6, 8, 10, 12, 14, 16, 18], f"Expected [2, 4, 6, 8, 10, 12, 14, 16, 18], but got {result3}"

    # Additional Edge Case: m = 0
    assert multiples_of_num(0, 10) == []

    # Additional Edge Case: n = 0
    assert multiples_of_num(3, 0) == [0, 0, 0]