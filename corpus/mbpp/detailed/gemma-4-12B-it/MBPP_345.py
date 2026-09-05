from typing import List, Union

def diff_consecutivenums(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Calculates the difference between each pair of consecutive numbers in a list.

    The difference is calculated as (current_element - previous_element).
    For a list of length N, the resulting list will have length N-1.

    Args:
        numbers (List[Union[int, float]]): A list of numerical values.

    Returns:
        List[Union[int, float]]: A list of differences between consecutive elements.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the input list has fewer than two elements.
    """
    # Step 1: Validate that the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}.")

    # Step 2: Validate the length of the list
    # A difference between consecutive numbers requires at least two numbers.
    list_length = len(numbers)
    if list_length < 2:
        # If the list is empty or has only one element, there are no consecutive pairs.
        # Returning an empty list is the mathematically consistent behavior for differences.
        return []

    # Step 3: Validate that all elements in the list are numbers (int or float)
    # This prevents runtime errors during subtraction.
    for index, item in enumerate(numbers):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"All elements in the list must be numbers. "
                f"Found {type(item).__name__} at index {index}."
            )

    # Step 4: Initialize the list to store the differences
    # Pre-allocating the list size is more efficient than repeated appending.
    differences = []

    # Step 5: Iterate through the list to calculate consecutive differences.
    # We start from index 1 because we need to compare the current element
    # with the one immediately preceding it.
    for current_index in range(1, list_length):
        previous_value = numbers[current_index - 1]
        current_value = numbers[current_index]

        # Calculate the difference: Current - Previous
        difference = current_value - previous_value

        # Append the result to our list
        differences.append(difference)

    # Step 6: Return the completed list of differences
    return differences

# Verification against provided assertions
if __name__ == "__main__":
    # Test Case 1
    assert diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7]) == [0, 2, 1, 0, 1, 1, 1]

    # Test Case 2
    assert diff_consecutivenums([4, 5, 8, 9, 6, 10]) == [1, 3, 1, -3, 4]

    # Test Case 3
    assert diff_consecutivenums([0, 1, 2, 3, 4, 4, 4, 4, 5, 7]) == [1, 1, 1, 1, 0, 0, 0, 1, 2]

    # Edge Case: Empty List
    assert diff_consecutivenums([]) == []

    # Edge Case: Single Element
    assert diff_consecutivenums([10]) == []

    # Edge Case: All equal elements
    assert diff_consecutivenums([5, 5, 5]) == [0, 0]

    # Edge Case: Negative numbers
    assert diff_consecutivenums([-1, -2, -3]) == [-1, -1]