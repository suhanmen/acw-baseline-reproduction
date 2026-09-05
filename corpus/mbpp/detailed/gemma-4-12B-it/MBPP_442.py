from typing import List


def positive_count(numbers: List[int]) -> float:
    """
    Calculates the ratio of positive integers (greater than zero) 
    to the total number of elements in a given list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        float: The ratio of positive numbers to the total count.

    Raises:
        TypeError: If the input is not a list or contains non-integers.
        ValueError: If the input list is empty.
    """
    # Step 1: Validate that the input is actually a list.
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}.")

    # Step 2: Handle the degenerate case of an empty list.
    # A ratio cannot be calculated for an empty set (division by zero).
    total_count = len(numbers)
    if total_count == 0:
        raise ValueError("The input list cannot be empty.")

    # Step 3: Validate that all elements in the list are integers.
    # This ensures the function behaves predictably with mixed types.
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # Step 4: Count the number of elements strictly greater than zero.
    # We use a clear, iterative approach to ensure readability.
    positive_elements_count = 0
    for num in numbers:
        if num > 0:
            positive_elements_count += 1

    # Step 5: Calculate the ratio.
    # Using floating point division to ensure precision.
    # The result is the count of positive numbers divided by the total size.
    ratio = float(positive_elements_count) / float(total_count)

    # Step 6: Round the result to match the expected precision in the assertions.
    # The provided assertions (e.g., 0.54, 0.69, 0.56) suggest 2 decimal places.
    # We use round() to ensure the floating point arithmetic doesn't cause mismatch.
    rounded_ratio = round(ratio, 2)

    return rounded_ratio

# Verification against provided test cases
if __name__ == "__main__":
    # These assertions confirm the correctness of the logic.
    assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]) == 0.69
    assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 0.56