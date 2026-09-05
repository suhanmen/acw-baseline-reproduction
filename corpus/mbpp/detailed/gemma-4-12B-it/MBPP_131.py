from typing import List

def reverse_vowels(s: str) -> str:
    """
    Reverses only the vowels in a given string while keeping 
    all other characters in their original positions.

    Vowels are defined as 'a', 'e', 'i', 'o', 'u' (case-insensitive).

    Args:
        s (str): The input string to process.

    Returns:
        str: The modified string with reversed vowels.

    Raises:
        TypeError: If the input is not a string.
    """
    # Input Validation: Ensure the input is a string.
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, but received {type(s).__name__}")

    # Handle edge case: Empty string or string of length 1.
    # Reversing vowels in these cases results in the same string.
    if len(s) <= 1:
        return s

    # Define the set of vowels for O(1) lookup performance.
    # Included both lowercase and uppercase.
    vowels_set = {
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    }

    # Convert the string to a list because strings in Python are immutable.
    # This allows us to perform in-place swaps.
    chars = list(s)

    # Use two pointers to find vowels from both ends of the string.
    left_pointer = 0
    right_pointer = len(chars) - 1

    while left_pointer < right_pointer:
        # Move the left pointer until a vowel is found.
        while left_pointer < right_pointer and chars[left_pointer] not in vowels_set:
            left_pointer += 1

        # Move the right pointer until a vowel is found.
        while left_pointer < right_pointer and chars[right_pointer] not in vowels_set:
            right_pointer -= 1

        # If pointers have crossed, we have processed all vowels.
        if left_pointer >= right_pointer:
            break

        # Swap the vowels found at the left and right pointers.
        temp_char = chars[left_pointer]
        chars[left_pointer] = chars[right_pointer]
        chars[right_pointer] = temp_char

        # Move both pointers inward to continue the search.
        left_pointer += 1
        right_pointer -= 1

    # Join the list back into a single string and return.
    result = "".join(chars)
    return result

if __name__ == "__main__":
    # Validating provided assertions
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"