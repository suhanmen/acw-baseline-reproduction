from typing import List, Optional, Tuple

def _validate_input(
    sequence: List[int],
    target_value: int
) -> Tuple[Optional[Exception], List[int], int]:
    """
    Validates the input arguments and returns a tuple containing:
    - A potential exception if validation fails (None if valid).
    - The validated sequence list.
    - The validated target value.

    Conditions checked:
    1. The sequence must be a list.
    2. All elements in the sequence must be integers.
    3. The target value must be an integer.
    """
    if not isinstance(sequence, list):
        return (ValueError("The 'sequence' argument must be a list."), sequence, target_value)

    for index, element in enumerate(sequence):
        if not isinstance(element, int) or isinstance(element, bool):
            return (
                ValueError(f"All elements in the sequence must be integers. Found non-integer at index {index}: {element!r}."),
                sequence,
                target_value
            )

    if not isinstance(target_value, int) or isinstance(target_value, bool):
        return (
            ValueError("The 'target_value' argument must be an integer."),
            sequence,
            target_value
        )

    # No exceptions raised; inputs are valid.
    return (None, sequence, target_value)

def _find_longest_subsequence_with_diff_one(
    sequence: List[int]
) -> int:
    """
    Finds the length of the longest contiguous subsequence where the absolute
    difference between adjacent elements is exactly 1.

    Parameters:
    - sequence: A list of integers.

    Returns:
    - The maximum length of such a subsequence.

    Logic:
    1. If the sequence is empty, return 0.
    2. Iterate through the sequence starting from the second element.
    3. Track the current run length and the maximum run length found so far.
    4. A run continues if |current_element - previous_element| == 1.
    5. Otherwise, the run resets to length 1 (starting a new run with the current element).
    """
    sequence_length = len(sequence)

    if sequence_length == 0:
        return 0

    # Initialize tracking variables
    max_length = 1
    current_length = 1

    # Start from the second element (index 1)
    for current_index in range(1, sequence_length):
        previous_element = sequence[current_index - 1]
        current_element = sequence[current_index]

        # Calculate absolute difference
        absolute_difference = abs(current_element - previous_element)

        # Check condition: difference must be exactly 1
        if absolute_difference == 1:
            current_length += 1
        else:
            # Reset current run length
            # The new run starts with the current element
            current_length = 1

        # Update global maximum if current run is longer
        if current_length > max_length:
            max_length = current_length

    return max_length

def longest_subseq_with_diff_one(
    sequence: List[int],
    target_value: int
) -> int:
    """
    Finds the length of the longest subsequence such that the difference 
    between adjacent elements is one for the given array.

    The provided 'target_value' argument is accepted for signature compliance 
    but is currently not utilized in the calculation logic, as the problem 
    description implies finding the longest subsequence within the given array 
    based solely on the adjacency difference rule. The function validates both 
    arguments explicitly.

    Parameters:
    - sequence (List[int]): The input array of integers.
    - target_value (int): An integer value (validated but not used in calculation).

    Returns:
    - int: The length of the longest subsequence with adjacent difference of 1.

    Raises:
    - ValueError: If input types are incorrect or elements are not integers.
    """
    # Step 1: Validate inputs
    validation_error, validated_sequence, validated_target = _validate_input(sequence, target_value)

    if validation_error is not None:
        raise validation_error

    # Step 2: Calculate the result using the validated sequence
    # Note: target_value is validated but not used per problem logic interpretation
    result_length = _find_longest_subsequence_with_diff_one(validated_sequence)

    return result_length