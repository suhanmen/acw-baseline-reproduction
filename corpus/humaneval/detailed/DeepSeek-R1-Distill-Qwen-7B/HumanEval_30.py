def get_positive(l: list):
    """Return only positive numbers in the list."""
    def filter_positives(numbers):
        """Helper function to filter out non-positive numbers."""
        return [num for num in numbers if num > 0]

    if not isinstance(l, list):
        raise ValueError("Input must be a list.")

    positives = filter_positives(l)

    return positives

# Example usage
if __name__ == "__main__":
    test_cases = [
        [-1, 2, -4, 5, 6],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    ]
    print("Test 1:", get_positive(test_cases[0]))  # Output: [2, 5, 6]
    print("Test 2:", get_positive(test_cases[1]))  # Output: [5, 3, 2, 3, 9, 123, 1]