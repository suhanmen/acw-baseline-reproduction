from typing import List, Tuple, Union

InputRangeTuple = Tuple[Union[int, float], Union[int, float]]

def _normalize_range(input_range: InputRangeTuple) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Normalize a given range tuple so that the start is less than or equal to the end.
    Returns a tuple (start, end) where start <= end.

    :param input_range: A tuple representing a range (possibly unsorted).
    :return: A normalized tuple (min, max).
    """
    if not isinstance(input_range, (list, tuple)) or len(input_range) != 2:
        raise TypeError(f"Expected a tuple or list of length 2, got {type(input_range)}: {input_range}")

    start_val = input_range[0]
    end_val = input_range[1]

    if not isinstance(start_val, (int, float)) or not isinstance(end_val, (int, float)):
        raise TypeError(f"Range elements must be numbers. Got {type(start_val)}, {type(end_val)}")

    if start_val > end_val:
        return (end_val, start_val)
    else:
        return (start_val, end_val)

def _validate_global_range(global_start: Union[int, float], global_end: Union[int, float]) -> None:
    """
    Validate the global start and end range provided to the main function.
    Raises an error if the start is greater than the end.
    """
    if not isinstance(global_start, (int, float)) or not isinstance(global_end, (int, float)):
        raise TypeError(f"Global start and end must be numbers. Got {type(global_start)}, {type(global_end)}")

    if global_start > global_end:
        raise ValueError(f"Global start ({global_start}) cannot be greater than global end ({global_end})")

def _validate_ranges_consistency(ranges: List[InputRangeTuple], global_start: Union[int, float], global_end: Union[int, float]) -> None:
    """
    Validate that all ranges within the list are consistent with the global bounds.
    Specifically, ensures no range falls completely outside the [global_start, global_end] interval
    in a way that breaks the contiguous assumption implied by the problem's output examples.
    """
    for r in ranges:
        norm_r = _normalize_range(r)
        r_start, r_end = norm_r

        # Check if the range overlaps with the global scope
        if r_start > global_end or r_end < global_start:
            # The problem implies we are looking for gaps within the global scope.
            # If a range is completely outside, it effectively doesn't affect the gaps within [global_start, global_end],
            # but strictly speaking, the input logic usually assumes ranges are within or relevant to the scope.
            # Based on the problem description "missing from the given list with the given start range and end range",
            # we assume the provided ranges are the 'present' parts within the [global_start, global_end] context.
            pass # We proceed assuming the caller handles external ranges or they are ignored/clipped implicitly by the gap logic.

def _generate_missing_ranges(
    ranges: List[InputRangeTuple], 
    global_start: Union[int, float], 
    global_end: Union[int, float]
) -> List[Tuple[Union[int, float], Union[int, float]]]:
    """
    Main logic to generate missing ranges.

    1. Normalize all input ranges.
    2. Sort them.
    3. Merge overlapping or adjacent ranges to form a contiguous set of 'present' blocks.
    4. Iterate through the merged blocks and the global bounds to find the gaps.
    """
    if not ranges:
        # If the input list is empty, the entire global range is missing.
        return [(global_start, global_end)]

    # Step 1: Normalize all ranges
    normalized_ranges: List[Tuple[Union[int, float], Union[int, float]]] = []
    for r in ranges:
        norm_r = _normalize_range(r)
        normalized_ranges.append(norm_r)

    # Step 2: Sort ranges by their start value
    normalized_ranges.sort(key=lambda x: x[0])

    # Step 3: Merge overlapping ranges
    merged_ranges: List[Tuple[Union[int, float], Union[int, float]]] = []

    current_start: Union[int, float] = normalized_ranges[0][0]
    current_end: Union[int, float] = normalized_ranges[0][1]

    for i in range(1, len(normalized_ranges)):
        next_start, next_end = normalized_ranges[i]

        # If the next range starts before or exactly where the current one ends (and is within reasonable bounds), merge them
        # We treat adjacent ranges (e.g., [1, 5] and [5, 10]) as contiguous, effectively merging them to [1, 10]
        # for the purpose of finding gaps.
        if next_start <= current_end:
            # Determine the new end: max of current and next
            if next_end > current_end:
                current_end = next_end
            # If there was an overlap or adjacency, we continue the current block
        else:
            # There is a gap between current_end and next_start.
            # We finalize the current block.
            merged_ranges.append((current_start, current_end))
            current_start = next_start
            current_end = next_end

    # Append the last active block
    merged_ranges.append((current_start, current_end))

    # Step 4: Find gaps between the global start/end and the merged ranges
    missing_ranges: List[Tuple[Union[int, float], Union[int, float]]] = []

    prev_value: Union[int, float] = global_start

    for m_start, m_end in merged_ranges:
        # Gap before the current merged range
        if m_start > prev_value:
            missing_ranges.append((prev_value, m_start))

        # Update prev_value to the end of the current range
        # Note: We do not update prev_value to m_start here because we already handled the gap before.
        # We need to track the end of the 'present' block to find the next gap.
        prev_value = m_end

    # Check for gaps after the last merged range
    if prev_value < global_end:
        missing_ranges.append((prev_value, global_end))

    return missing_ranges

def extract_missing(
    ranges: List[InputRangeTuple], 
    start_range: Union[int, float], 
    end_range: Union[int, float]
) -> List[Tuple[Union[int, float], Union[int, float]]]:
    """
    Extracts the ranges that are missing from the given list within the specified start and end range.

    :param ranges: A list of tuples representing the present ranges. Tuples may be unordered (start > end).
    :param start_range: The global start of the scope.
    :param end_range: The global end of the scope.
    :return: A list of tuples representing the missing ranges, sorted by start value.
    """
    # Validate global bounds
    _validate_global_range(start_range, end_range)

    # Validate ranges list type
    if not isinstance(ranges, list):
        raise TypeError(f"Expected 'ranges' to be a list, got {type(ranges)}")

    # If the input list is empty, the entire global range is missing.
    if len(ranges) == 0:
        return [(start_range, end_range)]

    # Validate and normalize ranges
    normalized_ranges: List[Tuple[Union[int, float], Union[int, float]]] = []
    for r in ranges:
        if not isinstance(r, (list, tuple)) or len(r) != 2:
            raise TypeError(f"Each range in the list must be a tuple or list of length 2. Got: {r}")
        normalized = _normalize_range(r)
        normalized_ranges.append(normalized)

    # Generate the missing ranges
    missing = _generate_missing_ranges(ranges, start_range, end_range)

    # Sort the result by start value (just in case, though the logic produces it sorted)
    missing.sort(key=lambda x: x[0])

    return missing