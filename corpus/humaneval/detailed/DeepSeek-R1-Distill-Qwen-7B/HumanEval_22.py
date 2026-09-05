from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values: A list containing elements of any type.

    Returns:
        A list containing only the integer elements from the input list.

    Raises:
        ValueError: If the input is not a list.
    """
    if not isinstance(values, list):
        raise ValueError("Input must be a list.")

    def is_integer(x: Any) -> bool:
        """Check if the given value is an integer, excluding boolean values."""
        if isinstance(x, bool):
            return False
        return isinstance(x, int)

    integers = []
    for value in values:
        if is_integer(value):
            integers.append(value)

    return integers

# Example usage
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
    print(filter_integers([True, False, 0]))  # Output: []
    print(filter_integers([1.0, -2, '3']))  # Output: [-2]
    print(filter_integers(['True', 3, '4', 5]))  # Output: [3,5]
    print(filter_integers(None))  # Raises ValueError