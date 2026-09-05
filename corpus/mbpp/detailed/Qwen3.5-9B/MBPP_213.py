from typing import Tuple, Union

def validate_strings_sequence(sequence: Union[tuple, list]) -> None:
    """
    Validates that the provided sequence is not None and contains only string elements.

    Args:
        sequence: The sequence to validate.

    Raises:
        TypeError: If the sequence is None or contains non-string elements.
    """
    if sequence is None:
        raise TypeError("Input sequence cannot be None.")

    if not isinstance(sequence, (tuple, list)):
        raise TypeError(f"Input must be a tuple or list, but got {type(sequence).__name__}.")

    for index, item in enumerate(sequence):
        if not isinstance(item, str):
            raise TypeError(f"Element at index {index} is not a string: {type(item).__name__}.")

def concatenate_pair(first_part: str, second_part: str) -> str:
    """
    Concatenates two individual strings together.

    Args:
        first_part: The first string.
        second_part: The second string.

    Returns:
        The concatenated string.
    """
    return first_part + second_part

def concatenate_tuples(tuple_a: Tuple[str, ...], tuple_b: Tuple[str, ...]) -> Tuple[str, ...]:
    """
    Main function to concatenate two tuples of strings element-wise.

    Each element in tuple_a is concatenated with the corresponding element 
    in tuple_b to form a new tuple of strings.

    Args:
        tuple_a: The first tuple of strings.
        tuple_b: The second tuple of strings.

    Returns:
        A new tuple where each element is the concatenation of corresponding 
        elements from tuple_a and tuple_b.

    Raises:
        ValueError: If the lengths of the two tuples are not equal.
        TypeError: If inputs are not tuples/lists of strings (validated separately).
    """
    # Validate input types and contents explicitly
    validate_strings_sequence(tuple_a)
    validate_strings_sequence(tuple_b)

    # Check for length equality
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    if length_a != length_b:
        raise ValueError(
            f"Tuples must be of equal length to concatenate element-wise. "
            f"Got length {length_a} and {length_b}."
        )

    # Handle the degenerate case of empty tuples explicitly
    if length_a == 0:
        return ()

    result_list: list = []

    # Iterate through the tuples to perform element-wise concatenation
    for i in range(length_a):
        current_element_a = tuple_a[i]
        current_element_b = tuple_b[i]
        combined_string = concatenate_pair(current_element_a, current_element_b)
        result_list.append(combined_string)

    # Convert the result list back to a tuple to match the expected return type
    return tuple(result_list)

# The function is defined above. 
# To ensure it meets the problem constraints exactly as requested without external test code blocks,
# we define the function signature and logic fully within this block.
# The assertions provided in the problem description are satisfied by the logic below.

# Re-exporting the function name as requested by the problem context (though in a real file 
# this would be the main entry point). The function above is `concatenate_tuples`.
# However, the problem asks to "Write a function... Your function must satisfy these assertions"
# with the name implied to be `concatenate_strings` based on the assertion calls.
# Therefore, I will create an alias or rename the main logic to match the assertion signature exactly.

concatenate_strings = concatenate_tuples