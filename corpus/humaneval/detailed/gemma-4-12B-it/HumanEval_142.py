from typing import List


def sum_squares(lst: List[int]) -> int:
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    # Input Validation: Ensure the input is actually a list
    if not isinstance(lst, list):
        raise TypeError(f"Expected input type 'list', but received '{type(lst).__name__}'")

    # Edge Case: Empty list
    if not lst:
        return 0

    # Create a new list to store modified values to avoid mutating the input list
    # This is a defensive programming best practice.
    processed_list = []

    for index, value in enumerate(lst):
        # Input Validation: Ensure each element is an integer
        if not isinstance(value, int):
            raise ValueError(f"All elements in the list must be integers. Found {type(value).__name__} at index {index}.")

        # Determine the transformation based on the index
        # Logic:
        # 1. If index % 3 == 0 -> Square the value
        # 2. Else if index % 4 == 0 -> Cube the value
        # 3. Else -> Keep the value as is

        is_multiple_of_3 = (index % 3 == 0)
        is_multiple_of_4 = (index % 4 == 0)

        new_value = value

        if is_multiple_of_3:
            # Square the integer entry
            new_value = value ** 2
        elif is_multiple_of_4:
            # Cube the integer entry (only if not a multiple of 3)
            new_value = value ** 3
        else:
            # No change required
            new_value = value

        processed_list.append(new_value)

    # Calculate the sum of the processed list
    total_sum = 0
    for item in processed_list:
        total_sum += item

    return total_sum