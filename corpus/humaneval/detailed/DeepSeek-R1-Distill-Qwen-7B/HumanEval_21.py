from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Edge Cases:
        - If list has fewer than two elements, raise ValueError
        - If all elements are equal, return list of zeros
        - Handle negative values and zero range appropriately

    Args:
        numbers: List of floats. Must have at least two elements.

    Returns:
        A new list where each element is rescaled to the [0,1] range.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_val = min(numbers)
    max_val = max(numbers)

    # If all elements are the same, return list of zeros
    if min_val == max_val:
        return [0.0 for _ in numbers]

    # Calculate the range of the input values
    range_val = max_val - min_val

    # Rescale each value to [0, 1]
    scaled_numbers = []
    for num in numbers:
        scaled = (num - min_val) / range_val
        scaled_numbers.append(scaled)

    return scaled_numbers

# Example usage:
if __name__ == "__main__":
    test_input = [1.0, 2.0, 3.0, 4.0, 5.0]
    print("Original:", test_input)
    print("Rescaled:", rescale_to_unit(test_input))