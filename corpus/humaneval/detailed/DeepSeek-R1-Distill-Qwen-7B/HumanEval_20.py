from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Validate input
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of floats.")
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")
    if not all(isinstance(num, float) for num in numbers):
        raise ValueError("All elements in the list must be floats.")

    # Handle case where all elements are the same
    if all(num == numbers[0] for num in numbers):
        return (numbers[0], numbers[0])

    # Find the closest pair
    closest = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            current_diff = abs(numbers[j] - numbers[i])
            if current_diff < min_diff:
                min_diff = current_diff
                closest = (numbers[i], numbers[j])

    # Ensure the tuple is in the order (smaller, larger)
    if closest[0] > closest[1]:
        closest = (closest[1], closest[0])

    return closest