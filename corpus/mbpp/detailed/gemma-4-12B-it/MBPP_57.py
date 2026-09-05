from typing import List


def find_Max_Num(digits: List[int], length: int) -> int:
    """
    Finds the largest number that can be formed using a given set of digits.

    Args:
        digits: A list of integers representing available digits.
        length: The number of digits to use to form the final number.

    Returns:
        int: The largest number formed by the specified number of digits.

    Raises:
        ValueError: If input validation fails.
    """
    # --- Input Validation ---

    # Check if the input list is empty
    if not digits:
        raise ValueError("The input list of digits cannot be empty.")

    # Ensure digits are non-negative integers (standard for digit-based problems)
    for d in digits:
        if not isinstance(d, int) or d < 0:
            raise ValueError(f"Invalid digit detected: {d}. All digits must be non-negative integers.")

    # Validate the length parameter
    if not isinstance(length, int) or length < 0:
        raise ValueError("The length parameter must be a non-negative integer.")

    # Check if the requested length is greater than the number of available digits
    if length > len(digits):
        raise ValueError(f"Requested length {length} exceeds the number of available digits ({len(digits)}).")

    # Handle the degenerate case where length is 0
    if length == 0:
        return 0

    # --- Core Logic ---

    # Step 1: Sort the digits in descending order.
    # To form the largest number, the largest digits must occupy the highest place values.
    # For example, given [1, 2, 9, 3], sorting yields [9, 3, 2, 1].
    sorted_digits = sorted(digits, reverse=True)

    # Step 2: Select the first 'length' digits from the sorted list.
    # Since the list is sorted descending, these are guaranteed to be the largest available.
    top_digits = sorted_digits[:length]

    # Step 3: Construct the number from these digits.
    # We iterate through the selected digits, multiplying the current total by 10 
    # to shift the place value and adding the new digit.
    # Example: digits [9, 3, 2], length 3
    # Initial: result = 0
    # Iteration 1: result = (0 * 10) + 9 = 9
    # Iteration 2: result = (9 * 10) + 3 = 93
    # Iteration 3: result = (93 * 10) + 2 = 932

    max_number = 0
    for digit in top_digits:
        max_number = (max_number * 10) + digit

    return max_number

# Assertions to verify the solution
if __name__ == "__main__":
    assert find_Max_Num([1, 2, 3], 3) == 321
    assert find_Max_Num([4, 5, 6, 1], 4) == 6541
    assert find_Max_Num([1, 2, 3, 9], 4) == 9321