from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix."""
    result = []
    if not prefix:
        return strings.copy()  # Return a copy to avoid modifying the original list
    for s in strings:
        if s.startswith(prefix):
            result.append(s)
    return result

# Example usage:
if __name__ == "__main__":
    # Test case 1: Empty input list
    print(filter_by_prefix([], 'a'))  # Output: []

    # Test case 2: Some strings match the prefix
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']

    # Test case 3: All strings match the prefix
    print(filter_by_prefix(['a', 'aa', 'aaa'], 'a'))  # Output: ['a', 'aa', 'aaa']

    # Test case 4: No strings match the prefix
    print(filter_by_prefix(['bcd', 'cde'], 'a'))  # Output: []

    # Test case 5: Empty prefix
    print(filter_by_prefix(['a', 'b', 'c'], ''))  # Output: ['a', 'b', 'c']

    # Test case 6: Case-sensitive matching
    print(filter_by_prefix(['Apple', 'Banana', 'Cherry'], 'apple'))  # Output: []