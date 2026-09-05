def comb_sort(lst):
    """
    Sorts a list using the comb sort algorithm.
    """
    if len(lst) <= 1:
        return lst

    gap = len(lst)
    # Start with a large gap to eliminate turtles (small elements near the end)
    while gap > 1:
        gap = max(1, gap // 2)  # Reduce gap by half each iteration

    # Perform the comb sort
    i = 0
    while i < len(lst) - 1:
        # Determine the current gap
        current_gap = gap if gap < len(lst) - i else 1
        # Compare elements and swap them if they are in the wrong order
        while i < len(lst) - current_gap:
            if lst[i] > lst[i + current_gap]:
                lst[i], lst[i + current_gap] = lst[i + current_gap], lst[i]
            i += 1
        gap = max(1, gap // 2)  # Reduce the gap for the next iteration

    return lst

# Example usage and testing
def example_usage():
    test_cases = [
        [5, 15, 37, 25, 79],
        [41, 32, 15, 19, 22],
        [99, 15, 13, 47]
    ]
    for case in test_cases:
        sorted_list = comb_sort(case)
        print(f"Original: {case}, Sorted: {sorted_list}")

if __name__ == "__main__":
    example_usage()