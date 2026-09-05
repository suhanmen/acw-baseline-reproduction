import math

def count_odd_squares(a, b):
    """
    Count the number of odd numbers whose squares lie within the range [a, b].
    """
    # Find the smallest odd integer whose square is >= a
    start = math.ceil(math.sqrt(a))
    if start % 2 == 0:
        start += 1
    else:
        # Ensure we are considering odd integers
        pass

    # Find the largest odd integer whose square is <= b
    end = math.floor(math.sqrt(b))
    if end % 2 == 0:
        end -= 1
    else:
        # Ensure we are considering odd integers
        pass

    # If start exceeds end, there are no such numbers
    if start > end:
        return 0

    # Calculate the count of odd numbers between start and end, inclusive
    count = ((end - start) // 2) + 1

    return max(count, 0)

# Test the function with the given assertions
assert count_odd_squares(5, 100) == 8
assert count_odd_squares(8, 65) == 6
assert count_odd_squares(2, 5) == 1