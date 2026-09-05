def check_last(arr, p, operations=1):
    # Validate input parameters
    if not isinstance(p, int) or p < 1:
        return "NO VALID INPUT"

    # Handle empty input
    if len(arr) == 0:
        return "NO VALID INPUT"

    # Check if all elements are the same
    if all(num == arr[0] for num in arr):
        last_element = arr[0]
    else:
        last_element = arr[-1]

    # Determine initial parity
    initial_parity = last_element % 2

    # Simulate operations based on parity of the number of operations
    if p % 2 == 1:
        initial_parity = 1 - initial_parity

    if initial_parity == 0:
        return "EVEN"
    else:
        return "ODD"