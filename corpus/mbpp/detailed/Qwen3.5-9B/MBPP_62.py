def validate_input_list(input_list):
    """
    Validates that the input is a list containing only numbers (int or float).

    Args:
        input_list (list): The list to validate.

    Returns:
        list: The validated input list.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty or contains non-numeric elements.
    """
    # Check if the input is a list
    if not isinstance(input_list, list):
        raise TypeError(
            f"Input must be a list, but got {type(input_list).__name__}."
        )

    # Check if the list is empty
    if len(input_list) == 0:
        raise ValueError("Input list cannot be empty.")

    # Validate that all elements are numeric (int or float, excluding bool)
    for index, element in enumerate(input_list):
        # Check for boolean types specifically, as bool is a subclass of int in Python
        if isinstance(element, bool):
            raise TypeError(
                f"Boolean values are not allowed at index {index}. "
                f"Expected a number."
            )
        if not isinstance(element, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number. "
                f"Got {type(element).__name__} instead of int or float."
            )

    return input_list

def find_min_recursive_helper(current_list, min_value, index):
    """
    Helper function for a recursive approach to find the minimum value.
    This is used to demonstrate explicit logic step-by-step.

    Args:
        current_list (list): The list being processed.
        min_value (number): The current known minimum value.
        index (int): The current index being examined.

    Returns:
        number: The smallest number found so far.
    """
    # Base case: If we have reached the end of the list
    if index >= len(current_list):
        return min_value

    # Get the current element
    current_element = current_list[index]

    # Compare current element with the running minimum
    if current_element < min_value:
        # Update the running minimum
        new_min_value = current_element
    else:
        # Keep the existing minimum
        new_min_value = min_value

    # Recursively process the next index
    return find_min_recursive_helper(current_list, new_min_value, index + 1)

def smallest_num(input_list):
    """
    Finds the smallest number in a list of numbers.

    This function performs the following steps:
    1. Validates the input to ensure it is a non-empty list of numbers.
    2. Handles edge cases (though validation catches most, we ensure logic covers single elements).
    3. Iterates through the list to find the minimum value explicitly.

    Args:
        input_list (list): A list of numbers (int or float).

    Returns:
        number: The smallest number in the list.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If the list is empty.
    """
    # Step 1: Validate the input
    validated_list = validate_input_list(input_list)

    # Step 2: Handle the trivial case of a single element explicitly
    # (Though the loop below would handle it, this makes the intent clear)
    if len(validated_list) == 1:
        smallest = validated_list[0]
        return smallest

    # Step 3: Initialize the smallest variable with the first element
    # This avoids magic numbers like 0 or float('inf') which might behave unexpectedly
    # with all negative numbers if not carefully chosen.
    smallest = validated_list[0]

    # Step 4: Iterate through the rest of the list starting from the second element
    # We use a loop to ensure explicit control flow is visible.
    index_to_check = 1
    total_elements = len(validated_list)

    while index_to_check < total_elements:
        # Retrieve the current candidate for minimum
        current_candidate = validated_list[index_to_check]

        # Explicit comparison logic
        is_smaller = (current_candidate < smallest)

        if is_smaller:
            # Update smallest if the current candidate is smaller
            smallest = current_candidate

        # Move to the next element
        index_to_check += 1

    return smallest