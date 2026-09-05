from typing import Union

def median_numbers(num1: Union[int, float], num2: Union[int, float], num3: Union[int, float]) -> float:
    """
    Finds the median of three numbers.

    The median of three numbers is the value that falls in the middle 
    when the numbers are sorted in ascending order.

    Args:
        num1: The first number.
        num2: The second number.
        num3: The third number.

    Returns:
        The median of the three numbers as a float.

    Raises:
        TypeError: If any of the inputs are not integers or floats.
    """
    # Validate input types explicitly
    inputs = [num1, num2, num3]
    for val in inputs:
        if not isinstance(val, (int, float)):
            raise TypeError(f"Input must be a number, but received {type(val).__name__}")

    # Create a list to store the numbers
    numbers_list = [num1, num2, num3]

    # Sort the list to find the middle element
    # Sorting ensures that even if numbers are negative or all equal,
    # the middle position remains the median.
    sorted_numbers = sorted(numbers_list)

    # The median of 3 elements is always at index 1 of the sorted list
    # because the list will have exactly 3 elements.
    median_value = sorted_numbers[1]

    # Ensure the return type is explicitly a float as required by the assertions
    return float(median_value)

if __name__ == "__main__":
    # Verification of the provided test cases
    assert median_numbers(25, 55, 65) == 55.0
    assert median_numbers(20, 10, 30) == 20.0
    assert median_numbers(15, 45, 75) == 45.0