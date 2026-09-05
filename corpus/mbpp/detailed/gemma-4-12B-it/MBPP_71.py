from typing import List, Any

def comb_sort(elements: List[Any]) -> List[Any]:
    """
    Sorts a list of elements using the Comb Sort algorithm.

    Comb sort is an improvement over Bubble Sort. It eliminates "turtles" 
    (small values at the end of the list) by using a gap that shrinks 
    in each iteration until it reaches 1.

    Args:
        elements (List[Any]): A list of comparable elements.

    Returns:
        List[Any]: A new list containing the sorted elements.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input contains incomparable types.
    """
    # --- Input Validation ---
    if not isinstance(elements, list):
        raise TypeError(f"Input must be a list, but received {type(elements).__name__}")

    # Create a copy to avoid mutating the input list (standard defensive practice)
    arr = list(elements)
    list_length = len(arr)

    # Handle edge cases: empty list or single element
    if list_length <= 1:
        return arr

    # --- Comb Sort Parameters ---
    # The shrink factor is a constant; 1.3 is the standard value
    shrink_factor = 1.3
    # Initialize the gap as the length of the list
    current_gap = list_length
    # The sorted flag ensures we keep passing over the list until no swaps occur
    # when the gap is 1 (which is essentially a Bubble Sort pass)
    is_sorted = False

    # --- Main Sorting Loop ---
    while not is_sorted:
        # Update the gap
        current_gap = int(current_gap / shrink_factor)

        # If the gap becomes less than 1, set it to 1
        if current_gap < 1:
            current_gap = 1

        # If the gap is 1, we assume the list is unsorted until a full 
        # pass completes without any swaps.
        if current_gap == 1:
            is_sorted = True

        # Perform the "comb" pass
        # We iterate through the list and compare elements at the gap distance
        for i in range(list_length - current_gap):
            try:
                left_element = arr[i]
                right_element = arr[i + current_gap]

                # If the element on the left is greater than the one on the right, swap them
                if left_element > right_element:
                    arr[i], arr[i + current_gap] = arr[i + current_gap], arr[i]

                    # If we performed a swap and the gap is 1, 
                    # we cannot be sure the list is sorted yet.
                    if current_gap == 1:
                        is_sorted = False

            except TypeError as exc:
                raise ValueError(
                    "List contains incomparable types. "
                    "Ensure all elements are of comparable types."
                ) from exc

    return arr

if __name__ == "__main__":
    # Validation based on requirements
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]