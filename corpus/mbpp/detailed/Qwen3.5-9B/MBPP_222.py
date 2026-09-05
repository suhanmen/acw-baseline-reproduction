from typing import Any, Tuple, Union


def check_type(input_tuple: Tuple[Any, ...]) -> bool:
    """
    Check if all elements in the given tuple have the same data type.

    This function validates that:
    1. The input is indeed a tuple.
    2. The tuple contains at least one element (though an empty tuple technically 
       has no conflicting types, the problem constraints and typical defensive 
       programming suggest treating it or handling it explicitly; here we assume 
       an empty tuple returns True as there are no counterexamples, but we explicitly 
       handle it).
    3. If the tuple has more than one element, all elements must be of the exact 
       same type (e.g., all ints, all strings, etc.).

    Parameters:
        input_tuple (Tuple[Any, ...]): The tuple to be checked.

    Returns:
        bool: True if all elements have the same type, False otherwise.
              If the input is not a tuple, a TypeError is raised.
    """

    # Step 1: Validate that the input is a tuple.
    # We explicitly check the type to prevent unexpected behavior with lists or other sequences.
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Input must be a tuple, but got {type(input_tuple).__name__}")

    # Step 2: Handle the edge case of an empty tuple.
    # An empty tuple has no elements that conflict, so it is logically consistent 
    # to say they are all the same type (vacuously true).
    if len(input_tuple) == 0:
        return True

    # Step 3: Handle the edge case of a single-element tuple.
    # A single element cannot conflict with another, so it is always True.
    if len(input_tuple) == 1:
        return True

    # Step 4: Extract the type of the first element.
    # This will serve as the reference type against which all others are compared.
    first_element = input_tuple[0]
    reference_type = type(first_element)

    # Step 5: Iterate through the rest of the tuple (starting from the second element).
    # We skip the first element since we already established its type.
    all_elements_match = True
    for index in range(1, len(input_tuple)):
        current_element = input_tuple[index]
        current_element_type = type(current_element)

        # Compare the current element's type with the reference type.
        if current_element_type != reference_type:
            # If a mismatch is found, we can immediately stop and return False.
            all_elements_match = False
            break

    # Step 6: Return the result of the check.
    return all_elements_match