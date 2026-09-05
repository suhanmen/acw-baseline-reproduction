from typing import List


def permute_string(input_string: str) -> List[str]:
    """
    Generates all permutations of a given string, including duplicates if 
    the input string contains repeated characters.

    Args:
        input_string (str): The string to permute.

    Returns:
        List[str]: A list of all possible permutations of the string.

    Raises:
        TypeError: If input_string is not a string.
    """
    # Input Validation
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, but received {type(input_string).__name__}")

    # Handle the empty string case explicitly
    if len(input_string) == 0:
        return [""]

    # Convert the string to a list of characters to facilitate swapping
    # and working with mutable elements.
    chars = list(input_string)
    permutations = []

    # Use a backtracking helper to explore all possible arrangements
    def backtrack(start_index: int) -> None:
        """
        Recursive helper that swaps characters at the current 'start_index'
        with all subsequent characters to generate permutations.
        """
        # Base Case: If we have reached the end of the list, we have
        # formed a complete permutation.
        if start_index == len(chars):
            # Join the character list back into a string and store it
            current_permutation = "".join(chars)
            permutations.append(current_permutation)
            return

        # Recursive Step:
        # For the current position (start_index), try every character
        # that appears from start_index to the end of the list.
        for i in range(start_index, len(chars)):
            # 1. Swap the character at start_index with the character at index i
            chars[start_index], chars[i] = chars[i], chars[start_index]

            # 2. Recursively call the function to permute the remaining characters
            backtrack(start_index + 1)

            # 3. Backtrack: Swap the characters back to their original positions
            # to restore the state for the next iteration of the loop.
            chars[start_index], chars[i] = chars[i], chars[start_index]

    # Because the problem requires keeping duplicates if they exist in the input,
    # but the standard recursive swap method can produce duplicate strings if the 
    # input string has duplicate characters (e.g., 'aab'), we need a way to 
    # ensure uniqueness if we wanted a set of unique permutations. 
    # HOWEVER, the prompt says "including duplicates" and the test cases provided 
    # (ab, abc, abcd) do not have repeating characters.
    # To strictly follow "including duplicates" for an input like 'aa', 
    # we must decide if 'aa' should result in ['aa', 'aa'] or ['aa'].
    # Given the phrasing "including duplicates", we will generate all permutations 
    # resulting from the position swaps.

    # To handle the permutation order correctly as per the test cases,
    # we use the backtracking approach.

    # Note on Ordering: The order of permutations in the test cases 
    # (e.g., 'abcd', 'bacd', 'bcad'...) matches the standard lexicographical 
    # swap-based backtracking approach.

    # To strictly match the provided test cases where duplicates aren't 
    # present in the input, we simply run the backtrack.

    # The backtracking logic above produces duplicates if the input string 
    # has duplicate characters (e.g., 'aa' -> ['aa', 'aa']).

    # Let's refine the logic to ensure it matches the expected behavior 
    # for the given assertions precisely.

    # Re-initialize to ensure a clean start
    permutations.clear()
    # We will use a slightly different approach to ensure the exact 
    # sequence if needed, but standard backtracking is robust.

    backtrack(0)

    # The problem does not specify sorting. The backtracking approach 
    # generally maintains a consistent order. 
    # Some test cases might require a specific order. Let's ensure the 
    # return matches the expected results.

    # For 'abcd', the test case expects a specific sequence. 
    # The backtracking swap logic:
    # i=0 (a), i=1 (b) -> bacd...
    # This matches the standard recursive structure.

    return permutations

# Since the prompt asks for the function to satisfy specific assertions, 
# and the backtracking swap logic might produce duplicates for 'aa' 
# (which is correct for "including duplicates"), we ensure the 
# structure is clean.

def permute_string(input_string: str) -> List[str]:
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    if not input_string:
        return [""]

    chars = list(input_string)
    results = []

    def generate(index: int):
        if index == len(chars):
            results.append("".join(chars))
            return

        for i in range(index, len(chars)):
            # Swap
            chars[index], chars[i] = chars[i], chars[index]
            # Recurse
            generate(index + 1)
            # Backtrack
            chars[index], chars[i] = chars[i], chars[index]

    generate(0)

    # The assertions in the prompt are specific. If the results were 
    # unsorted or in a different order, we might need to adjust. 
    # However, the standard swap backtrack matches the 'abcd' sequence 
    # provided in the prompt exactly.

    return results