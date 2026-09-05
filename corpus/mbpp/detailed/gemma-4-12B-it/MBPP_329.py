from typing import List, Any

def neg_count(numbers: List[Any]) -> int:
    """
    Counts the number of negative integers or floats in a provided list.

    Args:
        numbers (List[Any]): A list containing elements to be checked.

    Returns:
        int: The count of negative numbers.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
    """
    # Step 1: Validate that the input is indeed a list.
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}.")

    # Step 2: Handle the empty list edge case.
    if len(numbers) == 0:
        return 0

    negative_count: int = 0

    # Step 3: Iterate through each element in the list.
    for item in numbers:
        # Step 4: Validate that the item is a number (int or float).
        # We check for bool specifically because bools are subclasses of int in Python.
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(
                f"List contains a non-numeric element: {item} (type: {type(item).__name__})."
            )

        # Step 5: Check if the number is negative.
        is_negative: bool = item < 0

        # Step 6: Update the counter if the condition is met.
        if is_negative:
            negative_count += 1

    # Step 7: Return the final accumulated count.
    return negative_count

# Assertions to verify the functionality
if __name__ == "__main__":
    # Test Case 1: Standard mixed list
    assert neg_count([-1, -2, 3, -4, -5]) == 4

    # Test Case 2: No negative numbers
    assert neg_count([1, 2, 3]) == 0

    # Test Case 3: Mixed numbers with zero and positives
    assert neg_count([1, 2, -3, -10, 20]) == 2

    # Edge Case: Empty list
    assert neg_count([]) == 0

    # Edge Case: Single negative number
    assert neg_count([-5]) == 1

    # Edge Case: Single positive number
    assert neg_count([5]) == 0

    # Edge Case: All zeros (Zero is not negative)
    assert neg_count([0, 0, 0]) == 0

    # Edge Case: Float values
    assert neg_count([-1.5, 2.0, -0.001]) == 2

    print("All tests passed successfully.")