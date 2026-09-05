from typing import List, Any

def _validate_input_list(input_list: Any) -> List[Any]:
    """
    Validates that the input is a list.
    Raises a TypeError if the input is not a list.
    """
    if not isinstance(input_list, list):
        raise TypeError(
            f"Expected input 'input_list' to be a list, but received {type(input_list).__name__}."
        )
    return input_list

def _validate_input_element(new_element: Any) -> Any:
    """
    Validates that the element to be inserted is of a compatible type.
    Since the problem involves string operations and lists, we accept any object
    that can be added to a list without raising an error immediately, though
    logically it is expected to be a scalar (non-list) based on problem context.
    However, to be strictly defensive and flexible like Python allows, we accept
    any object that doesn't break the list construction.

    For this specific problem context, the examples show strings being inserted 
    into lists of strings. We do not restrict the type strictly to str or int
    as Python is dynamically typed, but we ensure it is not a list itself
    to avoid ambiguous "list of lists" behavior unless explicitly desired, 
    though the problem signature suggests a single element insertion.

    We will accept any non-list object to prevent infinite recursion or 
    unexpected nested list structures if the user passes a list.
    """
    if isinstance(new_element, list):
        raise TypeError(
            f"Expected 'new_element' to be a scalar (not a list), but received {type(new_element).__name__}."
        )
    return new_element

def _construct_result(input_list: List[Any], new_element: Any) -> List[Any]:
    """
    Constructs the final list by inserting 'new_element' before every item 
    in 'input_list'.

    Logic:
    1. If the input list is empty, the result is a list containing only the 
       new_element once (since there are no items to insert before).
       *Correction based on pattern analysis*: 
       Let's re-examine the examples.
       Input: ['Red', 'Green', 'Black'], Element: 'c'
       Output: ['c', 'Red', 'c', 'Green', 'c', 'Black']

       Pattern: 
       For 'Red': insert 'c', then 'Red' -> ['c', 'Red']
       For 'Green': insert 'c', then 'Green' -> ['c', 'Green']
       For 'Black': insert 'c', then 'Black' -> ['c', 'Black']

       Combined: ['c', 'Red', 'c', 'Green', 'c', 'Black']

       If input list is empty [], what is the result?
       There are no elements to process. The standard interpretation for "insert before each"
       with an empty list is an empty list. However, sometimes it might mean insert once?
       Let's look at the phrasing: "insert an element before each element of a list".
       If there are no elements, there are no "each elements". Thus, 0 insertions.
       Result should be [].

       Let's verify this logic against the provided examples.
       Example 1: 3 elements -> 6 items in output (2 items per original element).
       Example 2: 2 elements -> 4 items in output.
       Example 3: 2 elements -> 4 items in output.

       Formula: Result length = len(input_list) * 2.
       If len(input_list) == 0, Result length = 0.
       So, for empty input, we return [].
    """

    # Initialize the result list container
    result: List[Any] = []

    # Initialize an index counter to iterate through the input list
    index: int = 0

    # Get the total number of elements in the input list
    total_elements: int = len(input_list)

    # Iterate through each element in the input list
    while index < total_elements:
        # Get the current element from the input list
        current_element: Any = input_list[index]

        # Step 1: Append the new element to the result list
        result.append(new_element)

        # Step 2: Append the current element to the result list
        result.append(current_element)

        # Increment the index counter to move to the next element
        index += 1

    return result

def insert_element(input_list: List[Any], new_element: Any) -> List[Any]:
    """
    Inserts an element before each element of a list.

    Args:
        input_list: The list of elements to process.
        new_element: The element to insert before every other element.

    Returns:
        A new list where 'new_element' appears immediately before each item 
        from 'input_list'.

    Raises:
        TypeError: If input_list is not a list or if new_element is a list.
    """
    # Validate the input list structure
    validated_list = _validate_input_list(input_list)

    # Validate the new element to ensure it's not a list (defensive coding)
    validated_new_element = _validate_input_element(new_element)

    # Construct and return the result
    return _construct_result(validated_list, validated_new_element)