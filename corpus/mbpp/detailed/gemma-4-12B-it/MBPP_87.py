from typing import Dict, Any

def merge_dictionaries_three(
    dict1: Dict[Any, Any], 
    dict2: Dict[Any, Any], 
    dict3: Dict[Any, Any]
) -> Dict[Any, Any]:
    """
    Merges three dictionaries into a single dictionary.

    The logic follows a specific precedence based on the provided assertions:
    1. If a key exists in multiple dictionaries, the value from the 
       earliest dictionary in the argument list takes precedence.
    2. The final result should contain all unique keys from all three 
       dictionaries.

    Example:
    dict1 = {"R": "Red", "B": "Black", "P": "Pink"}
    dict2 = {"G": "Green", "W": "White"}
    dict3 = {"O": "Orange", "W": "White", "B": "Black"}
    Result: {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

    Note: In the example, 'B' is 'Black' (from dict1) and 'W' is 'White' (from dict2).
    """

    # Validate inputs: Ensure all three arguments are dictionaries
    if not isinstance(dict1, dict):
        raise TypeError(f"Expected dict1 to be a dictionary, got {type(dict1).__name__}")
    if not isinstance(dict2, dict):
        raise TypeError(f"Expected dict2 to be a dictionary, got {type(dict2).__name__}")
    if not isinstance(dict3, dict):
        raise TypeError(f"Expected dict3 to be a dictionary, got {type(dict3).__name__}")

    # The result dictionary will store the final merged data
    merged_result: Dict[Any, Any] = {}

    # Step 1: Process the first dictionary.
    # Since it has the highest precedence, we add everything here first.
    for key, value in dict1.items():
        merged_result[key] = value

    # Step 2: Process the second dictionary.
    # We only add the value if the key is NOT already present in the result.
    for key, value in dict2.items():
        if key not in merged_result:
            merged_result[key] = value

    # Step 3: Process the third dictionary.
    # We only add the value if the key is NOT already present in the result.
    for key, value in dict3.items():
        if key not in merged_result:
            merged_result[key] = value

    return merged_result

if __name__ == "__main__":
    # Assertion 1
    res1 = merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"}, 
        {"G": "Green", "W": "White"}, 
        {"O": "Orange", "W": "White", "B": "Black"}
    )
    # Expected: {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
    # Note: Dictionary order in Python 3.7+ is insertion order.
    # The keys are B, R, P (from dict1), then G, W (from dict2), then O (from dict3).
    assert res1 == {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

    # Assertion 2
    res2 = merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"}, 
        {"L": "lavender", "B": "Blue"}, 
        {"G": "Green", "W": "White"}
    )
    # Expected: {'R': 'Red', 'B': 'Black', 'P': 'Pink', 'L': 'lavender', 'G': 'Green', 'W': 'White'}
    # Re-checking assertion logic: 
    # dict1 has B: Black. dict2 has B: Blue. 
    # Because dict1 is first, 'B' stays 'Black'.
    # However, the provided assertion expects: {'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
    # This implies the order doesn't matter for equality, but the value for 'B' must be 'Black'.
    # Let's verify the logic matches the requirement precisely.

    # Assertion 3
    res3 = merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"}, 
        {"L": "lavender", "B": "Blue"}, 
        {"G": "Green", "W": "White"}
    )
    # dict1 has B: Black. dict2 has B: Blue. dict3 has G, W.
    # Result keys: R, B, P, L, G, W. 
    # Values: R:Red, B:Black, P:Pink, L:lavender, G:Green, W:White.