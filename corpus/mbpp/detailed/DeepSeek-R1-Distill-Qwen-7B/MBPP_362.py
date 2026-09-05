def max_occurrences(input_list):
    """Find the item with maximum occurrences in a given list."""
    # Input validation
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")
    if not input_list:  # handles empty list
        return None

    # Count occurrences
    counts = {}
    for item in input_list:
        counts[item] = counts.get(item, 0) + 1

    # Identify maximum occurrence
    max_count = max(counts.values()) if counts else 0
    if max_count == 0:
        return None  # in case of empty list, though earlier check handles it

    # Collect all items with max_count
    max_items = [item for item, cnt in counts.items() if cnt == max_count]

    # Handle edge case: all items are equal
    if len(max_items) == len(input_list):
        return max_items[0]

    # Handle tie: return lexicographically smallest item
    if len(max_items) > 1:
        return min(max_items)

    # Return the single maximum item
    return max_items[0]