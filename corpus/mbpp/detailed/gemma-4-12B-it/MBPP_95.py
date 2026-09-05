from typing import List

def Find_Min_Length(sublists: List[List[int]]) -> int:
    """
    Finds the minimum length among all sublists provided in a list of lists.

    Args:
        sublists (List[List[int]]): A list of lists, where each inner list 
                                     contains integers.

    Returns:
        int: The length of the shortest inner list.

    Raises:
        ValueError: If the input list is empty or contains non-list elements.
        TypeError: If the input is not a list of lists.
    """
    # Validate that the input is a list
    if not isinstance(sublists, list):
        raise TypeError("Input must be a list of lists.")

    # Handle the edge case where the outer list is empty
    if len(sublists) == 0:
        raise ValueError("Input list of sublists cannot be empty.")

    # Initialize the minimum length with a value larger than any possible length
    # float('inf') is used as a safe starting point for comparison
    min_length: float = float('inf')

    for index, sublist in enumerate(sublists):
        # Validate that every element in the outer list is actually a list
        if not isinstance(sublist, list):
            raise TypeError(f"Element at index {index} is not a list.")

        # Calculate the length of the current sublist
        current_length = len(sublist)

        # Update min_length if current_length is smaller
        if current_length < min_length:
            min_length = current_length

    # If min_length is still infinity, it means no valid lists were processed
    # (Though the initial empty check should prevent this)
    if min_length == float('inf'):
        raise ValueError("No valid sublists were found to measure.")

    # Convert the result to an integer as per function requirements
    result_length = int(min_length)

    return result_length

if __name__ == "__main__":
    # Verification based on the provided assertions
    assert Find_Min_Length([[1], [1, 2]]) == 1
    assert Find_Min_Length([[1, 2], [1, 2, 3], [1, 2, 3, 4]]) == 2
    assert Find_Min_Length([[3, 3, 3], [4, 4, 4, 4]]) == 3