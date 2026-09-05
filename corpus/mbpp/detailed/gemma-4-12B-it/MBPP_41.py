from typing import List, Any

def filter_evennumbers(numbers: List[Any]) -> List[int]:
    """
    Filters a list of numbers and returns only the even integers.

    Args:
        numbers (List[Any]): A list containing numbers (integers/floats).

    Returns:
        List[int]: A list containing only the even integers from the input.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-numeric values that 
                    cannot be checked for parity.
    """
    # 1. Validate input type
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # 2. Handle edge case: empty list
    if len(numbers) == 0:
        return []

    # 3. Define the criteria for an even number using a lambda function.
    # An even number is defined as a number divisible by 2 with a remainder of 0.
    # We also ensure the number is an integer, as floats like 2.0 are 
    # technically even but usually not expected in an integer filter.
    is_even = lambda n: isinstance(n, int) and n % 2 == 0

    # 4. Process the list and handle potential data issues
    filtered_list = []

    for item in numbers:
        # Explicit check to ensure we are dealing with numbers
        # If a non-numeric type is found that isn't handled by the lambda,
        # we decide how to handle it (here, we skip non-integers).
        if not isinstance(item, (int, float)):
            # Depending on requirements, we could raise an error or skip.
            # For production grade, we'll skip non-numeric types but 
            # could log a warning here.
            continue

        # If it's a float like 4.0, we treat it as an integer for parity 
        # if it has no fractional part, or we strictly follow the 'int' rule.
        # Based on the assertions, we assume integers.
        if isinstance(item, float):
            # Check if float is equivalent to an integer (e.g., 4.0)
            if item.is_integer():
                val_as_int = int(item)
                if val_as_int % 2 == 0:
                    filtered_list.append(val_as_int)
            else:
                # It's a float with decimals (e.g., 4.5), skip it
                continue
        else:
            # It is an integer
            if is_even(item):
                filtered_list.append(item)

    # The problem specifically asks to use the filter function with a lambda.
    # Let's re-implement the logic strictly using the functional 'filter' approach
    # to adhere to the "using lambda function" requirement while remaining robust.

    # Re-validating inputs to ensure they are numeric before passing to filter
    # to avoid crashes during the lambda execution.
    numeric_only_input = []
    for x in numbers:
        if isinstance(x, (int, float)):
            numeric_only_input.append(x)

    # Define a production-grade lambda that handles the even check
    # We use 'int(x) % 2 == 0' to handle both 2 and 2.0
    even_lambda = lambda x: isinstance(x, (int, float)) and x % 2 == 0 and float(x).is_integer()

    # However, the assertions suggest we want the resulting integers.
    # Let's use a list comprehension or filter to extract and cast to int.

    result = []
    # We use the filter function as requested by the prompt.
    # We wrap it in a way that ensures we only keep actual even integers.
    iterable_to_filter = [x for x in numbers if isinstance(x, (int, float))]

    # The core requirement: filter even numbers using lambda
    filtered_iterator = filter(lambda x: x % 2 == 0, iterable_to_filter)

    # Convert the filter object to a list and ensure all are ints
    # (Handles the case where 2.0 might be in the input)
    result = [int(x) for x in filtered_iterator]

    # Since we need to strictly follow the assertions, let's double check
    # if the filter should only apply to actual integers.
    # Re-calculating based on strict integer logic to match assertions exactly.

    final_result = []
    for item in numbers:
        if isinstance(item, int) and item % 2 == 0:
            final_result.append(item)

    # The prompt asks to "filter even numbers using lambda".
    # Here is the most direct implementation of that requirement:
    final_list = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, numbers))

    return final_list

# To ensure it passes the specific assertions provided:
def filter_evennumbers(numbers: List[Any]) -> List[int]:
    """
    Refined implementation to strictly pass the provided assertions
    while adhering to the 'use lambda' requirement.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Lambda function to check if a value is an even integer
    check_even = lambda x: isinstance(x, int) and x % 2 == 0

    # Using the built-in filter function with the lambda
    # filter() returns an iterator in Python 3
    even_numbers_iterator = filter(check_even, numbers)

    # Convert the iterator to a list to return
    result = list(even_numbers_iterator)

    return result