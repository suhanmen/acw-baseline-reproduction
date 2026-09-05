from typing import List, Tuple, Union, Optional

Entry = Tuple[str, int]

def _validate_single_entry(entry: Entry) -> None:
    """
    Validate that a single tuple entry is well-formed.

    Requirements:
    - Must be a tuple with exactly two elements.
    - The first element (key) must be a string.
    - The second element (value) must be an integer.

    Raises:
        TypeError: If the entry is not a tuple, has wrong length, or contains invalid types.
    """
    # Check type of the entry itself
    if not isinstance(entry, tuple):
        raise TypeError(f"Expected a tuple entry, but received: {type(entry).__name__}")

    # Check length of the tuple
    if len(entry) != 2:
        raise TypeError(f"Expected a tuple of length 2, but received a tuple of length: {len(entry)}")

    # Check type of the key (first element)
    key = entry[0]
    if not isinstance(key, str):
        raise TypeError(f"Expected the first element to be a string, but received: {type(key).__name__}")

    # Check type of the value (second element)
    value = entry[1]
    if not isinstance(value, int):
        raise TypeError(f"Expected the second element to be an integer, but received: {type(value).__name__}")

    # Optional defensive check: ensure value is not a boolean (since bool is a subclass of int in Python)
    # While the type check passed, we explicitly exclude booleans to be strict about "integer" data.
    if isinstance(value, bool):
        raise TypeError("Boolean values are not accepted as numeric values.")

def _sum_aggregates(entries: List[Entry]) -> Optional[Tuple[str, int]]:
    """
    Iterate through the list of entries, aggregating scores by name,
    and tracking the maximum aggregate found so far.

    Parameters:
        entries: A list of (name, score) tuples.

    Returns:
        A tuple (name, total_score) representing the person with the highest total score.
        Returns None if the input list is empty.
    """
    # Initialize a dictionary to store the running totals for each name.
    # Using a dictionary is explicit and clear for mapping strings to integers.
    aggregates: dict[str, int] = {}

    # Iterate through each entry explicitly.
    for current_entry in entries:
        name = current_entry[0]
        score = current_entry[1]

        # Check if this name is already in our tracking dictionary.
        if name in aggregates:
            # If yes, add the new score to the existing total.
            new_total = aggregates[name] + score
            aggregates[name] = new_total
        else:
            # If no, initialize the total with the current score.
            aggregates[name] = score

    # Helper to handle the case where no aggregates were found (empty input list).
    if not aggregates:
        return None

    # Identify the key with the maximum value in the aggregates dictionary.
    # We iterate explicitly to find the max rather than relying solely on the max() key lookup
    # to demonstrate the logic clearly, although max() is efficient.
    max_name = None
    max_score = None

    for name, total in aggregates.items():
        if max_name is None:
            max_name = name
            max_score = total
        else:
            # Compare the new total against the current maximum.
            if total > max_score:
                max_name = name
                max_score = total
            # If total == max_score, we keep the first one encountered (stable behavior based on iteration order).
            # If strict greater-than is required to update on ties, change > to >=.
            # Based on standard interpretation of "maximum", keeping the first is acceptable unless specified otherwise.

    return (max_name, max_score)

def max_aggregate(entries: List[Entry]) -> Optional[Entry]:
    """
    Calculate the maximum aggregate from the list of tuples.

    This function aggregates scores for each name across the list and returns
    the tuple (name, total_score) for the name with the highest total.

    Parameters:
        entries (List[Tuple[str, int]]): A list of tuples where each tuple contains
                                        a name (string) and a score (integer).

    Returns:
        Optional[Tuple[str, int]]: A tuple containing the name with the highest 
                                   aggregate score and that total score.
                                   Returns None if the input list is empty.

    Raises:
        TypeError: If the input list is not a list, or if any entry is not a valid
                   tuple of (string, integer).
    """
    # Validate the type of the main input argument.
    if not isinstance(entries, list):
        raise TypeError(f"Expected a list of tuples, but received: {type(entries).__name__}")

    # Validate each entry within the list.
    for idx, entry in enumerate(entries):
        _validate_single_entry(entry)

    # Compute the aggregates.
    result = _sum_aggregates(entries)

    return result

# Main execution block is omitted per instructions to provide ONLY the solution code block.
# The function is defined above and ready for import or usage.