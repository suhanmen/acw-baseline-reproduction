from typing import Any, List, Tuple, Optional

def _validate_input_lists(input_lists: List[List[Any]]) -> None:
    """
    Validates that the input is a non-empty list of lists.
    Raises a ValueError if validation fails.
    """
    if not isinstance(input_lists, list):
        raise TypeError("Input must be a list.")

    if len(input_lists) == 0:
        raise ValueError("Input list cannot be empty.")

    for index, item in enumerate(input_lists):
        if not isinstance(item, list):
            raise TypeError(f"All elements in the input list must be lists. Item at index {index} is not a list.")


def _find_min_length_index_and_value(
    input_lists: List[List[Any]], 
    use_lambda_for_filter: bool = True
) -> Tuple[int, List[Any]]:
    """
    Helper function to find the index of the shortest list and the list itself.
    It uses an explicit loop for clarity, but leverages a lambda function 
    to demonstrate the requirement of using lambda for the comparison logic 
    in a production context where such constraints might be imposed.

    Args:
        input_lists: The list of lists to search.
        use_lambda_for_filter: If True, uses a lambda to define the comparison key.
                               If False, uses a standard lambda-free approach for reference.
                               For this problem, we strictly use the lambda approach as per constraints.

    Returns:
        A tuple containing the index of the shortest list and the shortest list itself.
    """
    # We will use a lambda to define the length getter, as requested by the problem statement
    # "find the list with minimum length using lambda function".
    # Even though we can just use len() directly, we wrap the length calculation logic 
    # in a lambda to satisfy the specific constraint of the problem description.

    get_length = lambda lst: len(lst)

    # Initialize with the first element
    min_length = get_length(input_lists[0])
    min_index = 0
    min_list = input_lists[0]

    # Iterate through the rest of the lists starting from index 1
    for index in range(1, len(input_lists)):
        current_list = input_lists[index]
        current_length = get_length(current_list)

        # Use a lambda for the comparison check as well to be consistent with the spirit of the request
        # Condition: if the current length is strictly less than the minimum found so far.
        is_smaller = lambda curr_len, min_len: curr_len < min_len

        if is_smaller(current_length, min_length):
            min_length = current_length
            min_index = index
            min_list = current_list

    return min_index, min_list


def min_length_list(input_lists: List[List[Any]]) -> Tuple[int, List[Any]]:
    """
    Finds the list with the minimum length from a given list of lists.

    This function returns a tuple containing:
    1. The length of the shortest list (int).
    2. The shortest list itself (list).

    If multiple lists have the same minimum length, the first one encountered 
    (based on the original order) is returned.

    Args:
        input_lists: A list containing multiple lists of arbitrary elements.

    Returns:
        A tuple (min_length, shortest_list).

    Raises:
        TypeError: If the input is not a list or contains non-list elements.
        ValueError: If the input list is empty.
    """
    # Step 1: Validate the input structure explicitly
    _validate_input_lists(input_lists)

    # Step 2: Handle the edge case where the list has exactly one element.
    # Although the main loop handles this, explicit handling can clarify logic flow.
    # However, the general loop covers this naturally if initialized correctly.
    # We rely on the general algorithm below.

    # Step 3: Execute the core logic to find the minimum length list.
    # We use the helper function which encapsulates the search logic using lambdas.
    min_index, min_list = _find_min_length_index_and_value(input_lists)

    # Step 4: Return the result as a tuple (length, list).
    min_len_value = len(min_list)

    return min_len_value, min_list