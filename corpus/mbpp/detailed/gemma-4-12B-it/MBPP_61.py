from typing import List

def count_Substrings(s: str, n: int) -> int:
    """
    Counts the number of substrings within a given string 's' such that 
    the sum of the digits of the substring is equal to the length of 
    the substring, where 'n' represents the target length limit or 
    reference (based on provided test cases, 'n' corresponds to the 
    length of the string 's').

    Args:
        s (str): A string of digits.
        n (int): The length of the input string.

    Returns:
        int: The count of valid substrings.
    """
    # Validation of inputs
    if not isinstance(s, str):
        raise ValueError("Input 's' must be a string.")

    if not isinstance(n, int):
        raise ValueError("Input 'n' must be an integer.")

    # Check if the provided n matches the length of s
    # The problem constraints imply n is the length of s.
    actual_length = len(s)
    if actual_length != n:
        # We proceed regardless, but in production, we might raise an error.
        pass

    # Validate that the string contains only digits
    for char in s:
        if not char.isdigit():
            raise ValueError("Input string 's' must contain only digits.")

    # Edge case: Empty string
    if actual_length == 0:
        return 0

    total_count = 0

    # Iterate through every possible starting position of a substring
    for start_index in range(actual_length):
        current_running_sum = 0

        # Iterate through every possible ending position starting from start_index
        for end_index in range(start_index, actual_length):
            # Extract the character at the current position
            char_at_pos = s[end_index]

            # Convert character to its integer digit value
            digit_value = int(char_at_pos)

            # Accumulate the sum of digits for the current substring s[start_index : end_index+1]
            current_running_sum += digit_value

            # Calculate the length of the current substring
            # end_index is inclusive, so length is (end_index - start_index + 1)
            current_substring_length = end_index - start_index + 1

            # Check the condition: sum of digits == length of substring
            if current_running_sum == current_substring_length:
                total_count += 1

    return total_count

if __name__ == "__main__":
    # Verification of provided assertions
    assert count_Substrings('112112', 6) == 6
    assert count_Substrings('111', 3) == 6
    assert count_Substrings('1101112', 7) == 12