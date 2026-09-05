def merge_dictionaries_three(d1, d2, d3):
    """
    Merges three dictionaries into a single result dictionary. If there are conflicting
    keys, the value from the first dictionary with the conflicting key takes precedence.

    Args:
        d1, d2, d3: dictionaries to be merged.

    Returns:
        A merged dictionary with all key-value pairs. If a key exists in multiple dictionaries,
        the value from the first dictionary (d1, then d2, then d3) with that key is used.

    Raises:
        TypeError: If any of the inputs are not dictionaries.
    """
    # Validate that all inputs are dictionaries
    if not (isinstance(d1, dict) and isinstance(d2, dict) and isinstance(d3, dict)):
        raise TypeError("All inputs must be of type dict.")

    # Create a copy of the first dictionary to build the result
    merged = dict(d1)

    # Merge the second dictionary into the copy; if keys conflict, d2's values take precedence
    for key, value in d2.items():
        merged[key] = value

    # Merge the third dictionary into the copy; if keys conflict, d3's values take precedence
    for key, value in d3.items():
        merged[key] = value

    return merged

# Example usage and assertions
def check_assertions():
    # Example 1
    result = merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"},
        {"G": "Green", "W": "White"},
        {"O": "Orange", "W": "White", "B": "Black"}
    )
    assert result == {
        'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 
        'W': 'White', 'O': 'Orange'
    }, "Example 1 failed"

    # Example 2
    result = merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"},
        {"G": "Green", "W": "White"},
        {"L": "lavender", "B": "Blue"}
    )
    assert result == {
        'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 
        'G': 'Green', 'L': 'lavender'
    }, "Example 2 failed"

    # Example 3
    result = merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"},
        {"L": "lavender", "B": "Blue"},
        {"G": "Green", "W": "White"}
    )
    assert result == {
        'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 
        'L': 'lavender', 'W': 'White'
    }, "Example 3 failed"

    print("All assertions passed")

# Run the check function to verify the correctness of the implementation
check_assertions()