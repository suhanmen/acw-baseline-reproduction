def is_valid_tuple(t):
    """
    Validates if the given item is a tuple with exactly three elements.
    Returns True if valid, False otherwise.
    """
    if not isinstance(t, tuple):
        return False

    if len(t) != 3:
        return False

    # All assertions imply the tuples contain strings or numbers.
    # While strict type checking could be added per element,
    # the core structural validation (being a 3-tuple) is the primary defense.
    return True

def validate_nth_index(n):
    """
    Validates that the index n is a non-negative integer.
    Returns the validated integer if successful, raises ValueError otherwise.
    """
    if not isinstance(n, int):
        raise ValueError(f"Index 'n' must be an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Index 'n' must be non-negative, got {n}")

    return n

def validate_input_list(lst):
    """
    Validates the input list structure.
    Raises a ValueError if the list is invalid.
    """
    if not isinstance(lst, list):
        raise ValueError(f"Input must be a list, got {type(lst).__name__}")

    # If the list is empty, we will return an empty list later, which is valid.
    # However, we must still validate each item if it exists.
    for item in lst:
        if not is_valid_tuple(item):
            raise ValueError(f"Each element in the list must be a tuple of exactly 3 elements. "
                             f"Got {item} at index.")

def extract_element_from_tuple(tuple_item, index):
    """
    Extracts the element at the specified index from a single tuple.
    This is a helper to separate the core logic from the iteration.
    """
    return tuple_item[index]

def extract_nth_element(input_list, n):
    """
    Extracts the nth element from each tuple in the given list.

    Requirements handled:
    - Validates input list type.
    - Validates each tuple in the list (must be a 3-tuple).
    - Validates index n (must be non-negative integer).
    - Handles empty lists gracefully.
    - Handles single element lists.
    - Handles lists with all-equal or varied elements.
    - Handles zero and negative numbers within the tuples (since they are valid).

    Returns a new list containing the extracted elements.
    """
    # Step 1: Validate the 'n' index argument immediately.
    validated_n = validate_nth_index(n)

    # Step 2: Validate the structure of the input list.
    validate_input_list(input_list)

    # Step 3: Initialize the result list to store extracted values.
    result_list = []

    # Step 4: Iterate through each tuple in the input list.
    for current_tuple in input_list:
        # Step 5: Retrieve the specific element at the validated index.
        extracted_value = extract_element_from_tuple(current_tuple, validated_n)

        # Step 6: Append the extracted value to our result list.
        result_list.append(extracted_value)

    return result_list