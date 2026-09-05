from collections import Counter
from typing import List, Union

Number = Union[int, float]

def _validate_input_sequence(sequence: List[Number], length_hint: int) -> None:
    """
    Validates that the provided sequence is a list, contains no None values,
    and that the length matches the provided length_hint if it is positive.

    Args:
        sequence: The input list to validate.
        length_hint: An optional integer hint for the expected length.

    Raises:
        TypeError: If sequence is not a list or contains non-numeric values.
        ValueError: If length_hint does not match the actual sequence length.
    """
    # Check if sequence is a list
    if not isinstance(sequence, list):
        raise TypeError("The input sequence must be a list.")

    # Check for None values in the sequence
    for index, item in enumerate(sequence):
        if item is None:
            raise ValueError(f"Found None value at index {index} in the sequence.")
        if not isinstance(item, (int, float)):
            raise TypeError(f"Found non-numeric value '{item}' at index {index} in the sequence.")

    # Check length hint if provided and positive
    if length_hint is not None and length_hint > 0:
        actual_length = len(sequence)
        if actual_length != length_hint:
            raise ValueError(
                f"Length mismatch: provided length_hint is {length_hint}, "
                f"but actual sequence length is {actual_length}."
            )

def _count_element_occurrences(sequence: List[Number]) -> dict:
    """
    Counts the occurrences of each distinct number in the sequence.

    Args:
        sequence: The input list of numbers.

    Returns:
        A dictionary where keys are the numbers and values are their counts.
    """
    counts: dict = {}
    for item in sequence:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def _identify_non_repeated_elements(counts: dict) -> List[Number]:
    """
    Identifies and returns the elements that appear exactly once in the sequence.

    Args:
        counts: A dictionary mapping numbers to their occurrence counts.

    Returns:
        A list of numbers that appear exactly once.
    """
    non_repeated: List[Number] = []
    for number, count in counts.items():
        if count == 1:
            non_repeated.append(number)
    return non_repeated

def _calculate_product(sequence: List[Number]) -> Union[int, float]:
    """
    Calculates the product of all numbers in the sequence.

    Args:
        sequence: A list of numbers.

    Returns:
        The product of the numbers. Returns 1 if the list is empty.
    """
    product: Union[int, float] = 1
    for number in sequence:
        product = product * number
    return product

def find_Product(sequence: List[Number], length: int) -> Union[int, float]:
    """
    Finds the product of non-repeated elements in a given array.

    A non-repeated element is defined as an element that appears exactly once in the array.

    Args:
        sequence: A list of numeric values.
        length: An optional integer indicating the expected length of the sequence.

    Returns:
        The product of all elements that appear exactly once in the sequence.
        Returns 1 if no non-repeated elements exist (empty set product).

    Raises:
        TypeError: If sequence is not a list or contains invalid types.
        ValueError: If length is provided but does not match the sequence length.
    """
    # Step 1: Validate the input sequence and length hint
    _validate_input_sequence(sequence, length)

    # Step 2: Count occurrences of each element
    element_counts = _count_element_occurrences(sequence)

    # Step 3: Identify elements that appear exactly once
    non_repeated_elements = _identify_non_repeated_elements(element_counts)

    # Step 4: Calculate the product of these non-repeated elements
    result = _calculate_product(non_repeated_elements)

    return result