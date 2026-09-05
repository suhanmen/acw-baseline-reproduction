from typing import List
from statistics import mean


def _validate_input_list(numbers: List[float]) -> None:
    """
    Validates that the input list is not empty.

    Raises:
        ValueError: If the list is empty, as the mean and deviation cannot be calculated.
    """
    if not numbers:
        raise ValueError("Cannot calculate Mean Absolute Deviation for an empty list.")


def _calculate_mean(numbers: List[float]) -> float:
    """
    Calculates the arithmetic mean of the provided list of numbers.

    Args:
        numbers: A list of float values.

    Returns:
        The arithmetic mean of the numbers.
    """
    total_sum = sum(numbers)
    count = len(numbers)

    # This check is technically redundant if validate_input_list is always called,
    # but serves as a defensive safeguard within the helper logic itself.
    if count == 0:
        raise RuntimeError("List length is zero; mean cannot be computed.")

    return total_sum / count


def _calculate_absolute_deviations(numbers: List[float], dataset_mean: float) -> List[float]:
    """
    Calculates the list of absolute deviations for each number from the dataset mean.

    Formula for each element x_i: | x_i - dataset_mean |

    Args:
        numbers: The original list of numbers.
        dataset_mean: The pre-calculated mean of the dataset.

    Returns:
        A list of non-negative floats representing the absolute difference for each element.
    """
    deviations = []
    for value in numbers:
        absolute_difference = abs(value - dataset_mean)
        deviations.append(absolute_difference)
    return deviations


def _calculate_mean_of_deviations(deviations: List[float]) -> float:
    """
    Calculates the mean of the absolute deviations.

    This is the final step to arrive at the Mean Absolute Deviation (MAD).

    Args:
        deviations: A list of absolute deviations calculated previously.

    Returns:
        The average of the deviations.
    """
    if not deviations:
        raise RuntimeError("Deviations list is empty; mean cannot be computed.")

    return sum(deviations) / len(deviations)


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Step 1: Validate the input data immediately
    _validate_input_list(numbers)

    # Step 2: Calculate the arithmetic mean of the dataset
    # We use a helper to ensure this logic is isolated and clear.
    dataset_mean = _calculate_mean(numbers)

    # Step 3: Calculate the absolute deviation for every number in the list
    # Store these in a named variable for clarity.
    absolute_deviation_list = _calculate_absolute_deviations(numbers, dataset_mean)

    # Step 4: Calculate the mean of these absolute deviations
    # This yields the final MAD value.
    result = _calculate_mean_of_deviations(absolute_deviation_list)

    return result