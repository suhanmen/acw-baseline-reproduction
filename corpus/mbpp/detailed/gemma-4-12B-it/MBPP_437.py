from typing import List

def remove_odd_characters(input_string: str) -> str:
    """
    Removes characters from a string that are at odd indices (1, 3, 5, ...).
    The indices are 0-based. 
    Example: "python"
    Index 0: p (even) -> keep
    Index 1: y (odd)  -> remove
    Index 2: t (even) -> keep
    Index 3: h (odd)  -> remove
    Index 4: o (even) -> keep
    Index 5: n (odd)  -> remove

    Wait, let's check the provided assertions:
    assert remove_odd("python") == ("yhn")
    Index 0: p (even)
    Index 1: y (odd)
    Index 2: t (even)
    Index 3: h (odd)
    Index 4: o (even)
    Index 5: n (odd)

    If the result is "yhn", the logic must be:
    "python" -> indices 1, 3, 5 are kept?
    p(0), y(1), t(2), h(3), o(4), n(5)
    "yhn" corresponds to indices 1, 3, 5.

    Let's check "program" == "rga"
    p(0), r(1), o(2), g(3), r(4), a(5), m(6)
    Indices: 1, 3, 5 are r, g, a. Correct.

    Let's check "language" == "agae"
    l(0), a(1), n(2), g(3), u(4), a(5), g(6), e(7)
    Indices: 1, 3, 5, 7 are a, g, a, e. Correct.

    Therefore, the logic is: Keep characters at odd indices, 
    remove characters at even indices.
    """

    # Validate input type
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")

    # Handle empty string case
    if len(input_string) == 0:
        return ""

    # We will build the result as a list of characters to avoid 
    # the overhead of string concatenation in a loop.
    result_chars: List[str] = []

    # Iterate through the string by index
    for current_index in range(len(input_string)):
        current_char = input_string[current_index]

        # Check if the current index is odd
        # An integer is odd if the remainder when divided by 2 is non-zero.
        is_index_odd = (current_index % 2 != 0)

        if is_index_odd:
            # The requirements imply we only keep characters at odd indices.
            result_chars.append(current_char)
        else:
            # Character is at an even index, we do nothing (effectively "remove" it).
            pass

    # Join the list of characters into a final string.
    final_string = "".join(result_chars)

    return final_string

def remove_odd(input_string: str) -> str:
    """
    Wrapper function to match the required signature for the assertions.
    """
    # Perform explicit check for valid input type
    if not isinstance(input_string, str):
        raise TypeError(f"Expected string, got {type(input_string).__name__}")

    # Execute the logic
    result = remove_odd_characters(input_string)

    return result

# The following assertions are provided by the problem description.
# These would be passed during a test suite.
if __name__ == "__main__":
    # Manual verification based on the problem description
    assert remove_odd("python") == "yhn"
    assert remove_odd("program") == "rga"
    assert remove_odd("language") == "agae"