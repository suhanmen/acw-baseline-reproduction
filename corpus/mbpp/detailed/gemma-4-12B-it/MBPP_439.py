from typing import List

def multiple_to_single(numbers: List[int]) -> int:
    """
    Converts a list of integers into a single concatenated integer.

    Example:
    [11, 33, 50] -> 113350
    [-1, 2, 3, 4, 5, 6] -> -123456
    [10, 15, 20, 25] -> 10152025

    Logic:
    - The first number in the list determines the sign of the result.
    - All subsequent numbers are concatenated as strings.
    - If the first number is negative, the minus sign is preserved.
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    # Handle empty list case
    if len(numbers) == 0:
        return 0

    # Handle single element list case
    if len(numbers) == 1:
        return numbers[0]

    # We need to determine the sign of the result based on the first number.
    # If the first number is negative, the resulting concatenated string 
    # should start with a '-'.
    first_element = numbers[0]
    is_negative = first_element < 0

    # We use a list of strings to build the concatenation.
    # This is more efficient than repeated string concatenation.
    parts: List[str] = []

    # Process the first number. 
    # We take the absolute value to avoid double minus signs if 
    # there are multiple negative numbers in the list.
    # The problem's examples suggest that the negative sign applies 
    # to the total result based on the first element's sign.
    first_val_abs = abs(first_element)
    parts.append(str(first_val_abs))

    # Process the remaining numbers.
    # We treat every subsequent number as an absolute value for concatenation,
    # as the sign is governed by the first element.
    for i in range(1, len(numbers)):
        current_num = numbers[i]
        parts.append(str(abs(current_num)))

    # Join all parts into a single string.
    concatenated_str = "".join(parts)

    # Convert the concatenated string to an integer.
    result_value = int(concatenated_str)

    # Apply the negative sign if the first element was negative.
    if is_negative:
        # Ensure we don't return -0
        if result_value == 0:
            return 0
        return -result_value
    else:
        return result_value

# Verification based on provided assertions
if __name__ == "__main__":
    # Test case 1
    assert multiple_to_single([11, 33, 50]) == 113350
    # Test case 2
    assert multiple_to_single([-1, 2, 3, 4, 5, 6]) == -123456
    # Test case 3
    assert multiple_to_single([10, 15, 20, 25]) == 10152025