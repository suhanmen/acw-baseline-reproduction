from typing import Tuple, Any

def _validate_tuple_input(input_tuple: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """
    Validates that the provided argument is indeed a tuple.
    If it is not a tuple, raises a TypeError with a descriptive message.

    :param input_tuple: The argument to validate.
    :return: The validated tuple (returned for consistency, though mainly used for side-effect of raising).
    """
    if not isinstance(input_tuple, tuple):
        raise TypeError(
            f"Input must be a tuple, but got {type(input_tuple).__name__}."
        )
    return input_tuple

def _validate_repeat_count(count: int) -> int:
    """
    Validates that the repeat count is a non-negative integer.
    Negative counts do not make sense for repetition.
    Non-integer types are invalid.

    :param count: The number of times to repeat the tuple.
    :return: The validated integer count.
    :raises TypeError: If count is not an integer.
    :raises ValueError: If count is negative.
    """
    # We accept bool because bool is a subclass of int in Python, 
    # but semantically False (0) and True (1) might be confusing.
    # However, the requirement says "n times", implying an integer count.
    # Let's strictly check for int and exclude bool to be more semantic, 
    # or allow it if we treat True as 1 and False as 0.
    # Standard practice often allows integers. Let's be strict about types.

    if isinstance(count, bool) or not isinstance(count, int):
        raise TypeError(
            f"Repeat count must be an integer, but got {type(count).__name__}."
        )

    if count < 0:
        raise ValueError(
            f"Repeat count must be non-negative, but got {count}."
        )

    return count

def _create_repeated_structure(base_tuple: Tuple[Any, ...], n: int) -> Tuple[Tuple[Any, ...], ...]:
    """
    Creates a new tuple containing 'n' copies of the 'base_tuple'.
    Each element in the new tuple is a reference to the same base_tuple object.

    :param base_tuple: The tuple to be repeated.
    :param n: The number of times to repeat.
    :return: A tuple of n references to base_tuple.
    """
    # We build the result tuple explicitly to ensure clarity and control.
    # We use a list comprehension for readability and then convert to tuple.
    repeated_list = []
    for _ in range(n):
        repeated_list.append(base_tuple)

    return tuple(repeated_list)

def repeat_tuples(input_tuple: Tuple[Any, ...], n: int) -> Tuple[Tuple[Any, ...], ...]:
    """
    Repeats the given tuple n times.

    This function takes a single tuple and an integer n.
    It returns a new tuple where the original tuple appears n times as an element.

    Edge cases handled:
    - Empty input tuple: Returns a tuple of n empty tuples.
    - Single element input tuple: Returns a tuple of n single-element tuples.
    - All-equal elements: Handled naturally as data is not modified, only referenced.
    - Zero repetitions (n=0): Returns an empty tuple.
    - Large n: Handled by the loop logic (limited by memory constraints of Python).

    :param input_tuple: The tuple to repeat.
    :param n: The number of repetitions (must be a non-negative integer).
    :return: A tuple containing n copies of input_tuple.
    :raises TypeError: If input_tuple is not a tuple or n is not an integer.
    :raises ValueError: If n is negative.
    """
    # Step 1: Validate the input tuple type.
    validated_tuple = _validate_tuple_input(input_tuple)

    # Step 2: Validate the repeat count.
    validated_count = _validate_repeat_count(n)

    # Step 3: Generate the repeated structure using the validated inputs.
    result = _create_repeated_structure(validated_tuple, validated_count)

    return result