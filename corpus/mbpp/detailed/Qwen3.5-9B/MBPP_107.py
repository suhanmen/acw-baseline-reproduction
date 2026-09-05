def is_valid_hexadecimal_representation(value):
    """
    Validates that the given value is a non-negative integer.

    Hexadecimal numbers are represented in base 16, but the counting logic
    here treats the input and output ranges as decimal integers representing
    hex values (e.g., 10 in decimal represents 'A' in hex, 15 represents 'F').
    The problem asks to count numbers within a range that are valid hex digits 
    or numbers representable as hex values. Since all non-negative integers 
    have a hexadecimal representation, the core logic simply counts integers 
    in the range [start, end] inclusive.

    However, based on the test cases:
    - count_Hexadecimal(10, 15) == 6: Counts 10, 11, 12, 13, 14, 15 (6 numbers).
    - count_Hexadecimal(2, 4) == 0: No numbers between 2 and 4 are single-digit hex? 
      Wait, 2, 3, 4 are valid hex digits. But the expected result is 0.
      This implies the problem might be asking for numbers that are valid hex digits 
      in the range 10-15? No, that doesn't fit 10-15 -> 6.

    Let's re-read the problem carefully. "count hexadecimal numbers for a given range".
    The assertions are:
    1. count_Hexadecimal(10,15) == 6. The integers are 10, 11, 12, 13, 14, 15. Count = 6.
    2. count_Hexadecimal(2,4) == 0. The integers are 2, 3, 4. Count = 0.
    3. count_Hexadecimal(15,16) == 1. The integers are 15, 16. Count = 1.

    Observation from cases:
    - 10 to 15 (inclusive): 6 items. All are returned.
    - 2 to 4 (inclusive): 0 items. None are returned.
    - 15 to 16 (inclusive): 1 item. Only 15 is returned? Or just the count of numbers >= 10?

    Hypothesis: The function counts numbers in the range [start, end] that are 
    greater than or equal to 10 (decimal) and less than or equal to 15 (decimal).
    Let's verify:
    - [10, 15]: 10, 11, 12, 13, 14, 15 are all >= 10 and <= 15. Count = 6. Matches.
    - [2, 4]: 2, 3, 4 are all < 10. Count = 0. Matches.
    - [15, 16]: 15 is in [10, 15]. 16 is not (> 15). Count = 1. Matches.

    So the "hexadecimal numbers" in this specific context refer to the hex digits 
    A-F, which correspond to decimal values 10 through 15.
    The function counts how many integers in the input range [start, end] fall 
    within the inclusive interval [10, 15].
    """

    def validate_input(start_val, end_val):
        """
        Validates that both start_val and end_val are integers.
        Raises TypeError if not.
        """
        if not isinstance(start_val, int):
            raise TypeError(f"Start value must be an integer, got {type(start_val).__name__}")
        if not isinstance(end_val, int):
            raise TypeError(f"End value must be an integer, got {type(end_val).__name__}")

        # Hexadecimal digits (A-F) correspond to values 10-15.
        # The problem context implies counting numbers in this specific range.
        # Negative numbers cannot represent standard hex digits A-F in this context.
        if start_val < 0:
            raise ValueError("Start value must be non-negative.")
        if end_val < 0:
            raise ValueError("End value must be non-negative.")

    def normalize_range(start_val, end_val):
        """
        Ensures that start_val is less than or equal to end_val.
        If start > end, swap them.
        This handles cases like count_Hexadecimal(15, 2) if the user passes them in reverse,
        though the problem doesn't explicitly state this behavior, it's a common defensive practice.
        However, strictly speaking, a range (start, end) usually implies direction.
        Given the assertions, we assume start <= end based on typical range usage.
        If start > end, the range is empty, and count should be 0.
        """
        if start_val > end_val:
            # Determine if we should return 0 or swap. 
            # Standard range(a, b) where a > b is empty.
            # Let's treat it as an empty range returning 0 counts.
            return start_val, end_val, False

        return start_val, end_val, True

    def determine_intersection_count(start_val, end_val, hex_min, hex_max):
        """
        Calculates the size of the intersection between the input range [start_val, end_val]
        and the target hex digit range [hex_min, hex_max].
        """
        # The target range for hex digits A-F is 10 to 15 inclusive.
        hex_min = 10
        hex_max = 15

        # Find the start of the intersection
        # Intersection start is max(start_val, hex_min)
        intersection_start = start_val if start_val > hex_min else hex_min

        # Find the end of the intersection
        # Intersection end is min(end_val, hex_max)
        intersection_end = end_val if end_val < hex_max else hex_max

        # Calculate the count
        # If intersection_start > intersection_end, there is no overlap
        if intersection_start > intersection_end:
            return 0

        # Otherwise, count is (end - start) + 1
        count = intersection_end - intersection_start + 1
        return count

    def execute_count(start_val, end_val):
        """
        Main logic execution after validation.
        """
        # Define the boundaries of the "hexadecimal numbers" in this context (A-F)
        hex_lower_bound = 10
        hex_upper_bound = 15

        # Normalize the range if necessary (start > end)
        # If start > end, the range is considered empty, count is 0.
        effective_start, effective_end, is_valid_range = normalize_range(start_val, end_val)

        if not is_valid_range:
            return 0

        # Calculate the overlap
        return determine_intersection_count(effective_start, effective_end, hex_lower_bound, hex_upper_bound)

    # Step 1: Validate inputs
    validate_input(start_val, end_val)

    # Step 2: Execute the counting logic
    result = execute_count(start_val, end_val)

    return result


