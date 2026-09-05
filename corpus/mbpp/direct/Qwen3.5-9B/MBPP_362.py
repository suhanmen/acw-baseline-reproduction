from collections import Counter
from typing import List, Any, Union

def max_occurrences(lst: List[Any]) -> Union[Any, List[Any]]:
    if not lst:
        raise ValueError("Input list cannot be empty.")

    counts = Counter(lst)
    max_count = max(counts.values())

    max_items = [item for item, count in counts.items() if count == max_count]

    if len(max_items) == 1:
        return max_items[0]
    else:
        return max_items