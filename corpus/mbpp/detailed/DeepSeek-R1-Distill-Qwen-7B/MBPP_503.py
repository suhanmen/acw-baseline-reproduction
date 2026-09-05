def add_consecutive_nums(lst):
    def _validate_list(lst):
        """Check if the input is a list of integers."""
        if not isinstance(lst, list):
            raise ValueError("Input must be a list.")
        if not all(isinstance(x, int) for x in lst):
            raise ValueError("All elements in the list must be integers.")

    _validate_list(lst)

    if not lst:
        return []
    if len(lst) == 1:
        return [lst[0]]

    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i] + lst[i+1])

    return result