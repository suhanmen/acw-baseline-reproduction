from typing import List, Any, Tuple, Union, Dict
from collections import Counter

def max_occurrences(input_list: List[Any]) -> Union[Any, Tuple[Any, ...]]:
    """
    Finds the item(s) with the maximum occurrences in a given list.

    Returns:
        - A single value if there is one unique item with the maximum count.
        - A tuple of values if there is a tie for the maximum count.
        - None if the input list is empty.
    """
    # Step 1: Validate the input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    # Step 2: Handle the edge case of an empty list
    if len(input_list) == 0:
        return None

    # Step 3: Count the occurrences of each item
    # We use a dictionary to store counts to handle unhashable types if necessary,
    # however, for standard items like ints/strings, Counter is optimal.
    # If items are unhashable (like lists), this logic would need a different approach.
    # Based on the assertions, we assume hashable items.
    counts: Dict[Any, int] = {}
    for item in input_list:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1

    # Step 4: Find the maximum frequency value
    max_frequency: int = 0
    for count in counts.values():
        if count > max_frequency:
            max_frequency = count

    # Step 5: Identify all items that have that maximum frequency
    winners: List[Any] = []
    # We iterate over the original items' keys to maintain a predictable order
    # or simply iterate the keys.
    for item, count in counts.items():
        if count == max_frequency:
            winners.append(item)

    # Step 6: Determine the return format based on the number of winners
    num_winners = len(winners)

    if num_winners == 0:
        # This case should technically not be reachable given the empty list check
        return None

    if num_winners == 1:
        # Return the single winner
        return winners[0]
    else:
        # Return a tuple of winners for ties
        # Note: The order in the tuple depends on the dictionary insertion order (Python 3.7+)
        # To be deterministic, we could sort winners if they are comparable, 
        # but the problem doesn't specify sorting.
        return tuple(winners)

# Verification of assertions provided in the prompt:
# assert max_occurrences([1,2,3,1,2,3,12,4,2]) == 2
# Explanation: 1 appears 3 times, 2 appears 3 times, 3 appears 2 times, 12 appears 1 time, 4 appears 1 time.
# Wait, let's re-check the count: 1: [0,3], 2: [1,4,8], 3: [2,5], 12: [6], 4: [7].
# Wait, count of 1 is 3. Count of 2 is 3. This would return (1, 2).
# Let's re-read the assertion: max_occurrences([1,2,3,1,2,3,12,4,2]) == 2
# My manual count: 1(3), 2(3), 3(2), 12(1), 4(1).
# Actually, the prompt assertion says 2. Let me recount.
# [1, 2, 3, 1, 2, 3, 12, 4, 2]
# 1: index 0, 3 -> count 2
# 2: index 1, 4, 8 -> count 3
# 3: index 2, 5 -> count 2
# 12: index 6 -> count 1
# 4: index 7 -> count 1
# Max count is 3, which belongs to the value '2'. Correct.

# assert max_occurrences([1,2,6,7,0,1,0,1,0]) == 1,0
# 1: index 0, 5, 7 -> count 3
# 2: index 1 -> count 1
# 6: index 2 -> count 1
# 7: index 3 -> count 1
# 0: index 4, 6, 8 -> count 3
# Max count is 3. Values are 1 and 0. Returns (1, 0). Correct.

# assert max_occurrences([1,2,3,1,2,4,1]) == 1
# 1: index 0, 3, 6 -> count 3
# 2: index 1, 4 -> count 2
# 3: index 2 -> count 1
# 4: index 5 -> count 1
# Max count is 3. Value is 1. Returns 1. Correct.