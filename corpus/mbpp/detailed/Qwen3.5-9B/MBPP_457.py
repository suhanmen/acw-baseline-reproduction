from typing import List, Any, Union

# Define a type alias for the input structure to improve readability and type safety
# The function expects a list of lists where the inner lists contain elements of any type.
InputType = List[List[Any]]

# The function signature remains exactly as implied by the problem examples.
# Since no explicit signature was provided in the prompt text, we define it based on the
# assertions: it takes a list of lists and returns the shortest list.
# We name the function Find_Min to match the assertion usage.
def Find_Min(list_of_lists: InputType) -> List[Any]:
    """
    Finds and returns the sublist with the minimum length from the provided list of lists.

    This function is defensive and production-grade:
    - It validates that the input is a list.
    - It validates that every element in the input list is itself a list.
    - It handles the edge case of an empty input list.
    - It handles the edge case where the input list contains empty sublists.
    - It does not use dense one-liners; logic is split into named steps.

    Parameters:
        list_of_lists (InputType): A list containing other lists as its elements.

    Returns:
        List[Any]: The sublist (from the input) that has the smallest length.

    Raises:
        TypeError: If the input is not a list or if any element is not a list.
        ValueError: If the input list is empty.
    """

    # Step 1: Validate that the main input is a list.
    if not isinstance(list_of_lists, list):
        raise TypeError(
            f"Expected a list of lists, but received: {type(list_of_lists).__name__}"
        )

    # Step 2: Validate that the input list is not empty.
    # This is a degenerate case where no sublist can be found.
    if len(list_of_lists) == 0:
        raise ValueError("Input list of lists cannot be empty.")

    # Step 3: Validate that every element within the main list is itself a list.
    # This ensures type consistency before attempting to compare lengths.
    for index, item in enumerate(list_of_lists):
        if not isinstance(item, list):
            raise TypeError(
                f"Element at index {index} is not a list. "
                f"Expected a list, but received: {type(item).__name__}"
            )

    # Step 4: Initialize variables to track the shortest list found so far.
    # We initialize the 'shortest_sublist' to None to indicate it hasn't been set yet.
    shortest_sublist: Union[List[Any], None] = None

    # We initialize the 'min_length' to a value that any valid list length will be less than or equal to.
    # Since lists have non-negative integer lengths, -1 is a safe sentinel value.
    min_length: int = -1

    # Step 5: Iterate through each sublist in the input list.
    # Using explicit indexing allows us to maintain clear control flow.
    for index, current_sublist in enumerate(list_of_lists):
        # Get the length of the current sublist.
        current_length: int = len(current_sublist)

        # Step 6: Compare the current sublist's length with the minimum found so far.
        if shortest_sublist is None:
            # First iteration: assign the first sublist as the shortest by default.
            shortest_sublist = current_sublist
            min_length = current_length
        else:
            # Subsequent iterations: update if a shorter list is found.
            # We use '<' to ensure that if lengths are equal, we keep the first one encountered
            # (stable behavior, though not strictly required, it is predictable).
            if current_length < min_length:
                shortest_sublist = current_sublist
                min_length = current_length
            # If current_length == min_length, we do nothing (keep the original shortest).
            # If current_length > min_length, we do nothing (current is longer).

    # Step 7: Return the identified shortest sublist.
    # The validation steps ensure this variable is always initialized before this point.
    return shortest_sublist