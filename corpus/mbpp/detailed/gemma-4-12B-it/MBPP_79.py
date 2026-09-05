from typing import Any

def word_len(word: Any) -> bool:
    """
    Checks whether the length of the provided word is odd.

    The function returns:
    - True if the length of the word is an odd number.
    - False if the length of the word is an even number.

    Args:
        word (Any): The input to be checked. While the problem implies a string,
                     the function handles types that support len().

    Returns:
        bool: True if length is odd, False otherwise.

    Raises:
        TypeError: If the input does not support the len() function.
        ValueError: If the input is None.
    """
    # Step 1: Handle explicit None case
    if word is None:
        raise ValueError("The input 'word' cannot be None.")

    # Step 2: Validate that the input type supports len()
    # We check if the object is a string or a collection.
    # If it doesn't have a length, we raise a TypeError.
    try:
        input_length = len(word)
    except TypeError as exc:
        raise TypeError(
            f"Input of type {type(word).__name__} does not support length calculation."
        ) from exc

    # Step 3: Determine if the length is odd
    # A number is odd if the remainder when divided by 2 is not 0.
    remainder = input_length % 2
    is_odd = (remainder != 0)

    # Step 4: Return the final result
    return is_odd

# Assertions provided in the problem statement
if __name__ == "__main__":
    # Test Case 1: "Hadoop" length is 6 (Even) -> False
    assert word_len("Hadoop") == False

    # Test Case 2: "great" length is 5 (Odd) -> True
    assert word_len("great") == True

    # Test Case 3: "structure" length is 9 (Odd) -> True
    assert word_len("structure") == True