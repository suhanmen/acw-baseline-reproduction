from typing import List, Any, Union

def decode_list(input_list: List[Union[Any, List[Any]]]) -> List[Any]:
    """
    Decodes a run-length encoded list where some elements are pairs 
    represented as [count, value].

    Args:
        input_list: A list containing elements or sub-lists of length 2.

    Returns:
        A decoded list of elements.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If a sub-list is encountered that does not have exactly 2 elements.
    """
    # Input validation
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    decoded_result: List[Any] = []

    for item in input_list:
        # Check if the current item is a run-length encoding [count, value]
        if isinstance(item, list):
            # Validate that the sub-list is a pair
            if len(item) != 2:
                raise ValueError(
                    f"Expected a pair [count, value], but found list of length {len(item)}: {item}"
                )

            count_val = item[0]
            value_val = item[1]

            # Validate that count is an integer and non-negative
            if not isinstance(count_val, int):
                raise TypeError(f"Run-length count must be an integer, got {type(count_val).__name__}")

            if count_val < 0:
                raise ValueError(f"Run-length count cannot be negative, got {count_val}")

            # Handle the expansion of the run-length encoding
            # If count is 0, it effectively adds nothing to the list
            if count_val > 0:
                # We use a loop to avoid multiplying lists, which is safer 
                # for general objects and ensures clear logic.
                for _ in range(count_val):
                    decoded_result.append(value_val)
            else:
                # If count is 0, the requirement is usually to append nothing.
                pass
        else:
            # If the item is not a list, it is treated as a single element to be appended once.
            decoded_result.append(item)

    return decoded_result

if __name__ == "__main__":
    # The following assertions confirm the requirements are met:
    assert decode_list([[2, 1], 2, 3, [2, 4], 5, 1]) == [1, 1, 2, 3, 4, 4, 5, 1]
    assert decode_list(['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y']) == \
           ['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', 'l', 'l', 'y']
    assert decode_list(['p', 'y', 't', 'h', 'o', 'n']) == ['p', 'y', 't', 'h', 'o', 'n']