def sort_counter(counter):
    # Validate the input
    if not isinstance(counter, dict):
        raise ValueError("The input must be a dictionary.")

    # Check that all values are numeric
    for value in counter.values():
        if not isinstance(value, (int, float)):
            raise ValueError("All values in the counter must be numeric.")

    # Convert the dictionary items into a list of tuples
    items = list(counter.items())

    # Sort the list of tuples by value in descending order
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    # Return the sorted list
    return sorted_items

# Example usage and assertions
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)], "Basic test case failed."
assert sort_counter({'Math':400, 'Physics':300, 'Chemistry':250}) == [('Math', 400), ('Physics', 300), ('Chemistry', 250)], "Basic test case with descending values failed."
assert sort_counter({'Math':900, 'Physics':1000, 'Chemistry':1250}) == [('Chemistry', 1250), ('Physics', 1000), ('Math', 900)], "Basic test case with ascending values failed."

# Edge cases
# Empty input
try:
    sort_counter({})
except ValueError:
    print("Correctly handled empty input.")

# Single element
try:
    sort_counter({'Math': 80})
except ValueError:
    print("Correctly handled single element input.")

# All elements equal
try:
    sort_counter({'Math': 80, 'Physics': 80, 'Chemistry': 80})
except ValueError:
    print("Correctly handled all-equal elements case.")

# Zero and negative values
try:
    sort_counter({'Math': -100, 'Physics': -50, 'Chemistry': 0})
except ValueError:
    print("Correctly handled zero and negative values.")

# Degenerate case
try:
    sort_counter({'Math': 0, 'Physics': 100, 'Chemistry': 50})
except ValueError:
    print("Correctly handled degenerate case.")