from typing import List, Tuple, Union

def _is_valid_list_of_integers(input_list: List) -> bool:
    """
    Helper function to validate that the input is a list and all elements are integers.

    Returns:
        True if valid, False otherwise.
    """
    if not isinstance(input_list, list):
        return False

    for element in input_list:
        if not isinstance(element, int):
            return False

    return True

def _filter_negative_numbers(numbers: List[int]) -> Tuple[int, ...]:
    """
    Helper function to filter negative numbers from a list of integers.

    Returns:
        A tuple containing only the negative integers from the input list,
        preserving their original order. Returns an empty tuple if no
        negative numbers are found.
    """
    result_list = []

    for number in numbers:
        # Explicitly check if the number is strictly less than zero
        if number < 0:
            result_list.append(number)

    # Convert the resulting list to a tuple as required by the assertions
    return tuple(result_list)

def neg_nos(numbers: List) -> Tuple[int, ...]:
    """
    Prints nothing to stdout (as per standard function behavior, though the problem
    description mentions 'print', the assertions expect a return value). 
    This function returns a tuple of negative numbers found in the input list.

    This function is designed to be robust and defensive:
    1. It validates the input type and contents.
    2. It handles edge cases like empty lists, single elements, etc.
    3. It explicitly steps through the logic rather than using dense one-liners.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing all negative integers from the input list in their original order.
        If no negative numbers are found or the list is empty, returns an empty tuple.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Step 1: Validate the input structure
    if not _is_valid_list_of_integers(numbers):
        raise TypeError("Input must be a list containing only integers.")

    # Step 2: Explicitly handle the empty list edge case before processing (though the loop handles it, this makes intent clear)
    if len(numbers) == 0:
        return ()

    # Step 3: Initialize an empty list to collect negative numbers
    negative_numbers_collection = []

    # Step 4: Iterate through each number in the list with explicit control flow
    for current_number in numbers:
        # Step 5: Check the condition for being negative (strictly less than 0)
        if current_number < 0:
            # Step 6: Append the negative number to our collection
            negative_numbers_collection.append(current_number)

    # Step 7: Convert the final list to a tuple to match the expected return type in assertions
    final_result_tuple = tuple(negative_numbers_collection)

    return final_result_tuple