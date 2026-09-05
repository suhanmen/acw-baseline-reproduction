from typing import List, Tuple, Union

# Define the type alias for a tuple of integers to improve type clarity and documentation.
TupleOfIntegers = Tuple[int, ...]

# Define the type alias for a list of tuples to clarify the expected input structure.
ListOfTuples = List[TupleOfIntegers]

# Define the signature for the input validation function.
def _validate_inputs(tuples_list: Union[List, None], k: Union[int, None]) -> ListOfTuples:
    """
    Validates the input arguments for the add_K_element function.

    This function performs several checks:
    1. Checks if 'tuples_list' is None.
    2. Checks if 'tuples_list' is not a list.
    3. Checks if 'k' is None.
    4. Checks if 'k' is not an integer.
    5. Validates that every element in 'tuples_list' is a tuple.
    6. Validates that every element within the tuples is an integer.

    If any validation fails, it raises a TypeError with a descriptive message.
    """

    # Check if tuples_list is None
    if tuples_list is None:
        raise TypeError("The first argument 'tuples_list' must be a list of tuples, not None.")

    # Check if tuples_list is actually a list
    if not isinstance(tuples_list, list):
        raise TypeError(f"The first argument 'tuples_list' must be a list, but got: {type(tuples_list).__name__}.")

    # Check if k is None
    if k is None:
        raise TypeError("The second argument 'k' must be an integer, not None.")

    # Check if k is an integer (excluding booleans which are technically int subclass in Python)
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError(f"The second argument 'k' must be an integer, but got: {type(k).__name__}.")

    # Validate that every element in the list is a tuple
    for index, item in enumerate(tuples_list):
        if not isinstance(item, tuple):
            raise TypeError(
                f"The element at index {index} in 'tuples_list' must be a tuple, "
                f"but got: {type(item).__name__}."
            )

        # Validate that every element within the tuple is an integer
        for sub_index, sub_item in enumerate(item):
            if isinstance(sub_item, bool):
                raise TypeError(
                    f"Element at tuples_list[{index}][{sub_index}] must be an integer, "
                    f"but got a boolean value ({sub_item})."
                )
            if not isinstance(sub_item, int):
                raise TypeError(
                    f"Element at tuples_list[{index}][{sub_index}] must be an integer, "
                    f"but got: {type(sub_item).__name__}."
                )

    return tuples_list

# Define the type alias for a single resulting tuple.
SingleResultTuple = Tuple[int, ...]

# Define the helper function to process a single tuple.
def _process_single_tuple(t: TupleOfIntegers, k: int) -> SingleResultTuple:
    """
    Adds the value k to each element in a single tuple of integers.

    This function iterates over the input tuple, adds k to each number,
    and returns a new tuple containing the results.

    Args:
        t: A tuple of integers.
        k: The integer to add to each element.

    Returns:
        A new tuple where each element is (original_element + k).
    """

    # Initialize an empty list to hold the results of the addition operation.
    result_list: List[int] = []

    # Iterate through each element in the input tuple
    for element in t:
        # Perform the addition
        new_value = element + k

        # Append the new value to the result list
        result_list.append(new_value)

    # Convert the list of integers back into a tuple to match the required output format
    result_tuple: SingleResultTuple = tuple(result_list)

    return result_tuple

# Define the type alias for the final return type.
FinalReturnType = List[SingleResultTuple]

def add_K_element(tuples_list: List[Tuple[int, ...]], k: int) -> List[Tuple[int, ...]]:
    """
    Adds a specific integer k to each element within every tuple in the provided list.

    This function creates a new list of tuples. Each new tuple corresponds to an input
    tuple, but with k added to every single number inside it.

    The function is designed to be robust against invalid input types and empty structures,
    providing clear error messages for debugging purposes.

    Args:
        tuples_list: A list of tuples, where each tuple contains only integers.
        k: An integer value to be added to every element in the tuples.

    Returns:
        A list of tuples containing the modified integers.

    Raises:
        TypeError: If the input arguments do not meet the type requirements.
    """

    # Step 1: Validate all inputs against the requirements defined above
    validated_list = _validate_inputs(tuples_list, k)

    # Step 2: Initialize an empty list to store the results
    results: List[SingleResultTuple] = []

    # Step 3: Iterate through each validated tuple in the list
    for single_tuple in validated_list:
        # Step 4: Process the current tuple by adding k to its elements
        processed_tuple = _process_single_tuple(single_tuple, k)

        # Step 5: Append the processed tuple to the results list
        results.append(processed_tuple)

    # Step 6: Return the final list of processed tuples
    return results