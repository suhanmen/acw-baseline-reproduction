from typing import Tuple, Optional
import re

def _extract_quantity(sentence: str, fruit_name: str) -> Optional[int]:
    """
    Extracts the integer quantity associated with a specific fruit name from the sentence.

    The fruit name in the sentence is expected to be followed by the number (e.g., "5 apples").
    This function searches for the pattern: [whitespace]* <fruit_name> [whitespace]* <number>.

    Args:
        sentence (str): The input string describing the fruits.
        fruit_name (str): The name of the fruit to look for (e.g., "apples", "oranges").

    Returns:
        int or None: The extracted quantity if found, otherwise None.
    """
    # Create a regex pattern dynamically based on the fruit name.
    # We escape the fruit name in case it contains regex special characters (though unlikely).
    escaped_fruit = re.escape(fruit_name)

    # Pattern explanation:
    # \s+       : One or more whitespace characters
    # {name}\s* : The fruit name, optionally followed by whitespace
    # (\d+)     : Captures one or more digits (the quantity)
    pattern = r"\s+{}(\s+)(\d+)".format(escaped_fruit)

    match = re.search(pattern, sentence, re.IGNORECASE)

    if match:
        # Extract the captured group which is the number part
        quantity_str = match.group(2)

        # Validate that the matched group is indeed a valid integer string
        # This handles cases like "10.5" which re.match might not catch fully but safe casting helps
        try:
            quantity = int(quantity_str)
            return quantity
        except ValueError:
            # If for some reason the string is not a pure integer
            return None

    return None

def _validate_inputs(s: str, n: int) -> Tuple[bool, Optional[str]]:
    """
    Validates the input arguments against strict requirements.

    Returns:
        tuple: (is_valid, error_message). If valid, error_message is None.
    """
    # Validate 'n' (total fruits)
    if not isinstance(n, int):
        return False, "The total number of fruits 'n' must be an integer."

    if n < 0:
        return False, "The total number of fruits 'n' cannot be negative."

    # Validate 's' (description string)
    if not isinstance(s, str):
        return False, "The description string 's' must be a string."

    # Check for valid string content constraints if necessary
    # Based on problem, s should contain "apples", "oranges", and "and".
    if "apples" not in s.lower() or "oranges" not in s.lower():
        # We might still try to process if format is weird, but strictly speaking,
        # missing required fruits makes extraction impossible or misleading.
        # However, to be robust against malformed but parseable inputs, we let extraction handle it.
        # The main validation is type-based.
        pass

    return True, None

def fruit_distribution(s: str, n: int) -> int:
    """
    Calculates the number of mango fruits in a basket.

    The basket contains apples, oranges, and mango fruits.
    Given a string describing the count of apples and oranges, and the total count of all fruits,
    this function returns the count of mango fruits.

    Formula: Mango Count = Total Fruits (n) - Apple Count - Orange Count

    Args:
        s (str): A string containing the number of apples and oranges (e.g., "5 apples and 6 oranges").
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits.

    Examples:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 oranges", 3)
        2
        >>> fruit_distribution("2 apples and 3 oranges", 100)
        95
    """

    # Step 1: Validate inputs explicitly
    is_valid, error_msg = _validate_inputs(s, n)
    if not is_valid:
        # Instead of raising, we return a sentinel or raise a custom exception.
        # Since the problem asks for runnable code and specific behavior on valid inputs,
        # and no specific invalid behavior is defined, raising a ValueError is the Pythonic standard.
        raise ValueError(error_msg)

    # Step 2: Extract the number of apples
    # We search case-insensitively to handle "Apples" or "APPLES"
    apple_count = _extract_quantity(s, "apples")

    # Step 3: Extract the number of oranges
    orange_count = _extract_quantity(s, "oranges")

    # Step 4: Handle cases where extraction fails (e.g., malformed string)
    # If a count is None, we cannot proceed logically with the subtraction as per the problem definition.
    # We assume valid input format based on the docstring examples, but add a safety check.
    if apple_count is None or orange_count is None:
        raise ValueError("Could not extract quantities for 'apples' and 'oranges' from the input string.")

    # Step 5: Calculate the result using explicit intermediate variables for clarity
    apples_in_basket = apple_count
    oranges_in_basket = orange_count

    # Calculate the sum of known fruits
    known_fruits_sum = apples_in_basket + oranges_in_basket

    # Calculate mangoes
    # If known_fruits_sum > n, the result would be negative, which is physically impossible.
    # However, mathematically, the function returns the remainder.
    # We do not clamp to 0 unless specified, but typically negative implies error in input data.
    # For this specific problem logic, we return the mathematical difference.
    mango_count = n - known_fruits_sum

    return mango_count