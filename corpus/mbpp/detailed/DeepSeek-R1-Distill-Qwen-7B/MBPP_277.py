def dict_filter(data, threshold):
    """
    Filter a dictionary based on its values.

    Args:
        data (dict): The input dictionary to filter.
        threshold (int/float): The minimum value a key-value pair must meet.

    Returns:
        dict: A new dictionary containing only the key-value pairs where value >= threshold.
    """
    # Validate inputs
    if not isinstance(data, dict):
        raise ValueError("Invalid data type for data. Expected a dictionary.")
    if not isinstance(threshold, (int, float)):
        raise ValueError("Invalid type for threshold. Expected int or float.")

    # Helper function to check if a value meets the threshold
    def value_meets(v):
        return v >= threshold

    # Create an empty dictionary to store the filtered items
    filtered = {}

    # Iterate through the dictionary items
    for key, value in data.items():
        # Include the key-value pair if it meets the threshold
        if value_meets(value):
            filtered[key] = value

    # Return the filtered dictionary
    return filtered

# Example usage and test cases
def main():
    test_data = {
        'Cierra Vega': 175,
        'Alden Cantrell': 180,
        'Kierra Gentry': 165,
        'Pierre Cox': 190
    }

    # Test case 1: threshold = 170
    result1 = dict_filter(test_data, 170)
    print("Test case 1:", result1)
    assert result1 == {
        'Cierra Vega': 175,
        'Alden Cantrell': 180,
        'Pierre Cox': 190
    }

    # Test case 2: threshold = 180
    result2 = dict_filter(test_data, 180)
    print("Test case 2:", result2)
    assert result2 == {
        'Alden Cantrell': 180,
        'Pierre Cox': 190
    }

    # Test case 3: threshold = 190
    result3 = dict_filter(test_data, 190)
    print("Test case 3:", result3)
    assert result3 == {
        'Pierre Cox': 190
    }

if __name__ == "__main__":
    main()