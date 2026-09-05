from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # --- Input Validation ---
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")

    input_length = len(numbers)
    if input_length < 2:
        raise ValueError("Input list must contain at least two elements.")

    # Verify all elements are numbers (int or float)
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numbers. Found: {type(item)}")

    # --- Core Logic ---

    # To find the closest neighbors efficiently, we first sort the numbers.
    # Sorting ensures that the two closest numbers are adjacent in the sorted list.
    sorted_numbers = sorted(numbers)

    # Initialize variables to track the minimum difference and the corresponding pair.
    # We start with the first two elements in the sorted list.
    first_num = sorted_numbers[0]
    second_num = sorted_numbers[1]
    initial_diff = abs(second_num - first_num)

    min_difference = initial_diff
    closest_pair = (first_num, second_num)

    # Iterate through the sorted list and compare adjacent pairs.
    # Using a range allows us to access index i and i+1 safely.
    for i in range(len(sorted_numbers) - 1):
        current_val_a = sorted_numbers[i]
        current_val_b = sorted_numbers[i + 1]

        # Calculate the absolute difference between the current pair.
        current_diff = abs(current_val_b - current_val_a)

        # If we find a difference strictly smaller than the current minimum, 
        # update the minimum and the closest pair.
        # Using '<' ensures that if there are ties, we keep the first occurrence 
        # encountered in the sorted order.
        if current_diff < min_difference:
            min_difference = current_diff
            closest_pair = (current_val_a, current_val_b)

        # Optimization: If the difference is 0.0, we cannot get any closer.
        # We can return immediately.
        if min_difference == 0.0:
            break

    # The problem requires returning the pair in order (smaller, larger).
    # Since the input was sorted, current_val_a <= current_val_b is guaranteed.
    return closest_pair