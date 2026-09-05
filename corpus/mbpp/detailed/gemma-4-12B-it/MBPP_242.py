from typing import Any

def count_charac(input_string: Any) -> int:
    """
    Counts the total number of characters in a provided string.

    Args:
        input_string (Any): The input to be measured. While intended to be a string,
                             the function handles non-string types by attempting 
                             conversion or raising a descriptive error.

    Returns:
        int: The total count of characters in the input string.

    Raises:
        TypeError: If the input cannot be converted to a string.
    """
    # Step 1: Validate the input type.
    # While many Python functions are duck-typed, for production-grade code
    # we should be explicit about what we expect.
    if input_string is None:
        # Depending on requirements, None could be 0 or an error.
        # Given the context of counting characters in a string,
        # treating it as an empty string (0) is a safe default.
        return 0

    # Step 2: Ensure the input is treated as a string.
    # If it is already a string, we use it as is.
    # If it is another type (like an int), we convert it to a string representation.
    if isinstance(input_string, str):
        work_string = input_string
    else:
        try:
            work_string = str(input_string)
        except Exception as e:
            raise TypeError(f"Input of type {type(input_string)} could not be converted to string.") from e

    # Step 3: Handle the edge case of an empty string explicitly.
    # Although len("") returns 0 naturally, we can make the logic explicit.
    if len(work_string) == 0:
        return 0

    # Step 4: Calculate the character count.
    # We use the built-in len() function which is O(1) for strings in Python
    # as they store their length internally.
    total_count = len(work_string)

    # Step 5: Return the final result.
    return total_count

if __name__ == "__main__":
    # Testing the assertions provided in the problem description
    assert count_charac("python programming") == 18
    assert count_charac("language") == 8
    assert count_charac("words") == 5

    # Additional production-grade edge cases:
    assert count_charac("") == 0                # Empty string
    assert count_charac(" ") == 1               # Single whitespace
    assert count_charac("aaaaa") == 5          # All equal elements
    assert count_charac("123") == 3            # Numeric string
    assert count_charac(100) == 3              # Integer input (converted to "100")
    assert count_charac("!") == 1              # Special character