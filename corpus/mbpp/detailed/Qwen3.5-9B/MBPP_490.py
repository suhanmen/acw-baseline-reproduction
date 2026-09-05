def extract_symmetric(tuple_list):
    """
    Extracts all pairs which are symmetric in the given tuple list.

    A symmetric pair is defined as two tuples (a, b) and (b, a) where a != b.
    The function returns a set containing one representative from each symmetric
    pair found, with the smaller tuple (lexicographically) appearing first.

    Parameters:
    tuple_list (list): A list of tuples containing integers

    Returns:
    set: A set of tuples representing the symmetric pairs found

    Raises:
    TypeError: If the input is not a list or if any element is not a tuple of exactly 2 integers
    """

    # Step 1: Validate the input type
    if not isinstance(tuple_list, list):
        raise TypeError("Input must be a list of tuples")

    # Step 2: Initialize the set to store the result
    symmetric_pairs = set()

    # Step 3: Process each tuple in the list
    for current_tuple in tuple_list:

        # Step 4: Validate that the current element is a tuple
        if not isinstance(current_tuple, tuple):
            raise TypeError(f"All elements must be tuples, found: {type(current_tuple)}")

        # Step 5: Validate that the tuple has exactly 2 elements
        if len(current_tuple) != 2:
            raise TypeError(f"All tuples must have exactly 2 elements, found: {len(current_tuple)}")

        # Step 6: Validate that both elements are integers
        first_element, second_element = current_tuple

        if not isinstance(first_element, int):
            raise TypeError(f"First element must be an integer, found: {type(first_element)}")

        if not isinstance(second_element, int):
            raise TypeError(f"Second element must be an integer, found: {type(second_element)}")

        # Step 7: Create the reverse tuple
        reverse_tuple = (second_element, first_element)

        # Step 8: Check if the reverse tuple exists in the original list
        # We need to check if reverse_tuple is in tuple_list
        is_symmetric = reverse_tuple in tuple_list

        # Step 9: If symmetric, add the lexicographically smaller tuple to the result set
        if is_symmetric:
            if current_tuple < reverse_tuple:
                symmetric_pairs.add(current_tuple)
            elif reverse_tuple < current_tuple:
                symmetric_pairs.add(reverse_tuple)
            # If they are equal (which shouldn't happen if a != b), we don't add anything
            # as there's no distinct pair

    # Step 10: Return the set of symmetric pairs
    return symmetric_pairs