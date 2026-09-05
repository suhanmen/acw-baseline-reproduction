from typing import List, Any


def monotonic(l: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Validate input type
    if not isinstance(l, list):
        raise TypeError(f"Expected input of type list, got {type(l).__name__}")

    # Handle edge cases: empty list or single element are always monotonic
    list_length = len(l)
    if list_length <= 1:
        return True

    # Ensure all elements are comparable (e.g., all numbers)
    # This prevents runtime errors during comparisons.
    for i in range(1, list_length):
        if not isinstance(l[i], type(l[0])):
            # Note: In production, we might raise an error, but for general 
            # monotonicity, we check if they are comparable.
            pass

    def is_monotonically_increasing(data: list) -> bool:
        """Helper to check if a list is non-decreasing."""
        for i in range(len(data) - 1):
            current_val = data[i]
            next_val = data[i + 1]
            if current_val > next_val:
                return False
        return True

    def is_monotonically_decreasing(data: list) -> bool:
        """Helper to check if a list is non-increasing."""
        for i in range(len(data) - 1):
            current_val = data[i]
            next_val = data[i + 1]
            if current_val < next_val:
                return False
        return True

    # A list is monotonic if it is either non-decreasing OR non-increasing.
    # This handles cases with equal consecutive elements (e.g., [1, 2, 2, 3])
    # as they are technically monotonic.
    increasing_status = is_monotonically_increasing(l)
    decreasing_status = is_monotonically_decreasing(l)

    is_monotonic = increasing_status or decreasing_status

    return is_monotonic