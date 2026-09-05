def div_even_odd(lst):
    # Separate the list into even and odd numbers
    even_numbers = [num for num in lst if num % 2 == 0]
    odd_numbers = [num for num in lst if num % 2 != 0]

    # Find the first even and first odd numbers from the list
    first_even = even_numbers[0] if even_numbers else None
    first_odd = odd_numbers[0] if odd_numbers else None

    # Calculate the division of the first even by the first odd
    if first_odd is not None and first_even is not None:
        return first_even // first_odd

    # If either the even or odd list is empty, return None
    return None

# Test cases
assert div_even_odd([1,3,5,7,4,1,6,8]) == 4
assert div_even_odd([1,2,3,4,5,6,7,8,9,10]) == 2
assert div_even_odd([1,5,7,9,10]) == 10