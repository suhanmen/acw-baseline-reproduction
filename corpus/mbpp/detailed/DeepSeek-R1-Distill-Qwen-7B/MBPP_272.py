def rear_extract(records):
    # Check if the input is a list
    if not isinstance(records, list):
        raise ValueError("Input must be a list of tuples")

    result = []

    for record in records:
        # Check if each record is a tuple and has exactly two elements
        if not isinstance(record, tuple) or len(record) != 2:
            raise ValueError(f"Invalid record format: {record}")

        # Extract the second element (index 1) from each tuple
        result.append(record[1])

    return result