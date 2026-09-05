from typing import Tuple, Union

def substract_elements(tuple1: Tuple[Union[int, float], ...], 
                       tuple2: Tuple[Union[int, float], ...]) -> Tuple[Union[int, float], ...]:
    """
    Subtracts the elements of the second tuple from the corresponding elements 
    of the first tuple.

    Args:
        tuple1: The minuend tuple containing numbers.
        tuple2: The subtrahend tuple containing numbers.

    Returns:
        A tuple containing the results of (tuple1[i] - tuple2[i]).

    Raises:
        ValueError: If the tuples are not of the same length.
        TypeError: If the tuples contain non-numeric types.
    """

    # Validate input types: Ensure both inputs are tuples
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise TypeError("Both inputs must be of type tuple.")

    # Handle edge case: Empty tuples
    if len(tuple1) == 0 and len(tuple2) == 0:
        return ()

    # Validate lengths: The problem implies corresponding indices, 
    # which requires equal lengths.
    len1 = len(tuple1)
    len2 = len(tuple2)

    if len1 != len2:
        raise ValueError(
            f"Tuples must have the same length. Received lengths {len1} and {len2}."
        )

    # Result storage
    results: list = []

    # Iterate through elements using indices
    for index in range(len1):
        val1 = tuple1[index]
        val2 = tuple2[index]

        # Type checking for individual elements to ensure they are numeric
        if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
            raise TypeError(
                f"Elements at index {index} must be numbers. "
                f"Found {type(val1).__name__} and {type(val2).__name__}."
            )

        # Perform subtraction
        difference = val1 - val2
        results.append(difference)

    # Convert the list of results back into a tuple to maintain return type consistency
    final_tuple = tuple(results)

    return final_tuple

if __name__ == "__main__":
    # Verification against provided assertions
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    assert substract_elements((11, 2, 3), (24, 45, 16)) == (-13, -43, -13)
    assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)