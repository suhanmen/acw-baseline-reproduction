from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")

    # Handle the empty list case
    # MAD is undefined for an empty set as we cannot calculate a mean.
    if len(numbers) == 0:
        raise ValueError("Mean Absolute Deviation cannot be calculated for an empty list.")

    # Validate that all elements are numbers (int or float)
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numbers. Found: {type(item).__name__}")

    # Step 1: Calculate the arithmetic mean
    # Convert all items to floats to ensure consistent floating point division
    float_numbers = [float(n) for n in numbers]

    total_sum = 0.0
    for value in float_numbers:
        total_sum += value

    count = len(float_numbers)
    arithmetic_mean = total_sum / count

    # Step 2: Calculate the absolute deviations from the mean
    # Deviations = |x_i - x_mean|
    absolute_deviations = []
    for value in float_numbers:
        deviation = value - arithmetic_mean
        # Ensure we take the absolute value
        if deviation < 0:
            absolute_deviation = -deviation
        else:
            absolute_deviation = deviation
        absolute_deviations.append(absolute_deviation)

    # Step 3: Calculate the mean of these absolute deviations
    # MAD = (1/n) * sum(|x_i - x_mean|)
    total_deviation_sum = 0.0
    for dev in absolute_deviations:
        total_deviation_sum += dev

    mad = total_deviation_sum / count

    return mad