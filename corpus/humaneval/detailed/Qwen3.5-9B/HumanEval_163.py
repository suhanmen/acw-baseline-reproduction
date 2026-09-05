import math
import sys
from typing import List, Union

def validate_integer_input(value: Union[int, float], variable_name: str) -> int:
    """
    Validates that the provided value is a non-negative integer.

    Raises:
        ValueError: If the value is not an integer, is negative, or has non-integer components.
    """
    if not isinstance(value, int):
        if isinstance(value, float) and value.is_integer():
            # Handle float representations of integers like 5.0
            pass
        else:
            raise ValueError(
                f"Invalid input for '{variable_name}': expected an integer, "
                f"received type '{type(value).__name__}'."
            )

    if value < 0:
        raise ValueError(
            f"Invalid input for '{variable_name}': expected a non-negative integer, "
            f"received value {value}."
        )

    return value

def ensure_range_order(a: int, b: int) -> tuple:
    """
    Ensures that the start of the range is less than or equal to the end.
    Returns a tuple (start, end) where start <= end.
    """
    if a > b:
        return b, a
    return a, b

def is_even_digit(number: int) -> bool:
    """
    Checks if the given number is an even digit (0, 2, 4, 6, or 8).

    Args:
        number: The number to check. Must be a single-digit integer.

    Returns:
        True if the number is one of {0, 2, 4, 6, 8}, False otherwise.
    """
    even_digits = {0, 2, 4, 6, 8}
    if number in even_digits:
        return True
    return False

def extract_even_digits_from_range(start: int, end: int) -> List[int]:
    """
    Extracts all even digits found in the numbers from start to end (inclusive).
    The numbers themselves are iterated, and their constituent digits are checked.
    The problem description implies extracting digits FROM the range of numbers.
    However, looking at the examples:
    - generate_integers(2, 8) => [2, 4, 6, 8] (These are the even digits 2,4,6,8 which are also the even numbers 2,4,6,8)
    - generate_integers(8, 2) => [2, 4, 6, 8]
    - generate_integers(10, 14) => [] 
      Numbers: 10, 11, 12, 13, 14.
      Digits: 1,0, 1,1, 1,2, 1,3, 1,4.
      Even digits: 0, 2, 4.
      But the expected output is [].

    RE-EVALUATION OF PROBLEM STATEMENT:
    "return the even digits between a and b"

    If the example (10, 14) returns [], it strongly implies that we are NOT extracting 
    individual digits from the multi-digit numbers. Instead, it implies we are looking for 
    even *integers* (numbers) that lie between a and b.

    Let's re-read carefully: "return the even digits between a and b".
    In many programming puzzles, "even digits" might be a slightly imprecise way of saying 
    "even numbers". 
    If we treat them as even numbers:
    Range 2 to 8: 2, 4, 6, 8 are even. Result: [2, 4, 6, 8]. Matches.
    Range 8 to 2: Same set. Matches.
    Range 10 to 14: 10, 12, 14 are even numbers. 
    BUT the example says: generate_integers(10, 14) => []

    This is a contradiction if interpreted as "even numbers within the range".
    Why would 10 to 14 yield an empty list?
    10 is even. 12 is even. 14 is even.

    Is it possible the problem means "single digit even numbers"?
    If so, range(2, 8) contains single digits 2,3,4,5,6,7,8. Evens: 2,4,6,8.
    Range(10, 14) contains 10,11,12,13,14. None of these are single digits. 
    So if the constraint is "even digits" interpreted strictly as "numbers that are both 
    even AND are single digits", then:
    (2, 8) -> 2,4,6,8 are single digit evens. OK.
    (10, 14) -> 10,12,14 are multi-digit. Result []. OK.

    This interpretation fits all examples perfectly.
    Definition: "Even Digits" = Numbers x such that:
    1. x is an integer.
    2. 0 <= x <= 9.
    3. x % 2 == 0.
    4. x is within the inclusive range [min(a,b), max(a,b)].
    """

    result: List[int] = []

    # Determine the actual range boundaries
    lower_bound: int = start
    upper_bound: int = end

    # Iterate through every number in the inclusive range [lower_bound, upper_bound]
    current_number: int = lower_bound

    while current_number <= upper_bound:
        # Check if the current number is a single digit (0-9)
        # Mathematically: 0 <= current_number <= 9
        if current_number >= 0 and current_number <= 9:
            # Check if the single-digit number is even
            if current_number % 2 == 0:
                result.append(current_number)
        # Else: It is a multi-digit number, so it cannot be an "even digit"
        # per the logical deduction from the (10, 14) example.

        current_number += 1

    return result

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    Based on the provided examples:
    - generate_integers(2, 8) => [2, 4, 6, 8]
    - generate_integers(8, 2) => [2, 4, 6, 8]
    - generate_integers(10, 14) => []

    The logic deduced is to find all integers within the range [min(a,b), max(a,b)]
    that are both single-digit numbers (0-9) AND are even.

    Args:
        a: First boundary integer.
        b: Second boundary integer.

    Returns:
        A list of even single-digit integers found in the range, sorted ascending.
        Returns an empty list if no such numbers exist or inputs are invalid.

    Raises:
        ValueError: If inputs are not non-negative integers.
    """
    # Step 1: Validate Input 'a'
    validate_integer_input(a, "a")

    # Step 2: Validate Input 'b'
    validate_integer_input(b, "b")

    # Step 3: Normalize the range order (ensure start <= end)
    # We create a sorted tuple of the boundaries
    sorted_boundaries: tuple = ensure_range_order(a, b)

    # Step 4: Extract the even single-digit numbers from the normalized range
    # This function encapsulates the core logic derived from the examples
    final_result: List[int] = extract_even_digits_from_range(sorted_boundaries[0], sorted_boundaries[1])

    # Step 5: Return the result
    # The extraction logic already appends in ascending order (iterating from low to high)
    return final_result