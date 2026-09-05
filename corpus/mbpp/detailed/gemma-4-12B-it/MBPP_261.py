from typing import Tuple

def division_elements(numerator_tuple: Tuple[int, ...], denominator_tuple: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    Performs element-wise integer division on two tuples of numbers.

    Args:
        numerator_tuple: A tuple of integers to be divided.
        denominator_tuple: A tuple of integers to divide by.

    Returns:
        A tuple containing the results of the element-wise division.

    Raises:
        ValueError: If the tuples are of different lengths or are empty.
        ZeroDivisionError: If any element in the denominator_tuple is zero.
        TypeError: If inputs are not tuples or contain non-numeric types.
    """

    # 1. Input Validation: Type checking
    if not isinstance(numerator_tuple, tuple):
        raise TypeError(f"Expected numerator_tuple to be a tuple, got {type(numerator_tuple).__name__}")
    if not isinstance(denominator_tuple, tuple):
        raise TypeError(f"Expected denominator_tuple to be a tuple, got {type(denominator_tuple).__name__}")

    # 2. Input Validation: Length matching
    len_num = len(numerator_tuple)
    len_den = len(denominator_tuple)

    if len_num != len_den:
        raise ValueError(f"Tuples must have the same length. Numerator: {len_num}, Denominator: {len_den}")

    # 3. Input Validation: Empty check
    if len_num == 0:
        return ()

    # 4. Processing
    results_list = []

    for index in range(len_num):
        num_val = numerator_tuple[index]
        den_val = denominator_tuple[index]

        # Validate internal types
        if not isinstance(num_val, (int, float)) or not isinstance(den_val, (int, float)):
            raise TypeError(f"All elements in tuples must be numeric. Found {type(num_val)} and {type(den_val)} at index {index}")

        # Handle zero division explicitly
        if den_val == 0:
            raise ZeroDivisionError(f"Division by zero encountered at index {index} in denominator_tuple.")

        # Perform calculation
        # Using floor division (//) as the expected outputs are integers
        result = int(num_val // den_val)

        # Append result to our intermediate storage
        results_list.append(result)

    # 5. Final conversion
    final_result = tuple(results_list)
    return final_result

if __name__ == "__main__":
    # Verification based on provided assertions
    assert division_elements((10, 4, 6, 9), (5, 2, 3, 3)) == (2, 2, 2, 3)
    assert division_elements((12, 6, 8, 16), (6, 3, 4, 4)) == (2, 2, 2, 4)
    assert division_elements((20, 14, 36, 18), (5, 7, 6, 9)) == (4, 2, 6, 2)