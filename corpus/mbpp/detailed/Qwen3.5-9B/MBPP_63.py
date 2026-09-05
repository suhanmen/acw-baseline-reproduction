from typing import List, Tuple, Union

Number = Union[int, float]
Pair = Tuple[Number, Number]

def validate_pair(pair: Tuple[any, any], index: int) -> Pair:
    """
    Validates that a single item in the list is a valid pair of numbers.

    Checks:
    1. The item is a tuple or list of length 2.
    2. Both elements are numeric types (int or float).

    Raises:
    TypeError: If the structure or types are invalid.
    ValueError: If the length is not exactly 2.
    """
    if not isinstance(pair, (tuple, list)):
        raise TypeError(f"Item at index {index} is not a sequence (expected tuple or list).")

    if len(pair) != 2:
        raise ValueError(f"Item at index {index} does not have exactly 2 elements (got {len(pair)}).")

    first_element, second_element = pair[0], pair[1]

    if not isinstance(first_element, (int, float)) or isinstance(first_element, bool):
        raise TypeError(f"First element of pair at index {index} is not a number.")
    if not isinstance(second_element, (int, float)) or isinstance(second_element, bool):
        raise TypeError(f"Second element of pair at index {index} is not a number.")

    return pair

def calculate_difference(pair: Pair) -> float:
    """
    Calculates the absolute difference between the two numbers in a pair.

    Returns the absolute value to handle cases where the first number is larger
    than the second, regardless of the problem's implied ordering.
    """
    return abs(pair[0] - pair[1])

def find_maximum_difference(pairs: List[Pair]) -> float:
    """
    Finds the maximum difference between available pairs in the given tuple list.

    The function validates all inputs, calculates the difference for each valid pair,
    and returns the largest difference found.

    Args:
        pairs: A list of tuples or lists containing two numeric elements each.

    Returns:
        The maximum absolute difference found among all pairs.

    Raises:
        TypeError: If the input is not a list or if elements are invalid.
        ValueError: If the input list is empty.
    """
    # Input Validation for the list itself
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list of pairs.")

    # Edge Case: Empty Input
    if len(pairs) == 0:
        raise ValueError("Input list cannot be empty.")

    # Validation for each element and calculation preparation
    differences: List[float] = []

    for i, current_item in enumerate(pairs):
        validated_pair = validate_pair(current_item, i)
        diff = calculate_difference(validated_pair)
        differences.append(diff)

    # Find the maximum difference using explicit iteration for clarity
    # We initialize max_diff with the first element of our differences list
    # This handles negative numbers correctly as we are comparing absolute differences
    max_diff: float = differences[0]

    for diff in differences:
        if diff > max_diff:
            max_diff = diff

    return max_diff

# Verification against provided assertions (for internal logic check, not output)
if __name__ == "__main__":
    # Test Case 1
    result1 = find_maximum_difference([(3, 5), (1, 7), (10, 3), (1, 2)])
    # Differences: |3-5|=2, |1-7|=6, |10-3|=7, |1-2|=1. Max is 7.
    assert result1 == 7, f"Test 1 failed: expected 7, got {result1}"

    # Test Case 2
    result2 = find_maximum_difference([(4, 6), (2, 17), (9, 13), (11, 12)])
    # Differences: |4-6|=2, |2-17|=15, |9-13|=4, |11-12|=1. Max is 15.
    assert result2 == 15, f"Test 2 failed: expected 15, got {result2}"

    # Test Case 3
    result3 = find_maximum_difference([(12, 35), (21, 27), (13, 23), (41, 22)])
    # Differences: |12-35|=23, |21-27|=6, |13-23|=10, |41-22|=19. Max is 23.
    assert result3 == 23, f"Test 3 failed: expected 23, got {result3}"

    print("All internal assertions passed.")