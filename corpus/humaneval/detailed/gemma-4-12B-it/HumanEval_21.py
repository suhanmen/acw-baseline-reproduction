from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # --- Input Validation ---
    # Check if the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected list of floats, got {type(numbers).__name__}")

    # Check if the list contains at least two elements as per docstring requirements
    list_length = len(numbers)
    if list_length < 2:
        raise ValueError("Input list must contain at least two elements.")

    # Verify all elements are numbers (int or float)
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numbers. Found: {type(item).__name__}")

    # --- Calculation Logic ---
    # Identify the boundaries of the current range
    min_value = float(min(numbers))
    max_value = float(max(numbers))

    # Calculate the range (delta)
    range_delta = max_value - min_value

    # Handle the degenerate case where all numbers in the list are identical.
    # In this case, the range is 0. Since we cannot divide by zero, 
    # and the goal is to map the smallest to 0 and largest to 1, 
    # and they are the same number, a standard convention is to return 
    # a list of zeros (or any uniform value), but since the problem implies 
    # a linear transformation where the span is 1, we must decide on a behavior.
    # Given "smallest becomes 0 and largest becomes 1", if they are equal, 
    # the transformation is mathematically undefined. 
    # We will return a list of 0.0s to maintain the "smallest becomes 0" rule.
    if range_delta == 0.0:
        return [0.0 for _ in numbers]

    # --- Transformation ---
    # Apply the linear transformation: f(x) = (x - min) / (max - min)
    rescaled_list = []
    for val in numbers:
        # Convert to float to ensure precision
        current_val = float(val)

        # Step 1: Shift the value so the minimum becomes 0
        shifted_value = current_val - min_value

        # Step 2: Scale the value so the maximum becomes 1
        normalized_value = shifted_value / range_delta

        rescaled_list.append(normalized_value)

    return rescaled_list