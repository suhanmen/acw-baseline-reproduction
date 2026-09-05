def split_two_parts(lst, n):
    # Handle the case where the input list is empty or n is 0
    if not lst or n == 0:
        return ([], [])

    # Handle the case where n is greater than or equal to the length of the list
    if n >= len(lst):
        return ([], lst[:])

    # Handle the case where n is negative
    if n < 0:
        return ([], lst)

    # Calculate the split point
    split_point = n

    # Split the list into two parts
    first_part = lst[:split_point]
    second_part = lst[split_point:]

    return (first_part, second_part)