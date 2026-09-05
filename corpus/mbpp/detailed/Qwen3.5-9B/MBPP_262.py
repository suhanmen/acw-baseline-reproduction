from typing import List, Any, Tuple, Optional

def validate_list_input(input_list: Any) -> List[Any]:
    """
    Validates that the input is a list.
    Returns the list if valid, raises a TypeError otherwise.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but got {type(input_list).__name__}")
    return input_list

def validate_split_length(split_length: int) -> int:
    """
    Validates that the split length is a non-negative integer.
    Returns the split length if valid, raises a TypeError or ValueError otherwise.
    """
    if not isinstance(split_length, int) or isinstance(split_length, bool):
        raise TypeError(f"Split length must be an integer, but got {type(split_length).__name__}")
    if split_length < 0:
        raise ValueError(f"Split length cannot be negative, but got {split_length}")
    return split_length

def split_two_parts(input_list: Any, split_length: int) -> Tuple[List[Any], List[Any]]:
    """
    Splits a given list into two parts where the length of the first part
    is determined by the split_length parameter.

    Args:
        input_list: The list to be split.
        split_length: The desired length of the first part of the split list.

    Returns:
        A tuple containing two lists: the first part and the second part.

    Raises:
        TypeError: If input_list is not a list or split_length is not an integer.
        ValueError: If split_length is negative.
    """
    # Step 1: Validate the input list type
    validated_list = validate_list_input(input_list)

    # Step 2: Validate the split length
    validated_split_length = validate_split_length(split_length)

    # Step 3: Check for edge case where split length exceeds list length
    # Although slicing handles this gracefully by returning a shorter list for the second part,
    # explicit handling or awareness is important for defensive programming logic.
    list_length = len(validated_list)

    if validated_split_length > list_length:
        # In this specific problem context based on the assertions, 
        # the second part should be empty if the split length exceeds the list size.
        # Standard Python slicing [list_length:] returns an empty list, so we can proceed directly.
        # However, if strict adherence to "exactly split_length elements in first part" was required 
        # (even if negative), we would raise an error. Based on the provided assertions, 
        # the behavior should match standard slicing semantics where the second part absorbs the overflow logic 
        # implicitly by being empty.
        first_part = validated_list[:validated_split_length]
        second_part = validated_list[validated_split_length:]
        return first_part, second_part

    # Step 4: Perform the split using standard slicing
    # This handles all valid cases: empty list, single element, all equal elements,
    # boundary values, zero/negative numbers (if elements were numbers), etc.
    first_part = validated_list[:validated_split_length]
    second_part = validated_list[validated_split_length:]

    # Step 5: Return the result as a tuple of two lists
    return first_part, second_part