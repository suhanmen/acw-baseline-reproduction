from typing import List, Tuple

def validate_input_list(input_list) -> None:
    """
    Validates that the input is a list of numbers (int or float).
    Raises a TypeError if the input is not a list.
    Raises a TypeError if any element in the list is not a number.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list of numbers, but got {type(input_list).__name__}.")

    for index, element in enumerate(input_list):
        if not isinstance(element, (int, float)) or isinstance(element, bool):
            raise TypeError(
                f"Element at index {index} is not a valid number "
                f"(got {type(element).__name__}: {element})."
            )

def extract_positive_numbers(numbers: List[float]) -> List[float]:
    """
    Iterates through the list of numbers and collects only those that are strictly positive.

    Returns a new list containing the positive numbers in their original order.
    If no positive numbers are found, an empty list is returned.
    """
    positive_numbers = []

    for number in numbers:
        # Strictly greater than zero (excludes zero itself)
        if number > 0:
            positive_numbers.append(number)

    return positive_numbers

def format_output_tuple(output_list: List[float]) -> Tuple[float, ...]:
    """
    Converts the list of positive numbers into a tuple for consistent return formatting.
    Returns the tuple of positive numbers.
    """
    return tuple(output_list)

def pos_nos(numbers: List) -> Tuple[float, ...]:
    """
    Prints (for internal logic verification) and returns positive numbers in a list.

    The function:
    1. Validates that the input is a list of numeric types.
    2. Filters the list to keep only positive numbers (greater than 0).
    3. Returns the filtered numbers as a tuple.

    Note: The problem asks to "print" but the assertions check the return value.
    The standard interpretation for such function signatures returning values is
    to return the result. The 'print' instruction in the prompt text is likely
    descriptive of the intent or an instruction for a different context, 
    but the assertions strictly define the return value contract.
    To strictly follow the 'print' instruction while maintaining the assertion contract:
    We will print the message "Printing positive numbers:" followed by the items,
    but the return value is what the assertions check.

    However, looking at the assertions:
    assert pos_nos([-1,-2,1,2]) == 1,2

    This syntax in Python `assert func() == 1,2` actually evaluates as:
    `assert (func() == 1), 2`.
    Wait, the provided assertions in the prompt are:
    `assert pos_nos([-1,-2,1,2]) == 1,2`

    In Python, `1,2` is a tuple. So the assertion is checking if the function returns (1, 2).
    If the user meant "print 1, 2", the return value wouldn't be checked against a tuple of 1,2 
    unless the function was supposed to return that tuple.
    Given the requirement "Keep the given signature exactly as it is" (which implies returning something)
    and the assertions checking equality with `(1, 2)` (a tuple), the function must return a tuple.

    Let's re-read the prompt: "Write a python function to print positive numbers in a list."
    But the assertions are: `assert pos_nos(...) == 1,2`.
    This implies the expected output of the function (return value) is the tuple of positive numbers.
    If the function were only to print, the assertion `func() == ...` would be false unless the function returns the tuple too.
    Therefore, to satisfy the assertions, the function must return the tuple of positive numbers.
    We will also include a print statement as requested by the text description, but the primary 
    mechanism satisfying the test cases is the return value.

    Edge Cases Handled:
    - Empty input: Returns empty tuple ().
    - Single element: Checks if positive, returns tuple with element or empty tuple.
    - All-equal elements: Correctly filters based on value.
    - Zero/negative numbers: Excluded from result.
    - Invalid types: Raises TypeError with descriptive message.

    Args:
        numbers: A list of numeric values (int or float).

    Returns:
        A tuple containing the positive numbers from the input list.
        If no positive numbers exist, returns an empty tuple.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
    """
    # Step 1: Validate Input
    validate_input_list(numbers)

    # Step 2: Extract Positive Numbers
    positive_numbers = extract_positive_numbers(numbers)

    # Step 3: Format Output as Tuple
    result_tuple = format_output_tuple(positive_numbers)

    # Step 4: Print the numbers as requested by the problem description text
    # We print them separated by commas to match the visual style of the assertion examples
    if result_tuple:
        print(", ".join(map(str, result_tuple)))
    else:
        print("No positive numbers found.")

    # Step 5: Return the result to satisfy the assertions
    return result_tuple