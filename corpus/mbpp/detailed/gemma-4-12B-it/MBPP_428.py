from typing import List

def shell_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the Shell Sort algorithm.

    Shell sort is an improvement over insertion sort. It allows the 
    exchange of items that are far apart by using a sequence of gaps. 
    As the gap reduces to 1, it becomes a standard insertion sort, 
    but the array is already "nearly sorted," making it much faster.

    Args:
        arr (List[int]): A list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """

    # --- Input Validation ---
    if not isinstance(arr, list):
        raise TypeError(f"Input must be a list, got {type(arr).__name__}")

    # Ensure all elements are integers
    for element in arr:
        if not isinstance(element, int):
            raise TypeError(f"All elements in the list must be integers, found {type(element).__name__}")

    # Handle edge cases: empty list or single-element list
    if len(arr) <= 1:
        return list(arr)  # Return a copy to ensure original isn't mutated if not intended

    # Create a copy to avoid mutating the original input list (defensive programming)
    sorted_arr = list(arr)
    n = len(sorted_arr)

    # --- Shell Sort Implementation ---

    # We use the Shell sequence (n/2, n/4, ..., 1). 
    # While other sequences exist (like Knuth's), this is the standard definition.
    gap = n // 2

    while gap > 0:
        # Perform a "gapped" insertion sort for this gap size.
        # The elements at positions i, i-gap, i-2gap... are sorted relative to each other.
        for i in range(gap, n):
            # current_value is the element we are trying to place in the sorted sub-sequence
            current_value = sorted_arr[i]

            # j represents the index we are comparing against in the previous positions
            j = i

            # Standard insertion sort logic, but jumping by the gap size
            # Shift elements to the right if they are larger than current_value
            while j >= gap and sorted_arr[j - gap] > current_value:
                sorted_arr[j] = sorted_arr[j - gap]
                j = j - gap

            # Place the current_value in its correct position relative to the gap
            sorted_arr[j] = current_value

        # Reduce the gap for the next pass
        gap = gap // 2

    return sorted_arr

if __name__ == "__main__":
    # These assertions verify the requirements provided in the prompt.
    assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
    assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]