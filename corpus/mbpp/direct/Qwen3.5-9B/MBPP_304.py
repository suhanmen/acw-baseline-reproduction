def find_Element(arr, ops, start_idx, rotations):
    current = start_idx
    for op in ops:
        left, right = op
        size = right - left
        if start_idx >= left:
            current = (start_idx - left)
        else:
            current = size + (start_idx - left)
        current = (current + rotations) % size
        start_idx = left + current
    return arr[start_idx]