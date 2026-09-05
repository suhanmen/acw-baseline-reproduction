def list_to_float(lst):
    converted = []
    for elem in lst:
        try:
            # Convert each element in the tuple to a float
            elem = [float(e) for e in elem]
            converted.append(elem)
        except ValueError:
            # If conversion fails, leave the tuple as is
            converted.append(elem)
    return converted