from typing import List, Any, Union

def sum_of_digits(input_data: Union[List[Any], Any]) -> int:
    """
    Computes the sum of the digits of all numbers present in the input.
    The input can be a list of numbers/mixed types, or a nested list.
    Non-numeric characters (like 'a', 'b') are ignored.
    Negative signs are ignored (only the absolute value's digits are summed).

    Args:
        input_data: A list or nested list containing various types.

    Returns:
        int: The total sum of all digits found in all numbers.
    """
    # Initialize the total accumulator
    total_sum = 0

    def extract_digits_from_item(item: Any) -> int:
        """
        Helper to determine if an item is a number and return the sum of its digits.
        Handles integers, floats, and strings that represent numbers.
        """
        current_item_digit_sum = 0

        # Case 1: The item is a direct integer or float
        if isinstance(item, (int, float)):
            # Convert to string to iterate over digits, 
            # handle negative signs by taking absolute value.
            str_representation = str(abs(int(item)))
            for character in str_representation:
                if character.isdigit():
                    current_item_digit_sum += int(character)

        # Case 2: The item is a string (e.g., '70' or 'a')
        elif isinstance(item, str):
            # We treat the string as a potential number.
            # If the string represents a number (like '70'), we sum its digits.
            # If it is just a letter ('a'), it contributes 0.
            # We iterate through each character to be safe.
            for character in item:
                if character.isdigit():
                    current_item_digit_sum += int(character)

        # Case 3: Item is neither a number nor a string
        else:
            # Explicitly ignore other types (None, lists, dicts, etc. 
            # that aren't handled by recursion).
            pass

        return current_item_digit_sum

    def process_recursive(data: Any) -> None:
        """
        Recursively traverses nested lists to find numbers and sum their digits.
        """
        nonlocal total_sum

        # If the current data is a list, iterate through its elements
        if isinstance(data, list):
            for element in data:
                process_recursive(element)
        else:
            # If the data is a scalar, process it
            total_sum += extract_digits_from_item(data)

    # Defensive check: if input is None, return 0
    if input_data is None:
        return 0

    # Start the recursive processing
    process_recursive(input_data)

    return total_sum

# The following assertions are provided by the problem statement to verify logic
if __name__ == "__main__":
    # Test Case 1: Standard list of integers
    # 1+0 + 2 + 5+6 = 14
    assert sum_of_digits([10, 2, 56]) == 14

    # Test Case 2: Nested list with mixed types
    # 1+0 + 2+0 + 4 + 5 + (b=0) + 7+0 + (a=0) = 19
    assert sum_of_digits([[10, 20, 4, 5, 'b', 70, 'a']]) == 19

    # Test Case 3: Negative numbers
    # 1+0 + 2+0 + (abs -4 -> 4) + 5 + (abs -70 -> 7+0) = 19
    assert sum_of_digits([10, 20, -4, 5, -70]) == 19