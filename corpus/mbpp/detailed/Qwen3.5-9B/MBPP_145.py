from typing import List, Union, Tuple, Optional

Number = Union[int, float]

def validate_numeric_input(
    data: Tuple[Number, ...],
    n: int
) -> List[Number]:
    """
    Validates that the input data contains exactly 'n' numeric elements.
    Returns a list of the validated numbers.

    Raises:
        ValueError: If the length of data does not match n.
        TypeError: If any element in data is not a number (int or float).
    """
    if not isinstance(data, tuple):
        raise TypeError(f"Expected input data to be a tuple, but received {type(data).__name__}.")

    if not isinstance(n, int):
        raise TypeError(f"Expected second argument n to be an integer, but received {type(n).__name__}.")

    if n < 0:
        raise ValueError(f"The count parameter 'n' must be non-negative, but received {n}.")

    if n == 0:
        if len(data) != 0:
            raise ValueError(f"The data tuple must be empty when n is 0, but contained {len(data)} elements.")
        return []

    if len(data) != n:
        raise ValueError(
            f"The length of the data tuple ({len(data)}) does not match the provided count parameter n ({n})."
        )

    validated_list = []
    for index, element in enumerate(data):
        if not isinstance(element, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number. Received type: {type(element).__name__} with value: {element}"
            )

        # Explicitly handle booleans if they are passed as ints/floats but logically incorrect
        if isinstance(element, bool):
            raise TypeError(
                f"Element at index {index} is a boolean, which is not a valid numeric type for this calculation."
            )

        validated_list.append(element)

    return validated_list


def find_min_value(numbers: List[Number]) -> Optional[Number]:
    """
    Finds the minimum value in a list of numbers.

    Args:
        numbers: A list of numeric values.

    Returns:
        The minimum number found, or None if the list is empty.
    """
    if len(numbers) == 0:
        return None

    current_minimum = numbers[0]

    for i in range(1, len(numbers)):
        current_value = numbers[i]
        if current_value < current_minimum:
            current_minimum = current_value

    return current_minimum


def find_max_value(numbers: List[Number]) -> Optional[Number]:
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers: A list of numeric values.

    Returns:
        The maximum number found, or None if the list is empty.
    """
    if len(numbers) == 0:
        return None

    current_maximum = numbers[0]

    for i in range(1, len(numbers)):
        current_value = numbers[i]
        if current_value > current_maximum:
            current_maximum = current_value

    return current_maximum


def calculate_difference(min_val: Number, max_val: Number) -> float:
    """
    Calculates the absolute difference between the maximum and minimum values.

    Args:
        min_val: The minimum value.
        max_val: The maximum value.

    Returns:
        The absolute difference (max - min).
    """
    return max_val - min_val


def max_Abs_Diff(data: Tuple, n: int) -> float:
    """
    Finds the maximum difference between any two elements in a given array.
    This is equivalent to finding the difference between the maximum and minimum elements.

    The function validates the input to ensure:
    1. Data is a tuple.
    2. The second argument n is an integer.
    3. The length of the tuple matches n.
    4. All elements are numeric (int or float), excluding booleans.

    Parameters:
        data: A tuple of numbers.
        n: The expected number of elements in the tuple.

    Returns:
        The maximum absolute difference between any two elements (max - min).

    Raises:
        TypeError: If input types are incorrect.
        ValueError: If input counts are inconsistent or n is negative.
    """

    # Step 1: Validate and sanitize the input
    validated_numbers = validate_numeric_input(data, n)

    # Step 2: Check for empty array case
    if len(validated_numbers) == 0:
        raise ValueError("Cannot calculate maximum difference for an empty array.")

    # Step 3: Handle single element case
    if len(validated_numbers) == 1:
        # The difference between a number and itself is 0
        return 0.0

    # Step 4: Find the minimum value explicitly
    minimum_value = find_min_value(validated_numbers)

    # Step 5: Find the maximum value explicitly
    maximum_value = find_max_value(validated_numbers)

    # Step 6: Calculate and return the difference
    # Since we found the global max and global min, their difference is the max difference
    result_difference = calculate_difference(minimum_value, maximum_value)

    return result_difference