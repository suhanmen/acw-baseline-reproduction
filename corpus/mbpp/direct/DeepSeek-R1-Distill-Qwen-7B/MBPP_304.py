def find(Element, Rotations, index, rotation):
    # Convert the given element to the correct type (list)
    arr = list(Element)
    n = len(arr)

    for rot in Rotations:
        start, direction = rot
        if direction == 1:
            # Clockwise rotation
            length = start
            # Calculate the effective rotation length
            if length < 0:
                length += n
            if length == 0:
                continue
            # Rotate the segment from start to end
            # The new array after rotation
            temp = arr[start:] + arr[:start]
            arr = temp
        else:
            # Counter-clockwise rotation
            length = -start
            # Calculate the effective rotation length
            if length < 0:
                length += n
            if length == 0:
                continue
            # Rotate the segment from start to end
            # The new array after rotation
            temp = arr[start:] + arr[:start]
            arr = temp

    return arr[index]