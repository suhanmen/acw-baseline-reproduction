from typing import List


def extract_string(input_list: List[str], target_size: int) -> List[str]:
    """
    Extracts strings from a given list that have a length equal to the 
    specified target_size.

    Args:
        input_list (List[str]): A list of strings to evaluate.
        target_size (int): The length a string must have to be included 
                            in the output.

    Returns:
        List[str]: A list of strings from the input_list that match 
                    the target_size.

    Raises:
        TypeError: If input_list is not a list or target_size is not an int.
        ValueError: If target_size is a negative number.
    """
    # --- Input Validation ---

    # Check if input_list is actually a list
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input_list to be of type list, got {type(input_list).__name__}")

    # Check if target_size is an integer
    if not isinstance(target_size, int):
        raise TypeError(f"Expected target_size to be of type int, got {type(target_size).__name__}")

    # Check if target_size is non-negative
    if target_size < 0:
        raise ValueError(f"target_size must be a non-negative integer, got {target_size}")

    # --- Edge Case Handling ---

    # Handle empty list case
    if len(input_list) == 0:
        return []

    # --- Processing Logic ---

    result_list: List[str] = []

    # Iterate through every element in the provided list
    for current_string in input_list:
        # Validate that the current element is a string
        if not isinstance(current_string, str):
            # In production, we might skip, log, or raise. 
            # Given the problem context, we assume standard behavior is to process strings.
            # Here, we skip non-string types to maintain robustness.
            continue

        # Calculate the length of the current string
        actual_length = len(current_string)

        # Compare the actual length with the target size
        if actual_length == target_size:
            # If it matches, add it to our results
            result_list.append(current_string)

    return result_list


if __name__ == "__main__":
    # Verification of assertions provided in the problem description
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] , 8) == ['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] , 6) == ['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] , 9) == ['exercises']