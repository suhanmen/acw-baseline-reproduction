def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

    # Validate that the input is indeed a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    # Validate that all elements in the list are integers
    for index, element in enumerate(lst):
        if not isinstance(element, int):
            raise TypeError(f"All elements must be integers. Found non-integer at index {index}: {type(element)}")

    # Initialize a variable to hold the running sum
    total_sum = 0

    # Iterate through the list with explicit index tracking
    for index, value in enumerate(lst):
        # Determine the transformation based on the index

        # Check if the index is a multiple of 3
        is_multiple_of_3 = (index % 3 == 0)

        # Check if the index is a multiple of 4
        is_multiple_of_4 = (index % 4 == 0)

        # Determine the operation to perform
        if is_multiple_of_3:
            # Rule: Square the integer entry if its index is a multiple of 3
            transformed_value = value ** 2
        elif is_multiple_of_4:
            # Rule: Cube the integer entry if its index is a multiple of 4 and not a multiple of 3
            # The 'elif' ensures we don't square it if it was already caught by the 'if' above
            transformed_value = value ** 3
        else:
            # Rule: Do not change the entries whose indexes are not a multiple of 3 or 4
            transformed_value = value

        # Add the transformed value to the total sum
        total_sum += transformed_value

    # Return the final calculated sum
    return total_sum