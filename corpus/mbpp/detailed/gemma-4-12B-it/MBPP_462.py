from typing import List, Any

def combinations_list(input_list: List[Any]) -> List[List[Any]]:
    """
    Finds all possible combinations (power set) of the elements of a given list.

    The function generates the power set in a specific order observed in the 
    provided assertions: for each new element added to the set of items, 
    it builds combinations by prepending the new element to all previously 
    generated combinations.

    Args:
        input_list: A list of elements to generate combinations for.

    Returns:
        A list of lists, where each inner list is a unique combination.

    Raises:
        TypeError: If the input is not a list.
    """

    # Input Validation
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input type 'list', but received '{type(input_list).__name__}'")

    # Handle the base case of an empty input list immediately
    if len(input_list) == 0:
        return [[]]

    # Initialize the result list with the empty set.
    # This represents the base power set of an empty collection.
    all_combinations: List[List[Any]] = [[]]

    # Iterate through each item in the provided list sequentially.
    # The expected output order suggests a specific construction:
    # For every new element 'x', the new list of combinations includes:
    # 1. All combinations generated so far.
    # 2. The element 'x' by itself.
    # 3. 'x' prepended to every combination generated so far (excluding the empty one).
    # However, looking at the assertion:
    # ['orange', 'red'] is produced when 'red' is processed after 'orange'.
    # The order in the assertion for ['orange', 'red', 'green'] is:
    # [], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange']...
    # This means for each item in the input_list, we append:
    # [item] + [ [item] + prev_comb for prev_comb in current_combinations_list ]
    # and keep the previous combinations at the front.

    for current_element in input_list:
        # Identify the combinations generated in previous iterations
        previous_combinations_count = len(all_combinations)

        # Create a list to store the new combinations derived from the current element
        new_combinations_for_this_element: List[List[Any]] = []

        # Rule 1: The element itself is a combination
        # Note: The assertion shows ['red'] then ['red', 'orange']. 
        # This implies we add [current_element] as the first "new" entry.
        new_combinations_for_this_element.append([current_element])

        # Rule 2: Prepend the current element to every combination already in our list
        # We iterate through all combinations existing before we started processing this element.
        for i in range(previous_combinations_count):
            existing_comb = all_combinations[i]

            # We want to prepend the current_element to the existing_comb.
            # Example: if current_element is 'red' and existing_comb is ['orange'],
            # we produce ['red', 'orange'].
            new_comb = [current_element] + existing_comb

            # Only add if it's not the same as the single [current_element] we already added.
            # This happens when existing_comb is [].
            if new_comb != [current_element]:
                new_combinations_for_this_element.append(new_comb)

        # Append the new combinations to our master list.
        # The order of appending ensures we match the specific sequence required by the assertions.
        all_combinations.extend(new_combinations_for_this_element)

    return all_combinations