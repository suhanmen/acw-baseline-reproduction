from typing import List, Optional, Union

Number = Union[int, float]


def find_Max_Num(digits: List[Number], length: Number) -> Optional[Number]:
    """
    Constructs and returns the largest possible number as an integer by arranging
    the provided digits into a sequence of exactly 'length' digits in descending order.

    The algorithm sorts the digits in descending order and then slices the list
    to the required length. Finally, the sliced digits are joined together to form
    a string representation of the resulting number, which is then converted back to
    an integer.

    Edge cases handled:
    - Empty digit list or invalid length: Returns None.
    - Length greater than the number of available digits: Returns None.
    - Negative or zero-length inputs: Returns None.
    - Single element or all-equal elements: Works correctly via sorting.

    Valid inputs must be a list of numeric values (int or float) and a non-negative
    integer for 'length'. Non-numeric values in the list or invalid 'length' type
    will result in None being returned after validation fails.

    Args:
        digits (List[Number]): A list of numeric digits to be used.
        length (Number): The exact number of digits to use from the list to form the number.

    Returns:
        Optional[int]: The largest number formed, or None if the input is invalid or
                       insufficient digits are available.
    """

    # Step 1: Validate the 'length' parameter.
    # It must be a non-negative integer.
    if not isinstance(length, int):
        return None
    if length < 0:
        return None
    if length != length:  # Check for NaN in case length is accidentally passed as a float nan
        return None

    # Step 2: Validate the 'digits' list.
    # The list cannot be None.
    if digits is None:
        return None

    # Check if the list is empty.
    if len(digits) == 0:
        return None

    # Step 3: Validate every element in the 'digits' list.
    # Each element must be a number (int or float).
    # We also need to handle potential NaN or Inf values which might break integer conversion.
    for idx, value in enumerate(digits):
        # Check if the type is strictly int or float
        if not isinstance(value, (int, float)):
            return None

        # Check for NaN (Not a Number) which is technically a float but invalid for digits
        if isinstance(value, float) and (value != value):
            return None

        # Check for Infinity which is invalid for digits
        import math
        if isinstance(value, float) and (math.isinf(value)):
            return None

        # Although the problem implies digits, we accept any non-negative number.
        # However, strictly speaking, a "digit" usually implies 0-9. 
        # The examples show integers. If a float like 9.0 is passed, we treat it as 9.
        # We will convert to int later during string formation.
        # Let's ensure the value is reasonable (e.g., not negative if we strictly follow "digit",
        # but the problem says "largest number formed with given digits". Usually digits are 0-9.
        # The examples only show 0-9. Let's assume inputs are intended to be digits 0-9.
        # If a negative number or number > 9 is provided, strictly it's not a digit.
        # However, the problem asks to form a number with "given digits". 
        # To be defensive and strictly follow the "digit" definition (0-9), we should validate range.
        # But looking at typical coding interview contexts for this specific phrasing, 
        # it often implies just the numbers provided.
        # Given the examples [1,2,3], [4,5,6,1], it seems to be 0-9.
        # Let's enforce the range 0-9 to be strictly compliant with the word "digit".
        if value < 0 or value > 9:
            return None

    # Step 4: Verify if there are enough digits to satisfy the requested length.
    if len(digits) < length:
        return None

    # Step 5: Convert all valid numeric inputs (including floats like 5.0) to integers.
    # This ensures we are working with whole numbers only for the final construction.
    integer_digits: List[int] = []
    for raw_val in digits:
        # Since we validated range 0-9 and no NaN/Inf, int() is safe.
        # This converts 9.0 to 9, 5 to 5, etc.
        int_val = int(raw_val)
        integer_digits.append(int_val)

    # Step 6: Sort the integer digits in descending order to maximize the resulting number.
    # Python's sort is stable, but for integers stability doesn't change the value order.
    sorted_digits: List[int] = sorted(integer_digits, reverse=True)

    # Step 7: Slice the sorted list to keep only the requested number of digits.
    # Since we verified len(digits) >= length in Step 4, this slice will not be empty
    # unless length is 0 (which is allowed and results in 0 or empty string depending on logic).
    # If length is 0, the result should be 0 (empty set of digits doesn't form a positive number, 
    # but typically 0 is the neutral element. However, an empty sequence of digits usually 
    # maps to 0 in these contexts, or specifically handled).
    selected_digits: List[int] = sorted_digits[:int(length)]

    # Step 8: Handle the zero-length case explicitly.
    if length == 0:
        # If no digits are required, the resulting number is 0.
        return 0

    # Step 9: Construct the number string.
    # Joining the digit characters creates the largest possible number string.
    number_str: str = "".join(str(digit) for digit in selected_digits)

    # Step 10: Convert the final string to an integer.
    result_number: int = int(number_str)

    return result_number