def extract_missing(ranges, start, end):
    # Input validation
    if not ranges or start > end:
        return []

    missing = []
    prev_end = start

    # Process each range
    for current_start, current_end in ranges:
        # Check if there's a gap between prev_end and current_start
        if current_start > prev_end:
            missing.append((prev_end, current_start))
        # Update prev_end to max(current_end, prev_end)
        prev_end = max(prev_end, current_end)

    # Check the gap after the last range
    if prev_end < end:
        missing.append((prev_end, end))

    return missing