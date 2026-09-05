from typing import List

def _generate_permutations_recursive(sequence: List[str]) -> List[List[str]]:
    """
    Helper function to generate permutations of a list of strings.

    This function uses a recursive backtracking approach to generate all
    possible permutations of the input sequence. It handles duplicates
    naturally by generating all permutations and then removing duplicates.

    Args:
        sequence: A list of strings to permute

    Returns:
        A list of lists, where each inner list represents one permutation
    """
    length = len(sequence)

    # Base case: if the sequence is empty, return a list containing one empty permutation
    if length == 0:
        return [[]]

    # Base case: if the sequence has one element, return a list containing that single element
    if length == 1:
        return [sequence]

    all_permutations = []

    # Iterate through each element in the sequence
    for i in range(length):
        current_element = sequence[i]

        # Create a new sequence without the current element
        remaining_elements = []
        for j in range(length):
            if i != j:
                remaining_elements.append(sequence[j])

        # Recursively generate permutations of the remaining elements
        sub_permutations = _generate_permutations_recursive(remaining_elements)

        # For each sub-permutation, prepend the current element
        for sub_perm in sub_permutations:
            new_permutation = [current_element] + sub_perm
            all_permutations.append(new_permutation)

    return all_permutations

def _remove_duplicates_from_permutations(permutations: List[List[str]]) -> List[str]:
    """
    Helper function to remove duplicate permutations and join them into strings.

    This function converts list permutations to strings, removes duplicates
    while preserving order, and returns the result as a list of strings.

    Args:
        permutations: A list of lists, where each inner list is a permutation

    Returns:
        A list of strings with no duplicates
    """
    result_strings = []
    seen = set()

    for perm in permutations:
        # Convert the list permutation to a string
        perm_string = "".join(perm)

        # Only add if we haven't seen this permutation before
        if perm_string not in seen:
            seen.add(perm_string)
            result_strings.append(perm_string)

    return result_strings

def permute_string(s: str) -> List[str]:
    """
    Generate all permutations of a given string, including duplicates.

    This function takes a string as input and returns a list of all possible
    permutations of that string. If the string contains duplicate characters,
    all unique permutations will be returned (duplicates removed).

    The function handles various edge cases:
    - Empty string: returns ['']
    - Single character: returns [the character]
    - All identical characters: returns [the character repeated n times]
    - Strings with duplicate characters: returns unique permutations only

    Args:
        s: The input string to permute

    Returns:
        A list of strings, where each string is a unique permutation of the input
    """
    # Input validation
    if s is None:
        raise ValueError("Input string cannot be None")

    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Edge case: empty string
    if len(s) == 0:
        return ['']

    # Convert string to list of characters for easier manipulation
    char_list = list(s)

    # Generate all permutations recursively
    raw_permutations = _generate_permutations_recursive(char_list)

    # Remove duplicates and convert to string format
    unique_permutations = _remove_duplicates_from_permutations(raw_permutations)

    return unique_permutations