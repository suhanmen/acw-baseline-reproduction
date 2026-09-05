from typing import List, Union

def frequency_Of_Smallest(num_elements: int, numbers: List[Union[int, float]]) -> int:
    """
    Calculates the frequency of the smallest value in a provided list of numbers.

    Args:
        num_elements (int): The expected number of elements in the list.
        numbers (List[Union[int, float]]): A list of numeric values.

    Returns:
        int: The count of occurrences of the smallest numeric value.

    Raises:
        ValueError: If the input list is empty, the size doesn't match num_elements,
                    or if the list contains non-numeric types.
        TypeError: If inputs are of incorrect types.
    """
    # --- Input Validation ---

    # Check if 'numbers' is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list for 'numbers', but got {type(numbers).__name__}")

    # Check if 'num_elements' is an integer
    if not isinstance(num_elements, int):
        raise TypeError(f"Expected an integer for 'num_elements', but got {type(num_elements).__name__}")

    # Check if the length of the list matches the provided count
    actual_length = len(numbers)
    if actual_length != num_elements:
        raise ValueError(
            f"Input list length ({actual_length}) does not match "
            f"provided num_elements ({num_elements})."
        )

    # Handle the empty list case explicitly
    if actual_length == 0:
        return 0

    # Validate that all elements are numeric (int or float)
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise ValueError(f"List contains non-numeric element: {item} (Type: {type(item).__name__})")

    # --- Core Logic ---

    # Step 1: Identify the smallest value in the list.
    # We use a standard approach to find the minimum to keep logic explicit.
    current_minimum = numbers[0]
    for i in range(1, actual_length):
        current_element = numbers[i]
        if current_element < current_minimum:
            current_minimum = current_element

    # Step 2: Count the occurrences of that minimum value.
    frequency_count = 0
    for item in numbers:
        if item == current_minimum:
            frequency_count += 1

    return frequency_count

# The following logic ensures the function meets the requirements specified in the prompt.
if __name__ == "__main__":
    # These are the assertions provided in the problem description.
    assert frequency_Of_Smallest(5, [1, 2, 3, 4, 3]) == 1
    assert frequency_Of_Smallest(7, [3, 1, 2, 5, 6, 2, 3]) == 1
    assert frequency_Of_Smallest(7, [3, 3, 6, 3, 7, 4, 9]) == 3