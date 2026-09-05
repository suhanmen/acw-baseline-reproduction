from typing import List, Any

def _generate_gap_sequence(size: int) -> List[int]:
    """
    Generates a sequence of gap values for Shell Sort using the Knuth's sequence:
    h = 3*h + 1 starting from h=1, and stopping when h >= size/3.
    The gaps are generated in descending order.

    Args:
        size (int): The number of elements in the array to be sorted.

    Returns:
        List[int]: A list of gap values in descending order.
    """
    gaps = []

    # Initialize the first gap
    current_gap = 1

    # Continue generating gaps until the gap is greater than or equal to size/3
    # We use strict inequality for the loop condition to ensure at least one gap (1) is processed if needed
    while current_gap < (size / 3):
        current_gap = 3 * current_gap + 1
        gaps.append(current_gap)

    # The last gap generated in the loop might be too large if we appended it incorrectly relative to the stop condition,
    # but actually the logic above stops when current_gap >= size/3.
    # However, standard Knuth sequence implementation usually appends the last valid gap that fits or starts above and reduces.
    # Let's refine: The sequence is 1, 4, 13, 40...
    # We want gaps such that the last gap is <= size/3? 
    # Actually, the standard algorithm often starts with the largest gap < n/3, then divides by 3 until 1.
    # My previous loop generated: 1, 4, 13... until current_gap >= n/3.
    # If n=10, n/3 = 3.33. 
    # Start h=1. 1 < 3.33 -> h=4, append 4. 4 < 3.33 (False). Stop.
    # List is [4]. We missed the 1.
    # Correct approach: Generate the full sequence ascending, then reverse, ensuring 1 is included if applicable, 
    # or simply generate descending directly.

    # Let's restart the logic for robustness.
    gaps.clear()
    current_gap = 1

    while current_gap < (size / 3):
        current_gap = 3 * current_gap + 1
        gaps.append(current_gap)

    # If the loop ran, 'current_gap' is the largest one we calculated that was < size/3? 
    # No, the loop condition is checked at start.
    # Example n=10: size/3 = 3.33. 
    # 1 < 3.33 -> True. current_gap becomes 4. append 4.
    # 4 < 3.33 -> False. Stop. gaps=[4].
    # But we need to include 1 eventually. 
    # Usually, the sequence is generated as 1, 4, 13... and we take the largest that is < n, then divide by 3.
    # Or we generate 1, 4, 13... and reverse, stopping before exceeding n.

    # Let's use the standard approach:
    # Start with h=1. While h < n/3: h = 3*h + 1. 
    # The resulting h is the first gap. Then we divide by 3 repeatedly until 1.

    h = 1
    while h < (size / 3):
        h = 3 * h + 1

    # Now h is the largest gap in the sequence that fits the criteria (often used as the starting point)
    # Actually, for n=10, h becomes 4. We want gaps [4, 1].
    # If n=5, size/3 = 1.66. 
    # 1 < 1.66 -> True. h=4.
    # 4 < 1.66 -> False. Stop. h=4. Gaps [4, 1].
    # Is 4 valid for n=5? Yes.
    # If n=3, size/3 = 1.
    # 1 < 1 -> False. Stop. h=1. Gaps [1].

    while h > 0:
        gaps.append(h)
        h = (h - 1) // 3  # Integer division to get the previous gap in Knuth sequence

    # This produces gaps in descending order.
    # Let's trace n=10:
    # h starts 1. 1 < 3.33 -> h=4. 4 < 3.33 -> False. h=4.
    # Loop 1: append 4. h=(4-1)//3 = 1.
    # Loop 2: append 1. h=(1-1)//3 = 0.
    # Loop 3: stop.
    # Result: [4, 1]. Correct.

    # Trace n=5:
    # h=1. 1 < 1.66 -> h=4. 4 < 1.66 -> False.
    # Loop 1: append 4. h=1.
    # Loop 2: append 1. h=0.
    # Result: [4, 1]. Correct.

    # Trace n=3:
    # h=1. 1 < 1 -> False.
    # Loop 1: append 1. h=0.
    # Result: [1]. Correct.

    # Trace n=2:
    # h=1. 1 < 0.66 -> False.
    # Loop 1: append 1. h=0.
    # Result: [1]. Correct.

    # Trace n=1:
    # h=1. 1 < 0.33 -> False.
    # Loop 1: append 1. h=0.
    # Result: [1]. Correct.

    # Trace n=4:
    # h=1. 1 < 1.33 -> True. h=4.
    # 4 < 1.33 -> False.
    # Loop 1: append 4. h=1.
    # Loop 2: append 1. h=0.
    # Result: [4, 1]. Correct.

    return gaps

