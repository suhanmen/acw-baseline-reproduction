import re

def extract_numbers_from_string(input_string: str) -> list[int]:
    """
    Helper function to extract all integers from a given string.

    Args:
        input_string (str): The string containing fruit counts.

    Returns:
        list[int]: A list of integers found in the string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input string must be a string.")

    # Use regular expression to find all sequences of digits
    # \d+ matches one or more digits
    numbers_found = re.findall(r'\d+', input_string)

    # Convert the extracted strings to integers
    numeric_list = []
    for num_str in numbers_found:
        numeric_list.append(int(num_str))

    return numeric_list

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examle:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    # Input Validation: Ensure s is a string and n is an integer
    if not isinstance(s, str):
        raise ValueError("The fruit description must be a string.")

    if not isinstance(n, int):
        raise ValueError("The total number of fruits must be an integer.")

    # Handle degenerate case: Empty string input
    if not s.strip():
        # If no description is provided, we assume 0 apples and 0 oranges
        # unless the logic dictates otherwise; here we proceed to extraction.
        pass

    # Extract the numeric values for apples and oranges from the string
    # Example: "5 apples and 6 oranges" -> [5, 6]
    extracted_counts = extract_numbers_from_string(s)

    # According to the problem description, we need to subtract the 
    # count of apples and oranges from the total n.
    # Even if there are more or fewer numbers, the logic implies 
    # extracting the quantities mentioned.

    total_extracted_sum = 0
    for count in extracted_counts:
        total_extracted_sum += count

    # Calculate the number of mango fruits
    # Mangoes = Total - (Apples + Oranges)
    mango_count = n - total_extracted_sum

    # Defensive check: If the sum of apples and oranges exceeds n,
    # the result could be negative. We return the result as is, 
    # but in production, one might choose to raise an error or floor at 0.
    # Based on the examples, simple subtraction is the expected behavior.

    return mango_count