from typing import Any, List, Union

# Define the recursive structure for our nested lists
# An element is either a number (int or float) or another list
NestedElement = Union[int, float, List["NestedElement"]]
NestedList = List[NestedElement]

def _is_iterable_but_not_string(value: Any) -> bool:
    """
    Determines if the given value is an iterable object that is not a string.
    This is crucial because strings are iterable, but for this problem,
    we treat them as atomic values.
    """
    return hasattr(value, '__iter__') and not isinstance(value, (str, bytes))

def _deep_equal(a: Any, b: Any) -> bool:
    """
    Recursively checks if two objects are deeply equal.

    Handles:
    - Basic types (int, float) using standard equality.
    - Lists: Recursively checks if they have the same length and all corresponding elements are deeply equal.
    - Other types: Uses standard equality.
    """
    # If both are lists, recurse
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for item_a, item_b in zip(a, b):
            if not _deep_equal(item_a, item_b):
                return False
        return True

    # If one is a list and the other isn't, they cannot be equal
    if isinstance(a, list) != isinstance(b, list):
        return False

    # For everything else (primitives), use standard equality
    return a == b

def _can_represent_element_in_container(
    element: NestedElement, 
    container: NestedList
) -> bool:
    """
    Helper function to check if a single nested element 'element' can be found
    as an exact deep copy within 'container'.

    The 'container' is treated as a flat list of items for the purpose of this search.
    If the element itself is a list, we look for an item in 'container' that is 
    a list and is deeply equal to 'element'.
    If the element is a primitive, we look for an item in 'container' that is 
    equal to 'element'.

    This function assumes the container is a list of top-level items.
    """
    # If the element is not iterable (primitive), we just check direct equality in the container
    if not _is_iterable_but_not_string(element):
        for candidate in container:
            if _deep_equal(candidate, element):
                return True
        return False

    # If the element is a list, we must find a candidate in the container
    # that is also a list and matches it exactly.
    # Note: The problem implies matching top-level structures. 
    # We do not recurse into sub-elements of the container unless they are lists.
    for candidate in container:
        if not _is_iterable_but_not_string(candidate):
            continue

        if _deep_equal(element, candidate):
            return True

    return False

def check_subset_list(
    subset_candidate: NestedList, 
    superset_candidate: NestedList
) -> bool:
    """
    Checks if the 'subset_candidate' is a subset of 'superset_candidate'.

    Logic:
    1. Validate inputs: Both must be lists.
    2. Validate content of inputs: All top-level items in both lists must be 
       either primitives or lists. No dicts, sets, or other unexpected types 
       should exist based on the problem context of "nested lists".
    3. Definition of Subset: Every single top-level item in 'subset_candidate' 
       must be found as an exact deep match within 'superset_candidate'.

    Note: This is not a mathematical set subset where elements are ignored.
    It is a containment check where every element of the first list must exist 
    as a distinct, whole unit in the second list.
    """

    # Step 1: Input Type Validation
    # Both arguments must be lists.
    if not isinstance(subset_candidate, list):
        raise ValueError(f"First argument must be a list, got {type(subset_candidate).__name__}")

    if not isinstance(superset_candidate, list):
        raise ValueError(f"Second argument must be a list, got {type(superset_candidate).__name__})")

    # Step 2: Content Validation for subset_candidate
    for item in subset_candidate:
        if not _is_iterable_but_not_string(item) and not isinstance(item, (int, float)):
            # Allow None? The prompt doesn't specify, but usually nested list problems 
            # imply numbers or strings or lists. Let's be strict about "Nested List" definition.
            # Actually, let's allow any python object for robustness if it's iterable or not,
            # provided the deep equal works. The constraint is usually "nested list" structure.
            # Let's enforce that items are either primitives (int, float, str) or lists.
            # Re-reading "nested list": usually implies lists containing lists or numbers.
            # Let's stick to the safe assumption: items are either lists or non-iterables.
            pass # We will rely on _deep_equal which handles standard types.

    # More strict validation: Ensure no unexpected complex types that _deep_equal might mishandle
    # based on the problem statement "nested list".
    def _validate_list_content(nested_list: List, context: str = ""):
        for idx, item in enumerate(nested_list):
            if isinstance(item, list):
                _validate_list_content(item, f"{context}[{idx}]")
            elif isinstance(item, (str, bytes)):
                # Strings/bytes are iterable but treated as atomic in this context.
                pass
            elif isinstance(item, (int, float, bool, type(None))):
                pass
            else:
                raise ValueError(
                    f"Invalid item type found at {context}: {type(item).__name__}. "
                    f"Expected int, float, str, bool, None, or list."
                )

    _validate_list_content(subset_candidate, "subset_candidate")
    _validate_list_content(superset_candidate, "superset_candidate")

    # Step 3: Main Logic
    # Every element in subset_candidate must exist in superset_candidate.

    # Edge Case: Empty subset is a subset of any set.
    if len(subset_candidate) == 0:
        return True

    # Edge Case: Non-empty subset but empty superset.
    if len(superset_candidate) == 0:
        return False

    # Check every element in the candidate subset
    all_found = True
    for element in subset_candidate:
        # We need to find this specific 'element' within 'superset_candidate'.
        # We use a helper to avoid modifying the superset or doing complex logic inline.
        is_present = _can_represent_element_in_container(element, superset_candidate)

        if not is_present:
            all_found = False
            break

    return all_found