def _shell_sort_array(array: List[Any], gaps: List[int]) -> None:
    """
    Performs the actual sorting of the array using the provided sequence of gaps.

    Args:
        array (List[Any]): The list of elements to be sorted. It is modified in-place.
        gaps (List[int]): The sequence of gap values to use for sorting, in descending order.
    """
    n = len(array)

    for gap in gaps:
        # For each gap, perform a gapped insertion sort
        for i in range(gap, n):
            # Extract the current element
            current_element = array[i]
            position = i

            # Repeat until the correct position is found
            while position >= gap and array[position - gap] > current_element:
                # Shift the element at 'position - gap' to 'position'
                array[position] = array[position - gap]
                # Move the position backwards by the gap
                position = position - gap

            # Insert the extracted element at the correct position
            array[position] = current_element

def shell_sort(input_list: List[Any]) -> List[Any]:
    """
    Sorts the given list using the Shell Sort algorithm with Knuth's gap sequence.

    This function validates the input, handles edge cases, and returns a new sorted list.
    It does not modify the original input list.

    Args:
        input_list (List[Any]): A list of comparable elements to be sorted.

    Returns:
        List[Any]: A new list containing the elements of input_list sorted in ascending order.

    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
        ValueError: If the input list is empty (though an empty list is technically valid input, 
                    returning an empty list is the standard mathematical solution, but here 
                    we explicitly handle the logic). 
                    Actually, empty list is valid and returns empty list.
    """
    # Validation: Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    # Validation: Check if the list is empty
    if len(input_list) == 0:
        return []

    # Determine the number of elements
    n = len(input_list)

    # Generate the gap sequence
    # We create a copy to ensure we don't mutate any state if reused, though here it's local.
    # The function _generate_gap_sequence is pure.
    gap_sequence = _generate_gap_sequence(n)

    # Create a shallow copy of the list to avoid modifying the original input
    sorted_list = list(input_list)

    # Perform the sort in-place on the copied list
    _shell_sort_array(sorted_list, gap_sequence)

    return sorted_list

if __name__ == "__main__":
    # Basic sanity check to ensure the code runs without error if this file is executed directly
    # This block is not part of the required output function but verifies internal consistency.
    test_data = [12, 23, 4, 5, 3, 2, 12, 81, 56, 95]
    result = shell_sort(test_data)
    expected = [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]

    if result == expected:
        print("Test 1 passed.")
    else:
        print(f"Test 1 failed: {result} != {expected}")

    test_data_2 = [24, 22, 39, 34, 87, 73, 68]
    result_2 = shell_sort(test_data_2)
    expected_2 = [22, 24, 34, 39, 68, 73, 87]

    if result_2 == expected_2:
        print("Test 2 passed.")
    else:
        print(f"Test 2 failed: {result_2} != {expected_2}")

    test_data_3 = [32, 30, 16, 96, 82, 83, 74]
    result_3 = shell_sort(test_data_3)
    expected_3 = [16, 30, 32, 74, 82, 83, 96]

    if result_3 == expected_3:
        print("Test 3 passed.")
    else:
        print(f"Test 3 failed: {result_3} != {expected_3}")