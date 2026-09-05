from typing import Union, Tuple, List, Any

def _validate_list_input(item: Any) -> None:
    """
    Validates that the provided item is a list.
    Raises a TypeError if the input is not a list.

    :param item: The item to validate.
    :raises TypeError: If item is not a list.
    """
    if not isinstance(item, list):
        raise TypeError(f"Expected a list, but received {type(item).__name__}.")


def _validate_tuple_input(item: Any) -> None:
    """
    Validates that the provided item is a tuple.
    Raises a TypeError if the input is not a tuple.

    :param item: The item to validate.
    :raises TypeError: If item is not a tuple.
    """
    if not isinstance(item, tuple):
        raise TypeError(f"Expected a tuple, but received {type(item).__name__}.")


def add_lists(list_input: List[Any], tuple_input: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """
    Adds the elements of a given list to the end of a given tuple.

    The function takes a list and a tuple as input arguments. It validates
    that the first argument is indeed a list and the second argument is
    indeed a tuple. After validation, it constructs a new tuple consisting
    of all elements from the input tuple followed by all elements from
    the input list.

    This function handles edge cases such as empty lists, empty tuples,
    lists with single elements, tuples with single elements, lists with
    duplicate values, and negative numbers.

    :param list_input: A list of elements to be appended.
    :param tuple_input: A tuple of elements to serve as the base.
    :return: A new tuple containing elements of tuple_input followed by elements of list_input.
    :raises TypeError: If list_input is not a list or tuple_input is not a tuple.
    """

    # Step 1: Validate the list input explicitly
    _validate_list_input(list_input)

    # Step 2: Validate the tuple input explicitly
    _validate_tuple_input(tuple_input)

    # Step 3: Initialize a variable to hold the sequence of elements for the new tuple.
    # We start with the elements from the tuple input.
    combined_elements: List[Any] = list(tuple_input)

    # Step 4: Extend the combined_elements list with the elements from the list input.
    # This handles empty lists gracefully (no changes) and larger lists (all added).
    combined_elements.extend(list_input)

    # Step 5: Convert the combined list back into a tuple to match the return type.
    result_tuple: Tuple[Any, ...] = tuple(combined_elements)

    return result_tuple