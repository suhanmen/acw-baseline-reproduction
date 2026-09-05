from typing import Iterable, Tuple, Any, Union

def sum_of_alternates(numbers: Union[Iterable[Any], Tuple[Any, ...]]) -> Tuple[int, int]:
    """
    Calculates the sum of two alternating chains of numbers.

    The first chain sums elements at even indices (0, 2, 4...).
    The second chain sums elements at odd indices (1, 3, 5...).

    Parameters:
    numbers (Union[Iterable[Any], Tuple[Any, ...]]): An iterable of numbers (int or float).

    Returns:
    Tuple[int, int]: A tuple containing (sum_of_even_indices, sum_of_odd_indices).

    Raises:
    TypeError: If input is not an iterable or contains non-numeric elements.
    ValueError: If the input iterable is empty.
    """

    # Helper function to validate individual numeric items
    def _validate_numeric_item(item: Any) -> None:
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"All elements must be numeric (int or float). "
                f"Invalid type found: {type(item).__name__}."
            )
        if not isinstance(item, int) and not isinstance(item, float):
            # This is a catch-all, though int/float covers the main cases.
            # Specifically excludes bools if they sneak in as subclasses of int.
            if isinstance(item, bool):
                raise TypeError(
                    "Boolean values are not allowed as elements."
                )
        # Note: bool is a subclass of int in Python. We check for bool explicitly above.

    # Helper function to convert and validate the input stream
    def _prepare_values(iterator: Iterable[Any]) -> list:
        prepared_list = []
        seen_count = 0

        for item in iterator:
            # Validate the type
            _validate_numeric_item(item)

            # Convert to integer for accumulation to ensure return type is int
            # based on the problem's expected output types (e.g., (46, 18)).
            # If floats are passed but sum to whole numbers, we cast to int.
            numeric_value = int(item) if item == int(item) else item

            prepared_list.append(numeric_value)
            seen_count += 1

        return prepared_list

    # Step 1: Validate that the input is an iterable
    if not hasattr(numbers, '__iter__') or isinstance(numbers, str):
        raise TypeError(
            "Input must be an iterable of numbers (like a list or tuple). "
            "Strings are not accepted."
        )

    # Step 2: Convert the input to a list of validated numbers
    try:
        value_list = _prepare_values(numbers)
    except TypeError as type_error:
        # Re-raise the type error to provide a clear message
        raise type_error from None

    # Step 3: Validate that the list is not empty
    if len(value_list) == 0:
        raise ValueError(
            "Input iterable cannot be empty. At least one number is required."
        )

    # Step 4: Initialize accumulators for the two chains
    sum_even_chain = 0
    sum_odd_chain = 0

    # Step 5: Iterate through the values with explicit index tracking
    for index, current_value in enumerate(value_list):
        if index % 2 == 0:
            # Even index (0, 2, 4...) belongs to the first chain
            sum_even_chain = sum_even_chain + current_value
        else:
            # Odd index (1, 3, 5...) belongs to the second chain
            sum_odd_chain = sum_odd_chain + current_value

    # Step 6: Return the result as a tuple of integers
    return (sum_even_chain, sum_odd_chain)