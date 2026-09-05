from typing import List, Any

def is_sorted(lst: List[Any]) -> bool:
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''

    # Validate input type
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    # Validate input elements are integers
    for index, element in enumerate(lst):
        if not isinstance(element, int):
            raise TypeError(f"All elements in the list must be integers, but got {type(element).__name__} at index {index}.")
        if isinstance(element, bool):
            raise TypeError("Boolean values are not allowed as integers in this function.")

    # Handle empty list case
    if len(lst) == 0:
        return True

    # Helper function to check for strict ascending order without more than one duplicate
    def check_sorted_and_unique_dups(numbers: List[int]) -> bool:
        # Track previous number and count of consecutive duplicates
        previous_number = None
        consecutive_duplicate_count = 0

        # Iterate through each number in the list
        for current_number in numbers:
            if previous_number is not None:
                # Check if the current number is less than the previous number
                if current_number < previous_number:
                    return False

                # Check if the current number is equal to the previous number
                if current_number == previous_number:
                    # Increment the consecutive duplicate count
                    consecutive_duplicate_count += 1
                    # If more than one consecutive duplicate is found, return False
                    if consecutive_duplicate_count > 1:
                        return False
                else:
                    # Reset the consecutive duplicate count when moving to a new number
                    consecutive_duplicate_count = 0

            # Update the previous number for the next iteration
            previous_number = current_number

        # If the loop completes without returning False, the list is sorted correctly
        return True

    # Delegate the checking logic to the helper function
    return check_sorted_and_unique_dups(lst)