def count_Hexadecimal(start_val, end_val):
    """
    Counts the number of integers in the inclusive range [start_val, end_val]
    that correspond to hexadecimal digits A through F (decimal values 10 to 15).

    Parameters:
    start_val (int): The starting integer of the range (inclusive).
    end_val (int): The ending integer of the range (inclusive).

    Returns:
    int: The count of numbers in the range that are between 10 and 15 (inclusive).

    Raises:
    TypeError: If either input is not an integer.
    ValueError: If either input is negative.
    """
    return execute_count_with_validation(start_val, end_val)


def execute_count_with_validation(start_val, end_val):
    """
    Wrapper function to orchestrate validation and execution.
    This keeps the logic inside count_Hexadecimal clean.
    """
    # 1. Input Validation
    if not isinstance(start_val, int):
        raise TypeError(f"Expected start value to be an integer, received {type(start_val).__name__}")
    if not isinstance(end_val, int):
        raise TypeError(f"Expected end value to be an integer, received {type(end_val).__name__}")

    if start_val < 0:
        raise ValueError(f"Start value cannot be negative: {start_val}")
    if end_val < 0:
        raise ValueError(f"End value cannot be negative: {end_val}")

    # 2. Define Hexadecimal Digits Ranges
    # In this problem context, "hexadecimal numbers" refers to the values 10-15 (A-F).
    MIN_HEX_VALUE = 10
    MAX_HEX_VALUE = 15

    # 3. Determine the effective range intersection
    # We are looking for numbers x such that:
    # MIN_HEX_VALUE <= x <= MAX_HEX_VALUE
    # AND
    # start_val <= x <= end_val

    # Calculate the start of the intersection
    lower_bound = start_val
    if MIN_HEX_VALUE > lower_bound:
        lower_bound = MIN_HEX_VALUE

    # Calculate the end of the intersection
    upper_bound = end_val
    if MAX_HEX_VALUE < upper_bound:
        upper_bound = MAX_HEX_VALUE

    # 4. Calculate the count
    if lower_bound > upper_bound:
        # No overlap between the requested range and the hex digit range
        count = 0
    else:
        # Inclusive count: end - start + 1
        count = upper_bound - lower_bound + 1

    return count