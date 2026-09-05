def permute_string(s):
    """
    Print all permutations of a given string including duplicates.

    This function handles edge cases explicitly and uses recursive backtracking
    to generate all unique permutations. The approach ensures that even if the
    input string has duplicate characters, all possible permutations are
    considered.

    Args:
        s: A string for which to generate all permutations.

    Returns:
        A list of all possible permutations of the input string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Base case: empty string
    if not s:
        return [""]

    # Helper function to perform backtracking
    def backtrack(path, characters):
        """
        Perform backtracking to generate all permutations.

        Args:
            path: The current permutation being built.
            characters: List of remaining characters to permute.

        Returns:
            List of all permutations generated from the current state.
        """
        if not characters:
            # Add the complete permutation to the result
            result.append(path)
            return

        for i in range(len(characters)):
            # Choose the ith character
            char = characters[i]
            # Add it to the current path
            new_path = path + char
            # Remove it from the characters list
            new_characters = characters[:i] + characters[i+1:]
            # Recurse with the new state
            backtrack(new_path, new_characters)

    # Convert string to list of characters for manipulation
    characters = list(s)
    result = []

    # Start backtracking with an empty path and all characters available
    backtrack("", characters)

    return result

# Example usage
if __name__ == "__main__":
    # Test cases
    print(permute_string('ab'))          # Output: ['ab', 'ba']
    print(permute_string('abc'))         # Output: ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    print(permute_string('abcd'))        # Output: 24 permutations of 'abcd'