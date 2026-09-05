from typing import List, Union

# Define a type alias for clarity regarding the expected list structure.
# The function accepts a list of elements (any type) and a list of elements (any type).
ReplaceListInput = Union[List, tuple, None]  # Using Union to allow flexibility, though logic handles lists primarily.

def _is_empty_list(value) -> bool:
    """
    Helper function to check if the given value is a list and if it is empty.

    This separates the logic of checking for empty containers from the 
    assertion of the container type to make the code more readable and testable.
    """
    if not isinstance(value, list):
        return True
    return len(value) == 0

def _is_none_or_empty_list(value) -> bool:
    """
    Helper function to check if the value is None or an empty list.
    This handles the degenerate case where the original list has no elements.
    """
    if value is None:
        return True
    if not isinstance(value, list):
        # Based on problem context, we expect a list. If it's not a list, 
        # treating it as an empty/invalid state for the purpose of 'last element' access.
        return True
    if len(value) == 0:
        return True
    return False

def replace_list(original_list: List, replacement_list: List) -> List:
    """
    Replaces the last element of the original_list with the entire replacement_list.

    Logic:
    1. Validate inputs. If original_list is None or empty, handle appropriately (return copy of None or empty).
    2. Identify the last element of the original_list.
    3. Create a copy of the original_list to avoid mutating the input directly (defensive programming).
    4. Remove the last element from the copy.
    5. Append the replacement_list to the modified copy.
    6. Return the modified list.

    This function satisfies the requirement that the last element of the list 
    is replaced by another list, effectively flattening the structure at that specific index.
    """

    # Step 1: Input Validation and Edge Case Handling

    # Check if original_list is None
    if original_list is None:
        # If the input is None, we cannot replace a last element. 
        # We return a new list containing the replacement list as its only element? 
        # Or return None? Given the problem assertions only show valid lists, 
        # let's return a new list with the replacement as the sole element to be safe and productive.
        # However, strictly speaking, replacing the "last element of None" is undefined.
        # A defensive approach returning a copy of the replacement list seems logical here.
        # But looking at typical interview patterns for this specific problem statement:
        # Usually, the edge case is an empty list. Let's assume if None, we treat it as empty.
        return replacement_list[:] if replacement_list else []

    # Check if original_list is not a list (invalid type)
    if not isinstance(original_list, list):
        # Return original (defensive) or raise error? 
        # The prompt asks to deal with invalid inputs explicitly.
        # Let's return the original list unchanged but perhaps log or handle it.
        # To be strict with the "replace last element" logic, we need a list.
        # We will return a copy of the original list if it were valid, but since it's not,
        # we'll return a specific indicator or just the original. 
        # For this solution, we will return the original list unchanged with a note in comments,
        # but to strictly follow "deal with invalid", we might return None or raise.
        # Let's choose to return the original list as a 'best effort' or raise ValueError.
        # Given "complete and runnable", raising is cleaner for invalid types.
        raise TypeError("The first argument must be a list.")

    # Check if original_list is empty
    if _is_empty_list(original_list):
        # If the list is empty, there is no last element to replace.
        # We return the replacement list itself, effectively treating the 'empty slot' 
        # as the target for the replacement.
        # Example: replace_list([], [1,2]) -> [1, 2]
        return replacement_list[:]

    # Check if replacement_list is not a list (invalid type)
    if not isinstance(replacement_list, list):
        raise TypeError("The second argument must be a list.")

    # Step 2: Prepare the result list
    # Create a shallow copy to ensure we don't mutate the input list in place.
    result_list = original_list[:]

    # Step 3: Identify the last element
    last_element = result_list[-1]

    # Step 4: Remove the last element
    # Using pop is explicit and clear.
    result_list.pop()

    # Step 5: Extend the list with the replacement list
    # Since we are replacing the element with the list itself, we extend.
    # Example: [1, 3, 5] with [2, 4] -> [1, 3] + [2, 4] = [1, 3, 2, 4]
    result_list.extend(replacement_list)

    return result_list