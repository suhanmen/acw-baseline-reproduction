from typing import Tuple


def bitwise_xor(tuple_a: Tuple[int, ...], tuple_b: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    Performs a bitwise XOR operation between corresponding elements of two tuples.

    Args:
        tuple_a: A tuple of integers.
        tuple_b: A tuple of integers.

    Returns:
        A tuple of integers where each element is the result of tuple_a[i] ^ tuple_b[i].

    Raises:
        ValueError: If the input tuples are not of the same length.
        TypeError: If any element in the tuples is not an integer.
    """
    # Validate that both inputs are actually tuples
    if not isinstance(tuple_a, tuple) or not isinstance(tuple_b, tuple):
        raise TypeError("Both inputs must be of type 'tuple'.")

    # Validate that the tuples are of the same length
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    if length_a != length_b:
        raise ValueError(
            f"Tuples must have the same length. Received lengths: {length_a} and {length_b}."
        )

    # Handle the edge case of empty tuples explicitly
    if length_a == 0:
        return ()

    # Initialize a list to store results to maintain O(n) construction
    # We use a list because tuples are immutable.
    xor_results = []

    # Iterate through the indices of the tuples
    for index in range(length_a):
        val_a = tuple_a[index]
        val_b = tuple_b[index]

        # Validate that the elements are integers
        if not isinstance(val_a, int) or not isinstance(val_b, int):
            raise TypeError(
                f"All elements in the tuples must be integers. "
                f"Found {type(val_a)} and {type(val_b)} at index {index}."
            )

        # Perform the bitwise XOR operation
        # Example: 10 (1010) ^ 5 (0101) = 15 (1111)
        result = val_a ^ val_b

        # Append the result to our accumulator list
        xor_results.append(result)

    # Convert the result list back into a tuple to match the required output format
    final_tuple = tuple(xor_results)

    return final_tuple


if __name__ == "__main__":
    # Verification of the provided assertions
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)