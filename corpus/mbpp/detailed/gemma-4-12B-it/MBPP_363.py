from typing import List, Tuple, Union

def _validate_input(data: List[Tuple[int, ...]], k: int) -> None:
    """
    Validates the input types and structures to ensure production-grade robustness.

    Args:
        data: A list of tuples containing integers.
        k: An integer value to add to each element.

    Raises:
        TypeError: If data is not a list or k is not an integer.
        ValueError: If any element within the tuples is not an integer.
    """
    if not isinstance(data, list):
        raise TypeError(f"Expected input 'data' to be a list, but got {type(data).__name__}")

    if not isinstance(k, int):
        raise TypeError(f"Expected 'k' to be an integer, but got {type(k).__name__}")

    for index, inner_tuple in enumerate(data):
        if not isinstance(inner_tuple, tuple):
            raise TypeError(f"Element at index {index} must be a tuple, but got {type(inner_tuple).__name__}")

        for element_index, value in enumerate(inner_tuple):
            if not isinstance(value, int):
                raise ValueError(
                    f"Element at data index {index}, tuple index {element_index} "
                    f"must be an integer, but got {type(value).__name__}"
                )

def _transform_single_tuple(input_tuple: Tuple[int, ...], k: int) -> Tuple[int, ...]:
    """
    Takes a single tuple of integers and adds k to every element.

    Args:
        input_tuple: A tuple of integers.
        k: The integer to add.

    Returns:
        A new tuple with the modified values.
    """
    # Handle the case where the tuple might be empty
    if not input_tuple:
        return ()

    transformed_elements = []
    for value in input_tuple:
        new_value = value + k
        transformed_elements.append(new_value)

    return tuple(transformed_elements)

def add_K_element(data: List[Tuple[int, ...]], k: int) -> List[Tuple[int, ...]]:
    """
    Adds the value k to every element within every tuple inside a list of tuples.

    Args:
        data: A list of tuples (e.g., [(1, 2), (3, 4)]).
        k: The integer to add to each element.

    Returns:
        A new list of tuples where every integer has been incremented by k.

    Raises:
        TypeError/ValueError: If inputs are not of the correct types or structure.
    """
    # Step 1: Defensive Input Validation
    _validate_input(data, k)

    # Step 2: Handle edge case for empty list input
    if not data:
        return []

    # Step 3: Process the list
    # We initialize a new list to ensure we don't mutate the input list (immutability principle)
    result_list = []

    for current_tuple in data:
        # Step 4: Process each individual tuple
        # We call a helper function to encapsulate the transformation logic
        new_tuple = _transform_single_tuple(current_tuple, k)

        # Step 5: Collect the result
        result_list.append(new_tuple)

    return result_list

if __name__ == "__main__":
    # Test cases provided in the problem description
    assert add_K_element([(1, 3, 4), (2, 4, 6), (3, 8, 1)], 4) == [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
    assert add_K_element([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 8) == [(9, 10, 11), (12, 13, 14), (15, 16, 17)]
    assert add_K_element([(11, 12, 13), (14, 15, 16), (17, 18, 19)], 9) == [(20, 21, 22), (23, 24, 25), (26, 27, 28)]