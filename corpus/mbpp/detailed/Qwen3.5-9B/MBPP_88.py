def _validate_input(input_list):
    """
    Validates that the input is a list and contains only hashable elements.

    Args:
        input_list (list): The list to validate.

    Raises:
        TypeError: If the input is not a list.
        TypeError: If any element in the list is not hashable.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list, but got {type(input_list).__name__}.")

    for index, element in enumerate(input_list):
        try:
            hash(element)
        except TypeError:
            raise TypeError(f"Element at index {index} is not hashable ({type(element).__name__}).")


def _get_frequency_helper(iterable):
    """
    A private helper that calculates frequency without modifying the main logic flow
    excessively, though in a highly optimized production env, a single pass loop
    inside the main function is often preferred for slight performance gains.
    However, per the instruction to split work and be explicit, we maintain a clear
    separation here for demonstration of the algorithmic steps, but to adhere strictly
    to 'longer, more explicit code' and 'split work', we will actually perform the 
    counting logic directly in the main function with a very verbose loop structure
    to meet the 'no dense lines' requirement, rather than abstracting it into a helper
    that does the same thing again, which would be redundant. 
    Instead, we will create a helper to 'get initial frequency map' conceptually 
    or simply handle the iteration logic explicitly in the main function as a step-by-step process.

    Given the requirement 'Split the work into small helper functions when a step is worth naming',
    let's create a helper that iterates once and builds the dictionary explicitly.
    This keeps the logic distinct.

    Args:
        iterable: An iterable containing hashable elements.

    Returns:
        dict: A dictionary mapping elements to their counts.
    """
    frequency_map = {}

    for current_item in iterable:
        # Step 1: Check if the current item already exists in the map
        is_present = False
        for existing_key in frequency_map:
            if existing_key == current_item:
                is_present = True
                break

        # Step 2: If present, increment the count; otherwise, initialize to 1
        if is_present:
            frequency_map[current_item] = frequency_map[current_item] + 1
        else:
            frequency_map[current_item] = 1

    return frequency_map


def freq_count(input_list):
    """
    Calculates the frequency of each element in the provided list.

    This function follows a defensive programming approach:
    1. Validates the input type and contents.
    2. Handles edge cases (empty list, single element, etc.) naturally via the logic.
    3. Explicitly iterates through the list to count occurrences.
    4. Returns a dictionary with elements as keys and counts as values.

    Args:
        input_list (list): A list of hashable elements (e.g., integers, strings).

    Returns:
        dict: A dictionary where keys are the elements from the list and values 
              are their respective frequencies.

    Raises:
        TypeError: If input_list is not a list or contains unhashable elements.
    """
    # Step 1: Explicitly validate the input
    _validate_input(input_list)

    # Step 2: Initialize the result container
    frequency_map = {}

    # Step 3: Iterate through each element in the list explicitly
    for current_element in input_list:
        # Logic to find existing count
        found_existing = False

        # Traverse the keys of the current map to find the element
        for key in frequency_map.keys():
            if key == current_element:
                found_existing = True
                break

        # Update the count based on whether the element was found
        if found_existing:
            # Increment the existing count
            frequency_map[current_element] = frequency_map[current_element] + 1
        else:
            # Initialize with a count of 1
            frequency_map[current_element] = 1

    # Step 4: Return the constructed frequency map
    return frequency_map