from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate the Mean Absolute Deviation around the mean.

    Mean Absolute Deviation (MAD) is a measure of the average absolute difference between each 
    element in the dataset and the mean of the dataset. It provides a robust measure of 
    variability compared to the standard deviation.

    The formula for MAD is:
        MAD = (sum of |x_i - x_mean|) / n
        where x_i are the individual values, x_mean is the mean, and n is the number of values.

    Edge Cases:
        - Empty input list: raises ValueError
        - Single element list: returns 0.0
        - All elements are the same: returns 0.0

    Args:
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        float: The Mean Absolute Deviation of the dataset.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("The input list cannot be empty.")

    n = len(numbers)
    if n == 1:
        return 0.0

    mean_value = sum(numbers) / n
    absolute_differences = [abs(x - mean_value) for x in numbers]
    sum_of_differences = sum(absolute_differences)
    mad = sum_of_differences / n

    return mad

# Example usage:
if __name__ == "__main__":
    test_data = [1.0, 2.0, 3.0, 4.0]
    print("Mean Absolute Deviation:", mean_absolute_deviation(test_data))
    # Output: Mean Absolute Deviation: 1.0