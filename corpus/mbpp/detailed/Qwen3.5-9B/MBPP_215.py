def validate_count(value):
    """
    Validates that the given value can be used as a run-length count.

    A valid count must be:
    - An integer type
    - Greater than or equal to 0

    Returns True if valid, raises a ValueError otherwise.
    """
    if not isinstance(value, int):
        raise ValueError(f"Expected integer count, got {type(value).__name__}")

    if value < 0:
        raise ValueError(f"Expected non-negative count, got {value}")

    return True


def decode_pair(pair):
    """
    Decodes a run-length encoded pair [count, item] into a list.

    This helper takes a two-element list where:
    - The first element is the count (must be valid per validate_count)
    - The second element is the item to repeat

    Returns a list containing the item repeated 'count' times.
    Raises ValueError if the pair structure is invalid or count is invalid.
    """
    if not isinstance(pair, list):
        raise ValueError(f"Expected list for run-length pair, got {type(pair).__name__}")

    if len(pair) != 2:
        raise ValueError(f"Expected pair of length 2, got length {len(pair)}")

    count, item = pair[0], pair[1]

    validate_count(count)

    result_list = []
    for _ in range(count):
        result_list.append(item)

    return result_list


def decode_element(element, current_output):
    """
    Decodes a single element in the input list and appends to current_output.

    If element is a list of length 2: treated as [count, item] pair -> decode_pair
    Else: treated as a single literal item -> append as-is

    Returns the updated current_output list.
    """
    if isinstance(element, list):
        if len(element) == 2:
            decoded_pair = decode_pair(element)
            current_output.extend(decoded_pair)
        else:
            raise ValueError(f"Invalid pair found: {element} (expected length 2)")
    else:
        current_output.append(element)

    return current_output


def decode_list(input_data):
    """
    Decodes a run-length encoded list.

    The input list can contain:
    - Single elements (e.g., 'a', 5, 'x')
    - Pairs [count, item] where count >= 0 and item is any value except a list

    Rules:
    - If element is a list of length 2: [count, item] -> repeat 'item' 'count' times
    - Otherwise: treat as literal single element

    Edge cases handled:
    - Empty input list -> returns empty list
    - Input containing invalid structures -> raises ValueError
    - Input containing nested lists other than valid pairs -> raises ValueError

    Parameters:
        input_data (list): The run-length encoded list to decode

    Returns:
        list: The decoded list

    Raises:
        ValueError: If input contains invalid structures or invalid counts
        TypeError: If input is not a list
    """
    # Validate top-level type
    if not isinstance(input_data, list):
        raise TypeError(f"Expected list input, got {type(input_data).__name__}")

    # Handle empty input explicitly
    if len(input_data) == 0:
        return []

    output_list = []

    # Process each element in the input list
    for index, element in enumerate(input_data):
        try:
            output_list = decode_element(element, output_list)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid element at index {index}: {e}")

    return output_list