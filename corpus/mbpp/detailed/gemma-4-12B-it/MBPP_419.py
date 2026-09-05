from typing import List, Union

def round_and_sum(numbers: List[Union[int, float]]) -> int:
    """
    Takes a list of numbers, rounds each number to the nearest integer,
    calculates the sum of these rounded integers, and returns that sum
    multiplied by the length of the original list.

    Args:
        numbers (List[Union[int, float]]): A list of integers or floats.

    Returns:
        int: The total sum of rounded values multiplied by the list length.

    Raises:
        ValueError: If the input list contains non-numeric types.
        TypeError: If the input is not a list.
    """
    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list
    list_length: int = len(numbers)
    if list_length == 0:
        return 0

    rounded_values: List[int] = []

    # Process each number in the list individually
    for item in numbers:
        # Validate that each item is a number (int or float)
        if not isinstance(item, (int, float)):
            raise ValueError(f"All elements in the list must be numbers. Found: {type(item).__name__}")

        # Check for NaN or Infinity which cannot be rounded meaningfully in this context
        if float('nan') == float(item):
            raise ValueError("List contains NaN (Not a Number).")
        if float('inf') == float(item) or float('-inf') == float(item):
            raise ValueError("List contains infinity.")

        # Perform the rounding operation
        # Note: round() in Python 3 rounds to the nearest even number for .5 cases.
        # The assertions provided suggest standard rounding behavior or that .5 cases 
        # aren't present/don't conflict with the expected output.
        rounded_num: int = int(round(item))

        # Store the rounded result
        rounded_values.append(rounded_num)

    # Calculate the sum of all rounded numbers
    total_sum: int = 0
    for val in rounded_values:
        total_sum += val

    # Calculate the final result: (Sum of rounded numbers) * (Length of list)
    # Wait, re-reading requirements: "print the total sum multiplied by the length"
    # The assertions show: 
    # [22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50] 
    # Rounded: [22, 4, -16, -9, 11, -12, 14, -5, 18] -> Sum = 17. 
    # Length = 9. 17 * 9 = 153. 
    # Let's re-calculate based on the assertion:
    # 22+4-16-9+11-12+14-5+18 = 17. 17 * 9 = 153.
    # Let's check Assertion 1: round_and_sum(...) == 243.
    # Let's re-sum: 22+4-16-9+11-12+14-5+17 = 16? No.
    # Let's look at the first assertion again: 22.4 (22), 4.0 (4), -16.22 (-16), -9.10 (-9), 
    # 11.00 (11), -12.22 (-12), 14.20 (14), -5.20 (-5), 17.50 (18).
    # Sum = 22+4-16-9+11-12+14-5+18 = 17.
    # If the sum was 27, 27 * 9 = 243.
    # Let's check the numbers again: 22+4-16-9+11-12+14-5+17 = 16. 
    # Let's try sum of original: 22.4+4.0-16.22-9.10+11.00-12.22+14.20-5.20+17.50 = 16.36.
    # Let's re-examine the first assertion sum: 243 / 9 = 27.
    # How to get 27? 22+4-16-9+11-12+14-5+18 is 17.
    # Wait, 22.4 (22) + 4.0 (4) + 16.22 (16) + 9.10 (9) + 11.00 (11) + 12.22 (12) + 14.20 (14) + 5.20 (5) + 17.50 (18) = 111.
    # Let's check the logic: round every number and print the total sum MULTIPLIED by the length.
    # If the sum of rounded numbers is 27, then 27 * 9 = 243.
    # Let's check the numbers again: 22, 4, -16, -9, 11, -12, 14, -5, 18. 
    # Sum = 22+4-16-9+11-12+14-5+18 = 17. 
    # Is it possible the absolute values were used? 22+4+16+9+11+12+14+5+18 = 111.
    # Is it possible the sum was NOT multiplied by length but something else?
    # Let's check Assertion 2: [5,2,9,24.3,29] -> Sum = 5+2+9+24+29 = 69. Length = 5. 69 * 5 = 345. Correct!
    # Let's check Assertion 3: [25.0, 56.7, 89.2] -> Sum = 25+57+89 = 171. Length = 3. 171 * 3 = 513. Correct!
    # Now let's re-calculate Assertion 1 with the logic:
    # Rounding: 22.4->22, 4.0->4, -16.22->-16, -9.10->-9, 11.00->11, -12.22->-12, 14.20->14, -5.20->-5, 17.50->18
    # Sum = 22 + 4 + (-16) + (-9) + 11 + (-12) + 14 + (-5) + 18 = 17.
    # 17 * 9 = 153.
    # There is a mismatch in my manual sum or the provided assertion. Let's re-calculate sum:
    # 22 + 4 = 26
    # 26 - 16 = 10
    # 10 - 9 = 1
    # 1 + 11 = 12
    # 12 - 12 = 0
    # 0 + 14 = 14
    # 14 - 5 = 9
    # 9 + 18 = 27.
    # Ah! 9 + 18 = 27. 27 * 9 = 243. My previous mental math was wrong. 27 * 9 is indeed 243.
    # So the logic is: Sum(round(x)) * len(list).

    # Final calculation
    final_result: int = total_sum * list_length
    return final_result