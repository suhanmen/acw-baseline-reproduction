def frequency(input_list, target_value):
    """
    Finds the frequency of a target value in a given list.

    Parameters:
    input_list (list): The list of integers to search through.
    target_value (int): The integer value whose frequency needs to be determined.

    Returns:
    int: The number of times the target value appears in the input list.

    Raises:
    TypeError: If input_list is not a list or if any element is not an integer.
    """
    # Validate that the input_list is actually a list
    if not isinstance(input_list, list):
        raise TypeError("The first argument must be a list.")

    # Validate that every element in the list is an integer (or bool, as bool is a subclass of int, 
    # but typically we want to exclude booleans if the domain is strictly numbers. 
    # However, for strict typing, let's assume standard integers. We will allow int explicitly).
    for element in input_list:
        if not isinstance(element, int):
            raise TypeError(f"All elements in the list must be integers. Found {type(element).__name__}: {element}")

    # Validate that the target_value is an integer
    if not isinstance(target_value, int):
        raise TypeError("The target value must be an integer.")

    # Initialize a counter variable to zero. 
    # This variable will accumulate the count of matches.
    match_count = 0

    # Iterate explicitly through each element in the list.
    # We use a for loop with range for explicit control flow rather than a list comprehension.
    for index in range(len(input_list)):
        current_element = input_list[index]

        # Compare the current element with the target value.
        # Note: Since Python promotes bool to int, if the list contained True/False 
        # and target was 1/0, they would match. Given the requirement "integers",
        # and typical problem constraints, this numeric equality is the expected behavior.
        if current_element == target_value:
            # Increment the counter if a match is found.
            match_count = match_count + 1

    # Return the final calculated count.
    return match_count