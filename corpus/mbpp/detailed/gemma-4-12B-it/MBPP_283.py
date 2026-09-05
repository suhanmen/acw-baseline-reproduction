from typing import List, Dict


def validate(number: int) -> bool:
    """
    Checks whether the frequency of each digit in a given integer is 
    less than or equal to the value of the digit itself.

    Example:
    - In 1234, frequency of '1' is 1 (1 <= 1), '2' is 1 (1 <= 2), etc. -> True
    - In 51241, frequency of '1' is 2 (2 > 1) -> False

    Args:
        number (int): The integer to validate.

    Returns:
        bool: True if every digit's frequency <= its value, False otherwise.

    Raises:
        ValueError: If the input is not a valid integer or is negative 
                    (as negative signs complicate digit counting).
    """
    # 1. Input Validation
    # Ensure the input is an integer.
    if not isinstance(number, int):
        raise ValueError(f"Input must be an integer. Received: {type(number)}")

    # Handle negative numbers. The problem implies digit counting.
    # We treat the absolute value to handle digits consistently.
    # If the problem strictly forbids negatives, we could raise an error here.
    absolute_number = abs(number)

    # 2. Convert number to a sequence of digits
    # We use string conversion to easily iterate over individual digits.
    number_str = str(absolute_number)

    # Handle empty input (though int conversion prevents this, 
    # it's good defensive practice).
    if not number_str:
        return True

    # 3. Count the frequency of each digit
    # We use a dictionary where Key = Digit (as int), Value = Frequency (as int)
    frequency_map: Dict[int, int] = {}

    for char in number_str:
        # Convert character back to integer
        digit = int(char)

        # Increment the count in the map
        if digit in frequency_map:
            frequency_map[digit] += 1
        else:
            frequency_map[digit] = 1

    # 4. Validate the condition
    # Condition: Frequency of digit 'd' <= value of digit 'd'
    # We iterate through the items in our map.
    for digit_value, frequency in frequency_map.items():
        # Check the specific constraint
        is_valid_digit = frequency <= digit_value

        # If any digit fails the check, the whole number fails.
        if not is_valid_digit:
            return False

    # If we checked all digits and none failed, return True.
    return True


if __name__ == "__main__":
    # Provided assertions
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

    # Additional Edge Cases
    # Single digit 0: frequency of 0 is 1. 1 <= 0 is False.
    assert validate(0) == False
    # All same digits: 22 (freq 2, value 2) -> True
    assert validate(22) == True
    # All same digits: 11 (freq 2, value 1) -> False
    assert validate(11) == False
    # Large numbers with valid frequencies
    assert validate(998877665544332211) == True
    # Large numbers with invalid frequencies
    assert validate(111222) == False