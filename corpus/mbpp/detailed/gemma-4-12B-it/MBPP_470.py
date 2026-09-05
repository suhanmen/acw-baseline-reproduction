from typing import Tuple, Union

def add_pairwise(input_tuple: Tuple[Union[int, float], ...]) -> Tuple[Union[int, float], ...]:
    """
    Calculates the pairwise sum of adjacent elements in a tuple.

    Example:
    (1, 5, 7, 8, 10) -> (1+5, 5+7, 7+8, 8+10) -> (6, 12, 15, 18)

    Args:
        input_tuple: A tuple of numbers (integers or floats).

    Returns:
        A tuple containing the sums of adjacent pairs.

    Raises:
        TypeError: If the input is not a tuple or contains non-numeric values.
        ValueError: If the input tuple has fewer than two elements.
    """
    # 1. Input Validation: Ensure the input is actually a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Input must be a tuple, received {type(input_tuple).__name__}")

    # 2. Edge Case: Handle empty tuple or single element tuple
    # Pairwise addition requires at least two elements to form one pair.
    tuple_length = len(input_tuple)
    if tuple_length < 2:
        # The problem logic implies an empty tuple or single element results in an empty tuple
        # because no adjacent pairs exist.
        return ()

    # 3. Content Validation: Ensure all elements are numeric
    for item in input_tuple:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the tuple must be numeric. Found: {type(item).__name__}")

    # 4. Logic Implementation: Iterate through the tuple to calculate sums
    # We stop at the second to last element (index len - 2)
    # because the last element has no successor to add with.
    result_list = []

    for i in range(tuple_length - 1):
        current_element = input_tuple[i]
        next_element = input_tuple[i + 1]

        # Perform the addition
        pair_sum = current_element + next_element

        # Append the result to our intermediate list
        result_list.append(pair_sum)

    # 5. Final Conversion: Convert the list back to a tuple as per the signature requirement
    final_result = tuple(result_list)

    return final_result

# The following assertions verify the correctness of the implementation
if __name__ == "__main__":
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)